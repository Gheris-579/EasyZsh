# ⚡ EasyZsh  **v0.2.0**

> **Transform your terminal into a professional workstation with a single command.**  
> An interactive Python manager for Debian/Ubuntu-based distributions (Parrot OS, Kali Linux, Mint).

---

## 🚀 Why EasyZsh?
Manually configuring Zsh, Oh My Zsh, and plugins every time you install a new system is tedious. EasyZsh automates the entire process through an intuitive numbered menu and eye-catching banners.

### 🔥 What does EasyZsh handle for you?
*   ✅ **System Maintenance:** Handle `update`, `full-upgrade`, and `autoremove` from a single centralized menu.
*   ✅ **Essential Dependencies:** Installs `git`, `curl`, and required base packages automatically.
*   ✅ **Zsh Setup:** Installs Zsh and prepares it for daily use in seconds.
*   ✅ **Oh My Zsh Installation:** Sets up the Oh My Zsh framework in *unattended* mode (no interruptions).
*   ✅ **User Configuration:** Configures your user `.zshrc` with plugins, custom prompt, and improved defaults.
*   ✅ **Root Zsh Configuration:** Automatically configures the **ROOT** shell (Red Prompt 🔴) with automatic plugin synchronization.
*   ✅ **Productivity Plugins:** Adds `zsh-autosuggestions` and `zsh-syntax-highlighting` for a better terminal experience.
*   ✅ **Backup Protection:** Creates a safety backup of `.zshrc` with a timestamp before every important change.
*   ✅ **Smart Config Memory:** Stores preferences in `config.json` to remember your setup.
*   ✅ **Error-Aware Setup:** Verifies files, paths, and dependencies before applying changes to prevent crashes.

---

## 📥 Quick Installation (One-Liner)
No need to download anything manually. Paste this into your terminal and press Enter:

```bash
curl -sSL https://raw.githubusercontent.com/Gheris-579/EasyZsh/main/EasyZsh/install.sh | bash
```
After installation, restart your terminal and simply type:
```bash
easyzsh
```

# 🛠️ Requirements
- OS: Ubuntu, Debian, Parrot OS, Kali Linux, Pop!_OS.
- Python: 3.x (the installation script checks this for you).



## 🛠️ Roadmap (Upcoming Features)

We are constantly working to make EasyZsh even better. Here is what's coming next:

*   🎨 **Powerlevel10k Integration:** Automatic setup for the most popular and fastest Zsh theme.
*   📦 **Flatpak & Snap Support:** One-click installation for modern containerized applications.
*   🐧 **Cross-Distro Compatibility:** Expanding support for Arch Linux (pacman) and Fedora (dnf).



## 🤝 Contributing
Want to add a new banner or a new plugin? 
1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request


# 📂 Complete Project Structure
- **easyzsh.py:** Il file principale (Main) che l'utente lancia per aprire il menu.
- **install.sh:** The Bash script used for quick installation through the `curl` command.
- **LICENSE:** The MIT license that protects the project’s source code.
- **README.md:** The presentation page containing instructions, screenshots, and project information.
- **config.json:** The file, created automatically, that stores the username and Zsh installation status.
- **modules/__init__.py:** The required empty file that tells Python the folder contains modules.
- **modules/core.py:** The “engine” that contains `run_task` and the `apt` system commands.
- **modules/zsh_manager.py:** The “specialist” responsible for installing Oh My Zsh, plugins, and the custom prompt.
- **modules/art.py:** Your “art gallery” containing the 11 ASCII banners and color codes (`Re`, `Gr`, `Blu`).
- **modules/config_manager.py:** The manager that reads and writes data to the JSON configuration file.
- **modules/ui_utils.py:** (If created) The file that contains UI helper functions such as `clear()` or `show_header()`.



# 📸 Menu Preview
<img width="1106" height="657" alt="image" src="https://github.com/user-attachments/assets/b3e49e39-0631-402c-8a5a-1b70b9ea0f2b" />


# Video 📼

https://github.com/user-attachments/assets/7682c5d7-c735-44b1-809e-bdd8dee2413c


# SCREEN

<img width="1343" height="917" alt="image" src="https://github.com/user-attachments/assets/4997c410-01bf-4bb6-bc96-f710dbaf3b28" />

<img width="1195" height="808" alt="image" src="https://github.com/user-attachments/assets/97fda2c1-ce52-41b3-949e-0b7a852758ff" />

<img width="1183" height="809" alt="image" src="https://github.com/user-attachments/assets/668c7c34-80b0-44f3-8241-996792fa50ee" />

<img width="1257" height="925" alt="image" src="https://github.com/user-attachments/assets/740ceea3-c6e7-463a-952e-e6beb19d6685" />

<img width="1252" height="803" alt="image" src="https://github.com/user-attachments/assets/04a19ddf-4536-4f68-b8f8-0ba93b953a61" />

<img width="1215" height="730" alt="image" src="https://github.com/user-attachments/assets/49b9a219-0cf1-48de-afb3-74f38762c6d8" />

<img width="1247" height="924" alt="image" src="https://github.com/user-attachments/assets/5b3f60a6-ed5d-4a64-a66c-b79d56bc3bab" />

<img width="1222" height="806" alt="image" src="https://github.com/user-attachments/assets/9ce75e1b-58ff-487d-9a02-7562924bd9de" />

<img width="1361" height="910" alt="image" src="https://github.com/user-attachments/assets/40a5540a-8f55-4f86-810d-601ce523302c" />

<img width="1374" height="922" alt="image" src="https://github.com/user-attachments/assets/bec654b7-aee3-4795-b87c-7c8732fb3e77" />

<img width="1437" height="891" alt="image" src="https://github.com/user-attachments/assets/56a130f3-4b70-479d-a319-2b8db79b4f75" />

<img width="1314" height="688" alt="image" src="https://github.com/user-attachments/assets/070d023f-b95d-4048-884d-d0f853deaf01" />

<img width="1123" height="601" alt="image" src="https://github.com/user-attachments/assets/785e8b50-1d2c-4ec5-a4c9-ab53fb98742f" />

<img width="1082" height="649" alt="image" src="https://github.com/user-attachments/assets/1e761f90-0bfb-46ff-9ac8-eeaf0ea97730" />

<img width="1035" height="644" alt="image" src="https://github.com/user-attachments/assets/943a0aa1-0c74-4cf3-baf0-c92978f1b09d" />

<img width="763" height="333" alt="image" src="https://github.com/user-attachments/assets/dd743ffb-a5be-4b8a-9759-4665b85c4ef7" />

<img width="1021" height="670" alt="image" src="https://github.com/user-attachments/assets/c4e8c68a-3f7b-47e0-9ba9-bb8c8993c8cc" />

<img width="1051" height="643" alt="image" src="https://github.com/user-attachments/assets/1a71f8f2-72a3-496e-81cc-cb4594859e1f" />

<img width="1165" height="674" alt="image" src="https://github.com/user-attachments/assets/7f26fedc-adc6-4fc6-8e13-c470f210125e" />





