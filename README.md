What this program does:
This program updates the Devonian mod to the latest version with one click.

--------------------------------------------------

Python setup:

You need:
Python 3.10 or newer
Internet connection
Windows, macOS, or Linux

Check Python:
Open Command Prompt or Terminal
Type:
python --version

If it says 3.10 or higher, you are good.
If not, download Python from below or the Microsoft store.
https://www.python.org/downloads/

Windows only:
When installing Python, make sure "Add Python to PATH" is checked.

--------------------------------------------------

Step 1: Download the program

Download or clone the repository.
Extract the folder somewhere easy, like the Desktop.

--------------------------------------------------

Step 2: Set Minecraft mods folder (Python part)

Open script.py in Notepad or any text editor.

Find this line:
MODS_FOLDER = r"minecraft folder path here"

Replace it with your Minecraft mods folder path.

Examples:

MODS_FOLDER = r"C:\Users\Alex\AppData\Roaming\.minecraft\mods"
MODS_FOLDER = r"C:\Users\Alex\Documents\CurseForge\Minecraft\Instances\MyModpack\mods"
MODS_FOLDER = r"C:\Users\Alex\AppData\Roaming\PrismLauncher\instances\Fabric 1.21\mods"

Save the file.

--------------------------------------------------

How to get your folder path
WIN + R
%appdata%
If using Prism Launcher open up the folder called PrismLauncher, click on instances and select the instance

If using Modrinth Loader open the folder called ModrinthApp, Open profiles and select the profile.

Then click on the top and copy and paste it into the python file.
--------------------------------------------------

Step 3: Open terminal in the project folder

Open the folder with script.py.
Hold Shift and right-click.
Click "Open in Terminal" or "Open Command Prompt here".

-------------------------------------------------

Step 4: Install required packages

If requirements.txt exists:
pip install -r requirements.txt

If it does not exist:
pip install requests pyinstaller

--------------------------------------------------

Step 5: Run the Python file.
If it automatically closes you should be fine.
