"""
import re
test = re.findall("a.*c","Abbfc",re.IGNORECASE)
#test.group()
print(test)

str = "Hello this is <pritam> and <seema>"

result = re.sub("<.*>","PRITAM",str)
print(result)


#Check if given number is prime or not
n = int(input("Enter the number : "))
if(n>1):
    for i in range(2,n):
        if (n%i) == 0:
            print("Number is Not Prime")
            break
    else:
        print("Number is prime")
else:
    print("OUT-Number is Not Prime")


from urllib.request import urlopen



page = urlopen("http://olympus.realpython.org/profiles/dionysus")
html = page.read().decode('utf-8')
#print(html)

title = html.find("<TITLE >")
#print(title)

start_index = title + len("<title >")
end_index = html.find("</title  / >")

printTitle = html[start_index:end_index]
print(printTitle)


from urllib.request import urlopen
import re

page = urlopen("http://olympus.realpython.org/profiles/dionysus")
html = page.read().decode('utf-8')

pattern = "<title.*?>.*?</title.*?>"

match = re.search(pattern,html,re.IGNORECASE)
title = match.group()
#print(title)
title = re.sub("<.*?>"," ",title)
print(title)

"""

import re
from urllib.request import urlopen
page = urlopen("http://olympus.realpython.org/profiles/dionysus")
html = page.read().decode("utf-8")
#print(html)

list = ["Name:","Favorite Color:"]
for i in list:
    text_start_idx  = html.find(i) + len(i)
    print(text_start_idx,len(i))
    next_index = html[text_start_idx:].find("<")

    text_end_idx =text_start_idx  + next_index

    raw_test = html[text_start_idx : text_end_idx]
    print(raw_test)

    clear_text = raw_test.strip("\r\n\t")

