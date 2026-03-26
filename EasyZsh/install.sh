#!/bin/bash


CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}🚀 Starting EasyZsh installation...${NC}"

# 1. Controllo Dipendenze (Git e Python3)
if ! command -v git &> /dev/null; then
    echo -e "${RED}✘ Git not found. Installing it...${NC}"
    sudo apt update && sudo apt install -y git
fi

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✘ Python3 not found. Installing it...${NC}"
    sudo apt update && sudo apt install -y python3
fi

# 2. Definizione cartella di installazione (Nascosta nella Home)
INSTALL_DIR="$HOME/.easyzsh"

# Se esiste già, la aggiorniamo
if [ -d "$INSTALL_DIR" ]; then
    echo -e "${CYAN}➤ Updating existing files...${NC}"
    rm -rf "$INSTALL_DIR"
fi

# 3. Clonazione della Repository
echo -e "${CYAN}➤ Cloning the repository from GitHub...${NC}"
# SOSTITUISCI L'URL CON IL TUO VERO LINK GITHUB
git clone https://github.com/Gheris-579/EasyZsh.git "$INSTALL_DIR"

# 4. Creazione dell'Alias per Bash e Zsh
echo -e "${CYAN}➤ Setting up the easyzsh command...${NC}"
ALIAS_CMD="alias easyzsh='python3 $INSTALL_DIR/easyzsh.py'"

# Aggiunge l'alias a .bashrc
if ! grep -q "alias easyzsh=" "$HOME/.bashrc"; then
    echo "$ALIAS_CMD" >> "$HOME/.bashrc"
fi

# Aggiunge l'alias a .zshrc (se esiste)
if [ -f "$HOME/.zshrc" ]; then
    if ! grep -q "alias easyzsh=" "$HOME/.zshrc"; then
        echo "$ALIAS_CMD" >> "$HOME/.zshrc"
    fi
fi

echo -e "${GREEN}✅ Installation completed successfully!${NC}"
echo -e "${GREEN}👉 Close and reopen the terminal, or run: source ~/.bashrc${NC}"
echo -e "${CYAN}🚀 Then simply type 'easyzsh' to get started!${NC}"