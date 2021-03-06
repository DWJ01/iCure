import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):
	
	def setUp(self):
		dire = os.path.dirname(os.path.abspath(__file__))
		chrome_driver_path = dire + "/chromedriver"
		self.driver = webdriver.Chrome(chrome_driver_path)


	def test_search(self):
		#assert "Login" in driver.title
		driver = self.driver
		driver.get("http://localhost:3000")
		input_search_box = driver.find_element_by_id("input-text-mainpage")
		input_search_box.clear()
		input_search_box.send_keys("Tonja Burlew")
		search_button = driver.find_element_by_id("search-button")
		search_button.click()
		assert "Tonja Burlew" in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()