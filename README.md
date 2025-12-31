This program auto updates devonian to latest actions with one single click 




How to build:

Before building, make sure you have:

Python 3.10 or newer

pip (comes with Python)

Windows / Linux / macOS

Internet connection (for installing dependencies)

Step 1:

Download the script.py file

Step 2:

To make this program work, you must tell it where your Minecraft folder is located on your computer.
In the code (you can open in notepad), you will see this line:

`MODS_FOLDER = r"minecraft folder path here"`

You need to replace the text inside the quotes with the full path to your Minecraft mods folder.

Examples of path: 

`MODS_FOLDER = r"C:\Users\Alex\AppData\Roaming\.minecraft\mods"`

`MODS_FOLDER = r"C:\Users\Alex\Documents\CurseForge\Minecraft\Instances\MyModpack\mods"`

`MODS_FOLDER = r"C:\Users\Alex\AppData\Roaming\PrismLauncher\instances\Fabric 1.21\mods"`


Step 3:

right click anywhere in folder and `click open in terminal`

Step 4: 

paste each of these 

`pip install -r requirements.txt`

If requirements.txt does not exist:

`pip install requests pyinstaller`

`pip install pyinstaller`

`python -m PyInstaller --onefile script.py`

Step 5: Locate the Build Output

After the build completes, you will see new folders, your executable will be inside the dist folder.

Step 6:

double click to run
