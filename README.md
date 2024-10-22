Polkit Explorer
---------------

Polkit Explorer reads in a Polkit .policy file, parses its XML contents, and
presents the information it contains, on a more human-readable GUI window.

Polkit policies define what the default permissions users are given to perform
certain tasks on their systems, for example, can a user eject a disk. These
permissions are granted or denied depending on if a user is logged in locally
(Active) , logged in remotely (Inactive), or just plain logged in.

This utility is intended to give you an insight into how your system is
configured by default.

Written in Python using the QT5 library.

Requires
--------
    python3 (tested on python 3.12)
    pyside6
    python-lxml
    Qt libraries (whatever PySide6 needs)

Running
-------

To run:
0) Ensure your Python environment is set up. Tested on 3.12. Either use a virtualenv with pyside6 installed, or
   install the native python packages on your system. Your virtualenv should have pyside6 and python-lxml installed.
1) ensure the Ui_*.py files exist. If not, first run the compile_forms.sh shell script which will create them.
2) type ./polkitex.py (or python polkitex.py)

Polkit Explorer should now display the main window. Click on File-->Open and select a policy file, after which you
will be able to view the policies configured for that particular file using the drop-down menu.



Menus
-----

Use File--->Open from the GUI to open the .policy file you wish to explore.

File--->Quit exits the application.

Help--->About brings up the About window.

Help--->Glossary brings up a window explaining the meanings of the information
        displayed.
        
More details at http://scarygliders.net/2013/03/26/polkit-explorer-v1-0-released/

Tested on Debian, Arch Linux, and works. For other distributions you may have to browse to a
different directory where that particular distribution keeps its Polkit .policy
files.

Send patches, bug reports either to the GitHub repository.
My much-neglected website is at: http://scarygliders.net 

Files
-----

About.ui        : Qtdesigner file for the About window

Glossary.ui     : QtDesigner file for the Glossary window

PKEIconV001.png : The program's "logo"

polkitex.py     : The main Python program

polkitex.ui     : QtDesigner file for the main GUI

Ui_*.py         : Python code, compiled from the *.ui files using pyside6-uic

Any changes made to the .ui QtDesigner forms need to then be compiled via pyside6-uic.
A shell script called compile_forms.sh is provided for your convenience. Run that
first before trying to run the application.

Signal slots from the buttons to the main program are created inside QtDesigner.

Python will more than likely create some .pyc files after running this, it's
normal (compiled python files).

I hope this proves useful to someone.

Enjoy ;)

Kevin Cave
kevin@scarygliders.net
