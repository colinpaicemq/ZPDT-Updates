import pandas as pd
import xmltodict
import json
file="wlm.xml"
with open(file,"r") as myfile:
    data=myfile.read()
data = data.replace('\n',"")
book_dict = xmltodict.parse(data)

cg = book_dict["ServiceDefinition"]["ClassificationGroups"]["ClassificationGroup"]
for cg1 in cg:
  name = cg1["Name"]
  desc = cg1["Description"]
  qn = cg1["QualifierNames"]["QualifierName"]
  print("qn",qn,type(qn))
  for qn1 in qn:
    print("17",qn1,type(qn1))
    if isinstance(qn1, dict):
    	print(name,desc,qn1["Name"]) #,qn1["Description"])
    else:
     print(name,desc,qn1) 	
    

