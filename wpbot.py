from selenium import webdriver
from time import sleep


class whatsAppBot:
    def __init__(self):
        self.message = "Hi"
        self.groups = "Teste"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')

    def sendMessages(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for group in self.groups:
            group = self.driver.find_element_by_xpath(
                "//span[@title='{group}']")
            time.sleep(3)
            group.click()
            chat_box = self.driver.find_elements_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)
            button_send = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            button_send.click()
            time.sleep(5)

bot = whatsAppBot()
bot.sendMessages()


