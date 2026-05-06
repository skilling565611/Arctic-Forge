class Engine:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.modules = []

    def start(self):
        app_name = self.config.get("App_Name", "Arctic Forge")
        self.logger.log(f"{app_name} engine starting")

        print("Arctic Forge Engine Started")

        self._prepare_modules()
        self.logger.log(f"{app_name} engine started")

    def _prepare_modules(self):
        # Future Arctic Forge modules will be registered here.
        self.logger.log("Module system prepared")
