# Automação de Tarefas e Bots

# Importando Bibliotecas
import pyautogui as pag
import time
import pandas as pd

# pyautogui.click -> clicar em um lugar específico da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla
# pyautogui.hotkey -> combinação de teclas (atalho)

pag.PAUSE = 0.5

# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da empresa
pag.press("win")
pag.write("Chrome")
pag.press("enter")
time.sleep(1)

pag.press("tab")
pag.press("enter")
time.sleep(2)

pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")
time.sleep(4)

# Passo 2: Fazer login no sistema
pag.press("tab")
pag.write("pythonimpressionador@gmail.com")
pag.press("tab")
pag.write("Gui123")
pag.press("tab")
pag.press("enter")

# Passo 3: Importar a base de produtos para cadastrar no sistema
tabela = pd.read_csv("C:\\Users\\note\\OneDrive\\Desktop\\IntensivoPython\\A1_AUTOMACAO\\produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    pag.click(x=411, y=257) # clicando no camp para preencher

    codigo = str(tabela.loc[linha, "codigo"])
    pag.write(codigo)
    pag.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pag.write(marca)
    pag.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pag.write(tipo)
    pag.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pag.write(categoria)
    pag.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pag.write(preco)
    pag.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pag.write(custo)
    pag.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pag.write(obs)

    pag.press("tab")
    pag.press("enter")

    pag.scroll(5000)


# Passo 5: Repetir o passo 4 para todos os produtos