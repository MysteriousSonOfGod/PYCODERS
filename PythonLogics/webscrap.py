# import requests
# r = requests.get('https://authoraditiagarwal.com/')
# print(r.text[:200])

# import urllib3
# from bs4 import BeautifulSoup
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://authoraditiagarwal.com')
# soup = BeautifulSoup(r.data, 'lxml')
# print (soup.title)
# print (soup.title.text)


# from selenium import webdriver
# path = r'/usr/bin/chromedriver'
# browser = webdriver.Chrome(executable_path = path)
# browser.get('https://authoraditiagarwal.com/leadershipmanagement')
# browser.find_element_by_xpath('/html/body').click()


#Which technology is used by website?
import builtwith
# r=builtwith.parse('https://www.wikipedia.org/')
# print(builtwith.parse('https://www.wikipedia.org/'))
# print(builtwith.parse('https://www.facebook.com/'))
# print(builtwith.parse('https://www.hackerrank.com/'))
# print(builtwith.parse('https://www.google.co.in/'))
# print(builtwith.parse('https://www.instagram.com/'))
# print(builtwith.parse('https://web.whatsapp.com/'))
# print(builtwith.parse('https://www.amazon.in/'))
# print(builtwith.parse('https://www.flipkart.com/'))

# import whois
# # print(whois.whois('https://web.whatsapp.com/'))
# print(whois.whois('https://www.flipkart.com/'))
# print(whois.whois('https://www.amazon.in/'))
# print(whois.whois('https://www.wikipedia.org/'))



# import re
# import urllib.request
# response =urllib.request.urlopen('http://example.webscraping.com/places/default/view/India-102')
# html = response.read()
# text = html.decode()
# print(text)
# r=re.findall('<td class="w2p_fw">(.*?)</td>',text)
# print(r)


import requests
from bs4 import BeautifulSoup
import csv
import json
r = requests.get('https://authoraditiagarwal.com/')
soup = BeautifulSoup(r.text, 'lxml')
y = json.dumps(soup.title.text)
with open('JSONFile.txt', 'wt') as outfile:
   json.dump(y, outfile)





