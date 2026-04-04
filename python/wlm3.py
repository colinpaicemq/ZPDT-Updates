import xmltodict
import json
file="wlm.xml"
with open(file,"r") as myfile:
    data=myfile.read()
data = data.replace('\n',"")
book_dict = xmltodict.parse(data)
for a,b in book_dict.items():
  print("A=",a)
  # print("B=",b)
  rg = b["Workloads"]["Workload"]
  print("rg",rg)
  #for zz,bb in b.items():
  #   print("zz=",zz)
  #g   print("bb=",bb) 
  
json_data = json.dumps(book_dict,indent=1,sort_keys=True)
# print(json_data)
with open("data.json", "w") as json_file:
        json_file.write(json_data)
