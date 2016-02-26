from selenium	import	webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time,unittest
class Cunbai(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.get("http://139.196.18.143:10000/user/user/login")
		time.sleep(1)
		self.browser.find_element_by_class_name("com_input_text").send_keys("13524868549")
		self.browser.find_element_by_id("pass").send_keys("123456")
		self.browser.find_element_by_id("toLogin").click()
		time.sleep(3)
	def testGouMainLiu(self):
		u'''测试定期购买6个月'''
		browser=self.browser
		try:
			browser.find_element_by_class_name("m_money").click()
			browser.find_element_by_partial_link_text("6").click()
			browser.find_element_by_class_name("com_button").click()
			time.sleep(3)
			browser.find_element_by_id("money").send_keys("1000")
			mony=browser.find_element_by_id("money").get_attribute("value")
			mony=int(mony)
			time.sleep(2)
			browser.find_element_by_class_name("com_bank").click()
			time.sleep(2)
			m=browser.find_element_by_partial_link_text(u"余额")
			yu=m.find_element_by_class_name("t_num").text
			if len(yu)>5 :
				yu=yu.replace(',','')
				yu=int(yu[1:len(yu)-1])
			else:
				yu=int(yu[1:len(yu)-1])
			if yu > mony :
				try:
					browser.find_element_by_partial_link_text(u"余额").click()
					time.sleep(2)
				except:
					print(u"控件未点击")
			else:
				try:
					browser.find_element_by_partial_link_text(u"建设银行").click()
					time.sleep(3)
				except:
					print(u"就是找不到啊")
			browser.find_element_by_id("com_button").click()
			browser.find_element_by_class_name("key10").click()
			browser.find_element_by_class_name("key10").click()
			browser.find_element_by_class_name("key10").click()
			browser.find_element_by_class_name("key10").click()
			browser.find_element_by_class_name("key10").click()
			browser.find_element_by_class_name("key10").click()
			time.sleep(5)
			url='http://139.196.18.143:10000/account/transaction/success'
			cur_url=browser.current_url
			if url==cur_url:
				print(u"支付成功")
				browser.find_element_by_id("com_button").click()
				
			else:
				print(u"支付失败")
		except:
			# print(u"控件查找错误:")
			browser.get_screenshot_as_file('E:\\Cunbai\\ErrorImage\error_png.png')
	def tearDown(self):
		self.browser.quit()
if __name__== "__main__":
	unittest.main()
