import PySimpleGUI as sg
import controller

sg.theme('Topanga')

layout = [
    [sg.Text("Potential Energy Calculator", background_color='#696969', text_color='White')],
    [
        sg.Text(
            'Enter your Mass, Gravity Acceleration(9.8 for earth), and Height to calculate the potential energy.', 
          text_color='White',
          size=(45, 2)
        )
    ],
    [
        # Line for Mass
        sg.Text("Mass: ", background_color='#696969', text_color='White'),
        sg.Input(size=(31, 1), text_color='White',key='-MASS-'),
        sg.Text("kg.", background_color='#696969', text_color='White')
    ],
    [
        # Line for Gravity Acceleration
        sg.Text("Acceleration: ", background_color='#696969', text_color='White'),
        sg.Input(size=(25, 1), text_color='White',key='-ACCELERATION-'),
        sg.Text("g.", background_color='#696969', text_color='White')
    ],
    [
        # Line for Height
        sg.Text("Height: ", background_color='#696969', text_color='White'),
        sg.Input(size=(30, 1), text_color='White',key='-HEIGHT-'),
        sg.Text("ft.", background_color='#696969', text_color='White')
    ],
    # Buttons for calculations, and exiting program
    [sg.Button('Calculate', button_color='Green', mouseover_colors=("#000000","#ffffff")), 
     sg.Button('Exit', button_color='#A10000', mouseover_colors=("#000000","#ffffff"))
    ],
    # Lines for the Potential Energy
    [sg.Text("Potential Energy: ", background_color='#696969', text_color='White')],
    [sg.Text("", background_color='#696969', text_color='White', size=(40, 4), key='-OUTPUT-')],
]
window = sg.Window('Potential Energy Calculator', layout)

while True:  #Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        # Update output text element to be value of input element
        # get kilograms, gravity, and feet
        kilograms = values['-MASS-']
        gravity = values['-ACCELERATION-']
        feet = values['-HEIGHT-']

        # Calculates the potential energy by calling on controller
        results = controller.get_results(kilograms, gravity, feet)

        # Output results
        window['-OUTPUT-'].update(results)

window.close()
