
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