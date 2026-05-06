# Arctic Forge Architecture

Arctic Forge is a modular tool-builder and core engine for the AtlasCore ecosystem.

The current architecture is intentionally small. Each layer has one clear job so the app can run standalone now and later connect into a larger Master Application.

## Structure

```text
ArcticForge/
+-- App/
|   +-- Main.py
+-- Core/
|   +-- Engine.py
|   +-- ConfigLoader.py
|   +-- Logger.py
+-- Config/
|   +-- ArcticForge.Settings
+-- Logs/
+-- Docs/
    +-- ARCHITECTURE.md
```

## Layers

### App

`App/Main.py` is the application entry point.

It prepares the startup flow:

- Finds the project root
- Loads settings
- Starts logging
- Starts the core engine

### Core

The `Core` folder contains reusable system logic.

`Core/Engine.py`

Runs the Arctic Forge core and prepares the future module system.

`Core/ConfigLoader.py`

Loads `Config/ArcticForge.Settings`. If the settings file or required folders are missing, it creates them.

`Core/Logger.py`

Writes timestamped startup events into the configured log folder.

### Config

`Config/ArcticForge.Settings` stores simple JSON settings while preserving the custom `.Settings` file extension.

Current settings:

- `Debug_Mode`
- `Log_Path`
- `App_Name`

### Logs

The `Logs` folder stores runtime log files created by the logger.

## Design Rules

- Keep the base app standard-library only.
- Keep startup logic separate from engine logic.
- Keep config and logging reusable for future modules.
- Preserve custom file formats and extensions.
- Avoid adding dependencies until they are clearly needed.
- Keep source behavior compatible with future packaged executable behavior.

## Future Module Path

Future tools should plug into the engine through a module registration layer instead of being hard-coded into `Main.py`.

The current `Engine.modules` list is a placeholder for that future expansion.
