import pyvisa
import tkinter
import tkinter.filedialog as fd
import datetime
from PIL import Image, ImageOps

rm = pyvisa.ResourceManager('@py')
inst_1 = rm.open_resource("TCPIP::192.168.110.14::INSTR")
inst_1.timeout = 100000 
print("connect")
print(inst_1.query('*IDN?'))
inst_1.write(":MMEM:STOR:SCR 'R:PICTURE.GIF'")
capture = inst_1.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'", container=list, datatype='c')
print("capture")
root = tkinter.Tk()
root.withdraw()

today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

filename = fd.asksaveasfilename(filetypes=[("GIF", ".gif")], initialfile=today, defaultextension="gif")

with open(filename, 'wb') as fp:
    for byte in capture:
        fp.write(byte)


# img = Image.open(filename)
# im_inv = ImageOps.invert(img)
im_inv=Image.open(filename)
im_inv.save(filename, 'gif')

inst_1.write(":MMEM:DEL 'R:PICTURE.GIF'")
print("save")
inst_1.close()
rm.close()