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


from selenium import webdriver
path = r'/usr/bin/chromedriver'
browser = webdriver.Chrome(executable_path = path)
browser.get('https://authoraditiagarwal.com/leadershipmanagement')
browser.find_element_by_xpath('/html/body').click()


