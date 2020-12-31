import json
import urllib3
import tkinter as tk
from urllib.request import urlretrieve
from PIL import ImageTk, Image


class Photo:
    def __init__(self, types):
        self.types = types
        self.image_path = f'./types/{self.types}.png'

    def get_image(self):
        self.image_path = Image.open(self.image_path)
        self.image_path = self.image_path.resize((25, 25), Image.ANTIALIAS)
        return self.image_path


root = tk.Tk()

combos = {"rocknormal": 0.5,
          "ghostnormal": 0,
          "steelnormal": 0.5,
          "firefire": 0.5,
          "waterfire": 0.5,
          "grassfire": 2,
          "icefire": 2,
          "bugfire": 2,
          "rockfire": 0.5,
          "dragonfire": 0.5,
          "steelfire": 2,
          "firewater": 2,
          "waterwater": 0.5,
          "grasswater": 0.5,
          "groundwater": 2,
          "rockwater": 2,
          "dragonwater": 0.5,
          "firegrass": 0.5,
          "watergrass": 2,
          "grassgrass": 0.5,
          "poisongrass": 0.5,
          "groundgrass": 2,
          "flyinggrass": 0.5,
          "buggrass": 0.5,
          "rockgrass": 2,
          "dragongrass": 0.5,
          "steelgrass": 0.5,
          "waterelectric": 2,
          "grasselectric": 0.5,
          "electricelectric": 0.5,
          "groundelectric": 0,
          "flyingelectric": 2,
          "dragonelectric": 0.5,
          "fireice": 0.5,
          "waterice": 0.5,
          "grassice": 2,
          "iceice": 0.5,
          "groundice": 2,
          "flyingice": 2,
          "dragonice": 2,
          "steelice": 0.5,
          "normalfighting": 2,
          "icefighting": 2,
          "poisonfighting": 0.5,
          "flyingfighting": 0.5,
          "psychicfighting": 0.5,
          "bugfighting": 0.5,
          "rockfighting": 2,
          "ghostfighting": 0,
          "darkfighting": 2,
          "steelfighting": 2,
          "fairyfighting": 0.5,
          "grasspoison": 2,
          "poisonpoison": 0.5,
          "groundpoison": 0.5,
          "rockpoison": 0.5,
          "ghostpoison": 0.5,
          "steelpoison": 0,
          "fairypoison": 2,
          "fireground": 2,
          "grassground": 0.5,
          "electricground": 2,
          "poisonground": 0.5,
          "flyingground": 0,
          "bugground": 0.5,
          "rockground": 2,
          "steelground": 2,
          "grassflying": 2,
          "electricflying": 0.5,
          "fightingflying": 2,
          "bugflying": 2,
          "rockflying": 0.5,
          "steelflying": 0.5,
          "fightingpsychic": 2,
          "poisonpsychic": 2,
          "psychicpsychic": 0.5,
          "darkpsychic": 0,
          "steelpsychic": 0.5,
          "firebug": 0.5,
          "grassbug": 2,
          "fightingbug": 0.5,
          "poisonbug": 0.5,
          "flyingbug": 0.5,
          "psychicbug": 2,
          "ghostbug": 0.5,
          "darkbug": 2,
          "steelbug": 0.5,
          "fairybug": 0.5,
          "firerock": 2,
          "icerock": 2,
          "fightingrock": 0.5,
          "groundrock": 0.5,
          "flyingrock": 2,
          "bugrock": 2,
          "steelrock": 0.5,
          "normalghost": 0,
          "flyingghost": 2,
          "ghostghost": 2,
          "darkghost": 0.5,
          "steelghost": 0.5,
          "dragondragon": 2,
          "steeldragon": 0.5,
          "fairydragon": 0,
          "fightingdark": 0.5,
          "psychicdark": 2,
          "ghostdark": 2,
          "darkdark": 0.5,
          "steeldark": 0.5,
          "fairydark": 0.5,
          "firesteel": 0.5,
          "watersteel": 0.5,
          "icesteel": 2,
          "rocksteel": 2,
          "steelsteel": 0.5,
          "fairysteel": 2,
          "firefairy": 0.5,
          "fightingfairy": 2,
          "poisonfairy": 0.5,
          "dragonfairy": 2,
          "darkfairy": 2,
          "steelfairy": 0.5}

attack_types = {'normal': 1.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'ice': 1.0, 'fighting': 1.0, 'poison': 1.0,
                'ground': 1.0, 'flying': 1.0, 'psychic': 1.0, 'bug': 1.0, 'rock': 1.0, 'ghost': 1.0, 'dragon': 1.0, 'dark': 1.0,
                'steel': 1.0, 'fairy': 1.0}

