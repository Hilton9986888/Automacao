import pyautogui
import pandas
import time


pyautogui.PAUSE = 0.7


pyautogui.press("win")

pyautogui.write("Edge")

pyautogui.press("enter")

url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(url)

pyautogui.press("enter")
time.sleep(3)


#print(pyautogui.position()) --- encontra a posição que vai ser clicada


pyautogui.click(x=693, y=464)
time.sleep(0.5)
pyautogui.write("Exemplo123@gmail.com")



pyautogui.press("tab")
time.sleep(0.5)
pyautogui.write("minhasenhaeessa")



pyautogui.click(x=986, y=658)
time.sleep(3)


#importa a base de dados

tabela = pandas.read_csv("produtos.csv")

print(tabela)



#cadastrar produtos

for linha in tabela.index:

    pyautogui.click(x=819, y=304)

    codigo= tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, str("categoria")]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, str("preco_unitario")]))
    pyautogui.press("tab")

    pyautogui.write(str( tabela.loc[linha, "custo"]))                                                             
    pyautogui.press("tab")                              

    obs= tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")                                                                                                                                                                                                                                                                                                                            

    pyautogui.press("enter")
    pyautogui.scroll(5000)