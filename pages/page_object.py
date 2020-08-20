from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

from web_config import Drive

from values import source


class GuestShopper:

    def __init__(self):
        self.site = Drive()

    def setup(self, url):
        self.site.launch_site(url)

    def search_and_click(self, box, item, button):
        self.site.driver.find_element_by_css_selector(box).send_keys(item)
        self.site.driver.find_element_by_css_selector(button).click()

    def close_popup(self):
        WebDriverWait(self.site.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, source.ali_popup)))
        self.site.driver.find_element_by_css_selector(source.ali_close_popup).click()

    def scroll_page(self):
        self.site.driver.execute_script("window.scrollTo(0, 1000)")

    def select_item(self, pick):
        WebDriverWait(self.site.driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, pick)))
        self.site.driver.find_element_by_css_selector(pick).click()

    def scroll(self):
        self.site.driver.switch_to_window(self.site.driver.window_handles[1])
        self.site.driver.execute_script("window.scrollTo(0,500)")

    # def select_country(self):
        # WebDriverWait(self.site.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, source.select_count)))
        # action = ActionChains(self.site.driver)
        # element = self.site.driver.find_element_by_css_selector(source.select_count)
        # action.click(element).perform()
        # # element = self.site.driver.find_element_by_css_selector(source.select_count)
        # # self.site.driver.execute_script("arguments[0].click();", element)
        # self.site.driver.find_element_by_css_selector(source.select_count).send_keys(Keys.ENTER)


    def add_to_cart(self, add, new):
        WebDriverWait(self.site.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, add)))
        self.site.driver.find_element_by_css_selector(add).click()
        WebDriverWait(self.site.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, new)))

    def view_item(self):
        self.site.driver.find_element_by_css_selector(source.ali_view_shop_cart).click()

    def check_out(self, buy, new):
        WebDriverWait(self.site.driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, new)))
        self.site.driver.find_element_by_css_selector(buy).click()


    def verify_page(self, word):
        title = self.site.driver.title

        try:
            assert  word in title
            print("Assertion Failed")

        except AssertionError:
            "Text not found"
            print("Assertion Passed")











