from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
import telebot
import os


optionz = Options()
optionz.add_argument("--headless=new")

link = "https://www.instagram.com/"

class_name = "xpdipgo.x972fbf.xcfux6l.x1qhh985.xm0m39n.xk390pu.x5yr21d.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xl1xv1r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf.xh8yej3"
class_name1 = "_aadp"

API_TOKEN = 'API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, "Send the username")

    bot.register_next_step_handler(message, send_pfp)


def send_pfp(username):
    bot.send_message(username.chat.id, f"Grazie {username.text} il tuo messaggio è stato ricevuto!")
    url = link + username.text
    driver = webdriver.Chrome(options=optionz)
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

    username_clean = (username.text).replace(".", "-")

    filename_user = username_clean + "png"

    with open(filename_user, 'wb') as handler:
        handler.write(img_data)

    bot.send_photo(username.chat.id, open(filename_user, "rb"))

    os.remove(filename_user)


bot.infinity_polling()