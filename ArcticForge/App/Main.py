from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Core.ConfigLoader import ConfigLoader
from Core.Engine import Engine
from Core.Logger import Logger


def main():
    print("Starting Arctic Forge...")

    config_loader = ConfigLoader(PROJECT_ROOT)
    config = config_loader.load_config()

    logger = Logger(PROJECT_ROOT, config)
    logger.log("Arctic Forge startup initialized")

    engine = Engine(config, logger)
    engine.start()

    logger.log("Arctic Forge startup complete")
    print("Arctic Forge Ready")


if __name__ == "__main__":
    main()
