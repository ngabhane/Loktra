'''
Author	: Nikhil Gabhane
Date	: Sept 20, 2016 
'''

import re
import urllib2
from sys import argv

class crawler(object):
	def __init__(self, keyword):
		keyword = keyword.strip()
		self.keyword = keyword.replace(' ','%20')

	def GetNumberOfResults(self,url):
		url = url + self.keyword
		web_data = urllib2.urlopen(url)
		data = web_data.read()
		pattern  = re.compile(ur'Results 1 - (.*)', re.MULTILINE)
		response = re.findall(pattern, data)
		try:
			response = response[0].split('of')[1]
			response = response.strip()
		except:
			print "No results found for the keyword '%s'" % self.keyword
			return 0
		try:
			response = response.split('&')
			if response[1] == '#43;':
				return response[0]+'+'
			else:
				return response[0]
		except:
			return response[0]

	def GetResults(self,url):
		url = url + self.keyword
		web_data = urllib2.urlopen(url)
		data = web_data.read()
		try:
			data = (data.split("searchResultsContainer"))[1]
		except:
			print "No results found for the keyword '%s' on page number '%s'" % (self.keyword,argv[2])
			return 0
		try:
			data = (data.split("paginationNew"))[0]
		except:
			pass
		pattern = re.compile(ur'class=\"productName.*title=\"(.*)\"|<span.*title=\"((?!.*Quick\ View).*)\"', re.MULTILINE)
		response = re.findall(pattern, data)			
		found = []
		for i in response:
			if i[0]:
				found.append(i[0])
			elif i[1]:
				found.append(i[1])
		return found

if __name__ == "__main__":
	crawl = crawler(argv[1])
	# If more than 3 arguments are provided, then the code will simply ignore arguments beyond 3 and execute normally
	if len(argv) >= 3:
		results = crawl.GetResults('http://www.shopping.com/products~PG-'+argv[2]+'?KW=')
		if results != 0:
			print "\nFollowing Results are found for keyword '%s' on page number '%s':\n %s" %(argv[1],argv[2],results)
			print '\n'
	elif len(argv) == 2:
		results = crawl.GetNumberOfResults('http://www.shopping.com/products?KW=')
		if results != 0:
			print "\n Total number of Results found for keyword '%s' : %s" %(argv[1],results)
			print '\n'
	else:
		print "Please provide required arguments"