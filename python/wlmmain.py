import wlm
from lxml import etree  

with open("wlm.xml","r") as myfile:
    data=myfile.read()
data = data.replace('\n',"")  
data = data.replace('xmlns="http://www.ibm.com/xmlns/prod/zwlm/2000/09/ServiceDefinition.xsd"',"" )
#print(data)  
root = etree.fromstring(data)

for which in ["summary","workloadV","workloadART","rc",
              "classification","classificationGroup",
              "ae"]:
    
    pdxx =  wlm.main(root,which)
    print("===",which,pdxx)