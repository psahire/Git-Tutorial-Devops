import re
from urllib.request import urlopen

page = urlopen("https://www.adecco.ca/")
#print(page)

html = page.read().decode('utf-8')
#print(html)


search = re.findall('<title.*?>',html)
print(search)