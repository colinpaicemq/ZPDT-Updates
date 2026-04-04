import pandas as pd
import xmltodict
import json
file="wlm.xml"
with open(file,"r") as myfile:
    data=myfile.read()
data = data.replace('\n',"")
book_dict = xmltodict.parse(data)

rg = book_dict["ServiceDefinition"]["Workloads"]["Workload"]

dd = pd.DataFrame.from_records(rg)
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)
print(dd)
