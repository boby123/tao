import HTMLTestRunner,os,sys
from selenium import webdriver
def importHtml(filename):
		fp=open(filename,'wb')
		runner=HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title='CunBai_report',
		description='test_case',
		)
		return runner
# dirname:包的相对路径
def addPath(dirname):
		osPath=r"dirname"
		print (dirname)
		if not osPath in sys.path:
			sys.path.append(osPath)
def findId(driver,id):
	f = driver.find_element_by_id(id)
	return f
def findName(driver,name):
	f = driver.find_element_by_name(name)
	return f
def findClassName(driver,name):
	f = driver.find_element_by_class_name(name)
	return f
def findTagName(driver,name):
	f = driver.find_element_by_tag_name(name)
	return f
def findLinkText(driver,text):
	f = driver.find_element_by_link_text(text)
	return f
def findPLinkText(driver,text):
	f = driver.find_element_by_partial_link_text(text)
	return f
def findXpath(driver,xpath):
	f = driverfind_element_by_xpath(xpath)
	return f
def findCss(driver,css):
	f = driver.find_element_by_css_selector(css)
	return f
