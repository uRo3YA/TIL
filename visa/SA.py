import pyvisa

rm = pyvisa.ResourceManager()
instr = rm.open_resource('TCPIP::192.168.0.1::INSTR') # replace by your IP-address
instr.timeout = 10*1000

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
instr.write('HCOP:DEV:LANG PNG')

# set print to file
instr.write('HCOP:DEST "MMEM"')

# file path/name on instrument
instr.write('MMEM:NAME "C:\Temp\hcopy.png"')

# create screenshot
instr.write('HCOP:IMM')

PCfilePath = r'c:\Temp\hcopy.png'
query = 'MMEM:DATA? \'c:\\temp\\hcopy.png\''

# ask for file data from instrument and save to local hard drive
fileData = instr.query_binary_values(query, datatype='s')[0]
newFile = open(PCfilePath, "wb")
newFile.write(fileData)
newFile.close()

instr.close()