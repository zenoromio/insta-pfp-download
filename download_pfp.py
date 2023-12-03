from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests

optionz = Options()
optionz.add_argument("--headless=new")


driver = webdriver.Chrome(options=optionz)

link = "https://www.instagram.com/"
username = "USERNAME"
url = link + username

class_name = "xpdipgo.x972fbf.xcfux6l.x1qhh985.xm0m39n.xk390pu.x5yr21d.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xl1xv1r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf.xh8yej3"
class_name1 = "_aadp"
driver.get(url)

sleep(4)

try:
    #this works for public profiles
    posts = driver.find_element(By.CLASS_NAME, class_name)
except:
    #this works for private profiles
    posts = driver.find_element(By.CLASS_NAME, class_name1)


image_url = posts.get_attribute("src")


img_data = requests.get(image_url).content

with open("pfp.jpg", 'wb') as handler:
    handler.write(img_data)