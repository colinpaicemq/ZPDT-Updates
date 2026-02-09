# Catalog related activities

## Create a user catalog

You should define at least one user catalog for your non system datasets.  See [JCL](JCL/USERCAT.JCL)
You could have 

- a usercatalog for subsystem datasets, so MQ and DB2 datasets go in one catalog,
- a usercatlog for general users
- A usercatalog for sysprogs

## Migrate catalogs and aliases

List the aliases in the master catalog

```
//IBMUSERT JOB 1,MSGCLASS=H                                    
//S1  EXEC PGM=IDCAMS,REGION=0M                                
//SYSPRINT DD SYSOUT=*                
//SYSIN DD *                                                   
 LISTCAT  ALIAS ALL                                            
/*                                                             
```

Then use SDSF to edit the listing.  [LISTCATA](CLIST/LISTCATA.CLIST) processes the file.

This produces output like
```
TEST     2026.004 A4USR1.ICFCAT 
SYSOPR   2024.103 USERCAT.Z31B.USER 
```
The columns are

1. The alias
2. The data the alias was created
3. The catalog they relate to

If you sort of the date column, you can find the aliases you created, and those which came with the
system.
For example, I did not download the system until 2025, so all 2024..... came with the system.

Delete the entries you are not interested in, then run [MAKEALIA](CLIST/MAKEALIA.CLIST).   This then creates
the IDCAMS statement needed to define the aliases.

## List your datasets in the Master Catalog

```
//IBMLISC JOB 1,MSGCLASS=H 
// EXPORT SYMLIST=(*) 
// SET CAT=&SYSVER. 
//S1  EXEC PGM=IDCAMS 
//SYSPRINT DD SYSOUT=* 
//SYSIN DD *,SYMBOLS=JCLONLY 
 LISTCAT NONVSAM CATALOG(CATALOG.&CAT..MASTER) ALL
/* 
```

Use SDSF to edit the listing, and run [LISTCATN](CLIST/LISTCATN.CLIST) to get a one line for every dataset 
in the catalog

