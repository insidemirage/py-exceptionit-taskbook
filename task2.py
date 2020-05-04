from bs4 import BeautifulSoup
import requests
from random import choice
import string
MAIN_LINK = "https://klike.net"
LINK = "https://klike.net/1801-anime-krasivye-kartinki-50-foto.html"
symbols = string.ascii_letters + string.digits

def random_name():
    return "".join([choice(symbols) for i in range(30)])+".jpeg"


def download_images(images):
    for i,image in enumerate(images):
        with open(random_name(), "wb") as file:
            img = requests.get(MAIN_LINK + image.get("src"))
            file.write(img.content)
        print("="*20,f"Image {i} saved", "="*20)
def main():
    res = requests.get(LINK)
    soup = BeautifulSoup(res.text, 'html.parser')
    images = soup.find_all("img", class_="fr-dib")
    download_images(images)
if __name__ == "__main__":
    main()
