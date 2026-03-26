#!/bin/bash

set -e

REPO_URL="https://github.com/Gheris-579/EasyZsh.git"
INSTALL_DIR="$HOME/.easyzsh"
COMMAND_PATH="/usr/local/bin/easyzsh"

echo "🚀 Starting EasyZsh installation..."

# Controllo dipendenze base
if ! command -v git >/dev/null 2>&1; then
    echo "➤ Git not found. Installing..."
    sudo apt update
    sudo apt install -y git
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "➤ Python3 not found. Installing..."
    sudo apt update
    sudo apt install -y python3
fi

# Se la cartella esiste già, la rimuove
if [ -d "$INSTALL_DIR" ]; then
    echo "➤ Existing EasyZsh installation found. Removing old files..."
    rm -rf "$INSTALL_DIR"
fi

echo "➤ Cloning the repository from GitHub..."
git clone "$REPO_URL" "$INSTALL_DIR"

# Controllo file principale
if [ ! -f "$INSTALL_DIR/EasyZsh/easyzsh.py" ]; then
    echo "❌ Error: easyzsh.py not found in $INSTALL_DIR/EasyZsh/"
    exit 1
fi

echo "➤ Setting up the easyzsh command..."
sudo tee "$COMMAND_PATH" > /dev/null <<EOF
#!/bin/bash
python3 "$INSTALL_DIR/EasyZsh/easyzsh.py"
EOF

sudo chmod +x "$COMMAND_PATH"

echo "✅ Installation completed successfully!"
echo "👉 Close and reopen the terminal, or run: source ~/.bashrc"
echo "🚀 Then simply type 'easyzsh' to get started!"
