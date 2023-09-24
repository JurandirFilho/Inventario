from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter import filedialog as fd

# importanto view
from view import *


################# cores ###############

co0 = "#2e2d2b"  # Preta
co1 = "#fEffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  # 
co11 = "#f2f4f2"
colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']


################# criando janela #################

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

##################### criando Frames ##########

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)


# criando Funções -----------------------------------------
global tree

# Função inserir
def inserir():
    global imagem, imagem_string, l_imagem
    
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serieal.get()
    imagem = imagem_string
    
    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso', 'Dados inserridos com sucesso!')
    
    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serieal.delete(0, 'end')
     
    mostrar()

# Função Atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
    
        valor = treev_lista[0]
        
        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serieal.delete(0, 'end')
        
        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serieal.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]
        
        def update():
            global imagem, imagem_string, l_imagem 
            
            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serieal.get()
            imagem = imagem_string
            
            if imagem=='':
                imagem = e_serieal.insert(0, treev_lista[7])
            
            lista_atualizada = [nome, local, descricao, model, data, valor, serie, imagem, id]
            
            for i in lista_atualizada:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            
            atualizar_(lista_atualizada)
            messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso!')
            
            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serieal.delete(0, 'end')
            
            b_confirmar.destroy()
            
            mostrar()

        b_confirmar = Button(frameMeio, command=update, width=13, text=' Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=330, y=185)
    
    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha da tabela')
          
  
 # Função Deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])
        
        messagebox.showinfo('Sucesso', 'Dados Deletatos com sucesso!')
            
        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha da tabela')
   
  
  
           

# Função para escolher imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem
    
    imagem = fd.askopenfilename()
    imagem_string = imagem
    
    # abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1)
    l_imagem.place(x=700, y=10)
        

# Função pra ver imagem
def vw_imagem():
    global imagem, imagem_string, l_imagem
    
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']
    
    valor = [int(treev_lista[0])]
    
    item = vw_item(valor)
    
    
    imagem = item[0][8]
    
    # abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1)
    l_imagem.place(x=700, y=10)
    
  


#---------- trabalhando no frame Cima ----------------#

# abrindo imagem
app_img = Image.open('inventory.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventário', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

#---------- trabalhando no frame Meio ----------------#

# Criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)

e_nome = Entry(frameMeio, width=30, justify='left', relief='solid')
e_nome.place(x=130, y=11)


l_local = Label(frameMeio, text='Cômodo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)

e_local = Entry(frameMeio, width=30, justify='left', relief='solid')
e_local.place(x=130, y=41)


l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)

e_descricao = Entry(frameMeio, width=30, justify='left', relief='solid')
e_descricao.place(x=130, y=71)


l_model = Label(frameMeio, text='Modelo/Marca', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_model.place(x=10, y=100)

e_model = Entry(frameMeio, width=30, justify='left', relief='solid')
e_model.place(x=130, y=101)


l_cal = Label(frameMeio, text='Data da Compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)

e_cal = DateEntry(frameMeio, width=12, background='darkblue', borderwidth=2, year=2023, locale='pt_br')
e_cal.place(x=130, y=131)


l_valor = Label(frameMeio, text='Valor da Compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)

e_valor = Entry(frameMeio, width=30, justify='left', relief='solid')
e_valor.place(x=130, y=161)


l_serieal = Label(frameMeio, text='Número de Série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serieal.place(x=10, y=190)

e_serieal = Entry(frameMeio, width=30, justify='left', relief='solid')
e_serieal.place(x=130, y=191)


# Criando botões ----------------

# botõa carregar
l_carregar = Label(frameMeio, text='Imgagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)

b_carregar = Button(frameMeio, command=escolher_imagem, width=29, text='carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co9, fg=co0)
b_carregar.place(x=130, y=221)


# botõa inserir
img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, command=inserir, image=img_add, width=95, text=' Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)


# botõa atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, command=atualizar, image=img_update, width=95, text=' Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)


# botõa deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, command=deletar, image=img_delete, width=95, text=' Excluir'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)


# botõa ver imagem
img_item = Image.open('box.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio,command=vw_imagem, image=img_item, width=95, text=' Ver Item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=330, y=218)

# labels Quantidade e Valores
l_total = Label(frameMeio, text=' Valor Total de Todos os Itens  ', height=2, anchor=CENTER, font=('Ivy 10 bold'), bg=co6, fg=co1)
l_total.place(x=450, y=12)
l_total = Label(frameMeio, text='', width=14, anchor=CENTER, font=('Ivy 17 bold'), bg=co6, fg=co1)
l_total.place(x=450, y=40)

l_qtd = Label(frameMeio, text='   Quantidade Total de Itens     ', height=2, anchor=CENTER, font=('Ivy 10 bold'), bg=co6, fg=co1)
l_qtd.place(x=450, y=80)
l_qtd = Label(frameMeio, text='', width=14, anchor=CENTER, font=('Ivy 17 bold'), bg=co6, fg=co1)
l_qtd.place(x=450, y=108)



# tabela -----------------------------------------------------------
def mostrar():
    global tree
    
    # creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = vw_form()


    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()