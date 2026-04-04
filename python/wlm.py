import xmltodict
import json
import pprint
from lxml import etree  
from lxml.etree import tostring
from sys import stderr
import pandas as pd

def colinGet(a,b,c="None"):
   v = a.find(b)
   if v is None:
      v = c
      return c
   else:
      return v.text
def colinFind(fromRoot,what,notFound = "None"):
      output = {}
      for w,v in what.items():
         output[w] = colinGet(fromRoot,v)
      return output     


def summary(root):
      print("Doing summary")
      summary = colinFind(root, {"name":"Name", "desc":"Description","level":"Level","prodid":"ProdId",
                              "notes":"Notes"})
      # print("===Summary information")
      summaryRows = []
      summaryRows.append({**summary})
      #print("summry",pd.DataFrame.from_records(summaryRows))
      return pd.DataFrame.from_records(summaryRows)

def workload(root,what):
   workloadRowsART = []
   workloadRowsV = []
   for n in root.find("Workloads"):
      workloads = colinFind(n, {"wlname":"Name", "wldesc":"Description"})

      sc = n.find("ServiceClasses")

      for sc1 in sc:

         sclass = colinFind(sc1, {"scname":"Name", "CPUC":"CPUCritical"})
         goal   = sc1.find("Goal")
            
         for v in goal.findall("Velocity"):
            vel =colinFind(v, {"imp":"Importance", "level":"Level"})
            workloadRowsV.append({**workloads,**sclass,**vel})

         for v in goal.findall("AverageResponseTime"):
            art =colinFind(v, {"imp":"Importance", "rt":"ResponseTime"})
            workloadRowsART.append({**workloads,**sclass,**art})

   #print("===Workload - velocity")
   if what == "workloadV":
       return pd.DataFrame.from_records(workloadRowsV)
   else:
      return pd.DataFrame.from_records(workloadRowsART)
   #print(pdWorkloadV)
   #print("===Workoad - Average response time")
   #pdWorkloadART = pd.DataFrame.from_records(workloadRowsART)
   #print(pdWorkloadART)    

def reportClasses(root):
   rcRows = []
   for n in root.find("ReportClasses"):
      rc =colinFind(n, {"name":"Name", "desc":"Description"})
      rcRows.append({"type":"RC",**rc})


   # print("===Report Classes")
   return pd.DataFrame.from_records(rcRows)
   # print(pdReportClasses)
def classificationGroup(root):
   cgRows = []  
   for n in root.find("ClassificationGroups"):
      cgs =colinFind(n, {"name":"Name", "qt":"QualificationType"})

      for QNS in n.find("QualifierNames"):
         qns = colinFind(QNS, {"qnname":"Name", "qndesc":"Description"})
         cgRows.append(qns)

   #print("===Classification Groups")
   return pd.DataFrame.from_records(cgRows)
   #print(pdClassificationGGroups      )    

def classification(root):
   cRows = []
   for n in root.find("Classifications"):
      crowesh =colinFind(n, {"subsysType":"SubsystemType", "desc":"Description","defaultSN":"DefaultServiceName"})

      for ClassificationRule  in n.find("ClassificationRules"):
         crowdet =colinFind(ClassificationRule, {"qualType":"QualifierType", "qualValue":"QualifierValue",
                                                "scn":"ServiceClassName","storCrit":"StorageCritical","regGoal":"RegionGoal"})
         cRows.append({**crowesh,**crowdet})

   #print("===Classification")
   return pd.DataFrame.from_records(cRows)
   #print(pdClassifications.to_string(justify='left',index=False)   ) 
   #print(df.to_string(justify='left', index=False))

def applicationEnvironment(root):
   aeRows = []
   for n in root.find("ApplicationEnvironments"):
      ae =colinFind(n, {"name":"Name", "desc":"Description","subsysType":"SubsystemType","limit":"Limit","proc":"ProcedureName",
                        "startParms":"StartParameters" })
      aeRows.append({**ae})
   #print("===Application Environments")
   return pd.DataFrame.from_records(aeRows)
   #pd.set_option('display.max_rows', 500)

   #print(pdApplicationEnvironments   ) 
  


def main(xmline,what):

   if what == "summary":
      return summary(xmline)
   elif what in ["workloadV","workloadART"]:
      return workload(xmline,what)
   elif what == "rc":
      return reportClasses(xmline)
   elif what == "classificationGroup":
      return classificationGroup(xmline)
   elif what == "classification":
      return classification(xmline)
   elif what == "ae":
      return applicationEnvironment(xmline)
   else:
      print("Invalid parameter",what)
      return None
   




 
