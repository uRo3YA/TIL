import pyvisa

rm = pyvisa.ResourceManager()
instr = rm.open_resource('TCPIP::192.168.110.22::INSTR') # replace by your IP-address
instr.timeout = 10*1000
instr.read_termination="\n"
instr.write_termination="\n"
instr.write('*RST')
instr.write('*CLS')

print(instr.query('*IDN?'))

instr.write('INIT:CONT OFF')

instr.write('INIT')
instr.query('*OPC?')

print(instr.query('SYST:ERR?'))

# truns on color printing
instr.write('HCOP:DEV:COL ON')

# select file format
# (WMF | GDI | EWMF | BMP | PNG | JPEG | JPG | PDF | SVG | DOC | RTF)
instr.write('HCOP:DEV:LANG GIF')

# set print to file
instr.write('HCOP:DEST "MMEM"')

# file path/name on instrument
instr.write('MMEM:NAME "C:\Temp\hcopy.GIF"')

# create screenshot
instr.write('HCOP:IMM')

PCfilePath = r'c:\Temp\hcopy.GIF'
# print(PCfilePath)
query = 'MMEM:DATA?  c:\\temp\\hcopy.GIF\''

# ask for file data from instrument and save to local hard drive
# print(instr.query_binary_values(query,datatype='f',is_big_endian=True))
fileData = instr.query_binary_values(query, datatype='s')[0]
newFile = open(PCfilePath, "wb")
newFile.write(fileData)
newFile.close()
#pyvisa.errors.VisaIOError: VI_ERROR_TMO (-1073807339): Timeout expired before operation completed.
instr.close()