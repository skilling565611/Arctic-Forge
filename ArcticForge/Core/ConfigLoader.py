import json
from pathlib import Path


class ConfigLoader:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.config_dir = self.project_root / "Config"
        self.logs_dir = self.project_root / "Logs"
        self.docs_dir = self.project_root / "Docs"
        self.config_path = self.config_dir / "ArcticForge.Settings"

    def load_config(self):
        self._ensure_project_paths()

        if not self.config_path.exists():
            self._create_default_config()

        with self.config_path.open("r", encoding="utf-8") as config_file:
            return json.load(config_file)

    def _ensure_project_paths(self):
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.docs_dir.mkdir(parents=True, exist_ok=True)

    def _create_default_config(self):
        default_config = {
            "Debug_Mode": False,
            "Log_Path": "Logs",
            "App_Name": "Arctic Forge"
        }

        with self.config_path.open("w", encoding="utf-8") as config_file:
            json.dump(default_config, config_file, indent=4)
