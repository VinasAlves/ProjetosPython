from time import sleep

import pyautogui

# primeira parte da interface
pyautogui.click(992,543, duration=1)
pyautogui.write('Vinicius')

pyautogui.click(969,566, duration=1)
pyautogui.write('123456')

pyautogui.click(877,595, duration=1)

#SEGUNDA PARTE DA INTERFACE

with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(692,529, duration=0.5)
        pyautogui.write(produto)

        pyautogui.click(686,554, duration=0.5)
        pyautogui.write(quantidade)

        pyautogui.click(675,579, duration=0.5)
        pyautogui.write(preco)

        pyautogui.click(600,735, duration=1)
        sleep(1)
