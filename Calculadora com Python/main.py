#importando bibliotecas necessárias
from tkinter import *
from tkinter import ttk

#definindo cor
#3b3b3b - black
#feffff - white
#38576b - azul
#ECEFF1 - cinzenta
#FFAB40 - orange

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora Python")
janela.geometry("250x343")
janela.config(bg=cor1)

#criando frames
frame_tela = Frame(janela, width=290, height=65, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=290, height=300)
frame_body.grid(row=1, column=0)

#variavel todos os valores
todos_valores = ''

#criando função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

#lógica de calculos
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#criando label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'),bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#criando botões
b_1 = Button(frame_body, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_body, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=127, y=0)
b_3 = Button(frame_body, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=191, y=0)

b_4 = Button(frame_body, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=56)
b_5 = Button(frame_body, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=63, y=56)
b_6 = Button(frame_body, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=127, y=56)
b_7 = Button(frame_body, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=191, y=56)

b_8 = Button(frame_body, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=112)
b_9 = Button(frame_body, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=63, y=112)
b_10 = Button(frame_body, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=127, y=112)
b_11 = Button(frame_body, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=191, y=112)

b_12 = Button(frame_body, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=168)
b_13 = Button(frame_body, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=63, y=168)
b_14 = Button(frame_body, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=127, y=168)
b_15 = Button(frame_body, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=191, y=168)

b_1 = Button(frame_body, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=224)
b_2 = Button(frame_body, command = lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=127, y=224)
b_3 = Button(frame_body, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=191, y=224)


janela.mainloop()