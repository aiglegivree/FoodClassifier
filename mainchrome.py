import os
from io import BytesIO

import requests
from PIL import Image

from selenium import webdriver

name = "avocado"
driver = webdriver.Chrome()
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

driver.close()
