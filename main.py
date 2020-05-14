import os
from io import BytesIO

import requests
from PIL import Image

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

list = [
"Breadfruit",
"Buddha's hand (fingered citron)",
"Cactus pear",
"Crab apple",
"Currant",
"Cherry",
"Cherimoya (Custard Apple)",
"Chico fruit",
"Cloudberry",
"Coconut",
"Cranberry",
"Damson",
"Date",
"Dragonfruit (or Pitaya)",
"Durian",
"Elderberry",
"Feijoa",
"Fig",
"Goji berry",
"Gooseberry",
"Grape",
"Grewia asiatica (phalsa or falsa)",
"Raisin",
"Grapefruit",
"Guava",
"Hala Fruit",
"Honeyberry",
"Huckleberry",
"Jabuticaba",
"Jackfruit",
"Jambul",
"Japanese plum",
"Jostaberry",
"Jujube",
"Juniper berry",
"Kiwano (horned melon)",
"Kiwifruit",
"Kumquat",
"Lemon",
"Lime",
"Loganberry",
"Loquat",
"Longan",
"Lychee",
"Mango",
"Mangosteen",
"Marionberry",
"Melon",
"Miracle fruit",
"Monstera Delisiousa",
"Mulberry",
"Nectarine",
"Nance",
"Orange",
"Papaya",
"Passionfruit",
"Peach",
"Pear",
"Persimmon",
"Plantain",
"Plum",
"Pineapple",
"Pineberry",
"Plumcot ",
"Pomegranate",
"Pomelo",
"Purple",
"Quince",
"Raspberry",
"Rambutan ",
"Redcurrant",
"Salal berry",
"Salak",
"Satsuma",
"Soursop",
"Star apple",
"Star fruit",
"Strawberry",
"Surinam cherry",
"Tamarillo",
"Tamarind",
"Tangelo",
"Tayberry",
"Ugli fruit",
"White currant",
"White sapote",
"Yuzu"
]
driver = webdriver.Firefox()
for name in list:
    driver.get(f"https://duckduckgo.com/?q={name}&atb=v214-1&ia=images&iax=images")
    os.mkdir(f"images/{name}")
    images = []

    for i in range(1, 50):
        img = driver.find_elements_by_xpath(f"/html/body/div[2]/div[3]/div/div/div[2]/div/div[{i}]/div[1]/span/img")
        images.append(img[0].get_attribute("src"))

    j = 0
    for i in images:
        response = requests.get(i)
        img = Image.open(BytesIO(response.content))
        img.save(f"images/{name}/{j}.jpg")
        j+=1

    
    print("done")

driver.close()
display.stop()
