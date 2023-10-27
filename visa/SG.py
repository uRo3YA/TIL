import pyvisa as visa
import time
 
# initialize visa resource
rm = visa.ResourceManager()
 
# open the resource using the VISA address from Keysight Connection Expert
SGC = rm.open_resource('TCPIP::169.254.52.212::INSTR') 
 
# request the instrument to identify itself
modelSerialnumber = SGC.query('*IDN?')

SGC.write("SOUR:FREQ 3.2 GHz")
SGC.write("SOUR:POW:OFFS 1 dBm")
SGC.write("SOUR:POW 0 dBm")
SGC.write("OUTP ON")
print(modelSerialnumber)
print(SGC.query("SOUR:FREQ?"))
print(SGC.query("SOUR:POW?"))
print(SGC.query("OUTP?"))
# close
SGC.close()
rm.close()