#this is Link Collector Version 1
#Author: Omkar
#Date: 01/10/2016

from bs4 import BeautifulSoup as bs
from pymongo import MongoClient
import urllib2
import collections
import tldextract

done_links = {} #Global link,score store
refined_href_list = []


#Function for Proxy Handler
def proxyHandler():

	proxy=urllib2.ProxyHandler({})
	opener=urllib2.build_opener(proxy)
	opener.addheaders=[('User-agent','Mozilla/5.0')]
	urllib2.install_opener(opener)


def forPrinter(element):
	for i in element:
		print i


def hrefRefiner(element):
	refined_href_list = []
	
	for link in element:
		if link.startswith('//', 0, 2):
	
			refined_href_list.append('http:'+link)
	
		elif (link.startswith('http', 0, 4) or
				link.startswith('https', 0, 5) or
				link.startswith('www', 0, 3)):
	
			refined_href_list.append(link)
			myfile = open("links.txt", "a")
			myfile.write(link+"\n")

			myfile = open("links_domain.txt", "a")
			ext = tldextract.extract(link)
			myfile.write(ext.domain+"\n")


	return refined_href_list


def hrefExtractor(urltoopen):

	proxyHandler()

	print "--------------------------"
	print done_links
	print "LENGTH : ", len(refined_href_list)
	if urltoopen in done_links.keys():
		
		done_links[urltoopen] += 1         # existing url, add 1
		
		counter = collections.Counter(refined_href_list)
		done_links[urltoopen] += counter[urltoopen]   #counting duplicate links
		
		for i in range(counter[urltoopen]):
			refined_href_list.remove(urltoopen)			#removing duplicate links

	else:
		done_links[urltoopen] = 1          # New url , score 1

		url = urllib2.urlopen(urltoopen).read()
		soup = bs(url)

		href_list = []		#This dictionary stores all links found in the page and their scores

		for a in soup.find_all('a', href = True):
			href_list.append(a['href'])
	

		
		
	
		refined_href_list.extend(hrefRefiner(href_list))
		

	for link in refined_href_list:
		hrefExtractor(link)
	

urltoopen = "http://twitter.com/stackexchange"
hrefExtractor(urltoopen)






