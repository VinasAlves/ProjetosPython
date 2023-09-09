from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout= [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char = '*')],
    [sg.Checkbox('Salvar o login ?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED :
        break
    if eventos == 'Entrar':
        if valores == ['usuario'] == 'vinas' and valores ['senha'] == '123456':
            print('Bem vindo a Interface')