colors = ('wheat3', 'dark orange', 'SteelBlue1', 'chartreuse3', 'gold', 'CadetBlue1', 'firebrick4', 'DarkOrchid4',
          'LightGoldenrod2', 'MediumPurple2', 'VioletRed2', 'DarkOliveGreen3', 'DarkGoldenrod3', 'purple4', 'blue violet',
          'DarkOrange4', 'plum1', 'HotPink1')

label_list = []


def reset():
    global attack_types
    search_again.place_forget()
    button1.place(x=75, y=150, width=150)
    entry1.place(x=75, y=100, width=150, height=25)
    for label in label_list:
        label.destroy()
    canvas1.image = ''
    canvas1.image2 = ''
    attack_types = {'normal': 1.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'ice': 1.0,
                    'fighting': 1.0, 'poison': 1.0,
                    'ground': 1.0, 'flying': 1.0, 'psychic': 1.0, 'bug': 1.0, 'rock': 1.0, 'ghost': 1.0, 'dragon': 1.0,
                    'dark': 1.0,
                    'steel': 1.0, 'fairy': 1.0}


def load_pokemon_name(url):
    global label_list
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    pokemon = json.loads(response.data.decode('utf-8'))
    name = pokemon["name"].capitalize()
    label = tk.Label(bg="white", text=name, anchor='center', font=('Arial', 12, "bold"))
    label.place(x=110, y=120)
    label_list.append(label)


def load_pokemon_stats():
    x = 65
    y = 150
    image_list = []
    global label_list
    for color, types in enumerate(attack_types):
        labels = tk.Label(bg=colors[color], fg='White', text=f'{attack_types[types]}x', width=7, font=('Arial', 12, "bold"))
        labels.place(x=x, y=y)
        label_list.append(labels)
        if y < 425:
            y += 35
        else:
            x = 190
            y = 150
    for types in attack_types:
        image = Photo(types)
        photo = ImageTk.PhotoImage(image.get_image())
        image_list.append(photo)
    x = 65
    y = 150
    canvas1.image2 = image_list
    for photo in image_list:
        canvas1.create_image(x-20, y + 12, image=photo)
        if y < 425:
            y += 35
        else:
            x = 190
            y = 150
    root.update()


def load_pokemon_image(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    pokemon = json.loads(response.data.decode('utf-8'))
    image_url = pokemon["sprites"]["front_default"]
    urlretrieve(image_url, "./Pokemon.png")
    image = Image.open("./Pokemon.png")
    image = image.resize((150, 150), Image.NEAREST)
    photo = ImageTk.PhotoImage(image)
    canvas1.image = photo
    canvas1.create_image(150, 75, image=photo)


def delete_windows():
    button1.place_forget()
    entry1.place_forget()


def check_pokemon_reactions(url):
    global combos
    global attack_types
    test = 0
    defend_types = get_pokemon_type(url)
    if not defend_types:
        return
    delete_windows()
    for defend_type in defend_types:
        for attack_type in attack_types.keys():
            combo = f'{defend_type["type"]["name"]}{attack_type}'
            if combo in combos:
                attack_types[attack_type] *= combos[combo]
    load_pokemon_image(url)
    load_pokemon_name(url)
    search_again.place(x=75, y=470, width=150)
    load_pokemon_stats()



def get_pokemon_name(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    pokemon = json.loads(response.data.decode('utf-8'))
    return pokemon['name']


def get_pokemon_type(url):
    try:
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        pokemon = json.loads(response.data.decode('utf-8'))
        return pokemon["types"]
    except json.JSONDecodeError:
        print("This is not a valid pokemon")
    except urllib3.exceptions.ProtocolError:
        print("You are not connected to the internet")
    except urllib3.exceptions.ConnectTimeoutError:
        print('Your connection timed out')
    except KeyError:
        print("Please enter a Pokemon")


def main():
    pokemon = entry1.get().lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
    check_pokemon_reactions(url)


canvas1 = tk.Canvas(root, width=300, height=500, bg='White')
canvas1.pack()
canvas1.create_window(1000, 1000)
entry1 = tk.Entry(root, bg='PaleTurquoise1')
entry1.place(x=75, y=100, width=150, height=25)
button1 = tk.Button(text='Search for Pokemon', command=main, bg='brown1')
button1.place(x=75, y=150, width=150)
search_again = tk.Button(text='Search Again', command=reset, bg='brown1')


root.mainloop()