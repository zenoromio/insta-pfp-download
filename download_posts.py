from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests

optionz = Options()
#optionz.add_argument("--headless=new")

driver = webdriver.Chrome(options=optionz)

link = "https://www.instagram.com/zeno.romio"

driver.get(link)

sleep(5)

posts = driver.find_elements(By.CLASS_NAME, "_aagv")
posts_link = []
for i in posts:
    post = i.find_element(By.TAG_NAME, "img")
    posts_link.append(post.get_attribute("src"))


for num, url in enumerate(posts_link):
    img_data = requests.get(url).content
    with open((str(num) + ".jpg"), 'wb') as handler:
        handler.write(img_data)