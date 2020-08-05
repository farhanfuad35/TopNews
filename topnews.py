from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.thedailystar.net/"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# head = soup.find("div", {"class":"intro-box"})
head = soup.find(class_='intro-box')
attr = head.find("a")
full_text = head.p.string
print('### ', attr.text, ' ###')
print(full_text)
print('\n')
prompt = input("Do you want to read the full news? y/n: ")
if prompt is 'y':
	print('---------------------------------------------------------------')
	newsLink = attr.get('href')
	url = url + newsLink
	topNewsHtml = urlopen(url, context=ctx).read()
	topNewsSoup = BeautifulSoup(topNewsHtml, "html.parser")
	topNewsDiv = topNewsSoup.find(class_='field-body view-mode-full')
	topNewsParas = topNewsDiv.find_all("p")
	for para in topNewsParas:
		print('')
		print(para.string)