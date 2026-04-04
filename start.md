# List of actions to configure standard image

The IP address of z/OS is 172.26.1.2.  [You need to configure your laptop](laptop.md)

[Configure your devmap](devmap.md)

First IPL.  The default IPL starts up and starts lots of subsystems.  Use PARM xxxxAU initially, until you've done the
basic configuration.

[Configure parmlib](..parmlib.md)

[Configure VTAM to give you greater than 80 *24 screen size](vtam.md)

[Configure TCPIP](tcpip.md)

[Change the console pf keys](..consolepfkeys.md)

[Fix SMF](..SMF.md)

[Using z/OS Unix](..usingUnix.md)

[Confiure the syslog daemon](syslogd.md)

[Configure SSh](ssh.md)

[configure RACF](RACF.md)

[Configure Java](java.md)

[Configure RRS](RRS.md)

[Configuring CSF - ICSF](ICSF.md)

[Logrec](logrec.md)

[Misc fixes](fixes.md)

## Remembering how to shutdown 

I created USER.PARMLIB(PFKTAB00) with

```
PFKTAB TABLE(COMMANDS) 
   PFK(01) CMD('K E,1') 
   PFK(02) CMD('K E') 
   PFK(03) CMD('K E,D') 
   PFK(04) CMD('K D,F') 
   PFK(05) CMD('K S,DEL=R') 
   PFK(06) CMD('K S,DEL=RD') 
   PFK(07) CMD('D A,L') 
   PFK(08) CMD('D R,R,CN=(ALL)') 
   PFK(09) CMD('K D,U') 
   PFK(10) CMD('V TCPIP,TCPIP,OBEYFILE,USER.TCPPARMS(ROUTE)') CON(Y) 
   PFK(11) CMD('K E') 
   PFK(12) CMD("%NETV SHUTSYS") CON(Y) 
   PFK(13) CMD('K E,1') 
   PFK(14) CMD('K E') 
   PFK(15) CMD('K E,D') 
   PFK(16) CMD('K D,F') 
   PFK(17) CMD("D PFK") 
   PFK(18) CMD("%NETV SHUTSYS")CON(Y) 
   PFK(19) KEY(07) 
   PFK(20) KEY(08) 
   PFK(21) KEY(09) 
   PFK(22) KEY(10) 
   PFK(23) KEY(11) 
   PFK(24) KEY(12) 
```

If you press PF12, it will display *%NETV SHUTSYS* in the command line.  Press enter to execute it.

## clearing console messages

You can get messages on the operator console which do not roll off the screen.  For example

```
*IFB081I LOGREC DATA SET IS FULL,12.53.55,DSN=VSPROV.VS01.LOGREC                   
```

You can clear these using the command

```
K E,1,1
```

Which says clear the message on lines 1 to 1.

## WLM processing 

[Wlm display](wlm.md)