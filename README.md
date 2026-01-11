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

If it says 3.10 or higher, you are good.
If not, download Python from below or the Microsoft store.
https://www.python.org/downloads/

When installing Python, make sure "Add Python to PATH" is checked.

--------------------------------------------------

Step 1: Download the program

Download the script

--------------------------------------------------

Step 2: Set Minecraft mods folder (Python part)

Open script.py in Notepad or any text editor.

Find this line:
MODS_FOLDER = r"minecraft folder path here"

Replace it with your Minecraft mods folder path.

Example:

`MODS_FOLDER = r"C:\Users\Alex\AppData\Roaming\PrismLauncher\instances\Fabric 1.21\mods"`

Save the file.

--------------------------------------------------

Step 3: Open terminal in the project folder

Open the folder with script.py.

Hold Shift and right-click.

Click "Open in Terminal" or "Open Command Prompt here".

-------------------------------------------------

Step 4: Install required packages

run `pip install requests pyinstaller` in terminal 

--------------------------------------------------

Step 5: get python.exe path

run `python -c "import sys; print(sys.executable)"` in terminal and copy the path

--------------------------------------------------

Step 6: Set path in prism 

open prism launcher

select instance and click on edit 

then go to settings and click on custom commands

write `"add python path here" "add script path here"` under "pre launch command"

now add your python path and script path (the folder of script and

the end result will look like this 

`"C:\Users\Alex\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe" "E:\script.py"`

--------------------------------------------------

Now whenever you run minecraft, devonian will auto update to latest actions in github 







