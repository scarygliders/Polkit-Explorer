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

Written in Python using the QT4 library.

Requires
--------
    python
    python-qt
    python-lxml
    Qt libraries

Running
-------

To run, simply change into the PolkitExplorer directory and type ./polkitex.py

Menus
-----

Use File--->Open from the GUI to open the .policy file you wish to explore.

File--->Quit exits the application.

Help--->About brings up the About window.

Help--->Glossary brings up a window explaining the meanings of the information
        displayed.
        
More details at http://scarygliders.net/2013/03/26/polkit-explorer-v1-0-released/

Tested on Debian and works. For other distributions you may have to browse to a
different directory where that particular distribution keeps its Polkit .policy
files.

Send patches, bug reports either to the GitHub repository and/or my website at
http://scarygliders.net 

Files
-----

About.ui        : Qtdesigner file for the About window

Glossary.ui     : QtDesigner file for the Glossary window

PKEIconV001.png : The program's "logo"

polkitex.py     : The main Python program

polkitex.ui     : QtDesigner file for the main GUI

Ui_*.py         : Python code, compiled from the *.ui files using pyuic4

Any changes made to the .ui QtDesigner forms need to then be compiled via pyuic4.
Signal slots from the buttons to the main program are created inside QtDesigner.

Python will more than likely create some .pyc files after running this, it's
normal (compiled python files).

I hope this proves useful to someone.

I intend to create a spin-off utility which will enable the creation/editing of
policies, at a later date.

Enjoy ;)

Kevin Cave
kevin@scarygliders.net
