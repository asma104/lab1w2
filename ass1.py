import re
import urllib
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/comments_820335.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup.find_all('span')
nums = list()
for tag in tags:
    num = re.findall('[0-9]+',str(tag))
    nums += num
numbers = [ int(x) for x in nums ]
print(sum(numbers))
