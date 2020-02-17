from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self, headless=False):
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            self.driver = webdriver.Chrome('../../chromedriver', options=options)
        else:
            self.driver = webdriver.Chrome('../../chromedriver')
        self.driver.maximize_window()
    
    def navigate(self, link):
        self.driver.get(link)
    
    def wait(self, by=By.ID, element=None, wait_sec=5):
        try:
            element = WebDriverWait(self.driver, wait_sec).until(
                EC.presence_of_element_located((by, element)))
            return True
        except:
            print('Wait Timeout')
            return False
    
    def slowly_scroll(self, height_to_scroll=400, wait_sec=2):
        scrolled = height_to_scroll
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        for timer in range(page_height // height_to_scroll + 1):
            self.driver.execute_script("window.scrollTo(0, "+str(scrolled)+")")
            scrolled += height_to_scroll  
            time.sleep(wait_sec)
    
    def find_element_by_text(self, text='some text'):
        return self.driver.find_element_by_xpath(f"//*[contains(text(), '{text}')]")
    
    def find_elements_by_text(self, text='some text'):
        return self.driver.find_elements_by_xpath(f"//*[contains(text(), '{text}')]")
        
