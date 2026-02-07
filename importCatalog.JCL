//IBMUSERT JOB 1,MSGCLASS=H 
//* Import a user catalog into the master catalog                                     
//S1  EXEC PGM=IDCAMS,REGION=0M                                  
//SYSPRINT DD SYSOUT=*                                           
//SYSIN DD *                                                     
   IMPORT CONNECT -                                              
      OBJECTS -                                                  
        (('A4USR1.ICFCAT' VOLUME(A4USR1) DEVICETYPE(3390)  -     
        ))                                                       
/* 
