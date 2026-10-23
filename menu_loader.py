import json
def load_menu():
    with open('menu.json', 'r') as f:
        menu = json.load(f)
    menu_text=""
    for name,price in menu.items():
        menu_text = menu_text + f"-{name}: AED {price}\n\n"
    return menu_text
