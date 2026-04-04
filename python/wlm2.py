from lxml import etree
from bs4 import BeautifulSoup
import json

utf8_parser = etree.XMLParser(encoding='utf-8',recover=True)

# read the data from the file
file="wlm.xml"
with open(file,"r") as myfile:
    data=myfile.read()
data = data.replace('\n',"")  

soup = BeautifulSoup(data,  'xml')
s = soup.select("ClassificationGroup")
for ss in s:
  print("!!!",ss)
# print(s,type(s))
quit()
#print(str(soup))
# print(soup.prettify(formatter="minimal"))
i = 0;
#data = {}
# = json.dumps(soup)
#rint(r)
#for tag in soup.find_all():
#  print(0,tag)
#  i += 1
       #if not tag.name in data:
       #    data[tag.name] = []
     #
     #  attrs = {k: v for k, v in tag.attrs.items()}
     #  data[tag.name].append(attrs)
#print(data)
x =soup.prettify()
#for xx in x:
#  print(i,xx)
#  i += 1
print(x)
#or x in soup:#
#print(i,x)
#i += 1
	
#nonBreakSpace = u'\xa0'
'''
tables = soup.find_all(['table'])
for table in tables:
    tr = table.find_all("tr")
    for t in tr:
        line = list(t)
        if len(line) == 11:            
            print(line[1].get_text().strip(),line[7].get_text().strip())
        else: 
            print("len:",len(line),line)
'''            
quit() 
