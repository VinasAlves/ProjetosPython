import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('Planilha_devendas_Projeto2.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    
    # nome
    pyautogui.click(1808,452,dutarion=1.5)
    pyautogui.write(linha[0].value)
    
