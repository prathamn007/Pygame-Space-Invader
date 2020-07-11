from cx_Freeze import setup, Executable
import sys,os
os.environ['TCL_LIBRARY']=r'F:/Python Install/Lib/site-packages/tcl/tcl8.6'
os.environ['TK_LIBRARY']=r'F:/Python Install/Lib/site-packages/tcl/tk8.6'
setup(name="main",
      version="1.1",
      description="Description of the app here.",
      executables=[Executable("main.py")], requires=['pygame']
      )