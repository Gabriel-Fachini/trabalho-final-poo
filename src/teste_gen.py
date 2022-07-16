import PySimpleGUI as sg

data = {
    "question": [
        "Q1. What equation for force",
        "Q2. Define isotope",
        "Q3. Define wavelength",
        "Q4. Define modal dispersion"
    ],
    "answers": [

        "F=ma"
        ,
        "Isotopes are atoms of the same element but with a different number of neutrons"
        ,
        "The least distance between adjacent particles which are in phase"
        ,
        "Causes light travelling at different angles to arrive at different times"

    ],
}

# initialise the question, question number and answer
question = (data['question'])
answers = (data['answers'])
q_no = 0

sg.theme('DarkBrown4')  # Adding colour
# Stuff in side the window


layout = [[sg.Text("                      "), sg.Text(question[0], key = '_Q1_', visible = True), 
           sg.Text(size=(60, 1), key='-OUTPUT-')],
                [sg.Text("correct answer:"), sg.Text(size=(60, 1), key='-OUTPUTA-')],
                [sg.Text('Answer here:'), sg.InputText(size=(60, 1), key='-INPUT-')],
                [sg.Button('Submit'), sg.Button('Cancel')]]


# Create the Window
window = sg.Window('Quiz', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    window['_Q1_'].Update(visible = False)
    window['-OUTPUT-'].update(question[q_no])

    if values['-INPUT-'] == answers[q_no]:
        print('correct')
        q_no += 1
        window['-OUTPUT-'].update(question[q_no])  # accepts the answer as correct and moves onto the next question
        window['-OUTPUTA-'].update('')
        window['-INPUT-'].update('')

    else:
        print('incorrect')
        print('answer was:', answers[q_no])
        window['-OUTPUTA-'].update(answers[q_no])  # shows that the answer is incorrect and displays the right answer

window.close()