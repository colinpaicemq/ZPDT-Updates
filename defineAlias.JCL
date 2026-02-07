//IBMUSERT JOB 1,MSGCLASS=H 
//* define alias for HLQ to user catalog                                        
//S1  EXEC PGM=IDCAMS,REGION=0M                                     
//SYSPRINT DD SYSOUT=*                                              
//SYSIN DD *                                                        
   DEFINE ALIAS (NAME(BACKUP) RELATE('A4USR1.ICFCAT') )             
   DEFINE ALIAS (NAME(COLIN ) RELATE('A4USR1.ICFCAT') )             
/*                                                                  
//
