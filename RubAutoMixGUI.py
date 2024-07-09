from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
import time

chamou_iniciar2 = False  # Variável de controle
navegador = None  # Variável global para o objeto webdriver
janela_atual = None  # Variável global para a janela atual do navegador
chamou_fechar_pagina = False  # Variável que vai chamar a função "fechar pagina"

def trocar_pagina():
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.switch_to.window(navegador.window_handles[1])
    
    
def fechar_pagina():
    navegador.close()
    navegador.switch_to.window(janela_atual)


def iniciar():
    global chamou_iniciar2, navegador, janela_atual, chamou_fechar_pagina

    if chamou_iniciar2:
        iniciar2()
    else:
        ip = 'IP HERE'  # Digite o endereço de IP do servidor RUB, ex: 10.48.69.146
        usuario = 'USER HERE'  # Digite a matrícula de usuário ou login, ex: 544879
        senha = 'PASSWORD HERE'  # Digite a senha do usuário

        pyautogui.PAUSE = 0.2

        navegador = webdriver.Chrome()

        janela_atual = navegador.current_window_handle
        navegador.switch_to.window(janela_atual)

        time.sleep(1)

        navegador.get(f'http://{ip}/vue/#/core/op/produto')

        # Preenche os campos de Login / Senha e clica no botão de conectar
        navegador.find_element(By.ID, 'login-fld-usr').send_keys(usuario)
        navegador.find_element(By.ID, 'login-fld-pwd').send_keys(senha)
        navegador.find_element(By.ID, 'login-vbtn-loginbtn').click()

        time.sleep(1)

        navegador.maximize_window()

        fornecedor = fornecedor_entry.get().strip()

        navegador.maximize_window()

        time.sleep(1)

        # Clica em "Filtro"
        navegador.find_element(By.CLASS_NAME, 'btn-text').click()

        # Seleciona o "Adicionar Filtro" & "Fornecedor"
        select_element = navegador.find_element(By.TAG_NAME, 'select')
        select = Select(select_element)
        select.select_by_visible_text('Fornecedor')

        # Coloca o código do fornecedor no local
        navegador.find_element(By.CSS_SELECTOR, 'input[placeholder="Valor"]').send_keys(fornecedor.strip())

        # Seleciona o "Adicionar Filtro" & "Estoque"
        select_elementB = navegador.find_element(By.CSS_SELECTOR, 'select.form-control.addNewFilter')
        select = Select(select_elementB)
        select.select_by_visible_text('Estoque')

        # Seleciona a propriedade "Maior que..."" em "Estoque"
        elementos_select = navegador.find_elements(By.CSS_SELECTOR, 'select.operator')
        elemento_select = elementos_select[1]
        select = Select(elemento_select)
        select.select_by_visible_text('maior que...')

        # Envia o "Maior que 0"
        elementos_input = navegador.find_elements(By.TAG_NAME, 'input')

        # Verificar se existem mais de um elemento input
        if len(elementos_input) > 1:
            # Ignorar o primeiro elemento (índice 0) e obter o próximo elemento input
            elemento_input = elementos_input[2]

            # Realizar alguma ação no próximo elemento input, por exemplo, preencher um valor
            elemento_input.send_keys('0')

        time.sleep(1)

        # Clica em "Aplicar"
        navegador.find_element(By.XPATH, '//*[@id="mainview"]/div[2]/div[2]/a/span').click()

        # Espera x segundos para que a página carregue toda
        time.sleep(1.5)

        try:
            # Clica em gerar o arquivo PDF
            navegador.find_element(By.XPATH,
                                '//*[@id="mainview"]/div[1]/div/div[1]/div/div[3]/div[3]/ul[2]/li[3]/a').click()
            time.sleep(1.5)
            chamou_iniciar2 = True
            trocar_pagina()
            chamou_fechar_pagina = True
        except:
            messagebox.showerror("Erro", "O estoque está zerado Ou o código fornecido está incorreto. \n"
                                 "Verifique se o código fornecido está correto, caso esteja, o estoque está ZERADO")
            chamou_iniciar2 = True
            chamou_fechar_pagina = False


