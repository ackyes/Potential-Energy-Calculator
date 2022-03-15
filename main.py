import PySimpleGUI as sg
import controller
sg.theme('DarkTeal')

layout = [
    [sg.Text("Potential Energy Calculator")],
    [
        sg.Text(
            'Enter your Mass, Gravity Acceleration(9.8 for earth), and Height to calculate the potential energy.',
            size=(40, 3))
    ],
    [
      # Line for Mass
        sg.Text("Mass: "),
        sg.Input(size=(3, 1), key='-MASS-'),
        sg.Text("kg.")
    ],
    [
      # Line for Gravity Acceleration
        sg.Text("Acceleration: "),
        sg.Input(size=(3, 1), key='-ACCELERATION-'),
        sg.Text("g.")],
    [
      # Line for Height
     sg.Text("Height: "),
     sg.Input(size=(3, 1), key='-HEIGHT-'),
     sg.Text("ft.")
    ],
    # Buttons for calculations, and exiting program
    [sg.Button('Calculate'), sg.Button('Exit')],
    # Lines for the Potential Energy
    [sg.Text("Results: "),
     sg.Text("", size=(25, 4), key='-OUTPUT-')],
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
