# TTS Mod Transloader
TTS Mod Transloader uploads assets from any Tabletop Simulator mod to your Google Drive account and creates a corresponding savefile.
This guarantees you can always play a mod with your friends, even if the original files get taken down, without needing to manually share files.

TTS Mod Transloader is a simple command line application, but will get a UI if there is enough demand.



## Instructions
All of the mod's assets must be downloaded to your computer for TTS Mod Transloader to work properly.
This can be achieved two ways:

### TTS Mod Backup Tool 👍
The easiest way to download a mod's files is to use the awesome [TTS Mod Backup tool](http://www.berserk-games.com/forums/showthread.php?1362-TTS-Mod-Backup-tool) made by Froghut.

Steps:
1. Search for the mod you want to transload (in the left window pane).
1. Right click the mod and select **Download**.
    1. The mod will highlight green when all files are finished downloading. If any files are cannot be downloaded, the mod will remain highlighted red. As a last resort, try loading the mod in Tabletop Simulator. Sometimes TTS can download files which TTS Mod Backup can't.

### Old Fashioned Way
Alternatively, you can open the mod in Tabletop Simulator, then pull objects out of all the bags and wait for assets to load.
This method is not preferred because it is labor intensive and easy to miss items.



## Command Line Interface
```
tts-mod-transloader
    [--save-file PATH]                  | Absolute or relative path to the Tabletop Simulator JSON save file on your computer.
    [--google-drive-folder PATH]        | Absolute path in Google Drive where the assets and savefile will be uploaded. If any part of the path doesn't exists, the folders will be created.     
    [--continue-with-missing-assets]    | If set, the program will not abort if it encounters an asset file that is missing from your computer. In this case, the savefile will point to the original URL for this asset.

Example:
./tts-mod-transloader \
    --save-file "C:\Users\kevin-d-omara\Documents\My Games\Tabletop Simulator\Saves\TS_Save_57.json" \
    --google-drive-folder "My Drive/Tabletop Simulator/Hosted Mods/Cool Mod Name/"
```



## Developer Setup

### Python
Install [Python 3.6](https://www.python.org/downloads/).

### IntelliJ
Install [IntelliJ Community Edition](https://www.jetbrains.com/idea/download/#section=windows) w/ these plugins:
* [Python Community Edition](https://plugins.jetbrains.com/plugin/7322-python-community-edition)
* [Markdown Navigator](https://plugins.jetbrains.com/plugin/7896-markdown-navigator)

#### SDK
Set up the project's Python SDK:

1. Create a Python virtual environment for the project:
   * Project Structure > Platform Settings > SDK > + > Python SDK > New environment
1. Install these packages to the virtualenv:
   * Project Structure > Platform Settings > SDK > Python 3.6 (Heroes-System-Image-Cropper) > Packages > + 
   * `pytest`(4.5.0)
   * `PyInstaller` (3.4)
   * `PyDrive` (1.3.1)
   * `attrs` (19.1.0)
1. Select the Project SDK:
   * Project Structure > Project Settings > Project > Project SDK: > Python 3.6 (Heroes-System-Image-Cropper)
1. Apply

#### Run via IntelliJ
Follow these steps in order to run the program through IntelliJ:
1. Open `src/tts_mod_transloader/main.py`.
1. Right click anywhere within the file and select **Run 'main'**.
1. At the top right, select the dropdown titled **main** and click **Edit Configurations...**.
1. In **Parameters:** enter *TODO*. The paths are relative and start from the working directory `src/tts_mod_transloader`.

### Activate Venv
To run commands like `pytest` and `pyinstaller` you need to activate the virtual environment.
1. Open a terminal at the root of the project `Heroes-System-Image-Cropper/`
1. Run `venv/Scripts/activate`

*This must be done each time you open IntelliJ.*

### Run unit tests
1. Activate Venv
1. Run `pytest`

See also: https://docs.pytest.org/en/latest/

### Building the Executable
1. Activate venv
1. Run: `pyinstaller src/image_cropper/main.py --name heroes-system-image-cropper --onefile`

See also: https://pyinstaller.readthedocs.io/en/stable/usage.html
