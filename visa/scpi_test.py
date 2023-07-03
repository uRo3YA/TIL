import PySimpleGUI as sg
import pyvisa as visa

IP_address = '192.168.110.22'

rm = visa.ResourceManager()
ds1054z = rm.open_resource('TCPIP::' + IP_address + '::INSTR')

layout = [
    [sg.Text('SCPI command:'), sg.Input('*IDN?', key='-SCPI-'), sg.Button('Send')],
    [sg.Text('Response:'), sg.Input('SCPI answer', key='-ANSWER-', expand_x=True, readonly=True)],
    [sg.Button('Exit')]
]

window = sg.Window('Simple SCPI Sender', layout, finalize=True)
window['-SCPI-'].bind('<Return>', '_Enter')
window['-SCPI-'].bind('<KP_Return>', '_Enter')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Exit':
        break
    if event == 'Send' or event == '-SCPI-' + '_Enter':
        if values['-SCPI-'][-1] == '?':
            answer = ds1054z.query(values['-SCPI-'])
        else:
            answer = ds1054z.write(values['-SCPI-'])
        window['-ANSWER-'].update(answer)

ds1054z.close()
rm.close()
window.close()