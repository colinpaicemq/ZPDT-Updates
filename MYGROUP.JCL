//IBMUSERT JOB 1,MSGCLASS=H 
//* define a group to make access to resources easier
//S1  EXEC PGM=IKJEFT01,REGION=0M 
//SYSPRINT DD SYSOUT=* 
//SYSTSPRT DD SYSOUT=* 
//SYSTSIN DD * 
ADDGROUP MYGROUP OWNER(IBMUSER)
permit ACCT001 class(ACCTNUM)   id(MYGROUP) access(READ     ) 
permit ACCT#   class(ACCTNUM)   id(MYGROUP) access(READ     ) 
permit JCL     class(TSOAUTH)   id(MYGROUP) access(REAd) 
permit CONSOLE class(TSOAUTH)   id(MYGROUP) access(REAd) 
permit PROC001 class(TSOPROC)   id(MYGROUP) access(REAd) 
permit ISPFPROC  class(TSOPROC) id(MYGROUP) access(REAd) 
setropts raclist(TSOAUTH) refresh 
setropts raclist(ACCTNUM) refresh 
setropts raclist(TSOPROC) refresh 
PERMIT  *.**  CLASS(JESSPOOL) ID(MYGROUP) ACCESS(ALTER) 
SETR RACLIST(JESSPOOL) REFRESH 
/* 
