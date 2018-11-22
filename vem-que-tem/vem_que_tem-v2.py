 # -*- coding: utf-8 -*-
 # project: 2a Lista de Exercícios
 # course: Linguagens de Programação Script
 # university: Universidade Federal do Ceará - UFC
 # author (github): heldercostaa

from tkinter import Tk, Label, Button, Entry, IntVar, Toplevel, Listbox, StringVar, OptionMenu, Radiobutton, END, ACTIVE

# -------------------- #

class ViewPrincipal:

    def __init__(self, master):
        self.master = master
        master.title("Vem que Tem")

        # Elementos
        lbl_sub_titulo = Label(master, text="Mercadinho")
        lbl_titulo = Label(master, text="Vem que Tem")

        btn_distribuidor = Button(master, text="Distribuidores", command = lambda:self.viewDistribuidor())
        btn_produto = Button(master, text="Produtos", command = lambda:self.viewProduto())


        btn_sair = Button(master, text="Sair", command=self.master.quit)

        # Layout
        lbl_sub_titulo.grid(row=0,column=0)
        lbl_titulo.grid(row=1,column=0)

        btn_distribuidor.grid(row=2,column=0)
        btn_produto.grid(row=2,column=1)
        
        btn_sair.grid(row=3,column=0)

    def viewDistribuidor(self):
        self.master.withdraw()
        ViewDistribuidor(self)
    
    def viewProduto(self):
        self.master.withdraw()
        ViewProduto(self)

# -------------------- #

class ViewDistribuidor(Toplevel):

    def __init__(self, master):
        self.master_frame = master
        Toplevel.__init__(self)

        self.transient(root)
        self.geometry('400x400')
        self.lift()

        # Elementos
        lbl_titulo = Label(self, text = "Distribuidores")

        lbl_nome = Label(self, text = "Nome:")
        txt_nome = Entry(self)
        btn_alterar = Button(self, text = "Alterar", command = lambda:self.ControllerAlterar(self.list_distribuidores.get(ACTIVE),txt_nome.get()))
        btn_adicionar = Button(self, text = "Adicionar", command = lambda:self.ControllerAdicionar(txt_nome.get()))
        
        self.list_distribuidores = Listbox(self)
        btn_remover = Button(self, text = "Remover", command = lambda:self.ControllerRemover(self.list_distribuidores.get(ACTIVE)))


        btn_voltar = Button(self, text ="Voltar", command = lambda:self.voltar())

        # Layout
        lbl_titulo.grid(row=0,column=1)

        lbl_nome.grid(row=1,column=0)
        txt_nome.grid(row=1,column=1)
        btn_adicionar.grid(row=1,column=2)
        btn_alterar.grid(row=1,column=3)

        self.list_distribuidores.grid(row=2,column=1)
        btn_remover.grid(row=2,column=2)

        btn_voltar.grid(row=3,column=1)

        # Calculos
        self.ControllerListar()

    def ControllerAdicionar(self, nome):
    	ModelDistribuidor.adiciona(self, nome)
    	self.ControllerListar()

    def ControllerListar(self):
    	self.list_distribuidores.delete(0, END)
    	lista = ModelDistribuidor.lista(self)

    	for d in lista:
    	    self.list_distribuidores.insert(END, d)

    def ControllerRemover(self, nome):
    	ModelDistribuidor.remove(self, nome)
    	self.ControllerListar()

    def ControllerAlterar(self, nome, novo_nome):
    	ModelDistribuidor.altera(self, nome, novo_nome)
    	self.ControllerListar()
    
    def voltar(self):
    	self.destroy()
    	root.update()
    	root.deiconify()

class ModelDistribuidor:
    def adiciona(self, nome):
        arq = open('distribuidores.txt', 'a')
        arq.write(nome + '\n')
        arq.close()

        print('Adicionando distribuidor: ' + nome)

    def lista(self):
        with open('distribuidores.txt') as f:
            conteudo = f.readlines()
        conteudo = [x.strip() for x in conteudo]
        return conteudo

    def remove(self, nome):
        arq = open('distribuidores.txt', 'r')
        lines = arq.readlines()
        arq.close()

        print(lines)

        arq = open('distribuidores.txt', 'w')
        for line in lines:
            if line != nome + '\n':
                arq.write(line)
        arq.close()

        print('Removendo distribuidor: ' + nome)

    def altera(self, nome, novo_nome):
        arq = open('distribuidores.txt', 'r')
        lines = arq.readlines()
        arq.close()

        print(lines)

        arq = open('distribuidores.txt', 'w')
        for line in lines:
            if line != nome + '\n':
                arq.write(line)
            else:
                arq.write(novo_nome + '\n')
        arq.close()

        print('Alterando distribuidos: ' + nome)
        
