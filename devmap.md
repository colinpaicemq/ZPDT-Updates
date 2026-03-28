## devmap

-  Change the processors to match what your server has.  My dongle has support for 3 CPUs - but I can use n-1 ZIIPs 
- check the memory
-  add the 3270port 3270.  Without this you do not get any 3270's defined, and you get a line printer like console.
- I removed the IPL and put it in my shell script.

    [system]
    processors  5 cp cp cp ziip ziip  # number of processors
    memory 10G
    system_name     VS01
    # ipl DE27 DE28NVM
    3270port    3270       # port number for TN3270 connections

