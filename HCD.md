# Export and import the Hardward Configuration
You may want to export an existing hardware configuration.

## Export
From the HCD main ISPF panel

- option 6.  Maintain I/O definition files    
- option 5.  Export I/O definition file
- Specify userid and Node Id as *
- This creates a data set *tsoid.EXPORTED.iodfname*

## Import

From the HCD main ISPF panel

- option 6.  Maintain I/O definition files    
- option 6.  Import I/O definition file

To use it you will need to update your SYSn.IPLPARM(LOADxx) memberb 
