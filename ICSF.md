## ICSF

I have my own (I)CSF data sets, containing my keys.  My Started Task JCL is the same as the default, but with
a different member

```
//CSF  PROC PRM=CP 
//CSF  EXEC PGM=CSFINIT,PARM=&PRM,REGION=0M,TIME=1440,MEMLIMIT=NOLIMIT 
```

You could use the provided JCL, then stop and restart CSF

```
P CSF
S CSF,PRM=CP
```

The PARM=CP points to a member CSFPRMCP in USER.PARMLIB.  Mine has

```
CKDSN(COLIN.SCSFCKDS) 
PKDSN(COLIN.SCSFPKDS) 
TKDSN(COLIN.SCSFTKDS) 
DOMAIN(0) 
SSM(YES) 
KEYARCHMSG(YES) 
```

If this member does not exist you get an abend
```
IEF764I CSF CSF IEFPARM CSFMIOPD HCR77F0 PARMLIB READ FAILED - MEMBER CSFPRMCP NOT FOUND.        
CSFO0016 ERROR OCCURRED OPENING OPTIONS FILE. MEMBER CSFPRMCP IN DDNAME IEFPARM RC=12 RS=1.      
...                                                          
DUMP TITLE=COMPON=CSF...ABEND=S018F,REASON=0000001B                                                                                                         
```
