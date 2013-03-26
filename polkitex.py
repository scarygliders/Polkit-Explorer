#! /usr/bin/python

# Polkit Explorer
# View/Explore all entries within a Linux Polkit XML file
#
# v1.0
#
# Release date : 20130324
#                yyyymmdd
#
# Copyright (C) 2013, Kevin Cave <kevin@scarygliders.net>
#
# ISC License (ISC)
#
# Permission to use, copy, modify, and/or distribute this software for any purpose with
# or without fee is hereby granted, provided that the above copyright notice and this
# permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO
# THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
# AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
# WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

from PyQt4 import QtCore, QtGui
from Ui_polkitex import Ui_PolkitExplorer
from Ui_About import Ui_About
from Ui_Glossary import Ui_Glossary
from lxml import etree as ET
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class PolkitExplorer(QtGui.QMainWindow, Ui_PolkitExplorer):
    def __init__(self, parent=None):
       super(PolkitExplorer, self).__init__(parent)
       self.setupUi(self)
    
    @QtCore.pyqtSlot()

    # User wants to open a file...
    def fileOpen(self):
        self.openActionFileDialog()

    # User wants to quit...
    def fileQuit(self):
        QtGui.qApp.quit()

    # Event fires when comboBox changes (scrollwheel or click'n'select)
    def actionComboBoxChanged(self):
        self.actionID = str(self.actionComboBox.currentText())
        self.parseAction(self.actionID)

    def fileAbout(self):
        self.aboutDialog = aboutPolkitExplorer()
        self.aboutDialog.exec_()

    def helpGlossary(self):
        self.glossaryDialog = glossaryPolkitExplorer()
        self.glossaryDialog.exec_()

    # Display file open dialog at the correct dir and with a filename filter for the policy files
    # then fill the Actions Combobox
    def openActionFileDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open Polkit file...', '/usr/share/polkit-1/actions/', '*.policy')
        if fname != "":
            self.parsePolKitFile(str(fname))

    # fill Actions ComboBox with list of all actions for specified Policy File. 
    def parsePolKitFile(self, fname):

        # Display the filename of the policy kit file
        self.policyKitFileName.setText(fname)

        #Read the selected file and create the lxml tree object...
        parser = ET.XMLParser(encoding='utf-8')
        self.tree = ET.parse(fname, parser)
        self.root = self.tree.getroot()

        self.actionComboBox.clear()
        self.actionsCount = 0

        #fill the Actions combo box list with all actions from the loaded polkit file...
        for actionslist in self.root.iter('action'):
            actname = actionslist.get('id')
            self.actionComboBox.addItem(unicode(actname))
            self.actionsCount = self.actionsCount + 1
            self.actionsCounterDisplay.display(self.actionsCount)
    
    def parseAction(self, actionID):
        description = None
        for actionslist in self.root.iter('action'):
            policy = actionslist.get('id')
            if policy == actionID:
                # Get the default permissions for the selected Action...
                for action in self.root.xpath('.//action[@id = $policy]', policy=actionID):
                    self.anySet = 0
                    self.inSet = 0
                    self.actSet = 0
                    for defaults in action.findall("./defaults/"):
                        self.fillDefaultsTable(defaults.tag, defaults.text)
                # Get the desired Description of the Action...
                # Note: It's a complete PITA... some .policy XML files just have Descriptions with
                #       no xml:lang attributes, and some have, and one file has a Description element
                #       tag of "_description"! Yep, a complete PITA, all right... 
                for d in self.root.xpath('.//action[@id = $policy]/description[@xml:lang = $lang]', policy=policy, lang="en_GB"):
                    description = d.text
                if description is not None:
                    self.polkitActionDescription.setText(description)
                else:
                    # Okay so we didn't find a Description with an xml:lang attribute, so try to find one
                    # which has a "description" tag with no attributes...
                    for d in self.root.xpath('.//action[@id = $policy]/*[local-name()="description" or local-name()="_description"]', policy=actionID):
                        if d.attrib == "":
                            description = d.text
                    if description is not None:
                        # Found one!
                        self.polkitActionDescription.setText(description)
                    else:
                        # Booooo!
                        self.polkitActionDescription.setText("No description found - how helpfull!")

    def fillDefaultsTable(self, defaultTag, defaultText):
        if defaultTag == "allow_any":
            self.currentAllowAnyLabel.setText(defaultText)
            self.anySet = 1
        elif defaultTag == "allow_inactive":
            self.currentAllowInactiveLabel.setText(defaultText)
            self.inSet = 1
        elif defaultTag == "allow_active":
            self.currentAllowActiveLabel.setText(defaultText)
            self.actSet =1
        if self.anySet == 0:
            self.currentAllowAnyLabel.setText("")
        if self.inSet == 0:
            self.currentAllowInactiveLabel.setText("")
        if self.actSet == 0:
            self.currentAllowActiveLabel.setText("")

class aboutPolkitExplorer(QtGui.QDialog, Ui_About):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.aboutDialog = Ui_About()
        self.setupUi(self)

    def aboutClose(self):
        self.close()

class glossaryPolkitExplorer(QtGui.QDialog, Ui_Glossary):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.glossaryDialog = Ui_Glossary()
        self.setupUi(self)

    def closeGlossary(self):
        self.close()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = PolkitExplorer()
    window.show()
    sys.exit(app.exec_())
