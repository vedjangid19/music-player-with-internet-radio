
import cx_Freeze
import sys
base = None
if sys.platform == "win32":
    base = "Win32GUI"
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "music player",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\PygameWordgame.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="new.py",icon='cc.ico',base=base)]

cx_Freeze.setup(
    version="1.0",
    description="music player",
    
    name="new.py",
    options={"build_exe": {"packages":["pygame","vlc","tkinter","os"],
                           "include_files":['cc.ico']},
             "bdist_msi": bdist_msi_options,
             },
    executables = executables

    )