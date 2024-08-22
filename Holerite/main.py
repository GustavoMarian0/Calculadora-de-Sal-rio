from tkinter import *
import csv

#Config Janela Web:

jan = Tk()
jan.geometry('1500x720')
jan.title('Contracheque')
jan.config(bg='gray')

#Salvar dados:

def salvar_dados():
nome_valor = nome.get()
banco_valor = banco.get()
agencia_valor = agencia.get()
conta_valor = conta.get()
empresa_valor = empresa.get()
data_admissao_valor = datadeadmissao.get()
tipo_valor = Tipo.get()
salario_bruto = salario.get()

with open('dados.csv', 'a', newline='') as file:

writer = csv.writer(file)
writer.writerow([nome_valor, empresa_valor ,banco_valor,
agencia_valor, conta_valor, data_admissao_valor, tipo_valor,
salario_bruto])

#Calculo:

def calculodoinss(salario):
if salario <= 2112.00:
return 0
elif 2112.01 < salario <= 2826.65:
return 0.075
elif 2826.66 < salario <= 3751.05:
return 0.15
elif 3751.06 < salario <= 4664.68:
return 0.225
elif salario > 4664.69:
return 0.275
else:
raise ValueError('ErroIndex')
def calculoirrf(salario):
if salario < 1903.98:
return 0
elif 1903.99 < salario <= 2826.26:
return 0.075
elif 2826.27 < salario <= 3751.05:
return 0.15
elif 3751.06 < salario <= 4664.68:
return 0.225
elif salario > 4664.69:
return 0.275
else:
raise ValueError('ErroIndex')
def calcular():

salario_valor = float(salario.get())
inss_desconto = calculodoinss(salario_valor)
irrf_desconto = calculoirrf(salario_valor)
calc1 = salario_valor * inss_desconto
calc2 = salario_valor * irrf_desconto
desconto_inss = calc1
desconto_irrf = calc2
desconto_total = desconto_inss + desconto_irrf
inss_descontosss.config(text=f'{desconto_inss:.2f}')
irrf_descontosss.config(text=f'{desconto_irrf:.2f}')
salario_liquido = salario_valor - desconto_total
salarioliquidototal.config(text=f'{salario_liquido:.2f}')
total_desconto = desconto_total
totaldesconto.config(text=f'{total_desconto:.2f}')

#Apaga tudo:

def apaga_tudo():
nome.delete(0, END)
banco.delete(0, END)
agencia.delete(0, END)
conta.delete(0, END)
empresa.delete(0, END)
datadeadmissao.delete(0, END)
Tipo.delete(0, END)
salario.delete(0, END)
inss_descontosss.config(text='')
irrf_descontosss.config(text='')
totaldesconto.config(text='')
salarioliquidototal.config(text='')

#Botões:

texto1 = Label(jan, width=20, height=1, text='Nome:')
texto1.grid(row=1, column=5)
nome = Entry(jan, width=20, font=('arial'))
nome.grid(row=1, column=10, padx=10, pady=5)
texto2 = Label(jan, width=20, height=1, text='Banco:')
texto2.grid(row=2, column=5)
banco = Entry(jan, width=20, font=('arial'))
banco.grid(row=2, column=10, padx=10, pady=5)
texto3 = Label(jan, width=20, height=1, text='AG:')
texto3.grid(row=2, column=15)
agencia = Entry(jan, width=20, font=('arial'))
agencia.grid(row=2, column=20, padx=10, pady=5)
texto4 = Label(jan, width=20, height=1, text='Conta:')
texto4.grid(row=2, column=25)
conta = Entry(jan, width=20, font=('arial'))
conta.grid(row=2, column=30, padx=10, pady=5)
texto5 = Label(jan, width=20, height=1, text='Data de Admissão:')
texto5.grid(row=1, column=25)
datadeadmissao = Entry(jan, width=20, font=('arial'))
datadeadmissao.grid(row=1, column=30, padx=10, pady=5)
texto6 = Label(jan, width=15, height=1, text='Tipo:')
texto6.grid(row=1, column=35)
Tipo = Entry(jan, width=20, font=('arial'))
Tipo.grid(row=1, column=40, padx=10, pady=5)
texto7 = Label(jan, width=15, height=1, text='Salario:')
texto7.grid(row=2, column=35)
salario = Entry(jan, width=20, font=('arial'))
salario.grid(row=2, column=40, padx=10, pady=5)
texto8 = Label(jan, width=15, height=1, text='DESCRIÇÃO:')
texto8.grid(row=8, column=5, padx=10, pady=5)
texto9 = Label(jan, width=15, height=1, text='INSS:')
texto9.grid(row=9, column=5, padx=10, pady=5)
texto10 = Label(jan, width=15, height=1, text='IRRF:')
texto10.grid(row=10, column=5, padx=10, pady=5)
texto11 = Label(jan, width=15, height=1, text='REFERÊNCIA:')
texto11.grid(row=8, column=10, padx=10, pady=5)
texto12 = Label(jan, width=15, height=1, text='30 dias')
texto12.grid(row=9, column=10, padx=10, pady=5)
texto14 = Label(jan, width=15, height=1, text='Total desconto:')
texto14.grid(row=8, column=25, padx=10, pady=50)
totaldesconto = Label(jan, width=10, height=1, text='', font =
('arial'))
totaldesconto.grid(row=9, column=25, padx=10, pady= 5)
texto15 = Label(jan, width=15, height=1, text='Salario Liquido:')
texto15.grid(row=15, column=5, padx=0, pady=100)
salarioliquidototal = Label(jan,width=10, height=1, text='', font =
('arial'))
salarioliquidototal.grid(row=15, column=10, padx=0, pady= 5)
texto17 = Label(jan, width=20, height=1, text='DESCONTOS:')
texto17.grid(row=8, column=15, padx=10, pady=5)
inss_descontosss = Label(jan,width=20, height=1, text='',
font=('arial'))
inss_descontosss.grid(row=9, column=15, padx=10, pady= 5)
texto3 = Label(jan, width=20, height=1, text='Empresa:')
texto3.grid(row=1, column=15)
empresa = Entry(jan, width=20, font=('arial'))
empresa.grid(row=1, column=20, padx=10, pady=5)
irrf_descontosss = Label(jan,width=20, height=1, text='',
font=('arial'))
irrf_descontosss.grid(row=10, column=15, padx=10, pady= 5)
#Botões de ação:
botao_apagar = Button(jan, text="Apagar", command=apaga_tudo)
botao_apagar.grid(row=3, column=20, pady=10)
botao_calcular = Button(jan, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=25, pady=10)
botao_salvar = Button(jan, text="Salvar", command=salvar_dados)
botao_salvar.grid(row=3, column=15, pady=10)
jan.mainloop()