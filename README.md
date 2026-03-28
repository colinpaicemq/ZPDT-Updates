# ZPDT and ZD&T configuration 

TThis repository is a list of the customising I did to the new standard system

## Background

I have an existing ZD&T system where I do application development.  I have done a lot of configration 
and blogged my experiences.  For example, I have 

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

## Direction
The configuration of the IBM standard image for z/OS is different to standard customer production systems.

-  "Production customers" have a z/OS image, and they 
refresh the products, while keeping userid, user datasets etc. The production system gradually changes over time.
-   With the IBM standard image, IBM makes a new level of z/OS available, and you have to migrate userids, datasets etc into the image.  Every 3-6 months there may be a new image available.

Moving from one standard image to the next version of the 
standard image is different to how production customers 
migrate to newer levels of products.

I have not seen a document on how to move from one 
standard image instance to another standard image istance.

This Git repository aims to provide guidance on how to do it.
Moving to the first standard image may mean a lot of work, but if you do it the right way moving on should be easy.

##  Guidance

My recommendations are

- Create resources. Use JCL to issue command, rather than 
issue the commands manually.  For example with the standard image
you may get one userid (IBMUSER), and you want to create more userids.
Have a JCL member of your create  userid commands.  
Once created, you just submit the JCL for the follow-on standard image.
- Have an ordering to the members in a dataset.  
If you have to define a group before you create a userid 
which uses this group, then have members R1GROUP, R2USER1.   
If you sort the file in alphabetical order, and submit 
them in order, they pre-reqs should be resolved.


## Setting up connectivity

The IP addess of the z/OS system is 172.26.1.2
I had to configure my laptop with this address (running on the server)

    sudo ip route add 172.26.1.0/24 via 10.1.0.3




## Work in progress

- [copying IODS from one system to another](HCD.md)
- [Catalog stuff](CATALOG.md)

## The system I am moving to

This is a different configuration to the ZD&T and ZPDT systems, and the migration is not easy.
The new system does not follow best practices, and I want to implement some of these best practices

The top requirement is to create a userid COLIN, and get access to the datasets owned by COLIN.

I want to put members in USER.PROCLIB, and USER.PARMLIB.

## Check the new devmap

I had to merge the devices from my old system and the new one.

Check the storage, and the processors in the devmap

I have

    [system]
    processors  5 cp cp cp ziip ziip  # number of processors

    memory 10G
    ...


### Setting up to logon

Datasets owned by userid COLIN map to a usercatalog.   
To use the usercatalog it has to be in the master catalog.
See [import user catalog](JCL/importCatalog.JCL).

To point a High Level Qualifier(HLQ) at this user catalog you need to [define an alias](JCL/defineAlias.JCL)

Best practice is not to give a userid access to resources, but to connect them to a group, 
and give the group access to the resources.  
For example, if someone in your organisation is replaced, 
then when using a group it is easy to give the new person access.  
If a userid is given access - it is very hard to find what acccess a userid has, 
and to give another userid access to the resources.

See [defintion of my group](JCL/MYGROUP.JCL). 

Define my userid see [Batch define](JCL.COLIN.JCL).   Things to note

- I found it easier to define it then alter it. - 
- If you let the system give you a Unix ID (UID) it can change from day to day.  
If you want to import USS file systems, the files may have a differnt UID.  
I found it best to specify a userid, then change all the files owned by my userid to have this UID.
- Do not give a userid access to resources - connect the userid to a group, and give the group the required accesses.
- As this userid will be using TSO ISPF and ISPF, you need to give the userid access to these facilities.
If the userid is to be able to access spool datasets from SDSF it needs access to them.

When these jobs have run, I should be able to logon with my userid using the TSO class and accounting information.

## Change ISPF options
In ISPF option 0

- Remove the / from *Command line at bottom*
- Scroll down
    - Screen format 3 ... *3. Max* ...
    - Terminal Type 4 ... *4. 3278A()...* 
## Set up your PF keys
In ISPF issue *KEYS*, change PF12 to RETRIEVE

## Setting up VTAM(NET)

The VTAM definitions are configured for screens 24 deep by 80 wide.  I use wider than this.

