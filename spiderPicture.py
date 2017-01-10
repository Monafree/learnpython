# -*- coding: UTF-8 -*-
import re
import urllib
import urllib2
import os


def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def mkdir(path):
	path = path.strip()

	isExists = os.path.exists(path)
	if not isExists:
		os.makedirs(path)
		return True
	else:
		return False

def saveImages(imglist, name):
	number = 1
	for imageURL in imglist:
		print imageURL
		splitPath = imageURL.split('.')
		fTail = splitPath.pop()
		if len(fTail) > 3:
			fTail = 'jpg'
		fileName = name + '/' + str(number) + '.' + fTail

		try:
			# u = urllib2.urlopen('https://imgsa.baidu.com/baike/s%3D290/sign=3ab82b938282b90139adc43a438ca97e/a1ec08fa513d2697acaa08e95dfbb2fb4316d80d.jpg')
			u = urllib2.urlopen(imageURL.lstrip('src="'))
			data = u.read()
			print data

			f = open(fileName, 'wb+')
			f.write(data)
			print ("save pic ", fileName)
			f.close()
		except urllib2.URLError as e:
			
			print(e.reason)
		number += 1

def getAllImg(html):
	reg = r'src=.+\.jpg'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	print imglist
	return imglist

if __name__ == '__main__':
	url = u'https://baike.baidu.com/pic/宋民国/19775279'.encode('utf=8')
	html = getHtml(url)
	# print html
	path = "spiderPicture"
	mkdir(path)
	imglist = getAllImg(html)
	saveImages(imglist, path)
