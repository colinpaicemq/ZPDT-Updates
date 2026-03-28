## RRS

At start up you get 

```
ATR132I RRS LOGSTREAM CONNECT HAS FAILED FOR                       
 - OPTIONAL LOGSTREAM ATR.VS01.ARCHIVE.                                                       
 - RC=00000008, RSN=0000080B           
 ```

 See [here](https://www.ibm.com/docs/en/zos/2.5.0?topic=command-setrrs-archivelogging).

 ### Issue

     SETRRS ARCHIVELOGGING,DISABLE 