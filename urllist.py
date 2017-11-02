import urllib2
import re

def scrape(_url):

	user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
	headers = { 'User-Agent' : user_agent }
	req = urllib2.Request(_url, None, headers)
	response = urllib2.urlopen(req)
	page = response.read()
	emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",page)
	_noDups = list(set(emails))

	if len(_noDups) == 0:
		noEmailFound(_url)
	else:

		for line in _noDups:
			print line.strip()

	response.close()


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

def noEmailFound(_url):
	print ("-------------------------------------")
	print ("Sorry no emails found on url: " + _url)
	print ("-------------------------------------")


def main():	
	getFile()

main()
