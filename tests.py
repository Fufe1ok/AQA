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
  
  def test_register_an_account(self):
    """Register new user account""" 
    self.driver.get("http://openncart.herokuapp.com/")
    self.driver.find_element_by_css_selector('#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md').click()
    time.sleep(2)
    self.driver.find_element_by_css_selector('#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a').click()
    time.sleep(2)
    self.driver.find_element(By.NAME, "firstname").send_keys("Yura")
    self.driver.find_element(By.NAME, "lastname").send_keys("Paneyko")
    self.driver.find_element(By.NAME, "email").send_keys("yura@gmail.com")
    self.driver.find_element(By.ID, "input-telephone").send_keys("0630275662")
    self.driver.find_element(By.NAME, "address_1").send_keys("lviv")
    self.driver.find_element(By.NAME, "city").send_keys("lviv")
    self.driver.find_element(By.NAME, "postcode").send_keys("79019")
    # self.driver.find_element(By.NAME, "country_id").send_keys("macbook")
    self.driver.find_element(By.ID, "input-zone").click()
    dropdown = self.driver.find_element(By.ID, "input-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Anglesey']").click()
    self.driver.find_element(By.ID, "input-password").send_keys("password_123")
    self.driver.find_element(By.ID, "input-confirm").send_keys("password_123")
    self.driver.find_element_by_css_selector('#content > form > div > div > input[type=checkbox]:nth-child(2)').click()
    self.driver.find_element_by_css_selector('#content > form > div > div > input.btn.btn-primary').click()

  def test_log_in(self):
    """ Log into your account """
    self.driver.get("http://openncart.herokuapp.com/")
    self.driver.find_element_by_css_selector('#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md').click()
    time.sleep(2)
    self.driver.find_element_by_css_selector('#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a').click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "email").send_keys("yura@gmail.com")
    self.driver.find_element(By.NAME, "password").send_keys("password_123")
    self.driver.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input").click()
    
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
    
    # time.sleep(15)
  
  
  
  
  
