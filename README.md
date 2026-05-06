# Arctic Forge

Arctic Forge is a lightweight Python application scaffold built to run as a standalone tool now and later fit into a larger Master Application ecosystem.

The current version provides a clean startup path, settings loading, startup logging, and a placeholder engine layer for future modules.

## Project Goals

- Keep the application modular and easy to extend.
- Use Python standard library only for the base system.
- Preserve Windows-friendly development and executable-packaging compatibility.
- Separate app startup, core engine logic, config loading, and logging.
- Keep the structure small enough for laptop-friendly development.

## Requirements

- Python 3.11 or newer
- Windows recommended
- No external Python packages required

## Project Structure

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
|   +-- ArcticForge.log
+-- Docs/
    +-- README.md
```

## Run

From the repository root:

```powershell
python ArcticForge\App\Main.py
```

Expected console output:

```text
Starting Arctic Forge...
Arctic Forge Engine Started
Arctic Forge Ready
```

## Configuration

Settings are stored in:

```text
ArcticForge/Config/ArcticForge.Settings
```

Current settings:

```json
{
    "Debug_Mode": false,
    "Log_Path": "Logs",
    "App_Name": "Arctic Forge"
}
```

If the settings file is missing, Arctic Forge creates a default version on startup.

## Logging

Startup events are written to:

```text
ArcticForge/Logs/ArcticForge.log
```

The logger creates the log folder automatically if it is missing.

## Core Files

`App/Main.py`

Main entry point. It loads config, starts logging, initializes the engine, and prints clean startup output.

`Core/ConfigLoader.py`

Ensures required folders exist, creates the default settings file if needed, and loads JSON config data.

`Core/Logger.py`

Writes timestamped log entries to the configured log path.

`Core/Engine.py`

Starts the core engine and provides a placeholder for future module registration.

## Development Notes

- Keep new modules separated from the startup layer.
- Avoid external dependencies unless they provide clear long-term value.
- Preserve custom file extensions such as `.Settings`.
- Keep source behavior aligned with future packaged executable behavior.
