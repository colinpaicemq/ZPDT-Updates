## fixes

### FSUM2378 The start of the session was not recorded. The slot (in /etc/utmpx) for this terminal could not be updated, or a new slot for the terminal could not be created.
and
### Function = pututxline(), terminal name = '/dev/ttyp0000', program name = '/bin/fomtlinc', errno = 113 (X'00000071'), reason code = 053501B2, message = 'EDC5113I Bad file descriptor.'

See https://www.mail-archive.com/ibm-main@bama.ua.edu/msg118190.html  
I had to do

```
chmount -w /bin
chmod u+s /bin/fomtlinc
chmod u+s /bin/fomtlout 
chmount -r /bin 
```

### /usr/lpp/IBM/cvg/v1r24/go/etc/envsetup : EDC5129I No such file or directory.

It does not look like go is installed.

comment out /etc/profile

    #PATH=$PATH:/usr/lpp/IBM/cvg/v1r24/go/bin 
    ...
    #if [ ${shell} = '-bash' ];
    #then
    # source /usr/lpp/IBM/cvg/v1r24/go/etc/envsetup
    #fi
