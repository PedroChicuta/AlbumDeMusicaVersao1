from tkinter import *


def pegarValores():
    todosInputs = []
    for i in inputs:
        todosInputs.append(i.get())
    selecionado = v0.get()
    todosInputs.append(selecionado)
    return todosInputs


def erro():
    newWindow = Tk()
    newWindow.geometry('300x300')
    newWindow.title("Erro")
    newlbl = Label(newWindow, text= "Erro, digite um valor válido" , font=('helvetica', 16), bg="red")
    newlbl.pack()
    newWindow.mainloop()

def moldarValores(y):
    itens = ''  
    for i in y:
        try:
            int(y[1])
        except:
            erro()
            break
        if len(str(i)) == 0 or y[-1] == 0:
            erro()
            break
    for i in y:        
        if y.index(i) != len(y)-1:
            itens += str(i) + "|"
        else:
            if i == 1:
                i = "Sim"
            else:
                i = "Não"
            itens += str(i) + "\n"
    return itens 
    


def escrever(y):
    db = open('pasta.txt', 'a', encoding = "utf-8")
    db.write(y)
    db.close()


def ler():
    leitura = open("pasta.txt", "r", encoding='utf-8')
    leitura = leitura.read()
    newWindow = Tk()
    newWindow.geometry('1200x800')
    newWindow.title("Albuns cadastrados")
    leitura = leitura.split('\n')
    albuns = []
    for i in leitura:
        albuns.append(i.split('|'))
    albuns.pop()
    albunsFormatados = formatandoLeitura(albuns)
    lblMain = Label(newWindow, text= 'Albuns Cadastrados', font=('helvetica', 32)) 
    lblMain.pack()
    for i in albunsFormatados:
       lbl = Label(newWindow, text= i, font=('helvetica', 16)) 
       lbl.pack()
    newWindow.mainloop()


def formatandoLeitura(x):
    listaFormatada = []
    for i in x:
        listaTemp = []
        listaTemp.append(f'nome do álbum:{i[0]}')
        listaTemp.append(f"ano de lançamento:{i[1]}")
        listaTemp.append(f"nome da banda/artista:{i[2]}")
        listaTemp.append(f"álbum lançamento do artista:{i[3]}")
        listaFormatada.append(listaTemp)
    return listaFormatada
                


def enviar(x):
   values = pegarValores()
   valores = moldarValores(values)
   escrever(valores)
   ler()



#window
window = Tk()
window.title("Músicas")
window.geometry('1200x800')
window.configure(background='#ccc')
#label
labelPrincipal = Label(text="Cadastro de album",fg="Red", font=("Helvetica", 32),bg='#ccc')
labelPrincipal.pack()

temas = ["nome do álbum","ano de lançamento","nome da banda/artista","álbum lançamento do artista"]
constDePosicionamento = 60
for i in temas:
    lbl = Label(window, text= i.capitalize() + ":" , font=('helvetica', 16), width=25, bg="#ccc")
    lbl.pack()
    lbl.place(x=0, y = constDePosicionamento)
    constDePosicionamento += 35
    if temas.index(i) == len(temas)-1:
        constDePosicionamento = 60

#inputs
inputs = []
for x in range(0, len(temas)):
    if x == len(temas)- 1:
        v0 = IntVar()
        r1 = Radiobutton(window, text='Sim', variable=v0, value=1)
        r2 = Radiobutton(window, text='Não', variable=v0, value=2)
        r1.place(x=350,y = constDePosicionamento)
        r2.place(x=440, y= constDePosicionamento)
        constDePosicionamento = 60
    else:
        txt = Entry(window, background='white')
        txt.place(x= 350, y = constDePosicionamento)
        inputs.append(txt)
        constDePosicionamento += 35


#botao
botao = Button(window,text="Enviar",font=("Helvetica",16))
botao.place(x = 15, y=200)
botao.bind('<Button-1>', enviar)
window.mainloop()