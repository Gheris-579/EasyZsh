# Install Zsh on Ubuntu (Step by Step)
# Create by Gheris
# inizio del programma 19/02/2026
# Nome del programma EasyZsh
import sys
import time
import modules.art as art
import modules.core as core
import modules.config_manager as config_manager
import modules.zsh_manager as zsh_manager








def menu():
    # Carica le impostazioni dal JSON
    settings = config_manager.load_settings()


    while True:
        art.clear()
        # LOGICA BANNER DINAMICO
        if settings.get('is_zsh_installed', False):
            print(art.bannerszsh)
        else:
            print(art.helloprimo)

        print(f"\nHello {settings.get('user_name', 'Utente')}, Welcome to EasyZsh!")

        print(f"""\n
            1, Update Systeme-|_
                                |– Update
                                |-Full Upgrade                          
            2, AutoRemove
            3, Install Zsh
            4, Install Oh My Zsh (Themes & Plugins)
            5, Install Autosuggestions Plugin
            6, Install Zsh Syntax Highlighting
            7, Automatic .zshrc Backup 
            8, Configure .zshrc Plugins \n
            99, Exit Bye 😭
            """)
        try:
            opzione = int(input(f"""\n{art.Re}┌─[{art.Cy}EasyZsh{art.Blu}~{art.Wh}@HOME{art.Re}]
└──╼{art.Wh}$ """))

            if opzione == 1:
                core.update_system()
            elif opzione == 2:
                core.system_cleanup()
            elif opzione == 3:
                zsh_manager.install_zsh()
            elif opzione == 4:
                zsh_manager.install_oh_my_zsh()
            elif opzione == 5:
                zsh_manager.install_zsh_autosuggestions()
            elif opzione == 6:
                zsh_manager.install_syntax_highlighting()
            elif opzione == 7:
                zsh_manager.backup_zshrc()
            elif opzione == 8:
                zsh_manager.setup_zsh_plugin()
            elif opzione == 99:
                art.clear()
                print(art.banners_bye)
                sys.exit()
            else:
                art.clear()
                menu()

        except ValueError:
            print('Type number')
            time.sleep(1)
            art.clear()






if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print(f'\n{art.Wh}[ {art.Re}! {art.Wh}] {art.Re}Exit')



