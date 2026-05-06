from datetime import datetime
from pathlib import Path


class Logger:
    def __init__(self, project_root, config):
        self.project_root = Path(project_root)
        self.config = config
        self.log_dir = self.project_root / self.config.get("Log_Path", "Logs")
        self.log_path = self.log_dir / "ArcticForge.log"

        self.log_dir.mkdir(parents=True, exist_ok=True)

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"

        with self.log_path.open("a", encoding="utf-8") as log_file:
            log_file.write(log_entry + "\n")
