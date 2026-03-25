# ⚡ EasyZsh 

> **Transform your terminal into a professional workstation with a single command.**  
> An interactive Python manager for Debian/Ubuntu-based distributions (Parrot OS, Kali Linux, Mint).

---

## 🚀 Why EasyZsh?
Manually configuring Zsh, Oh My Zsh, and plugins every time you install a new system is tedious. EasyZsh automates the entire process through an intuitive numbered menu and eye-catching banners.

### 🔥 What does EasyZsh handle for you?
- ✅ **System Health:** Automatic Update, Full Upgrade, and package cleanup (`autoremove`).
- ✅ **Core Tools:** Instantly installs `git`, `curl` and essential base dependencies.
- ✅ **Zsh Master:** Installs Zsh and sets it as the default shell.
- ✅ **Oh My Zsh:** Complete framework setup in unattended mode.
- ✅ **Power-User Plugins:** Installs and configures `autosuggestions` and `syntax-highlighting`.
- ✅ **Safety First:** Automatic backup of the `.zshrc` file before every change.
- ✅ **Smart Config:** Saves your preferences in a `config.json` file to remember your setup.

---

## 📥 Quick Installation (One-Liner)
No need to download anything manually. Paste this into your terminal and press Enter:

```bash
curl -sSL https://raw.githubusercontent.com | bash
```
After installation, restart your terminal and simply type:
```bash
easyzsh
```

# 🛠️ Requirements
- OS: Ubuntu, Debian, Parrot OS, Kali Linux, Pop!_OS.
- Python: 3.x (the installation script checks this for you).

# 📂 Complete Project Structure
- **easyzsh.py:** Il file principale (Main) che l'utente lancia per aprire il menu.
- **install.sh:** The Bash script used for quick installation through the `curl` command.
- **LICENSE:** The MIT license that protects the project’s source code.
- **README.md:** The presentation page containing instructions, screenshots, and project information.
- **config.json:** The file, created automatically, that stores the username and Zsh installation status.
- **modules/init.py:** The required empty file that tells Python the folder contains modules.
- **modules/core.py:** The “engine” that contains `run_task` and the `apt` system commands.
- **modules/zsh_manager.py:** The “specialist” responsible for installing Oh My Zsh, plugins, and the custom prompt.
- **modules/art.py:** Your “art gallery” containing the 11 ASCII banners and color codes (`Re`, `Gr`, `Blu`).
- **modules/config_manager.py:** The manager that reads and writes data to the JSON configuration file.
- **modules/ui_utils.py:** (If created) The file that contains UI helper functions such as `clear()` or `show_header()`.



# 📸 Menu Preview
<img width="1151" height="629" alt="image" src="https://github.com/user-attachments/assets/9afdd3a4-d954-45e9-ae78-23d180f3fc67" />



