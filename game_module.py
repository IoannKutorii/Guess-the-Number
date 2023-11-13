# game_module.py

import PySimpleGUI as sg
from base import get_target_number

def is_even(number):
    return number % 2 == 0

def run_game():
    target_number = get_target_number()
    attempts = 0

    layout = [
        [sg.Text('Вгадайте число від 1 до 20:')],
        [sg.InputText(key='-GUESS-')],
        [sg.Button('ОК'), sg.Button('Вихід')],
        [sg.Text('', size=(40, 2), key='-OUTPUT-')],
        [sg.Text('', size=(40, 2), key='-EVEN-')]
    ]

    window = sg.Window('ВГАДАЙ ЧИСЛО', layout, finalize=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Вихід'):
            break

        user_guess = values['-GUESS-']

        if event == 'ОК':
            if user_guess.isdigit():
                user_guess = int(user_guess)
                attempts += 1

                if user_guess < target_number:
                    window['-OUTPUT-'].update('Загадане число більше.')
                elif user_guess > target_number:
                    window['-OUTPUT-'].update('Загадане число менше.')
                else:
                    window['-OUTPUT-'].update(f"Вітаємо! Ви вгадали число {target_number} за {attempts} спроб.")
                    
                    # Додано виведення про парність числа
                    if is_even(target_number):
                        window['-EVEN-'].update('Загадане число парне!')
                    else:
                        window['-EVEN-'].update('Загадане число непарне!')

                    event, _ = window.read()
                    break

    window.close()
