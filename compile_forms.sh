#!/usr/bin/env bash

echo "Compiling the UI files..."
echo "About..."
pyside6-uic About.ui -o Ui_About.py
echo "Glossary..."
pyside6-uic Glossary.ui -o Ui_Glossary.py
echo "Polkit Explorer..."
pyside6-uic polkitex.ui -o Ui_polkitex.py
echo "Done."