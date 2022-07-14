import PySimpleGUI as sg

sg.theme('Dark Blue 3')

layout = [[sg.Text('O que você escrever aparece aqui: '), sg.Text(key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('Janelinha dos cria', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'OK':
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
