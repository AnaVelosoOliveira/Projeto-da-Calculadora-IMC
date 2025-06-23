from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

co0 ="#753B3B"
co1 ="#D6D650"
co2 ="#3e9e26" 
co3 ="#000000"
co4 ="#fbfbfb"

janela = Tk()
janela.title("")
janela.geometry("410x400")
janela.configure(bg=co1)
janela.resizable(False, False)

frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


l_peso = Label(frame_cima, text="CALCULO DE IMC 👧🏾", height=1, anchor=NE, font =('Ivy 22'), bg=co1, fg=co4)
l_peso.place(x=5, y=5)


l_linha = Label(frame_cima, width=275, text="", height=1, anchor= NW, font=('Ivy 1'), bg=co2)
l_linha.place(x=10, y=45)


def verificar_imc():
    peso = float(e_peso.get())
    altura = float(e_pass.get())
    
    imc = (altura * altura / peso )

    if (imc < 16):

        l_peso = Label(frame_baixo, text="O IMC é de: Magreza grave", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
        l_peso.place(x=5, y=200)

    elif (imc > 16 or imc < 17):
        l_peso = Label(frame_baixo, text="O IMC é de: Magreza moderada", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
        l_peso.place(x=35, y=230)
    elif (imc > 17 or imc < 18,5):
        l_peso = Label(frame_baixo, text="O IMC é de: Magreza leve", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
        l_peso.place(x=35, y=230)
    elif (imc > 18,5 or imc < 25):
        l_peso = Label(frame_baixo, text="O IMC é de: Saudável ", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
        l_peso.place(x=35, y=230)
    elif (imc > 25 or imc < 30):
        l_peso = Label(frame_baixo, text="O IMC é de: Sobrepeso", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
        l_peso.place(x=35, y=230)
    elif (imc > 30 or imc < 35):
        l_peso = Label(frame_baixo, text="O IMC é de: Obesidade grau I", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
        l_peso.place(x=35, y=230)
    elif (imc > 35 or imc < 40):
         l_peso = Label(frame_baixo, text="O IMC é de: Obesidade grau II", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
         l_peso.place(x=35, y=230)
    elif (imc > 40):
         l_peso = Label(frame_baixo, text="O IMC é de: Obesidade grau III", height=1, anchor=NE, font=('Ivy 14'), bg=co1, fg=co4)
         l_peso.place(x=35, y=230)

l_peso = Label(frame_baixo, text="Peso ", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_peso.place(x=10, y=20)
e_peso = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_peso.place(x=14, y=50)


l_pass = Label(frame_baixo, text="Altura ", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, show='', width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_pass.place(x=15, y=130)

botao_confirmar = Button(frame_baixo, text="Calcular IMC", width=39, height=2, bg= co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_imc)
botao_confirmar.place(x=15, y=180)

janela.mainloop()