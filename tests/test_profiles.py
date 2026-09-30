import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "profiles"
ROLES = {"explorer", "researcher", "worker", "tester", "reviewer"}
EXPECTED = {
    "plus": ("gpt-6-luna", "max", 2, "gpt-6-luna"),
    "pro-100": ("gpt-6.1-sol", "medium", 2, "gpt-6.1-sol"),
    "pro-200": ("gpt-6.1-sol", "medium", 3, "gpt-6.1-sol"),
    "pro-500": ("gpt-6.1-sol", "medium", 4, "gpt-6.1-sol"),
}
ALIASES = {
    "plus-max-2-subagents": "plus",
    "pro": "pro-100",
    "pro-max-2-subagents": "pro-100",
}


def bundle_files(profile: Path) -> dict[str, bytes]:
    return {path.relative_to(profile).as_posix(): path.read_bytes() for path in profile.rglob("*") if path.is_file()}


class ProfileTopologyTests(unittest.TestCase):
    def test_canonical_profiles_are_complete(self) -> None:
        expected_files = {"codex/config.toml", "agents/skills/codex-orchestrator/SKILL.md"}
        expected_files.update(f"codex/agents/{role}.toml" for role in ROLES)
        for name in EXPECTED:
            with self.subTest(profile=name):
                files = bundle_files(PROFILES / name)
                self.assertEqual(set(files), expected_files)
                frontmatter = files["agents/skills/codex-orchestrator/SKILL.md"].decode().split("---", 2)[1]
                self.assertIn("name: codex-orchestrator", frontmatter.splitlines())

    def test_canonical_profile_settings_and_roles(self) -> None:
        for name, (root_model, root_effort, cap, execution_model) in EXPECTED.items():
            with self.subTest(profile=name):
                profile = PROFILES / name
                config = tomllib.loads((profile / "codex/config.toml").read_text())
                self.assertEqual((config["model"], config["model_reasoning_effort"]), (root_model, root_effort))
                self.assertEqual(config["service_tier"], "default")
                self.assertEqual((config["approval_policy"], config["sandbox_mode"]), ("on-request", "workspace-write"))
                agents = config["agents"]
                self.assertTrue(agents["enabled"])
                self.assertEqual(agents["max_concurrent_threads_per_session"], cap)
                self.assertEqual(
                    (agents["default_subagent_model"], agents["default_subagent_reasoning_effort"]),
                    ("gpt-6-luna", "high"),
                )
                for role in ROLES:
                    data = tomllib.loads((profile / "codex/agents" / f"{role}.toml").read_text())
                    self.assertEqual(data["name"], role)
                    expected = (
                        (execution_model, "high" if name == "plus" else "medium", "workspace-write")
                        if role in {"worker", "tester"}
                        else ("gpt-6.1-sol", "medium", "read-only")
                        if role == "reviewer"
                        else ("gpt-6-luna", "high", "read-only")
                    )
                    self.assertEqual(
                        (data["model"], data["model_reasoning_effort"], data["sandbox_mode"]),
                        expected,
                    )
                    self.assertTrue(data["developer_instructions"].strip())

    def test_aliases_are_complete_byte_identical_bundles(self) -> None:
        for alias, canonical in ALIASES.items():
            with self.subTest(profile=alias):
                self.assertEqual(bundle_files(PROFILES / alias), bundle_files(PROFILES / canonical))

    def test_all_profiles_share_the_same_orchestration_policy(self) -> None:
        reference = (PROFILES / "plus/agents/skills/codex-orchestrator/SKILL.md").read_bytes()
        self.assertEqual({path.name for path in PROFILES.iterdir() if path.is_dir()}, set(EXPECTED) | set(ALIASES))
        for name in EXPECTED | ALIASES:
            with self.subTest(profile=name):
                self.assertEqual(
                    (PROFILES / name / "agents/skills/codex-orchestrator/SKILL.md").read_bytes(),
                    reference,
                )


if __name__ == "__main__":
    unittest.main()
