# <-- Grafica, colori e banner ASCII
import os
import art

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_header(banner_name):
    art.clear()
    banner_text = getattr(art, banner_name, art.banners_bye)
    print(banner_text)
    print("-" * 50)  # Una linea di separazione elegante

show_header(banner_name="banner")
