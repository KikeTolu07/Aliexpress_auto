from selenium import webdriver

from values import  source



class Drive:
    def __init__(self):
        self.driver = webdriver.Chrome()


    def launch_site(self, url):
        self.driver.get(url)

