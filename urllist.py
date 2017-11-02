import os
from bs4 import BeautifulSoup as soup
import re
from urllib2 import urlopen

def scrape(_url):
	f = urlopen(_url)
	s = soup(f, "html.parser")
	s = s.get_text()
	emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)
	if len(emails) == 0:
		print("Sorry, no emails found")
	else:
		count = 1
		for item in emails:
			print(item)


def urlHandler(file1):
	f = open(file1, "r")
	for line in f:
		scrape(line.strip())
	return line
	f.close()


def getFile():
	_fileName = raw_input("Enter file name: ")
	urlHandler(_fileName)
	return _fileName


def main():	
	getFile()

main()
   