import pyautogui as pa
import time

pa.PAUSE = 0.5 

#abrir navegador
pa.press("win")
pa.write("chrome")
pa.press("enter")

#entrar no site
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")

time.sleep(1)

#fazer login 
pa.press("tab") # ou pa.click(x=938, y=510) - coordenada do mouse
pa.write("gugasouto2004@gmail.com")#email

pa.press("tab")
pa.write("gustavosouto02")#senha

pa.press("tab")
pa.press("enter")

time.sleep(1)

#importar base de dados
import pandas as pd 

tabela = pd.read_csv("produtos.csv")
print(tabela)

#cadastrar produtos
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])#transformar informação em texto
    #codigo
    pa.click(x=818, y=361)
    pa.write(codigo)
    pa.press("tab")
    #marca
    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")
    #tipo
    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")
    #categoria 
    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")
    #preco
    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")
    #custo
    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pa.write(obs)   
    #proximo campo      
    pa.press("tab") 
    #enviar
    pa.press("enter")
    pa.scroll(5000)
