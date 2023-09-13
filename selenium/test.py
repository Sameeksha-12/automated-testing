from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import HtmlTestRunner

class SparkFoundationTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.thesparksfoundationsingapore.org/")

    def test_01_verify_logo(self):
        self.driver.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a')
        assert True

    def test_02_verify_nav_bar(self):
        self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul')
        assert True

    def test_03_know_more_button(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/a')
        a.click()
        time.sleep(2)
        assert True

    def test_04_learn_more_button(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/a')
        a.click()
        time.sleep(2)
        assert True

    def test_05_visit_now_button(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/a')
        a.click()
        time.sleep(2)
        assert True

    def test_06_explore_button (self):
        a = self.driver.find_element(By.XPATH,'//*[@id="owl-demo2"]/div[1]/div/div[1]/div/div[1]/div[1]/p/a')
        a.click()
        time.sleep(2)
        assert True

    def test_07_GRIP_link (self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/div[2]/ul/li[1]/a')
        a.click()
        time.sleep(2)
        assert True
    
    def test_08_scroll_to_top (self):
        a = self.driver.find_element(By.XPATH,'//*[@id="toTopHover"]')
        a.click()
        time.sleep(2)
        assert True

    def test_09_about_page(self):
        a = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[1]/a')
        a.click()
        time.sleep(2)
        b = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_10_policies_page(self):
        a = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[2]/a')
        a.click()
        time.sleep(2)
        b = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[2]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_11_programs_page(self):
        a = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[3]/a')
        a.click()
        time.sleep(2)
        b = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[3]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_12_links_page(self):
        a = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[4]/a')
        a.click()
        time.sleep(2)
        b = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[4]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_13_join_us_page(self):
        a = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[5]/a')
        a.click()
        time.sleep(2)
        b = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[5]/ul/li[1]/a')
        b.click()
        time.sleep(2)
        assert True

    def test_14_contact_page(self):
        a = self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[6]/a')
        a.click()
        time.sleep(2)
        assert True

    def test_15_facebook_page(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[1]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_16_linkedin_page(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[2]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_17_medium_page(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[3]/a/i')
        a.click()
        time.sleep(5)
        assert True

    def test_18_twitter_page(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[4]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_19_instagram_page(self):
        a = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[6]/a')
        a.click()
        time.sleep(5)
        assert True

    def test_20_fill_and_submit_info(self):
        a = self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div[1]/div[2]/ul/li[5]/a")
        a.click()
        time.sleep(2)
        name = self.driver.find_element(By.XPATH,'//input[@name="Name"]')
        time.sleep(2)
        name.send_keys('Sameeksha')
        time.sleep(2)
        email = self.driver.find_element(By.NAME,"Email")
        time.sleep(2)
        email.send_keys('sameekshareddy04@gmail.com')
        time.sleep(2)
        select = Select(self.driver.find_element(By.CLASS_NAME,"form-control"))
        time.sleep(2)
        select.select_by_visible_text('Student')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@value='Submit']").click()
        time.sleep(2)
        assert True

    def tearDown(self):
        self.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/pingi/Desktop/selenium/reports'))
