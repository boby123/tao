# coding = utf-8

from selenium	import	webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time,unittest
class Cunbai(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.get("http://139.196.18.143:10000/user/user/login")
	def testLogin(self):
		u'''存呗登陆测试'''
		self.browser.find_element_by_class_name("com_input_text").send_keys("13524868549")
		self.browser.find_element_by_id("pass").send_keys("123456")
		self.browser.find_element_by_id("toLogin").click()
		time.sleep(3)
	def tearDown(self):
		self.browser.quit()
if __name__== "__main__":
	unittest.main()