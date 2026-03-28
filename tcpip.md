## TCPIP

### TCPIP V6

You need a BPXPRMv6 member in user.parmlib

    FILESYSTYPE TYPE(CINET) 
         ENTRYPOINT(BPXTCINT) 
    SUBFILESYSTYPE NAME(TCPIP) 
           TYPE(CINET) 
        ENTRYPOINT(EZBPFINI) 
        DEFAULT 
    NETWORK DOMAINNAME(AF_INET6) 
            DOMAINNUMBER(19) 
            MAXSOCKETS(50000) 
            TYPE(CINET) 

[You need to get this picked up at IPL](..parmlib.md)

### Setting up DNS

    f resolver,display

#### Edit  /etc/hosts

Insert

    151.101.128.223        pypi.org    pip 
    151.101.192.223        pypi.org    pip 
    151.101.192.223        files.pythonhosted.org   pipfiles 
    20.26.156.215          github.com 
    # 151.101.128.81         bbc.co.uk 
    151.101.1.91           curl.se 
    185.199.110.133        raw.githubusercontent.com 
    185.199.110.133        release-assets.githubusercontent.com 
    169.63.188.167         downloads.pyaitoolkit.ibm.net       

#### edit /etc/resolv.conf

    nameserver 8.8.8.8 
    nameserver 1.1.1.1

#### The parms

    DEFAULTTCPIPDATA('COLIN.TCPPARMS(GBLTDATA)') 
    GLOBALTCPIPDATA(/etc/resolv.conf) 
    ;                 
    # ---------------------------------     
    # Default zPDT Linux Base to z/OS Tunnel (Stand-Alone) 
    # --------------------------------     
    ;                                                                        
    GLOBALIPNODES(/etc/hosts)
    # ---------------------------------------
    # External connection VIA zPDT Linux Base to z/OS Tunnel using NAT 
    # -------------------------------
    ;                                                                        
    ; GLOBALIPNODES('COLIN.TCPPARMS(ZPDTIPN2)') 
    ;                                                                        
    # -----------------------------------    
    # Default zPDT Linux Base to z/OS Tunnel (Stand-Alone) 
    # -----------------------------------------
    ;                                                                        
    DEFAULTIPNODES('COLIN.TCPPARMS(ZPDTIPN1)')   
    # -----------------------------------  
    # External connection VIA zPDT Linux Base to z/OS Tunnel using NAT 
    # ----------------------------------------
    ;                                                                        
    ; DEFAULTIPNODES('COLIN.TCPPARMS(ZPDTIPN2)') 
    ;                                         
    COMMONSEARCH   
    CACHE  
    CACHESIZE(200M)                   
    MAXTTL(2147483647)                   
    UNRESPONSIVETHRESHOLD(25)               
