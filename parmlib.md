## parmlib set up

The sys0.iplparm points to loadxx members.
You need a load member with USER.PARMLIB in it (such as LOADAU)

- Copy it to LOADCP
- Change SYSPARM to SYSPARM AU,CP
- In user.parmlib create IEASYSCP (CP matching the CP above)
- add your parameters, such as OMVS=(CP) for IP(V6) support

You can IPL with this LOADCP definition. If the IPL fails, go back to LOADAU
