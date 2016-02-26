import unittest
import HTMLTestRunner
import os,time
listaa=r'E:\Cunbai\test_case' 
def createSuitel():
	testUnit=unittest.TestSuite()
	discover=unittest.defaultTestLoader.discover(listaa,
	pattern='test*.py',
	top_level_dir=None)
	for test_suite in discover:
		for test_case in test_suite:
			testUnit.addTests(test_case)
			print(testUnit)
	return testUnit
alltestnames=createSuitel()
now = time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))
filename='E:\\Cunbai\\report\\'+now+'result.html' 
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u'存呗测试报告',
		description=u'存呗测试用例执行',
		)
# 控制什么时间执行脚本

k=1
while k<2:
	timing=time.strftime('%H_%M',time.localtime(time.time()))
	if timing=='19_18':
		print(u"开始运行脚本:")
		runner.run(alltestnames)
		print(u"运行完成退出:")
		break
	else:
		time.sleep(5)
		print(timing)