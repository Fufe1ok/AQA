import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_add_to_cart(self):
    """Add 15 macbooks pro to cart"""

    self.driver.get("http://openncart.herokuapp.com/")
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.NAME, "search").send_keys("macbook")
    self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
    time.sleep(2)
    self.driver.find_element_by_css_selector('#content > div:nth-child(10) > div:nth-child(3) > div > div.caption > h4 > a').click()
    quantity_field = self.driver.find_element(By.NAME, "quantity")
    actions = ActionChains(self.driver)
    actions.double_click(quantity_field).perform()
    self.driver.find_element(By.NAME, "quantity").send_keys("15")
    self.driver.find_element(By.ID, "button-cart").click()
    
    time.sleep(2)
  
  # def test_checkout(self):
  #   """Buy ordered macbooks""" 

  #   self.driver.find_element_by_css_selector('#cart > button').click()
  #   self.driver.find_element_by_css_selector('#cart > ul > li:nth-child(2) > div > p > a:nth-child(2) > strong').click()
    
  #   time.sleep(10)
  
