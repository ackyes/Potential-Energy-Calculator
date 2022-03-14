import PySimpleGUI as sg

"""
Mass = float(input("The mass: "))
Acceleration = float(input("The gravitational acceleration: "))
Height = float(input("The height: "))

Potential_Energy = Mass * Acceleration * Height

print("Potential Energy: " + str(Potential_Energy))
"""

sg.theme('DarkTeal')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Potential Energy Calculator')],
            [sg.Text('Mass: '), sg.InputText()],
            [sg.Text('Acceleration: '), sg.InputText()],
            [sg.Text('Height: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Potential Energy:', values[0])

window.close()
