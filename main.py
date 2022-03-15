import PySimpleGUI as sg
"""
Mass = float(input("The mass: "))
Acceleration = float(input("The gravitational acceleration: "))
Height = float(input("The height: "))

Potential_Energy = Mass * Acceleration * Height

print("Potential Energy: " + str(Potential_Energy))
"""

sg.theme('DarkTeal')

layout = [
    [sg.Text("Potential Energy Calculator")],
    [
        sg.Text(
            'Enter your Mass, Gravity Acceleration(9.8 for earth), and Height to calculate the potential energy.',
            size=(40, 3))
    ],
    [
        sg.Text("Mass: "),
        sg.Input(size=(3, 1), key='-MASS-'),
        sg.Text("kg."),
        sg.Text("Acceleration: "),
        sg.Input(size=(3, 1), key='-ACCELERATION-'),
        sg.Text("g.")
    ],
    [sg.Text("Height: "),
     sg.Input(size=(3, 1), key='-FT-'),
     sg.Text("ft.")],
    [sg.Button('Calculate'), sg.Button('Exit')],
    [sg.Text("Results: "),
     sg.Text("", size=(25, 4), key='-OUTPUT-')],
]

window = sg.Window('Potential Energy Calculator', layout)

while True:  #Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('Potential Energy:', values[0])

window.close()
