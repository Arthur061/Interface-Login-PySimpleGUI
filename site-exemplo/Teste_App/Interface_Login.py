import PySimpleGUI as sg

JanelaLoguin = [
    [sg.Text('Sistema Login')],
    [sg.Text('Usuário')],
    [sg.Input(key='usuário')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('', key='mensagem')]
]

window = sg.Window('Login', layout=JanelaLoguin)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        senha_certo= 'Arthur'
        usuario_certo = 'ArthuR007'
        usuario = values['usuário']
        senha = values['senha']
        if senha == senha_certo and usuario == usuario_certo:
            window['mensagem'].update('Login feito com sucesso!')
        else:
            window['mensagem'].update('Senha ou usuário incorreto :(')