# -------------------- #

class ViewProduto(Toplevel):

    def __init__(self, master):
        self.master_frame = master
        Toplevel.__init__(self)

        self.transient(root)
        self.geometry('400x400')
        self.lift()

        # Elementos
        lbl_titulo = Label(self, text = "Produtos")

        lbl_nome = Label(self, text = "Nome:")
        txt_nome = Entry(self)

        lbl_consignado = Label(self, text = "Consignado:")
        var_rdio = IntVar()
        rdio_consignado = Radiobutton(self, text="Sim", variable=var_rdio, value=1)
        rdio_consignado.grid(row=2,column=1)
        rdio_consignado = Radiobutton(self, text="Não", variable=var_rdio, value=0)
        rdio_consignado.grid(row=2,column=2)

        lbl_distribuidor = Label(self, text = "Distribuidor:")
        var_drop = StringVar(root)
        list_distribuidores = ModelDistribuidor.lista(self)
        var_drop.set(list_distribuidores[0])
        popupMenu = OptionMenu(self, var_drop, *list_distribuidores)
        
        btn_alterar = Button(self, text = "Alterar", command = lambda:self.ControllerAlterar(self.list_produtos.get(ACTIVE),txt_nome.get()))
        btn_adicionar = Button(self, text = "Adicionar", command = lambda:self.ControllerAdicionar(txt_nome.get()))
        
        self.list_produtos = Listbox(self)
        btn_remover = Button(self, text = "Remover", command = lambda:self.ControllerRemover(self.list_produtos.get(ACTIVE)))

        btn_voltar = Button(self, text ="Voltar", command = lambda:self.voltar())

        # Layout
        lbl_titulo.grid(row=0,column=1)

        lbl_nome.grid(row=1,column=0)
        txt_nome.grid(row=1,column=1)

        lbl_consignado.grid(row=2,column=0)

        lbl_distribuidor.grid(row=3,column=0)
        popupMenu.grid(row=3,column=1)

        btn_adicionar.grid(row=4,column=2)
        btn_alterar.grid(row=4,column=3)

        self.list_produtos.grid(row=5,column=1)
        btn_remover.grid(row=5,column=2)

        btn_voltar.grid(row=6,column=1)

        # Calculos
        self.ControllerListar()

    def ControllerAdicionar(self, nome):
    	ModelProduto.adiciona(self, nome)
    	self.ControllerListar()

    def ControllerListar(self):
        self.list_produtos.delete(0, END)
        lista = ModelProduto.lista(self)

        for d in lista:
    	    self.list_produtos.insert(END, d)

    def ControllerRemover(self, nome):
    	ModelProduto.remove(self, nome)
    	self.ControllerListar()

    def ControllerAlterar(self, nome, novo_nome):
    	ModelProduto.altera(self, nome, novo_nome)
    	self.ControllerListar()
    
    def voltar(self):
    	self.destroy()
    	root.update()
    	root.deiconify()

class ModelProduto:
    def adiciona(self, nome):
        arq = open('produtos.txt', 'a')
        arq.write(nome + '\n')
        arq.close()

        print('Adicionando produto: ' + nome)

    def lista(self):
        with open('produtos.txt') as f:
            conteudo = f.readlines()
        conteudo = [x.strip() for x in conteudo]
        return conteudo

    def remove(self, nome):
        arq = open('produtos.txt', 'r')
        lines = arq.readlines()
        arq.close()

        print(lines)

        arq = open('produtos.txt', 'w')
        for line in lines:
            if line != nome + '\n':
                arq.write(line)
        arq.close()

        print('Removendo produto: ' + nome)

    def altera(self, nome, novo_nome):
        arq = open('produtos.txt', 'r')
        lines = arq.readlines()
        arq.close()

        print(lines)

        arq = open('produtos.txt', 'w')
        for line in lines:
            if line != nome + '\n':
                arq.write(line)
            else:
                arq.write(novo_nome + '\n')
        arq.close()

        print('Alterando produto: ' + nome)

# -------------------- #

root = Tk()
sistema = ViewPrincipal(root)
root.geometry('400x400')
root.mainloop()