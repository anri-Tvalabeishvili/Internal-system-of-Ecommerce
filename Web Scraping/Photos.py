from bs4 import BeautifulSoup
from PIL import Image
import requests, time, json, os, random, string
from Links import *

path = f"{os.getcwd()}\\Data\\Products"
dir_list = os.listdir(path)
files = {}
categories = []


def download_img(name, link, filename):

    img = Image.open(requests.get(link, stream=True).raw)

    exist = os.path.exists(f'Data/Photos/{filename}')
    if not exist:
        os.makedirs(f'Data/Photos/{filename}')

    try:

        img.save(f'Data/Photos/{filename}/{name}.png')
        return True

    except:
        try:
            img.save(f'Data/Photos/{filename}/{name}.jpg')
            return True
        except:
            return False



counter = 1

for category in dir_list:
    new_path = f"{path}\\{category}"
    dir_list = os.listdir(new_path)
    if category != "Photos":
        categories.append(category)
        files[category] = dir_list


for category in categories:
    file_names = files[category]
    for file in file_names:
        opened_file = open(f"{path}\\{category}\\{file}", "r")
        data = opened_file.read()
        components = data.split(";\n")

        for component in components[0:-1]:
            component = eval(component)
            component_keys = list(component.keys())
            all_imgs = [i for i in component_keys if "online_img" in i]
            for i in range(len(all_imgs)):
                name = component["img" + str(i+1)][-34:-4]
                link = component["online_img" + str(i + 1)]
                print(f"downloading img number {counter}")
                download_img(name, link, file)
                counter += 1
                time.sleep(6)
        print(f"{file} is done")