def iniciar2():
    global navegador, janela_atual, chamou_iniciar2, chamou_fechar_pagina
    
    fornecedor = fornecedor_entry.get().strip()
    
    if chamou_fechar_pagina:
        fechar_pagina()
        navegador.find_element(By.CLASS_NAME, 'btn-text').click()  # Clica em "Filtro"

        # O código abaixo ele "Limpa" o Input de Fornecedor e logo depois insere o novo código
        navegador.find_element(By.CSS_SELECTOR, 'input[placeholder="Valor"]').clear()
        navegador.find_element(By.CSS_SELECTOR, 'input[placeholder="Valor"]').send_keys(fornecedor.strip())

        # Aplicar
        navegador.find_element(By.XPATH, '//*[@id="mainview"]/div[2]/div[2]/a/span').click()

        # Espera x segundos para que a página carregue toda
        time.sleep(1)

        try:
            # Clica em gerar o arquivo PDF
            navegador.find_element(By.XPATH,
                                '//*[@id="mainview"]/div[1]/div/div[1]/div/div[3]/div[3]/ul[2]/li[3]/a').click()
            time.sleep(1.5)
            chamou_iniciar2 = True
            trocar_pagina()
            chamou_fechar_pagina = True
        except:
            messagebox.showerror("Erro", "O estoque está zerado Ou o código fornecido está incorreto. \n"
                                    "Verifique se o código fornecido está correto, caso esteja, o estoque está ZERADO")
            chamou_iniciar2 = True
            chamou_fechar_pagina = False
            
            
    else:
        navegador.find_element(By.CLASS_NAME, 'btn-text').click()  # Clica em "Filtro"

        # O código abaixo ele "Limpa" o Input de Fornecedor e logo depois insere o novo código
        navegador.find_element(By.CSS_SELECTOR, 'input[placeholder="Valor"]').clear()
        navegador.find_element(By.CSS_SELECTOR, 'input[placeholder="Valor"]').send_keys(fornecedor.strip())

        # Aplicar
        navegador.find_element(By.XPATH, '//*[@id="mainview"]/div[2]/div[2]/a/span').click()

        # Espera x segundos para que a página carregue toda
        time.sleep(1)

        try:
            # Clica em gerar o arquivo PDF
            navegador.find_element(By.XPATH,
                                '//*[@id="mainview"]/div[1]/div/div[1]/div/div[3]/div[3]/ul[2]/li[3]/a').click()
            time.sleep(1.5)
            chamou_iniciar2 = True
            trocar_pagina()
            chamou_fechar_pagina = True
        except:
            messagebox.showerror("Erro", "O estoque está zerado Ou o código fornecido está incorreto. \n"
                                    "Verifique se o código fornecido está correto, caso esteja, o estoque está ZERADO")
            chamou_iniciar2 = True
            chamou_fechar_pagina = False

time.sleep(1)

root = Tk()
root.title("MIX - Relatório de Estoque By David Rodrigues TI (5353181) - L232, Macaé-RJ")

# Definir tamanho da janela
root.geometry("580x200")

root.attributes("-topmost", True)

# Estilos
style = Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))

# Interface gráfica

fornecedor_label = Label(root, text="Digite o código de fornecedor:", style='TLabel')
fornecedor_entry = Entry(root, style='TEntry')

def iniciar_button_click_():
    fornecedor = fornecedor_entry.get().strip()
    if fornecedor.isdigit():  # Verifica se é um número inteiro
        iniciar()
    else:
        messagebox.showerror("Erro", "O código de fornecedor deve conter somente números,\n"
                                     "consulte no RUB Web caso não saiba qual é o código.")


iniciar_button = Button(root, text="Iniciar", command=iniciar_button_click_, style='TButton')

fornecedor_label.pack()
fornecedor_entry.pack()
iniciar_button.pack()

root.mainloop()
