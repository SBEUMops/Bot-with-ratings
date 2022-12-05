from selenium import webdriver
from fake_useragent import UserAgent
import time
import telebot

# from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
useragent = UserAgent()
token = ""
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['ocenka'])
def get_fact(message):
    options.add_argument(f'user-agent={useragent.random}')
    url = 'https://login.school.mosreg.ru/?ReturnUrl=https%3A%2F%2Fschool.mosreg.ru%2F'
    driver = webdriver.Chrome(
    executable_path=r"C:\Users\Zahar\PycharmProjects\pythonProject1\cromedbrowser\cromedbrowser.exe")
    # try:
    driver.get(url=url)

    login_input = driver.find_element("xpath", '/html/body/div/div/div/form/input[1]')
        # login_input.clear()
    login_input.send_keys("")
    password_input = driver.find_element("xpath", '/html/body/div/div/div/form/input[2]')
        # password_input.clear()
    password_input.send_keys("")

    driver.find_element("xpath",
                            '/html/body/div/div/div/form/input[3]').click()

        # time.sleep(2)
    driver.find_element("xpath", '//*[@id="login_notification_container"]/div[4]/a').click()

    driver.find_element("xpath", '/html/body/div[2]/div/div[2]/ul/li[1]/ul/li[3]/a').click()

    driver.find_element("xpath", '//*[@id="TabPeriod"]').click()
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0,450)")
    time.sleep(5)
    driver.save_screenshot('govono.png')

    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     driver.close()
    #     driver.quit()
    bot.send_photo(message.chat.id, photo=open(r'C:\Users\Zahar\Desktop\govono.png', 'rb'))
    bot.send_message(message.chat.id,'Ваши оценки')

bot.polling()