- edit  SYS1.VTAMLST(EXLOCAL)
- Create a new member EXLOCALO from EXLOCAL
- *C NSX32702 D4B32XX3 ALL* this makes all devices support wide screens
- Make a defintion for address 0061.   
0060 is used as the system console,  
the next 3270 defined will be at 0061 - which is not used, so this makes it available to VTAM.
- Next time you IPL you should pick up your changes.  If they do not work, issue
    - V NET,INACT,ID=EXLOCAL
    - V NET,ACT,ID=EXLOCALO

# Setting up a userid    

### give access  to group IZUADMIN 

   PERMIT ACCT001 CLASS(ACCT) access(read) ID(IZUADMIN) 
   PERMIT PROC001 CLASS(TSOPROC) access(read) ID(IZUADMIN) 
   tso setr raclist(TSOPROC,ACCT) refresh 

### Connect a userid to the group
 
   CONNECT  COLIN GROUP(IZUADMIN) 

### FTP startup

I get

     BPXF024I ... EZYFT47I ... line 57: Ignoring keyword "EPSV4".

This is because the FTP configuration file has a mixture of Server and Client configuration.

Add *SUPPRESSIGNOREWARNINGS  TRUE* to TCPIP.TCPPARMS(STPSDATA)

## SMF

Message


HSF0066W Required exit IEFU86 for SMF subsystem SYS not enabled.
Some data may be missing in SDSF event log.

Create USER.PARMLIB(SMFPRMCP), copy SYS1.PARMLIB(SMFPRM00)
add IEFU86

    SYS(EXITS(IEFACTRT,IEFUJI,IEFU83,IEFU84,IEFU85,IEFUJV,*IEFU86*)), 
    SUBSYS(STC,EXITS(IEFU83,IEFU84,IEFU85,IEFU29,*IEFU86*),
    INTERVAL(SMF,SYNC)) 

### Cleanup 
Edit SYS1.VTAMLST(ATCCON00).  Remove IVPLCLI,IVPLCLT because the devices they reference do not exist. 

## Don't know
     ICH408I USER(BPXROOT ) GROUP(SYS1    ) NAME(##) 
     SO.JWTTOK.FEKAPPL CL CRYPTOZ ) 
     INSUFFICIENT ACCESS AUTHORITY ACCESS INTENT(CONTROL)  
     ACCESS ALLOWED(NONE   )                  

# Set up OMVS 

The /usr file system is set up read only.  
I want to mount various files systems, so you need to define a directory.
You cannot use /u because of automount getting in the way.

    chmount -w /usr          
    mkdir /usr/zopen/        
    mkdir /usr/tmp/          
    chmount -r /usr   


## syslogd

```
*.INETD*.*.*       /var/log/inetd.log 
auth.* /var/log/auth.log 
mail.* /var/log//mail -F 640 -D 770 
local1.err       /var/log/local1.log 
*.err            /var/log/errors.log 
# *.CPAGENT.*.*       /var/log/CPAGENT.log 
*.CPATTLS.*.*       /var/log/CPATTLS 
*.TTLS*.*.*          /var/log/TTLS.log 
*.Pagent.*.*        /var/log/Pagent.log 
*.TCPIP.*.debug     /var/log/TCPIPdebug.log 
*.TCPIP.*.warning   /var/log/TCPIP.log 
*.TCPIP.*.err       /var/log/TCPIPerr.log 
*.TCPIP.*.info      /var/log/TCPIPinfo.log 
*.SYSLOGD*.*.*      /var/log/syslogd.log 
*.TN3270*.*.*       /var/log/tn3270.log 
*.SSHD*.*.*         /var/log/SSHD.log 
*.FTPD*.*.*         /var/log/FTPD.log 
daemon.debug        /var/log/SSHDdebug.log 
*.TCPIP.*.none; 
*.err            /var/log/errors 
*.CPAGENT.*.*       /var/log/CPAGENT.log 
*.TRMD1.*.info      /var/log/TRMD1I.log 
*.DMD.*.*           /var/log/DMD.log 
```

            PARM='PGM /usr/sbin/sshd -f /etc/ssh/sshd_config '                      
edit /etc/ssh/sshd_config to add 

    ALLOWGROUPSS  SYS1  IZUADMIN            

and connect the userid to the group   

Add BPXPRMv6 to add IPV6 support to TCPIP.

