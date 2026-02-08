# ZPDT and ZD&T configuration 

TThis repository is a list of the customising I did to the new standard system

## Background

I have an existing ZD&T system where I do application development.  I have done a lot of configration and blogged my 
experiences.  For example, I have 

- started tasks
- parmlib updates
- members in proclib
- RACF configuration
- digital certificates
- WorkLoad Mmanager changes
- ICSF certificates
- datasets
- VSAM files
- USS file systems

## Work in progress

- [copying IODS from one system to another](HCD.md)
- [Catalog stuff](CATALOG.md)

## The system I am moving to

This is a different configuration to the ZD&T and ZPDT systems, and the migration is not easy.
The new system does not follow best practices, and I want to implement some of these best practices

The top requirement is to create a userid COLIN, and get access to the datasets owned by COLIN.

I want to put members in USER.PROCLIB, and USER.PARMLIB.

### Setting up to logon

Datasets owned by userid COLIN map to a usercatalog.   To use the usercatalog it has to be in the master catalog.
See [import user catalog](JCL/importCatalog.JCL).

To point a High Level Qualifier(HLQ) at this user catalog you need to [define an alias](JCL/defineAlias.JCL)

Best practice is not to give a userid access to resources, but to connect them to a group, and give the group access to the resources.  For example, if someone in your organisation is replaced, then when using a group it is easy to give the new person access.  If a userid is given access - it is very hard to find what acccess a userid has , and to give another userid access to the resources.

See [defintion of my group](JCL/MYGROUP.JCL). 

Define my userid see [Batch define](JCL.COLIN.JCL).   Things to note

- I found it easier to define it then alter it. - 
- If you let the system give you a Unix ID (UID) it can change from day to day.  If you want to import USS file systems, the files may have a differnt UID.  I found it best to specify a userid, then change all the files owned by my userid to have this UID.
- Do not give a userid access to resources - connect the userid to a group which has the required accesses.
- As this userid will be using TSO ISPF and ISPF, you need to give the userid access to these.
If the userid is to be able to access spool datasets from SDSF it needs access to them.

When these jobs have run, I should be able to logon with my userid using the TSO class and accounting information.



## Using USER.PARMLIB
You can configure the IPL to use definitions from different datasets, typically names like SYS1.PARMLIB, and USER.PARMLIB.
The order may be USER.ABCD.PARMLIB. SYS1.ABCD.PARMLIB, SYS1,PARMLIB. Where ABCD is the name of a system, and has members specific to that system name.

You can specify these datasets in the SYSn.IPLPARM member.
In SYS1.IPLPARM(LOADCP) is
```
IODF     99 SYS1 
INITSQA  0000M 0008M 
SYSCAT   B3SYS1113CCATALOG.Z31B.MASTER 
SYSPARM  CP 
IEASYM   (00,CP) 
NUCLST   00 
PARMLIB  USER.Z31B.PARMLIB                            B3CFG1 
PARMLIB  FEU.Z31B.PARMLIB                             B3CFG1 
PARMLIB  ADCD.Z31B.PARMLIB                            B3SYS1 
PARMLIB  SYS1.PARMLIB                                 B3RES1 
NUCLEUS  1 
SYSPLEX  ADCDPL 
```
showing the PARMLIB members, and the disk volume they are on.

When a system is IPLed you use a command like

```
ipl 0ad8 parm 0adfcp

```
Where 0adf is the address of the DASD volume with the SYS*.IPLPARM on it, and CP is the LOADCP name.

## System startup.

There are various members which affect startup for example in the IEASYSxx parmlib member, is (usually) a MSTJCLxx member.

This is like
```
//MSTJCL00 JOB MSGLEVEL=(1,1),TIME=1440                               
//         EXEC PGM=IEEMB860,DPRTY=(15,15)                            
//STCINRDR DD SYSOUT=(A,INTRDR)                                       
//TSOINRDR DD SYSOUT=(A,INTRDR)                                       
//IEFPDSI  DD DSN=USER.&SYSVER..PROCLIB,DISP=SHR                      
//         DD DSN=FEU.&SYSVER..PROCLIB,DISP=SHR                       
//         DD DSN=ADCD.&SYSVER..PROCLIB,DISP=SHR                      
//         DD DSN=SYS1.PROCLIB,DISP=SHR                               
//SYSUADS  DD DSN=SYS1.UADS,DISP=SHR                                  
//SYSLBC   DD DSN=SYS1.BRODCAST,DISP=SHR                              
```
Commands are issued during IPL as defined in 
COMMNDxx members and IEACMDxx members.
ADCD.Z31B.PARMLIB(COMMNDWS)  has

