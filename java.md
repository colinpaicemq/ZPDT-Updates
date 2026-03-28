## Java

I got messages like

'''
BPXM023I (STCDBG) 184 
JVMSHRC023E Cache does not exist 

BPXM023I (STCDBG) 185 
JVMSHRC840E Failed to start up the shared cache. 

F AXR,SYSREXX STOPTSO 
AXR0214I SYSREXX STOPTSO IS ACCEPTED.  ALL SUBSEQUENT TSO=YES REQUES
WILL BE REJECTED 
AXR0209I SYSREXX STOPTSO COMMAND COMPLETE.  ISSUE SYSREXX STARTTSO T
RESUME AXREXX TSO=YES PROCESSING 
$PLNE(*) 
$HASP003 RC=(25),P LNE(*)  - NO SELECTABLE DEVICE(S) FOUND 
BPXM023I (STCDBG) 194 
JVMSHRC023E Cache does not exist 

BPXM023I (STCDBG) 195 
JVMSHRC701E Failed to create a snapshot of non-persistent shared 
cache "eqarmtdcache" 

IEA631I  OPERATOR IBMUSER  NOW INACTIVE, SYSTEM=VS01    , LU=EXL003 
NETVIEW SYSTEM SHUTDOWN IS STOPPING: CSF 
P CSF 
CSFM401I CRYPTOGRAPHY - SERVICES ARE NO LONGER AVAILABLE. 
JVMSHRC023E Cache does not exist 200 

JVMSHRC840E Failed to start up the shared cache. 201 
'''

and messages like

```
JVMJ9VM015W Initialization error for library j9shr29(11): JVMJ9VM009E J9VMDllMain failed         
Error: Could not create the Java Virtual Machine.                                                
Error: A fatal exception has occurred. Program will exit.                                        
```

### Create  SMFLIM
See [JVMJ9VM015W Initialization error for library j9shr29(11): JVMJ9VM009E J9VMDllMain failed](https://colinpaice.blog/2025/03/12/java-persistent-shared-classes-cache-on-z-os/#JVMJ9VM015W)
]
```
REGION JOBNAME(JCACHER) JOBMSG(ISSUE) MAXSHARE(80000) 
```