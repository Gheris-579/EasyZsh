#!/bin/bash


CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}🚀 Inizio installazione di EasyZsh...${NC}"

# 1. Controllo Dipendenze (Git e Python3)
if ! command -v git &> /dev/null; then
    echo -e "${RED}✘ Git non trovato. Lo installo...${NC}"
    sudo apt update && sudo apt install -y git
fi

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✘ Python3 non trovato. Lo installo...${NC}"
    sudo apt update && sudo apt install -y python3
fi

# 2. Definizione cartella di installazione (Nascosta nella Home)
INSTALL_DIR="$HOME/.easyzsh"

# Se esiste già, la aggiorniamo
if [ -d "$INSTALL_DIR" ]; then
    echo -e "${CYAN}➤ Aggiornamento file esistenti...${NC}"
    rm -rf "$INSTALL_DIR"
fi

# 3. Clonazione della Repository
echo -e "${CYAN}➤ Clonazione della repository da GitHub...${NC}"
# SOSTITUISCI L'URL CON IL TUO VERO LINK GITHUB
git clone https://github.com/Gheris-579/EasyZsh.git "$INSTALL_DIR"

# 4. Creazione dell'Alias per Bash e Zsh
echo -e "${CYAN}➤ Configurazione comando 'easyzsh'...${NC}"
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

echo -e "${GREEN}✅ Installazione completata con successo!${NC}"
echo -e "${GREEN}👉 Chiudi e riapri il terminale o scrivi: source ~/.bashrc${NC}"
echo -e "${CYAN}🚀 Poi scrivi semplicemente 'easyzsh' per iniziare!${NC}"