```
COM='S JES2,PARM='WARM,NOREQ'' 
COM='S VLF,SUB=MSTR' 
COM='S HZR,SUB=MSTR' 
COM='S VTAM' 
COM='S VTAM00' 
COM='S DLF,SUB=MSTR' 
COM='DD ADD,VOL=B3SYS1' 
COM='DD NAME=SYS1.&SYSNAME..&SYSVER..DMP&SEQ' 
COM='DD ALLOC=ACTIVE' 
```


For most people the JES2 proc is configured, for example 
```
//JES2      PROC MEMBER=JES2PARM,ALTMEM=JES2BACK 
//IEFPROC   EXEC PGM=HASJES20,DPRTY=(15,15),TIME=1440,PERFORM=9 
//ALTPARM   DD   DSN=ADCD.&SYSVER..PARMLIB(&ALTMEM),DISP=SHR 
//HASPPARM  DD   DSN=ADCD.&SYSVER..PARMLIB(&MEMBER),DISP=SHR 
//PROC00    DD   DSN=USER.&SYSVER..PROCLIB,DISP=SHR 
//          DD   DSN=FEU.&SYSVER..PROCLIB,DISP=SHR 
//          DD   DSN=ADCD.&SYSVER..PROCLIB,DISP=SHR 
//          DD   DSN=SYS1.PROCLIB,DISP=SHR 
//HASPLIST  DD   DDNAME=IEFRDER 
```

So there are several places where USER.*.PROCLIB is specified.

If you want to change these, create another set of parmlib members, in case you have an error.  If you make an error the system may not be IPLable, and so you will not be able to fix it. 

### VTAM00
VTAM00 is a way of issuing a set of console commands.

For example it reads member ADCD.&SYSVER..PARMLIB(VTAM00), which has in it

```
COMMANDPREFIX=NONE   /* THIS IS THE DEFAULT VALUE */ 
/*--------------------------------------------------------------------* 
/*--------------------------------------------------------------------* 
PAUSE 10      /* WAIT FOR SYS TO GET UP FIRST  */ 
S RRS,SUB=MSTR,GNAME=&SYSNAME 
S TSO         /* TIME SHARING OPTION */ 
S SDSF 
S EZAZSSI,P=S0W1 
S TCPIP 
PAUSE 5 
S TN3270 
PAUSE 5 
/*S INETD */ 
S HTTPD1 
S CSF 
S HZSPROC 
PAUSE 10 
S SSHD 
PAUSE 10 
S IZUANG1 
PAUSE 3 
* S IZUSVR1 
D T                          /* DISPLAY ENDING TIME                 */ 
* COMMENT LINES MAY ALSO START WITH A SINGLE ASTERISK. 
* REMEMBER - BLANK LINES ARE A BIG NO-NO. 
*@ *--------------------------* 
*@ * IPL STARTUP IS COMPLETE! * 
*@ * >>> HAVE A NICE DAY! <<< * 
*@ *--------------------------* 
```

I use a member STARTMQ
```
s izusvr1 
SETSSI ADD,S=CSQ9,I=CSQ3INI,P='CSQ3EPX,%CSQ9,M' 
PAUSE 1 
%CSQ9 Start QMGR 
S Csq9ang 
S Csq9web 
PAUSE 10 
%CSQ9 Start chinit 
```

## Getting to best practice 

### Use of RACF PROTECTALL

The documentation says
*
PROTECTALL(FAILURES | WARNING)
Activates PROTECTALL processing. When PROTECTALL processing is active, the system
automatically rejects any request to create or access a data set that is not RACF-protected. This
processing includes DASD data sets, tape data sets, catalogs, and GDG basenames. Temporary
data sets that comply with standard MVS temporary data set naming conventions are excluded
from PROTECTALL processing.

Note that PROTECTALL requires all data sets to be RACF-protected. This includes tape data sets if
your installation specifies the TAPEDSN operand on the SETROPTS command.
In order for PROTECTALL to work effectively, you must specify GENERIC to activate generic profile
checking. Otherwise, RACF would allow users to create or access only data sets protected by
discrete profiles. If your installation uses nonstandard names for temporary data sets, you must
also predefine entries in the global access checking table that allow these data sets to be created
and accessed.

See [JCL PROTECTALL](JCL/PROJECTALL.JCL.) to enable this.

The above JCL also makes the master catalgo read only for most people  except those in SYS1 group.
