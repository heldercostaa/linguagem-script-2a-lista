 # -*- coding: utf-8 -*-
 # project: 2a Lista de Exercícios
 # course: Linguagens de Programação Script
 # university: Universidade Federal do Ceará - UFC
 # author (github): heldercostaa

from tkinter import Tk, Label, Button, Entry, IntVar, Toplevel, Listbox, END, ACTIVE

# -------------------- #

class ViewPrincipal:

    def __init__(self, master):
        self.master = master
        master.title("Vem que Tem")

        # Elementos
        lbl_sub_titulo = Label(master, text="Mercadinho")
        lbl_titulo = Label(master, text="Vem que Tem")

        btn_distribuidor = Button(master, text="Distribuidores", command = lambda:self.viewDistribuidor())
        
        btn_sair = Button(master, text="Sair", command=self.master.quit)

        # Layout
        lbl_sub_titulo.grid(row=0)
        lbl_titulo.grid(row=1)

        btn_distribuidor.grid(row=2)
        
        btn_sair.grid(row=4)

    def viewDistribuidor(self):
        self.master.withdraw()
        ViewDistribuidor(self)

# -------------------- #

class ViewDistribuidor(Toplevel):

    def __init__(self, master):
        self.master_frame = master
        Toplevel.__init__(self)

        self.transient(root)
        self.geometry("400x300")
        self.lift()

        # Elementos
        lbl_titulo = Label(self, text = "Distribuidores")

        lbl_nome = Label(self, text = "Nome:")
        txt_nome = Entry(self)
        btn_alterar = Button(self, text = "Alterar", command = lambda:self.alterar(self.list_distribuidores.get(ACTIVE),txt_nome.get()))
        btn_adicionar = Button(self, text = "Adicionar", command = lambda:self.adicionar(txt_nome.get()))
        
        self.list_distribuidores = Listbox(self)
        btn_remover = Button(self, text = "Remover", command = lambda:self.remover(self.list_distribuidores.get(ACTIVE)))


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
        self.listar()

    def adicionar(self, nome):
    	ModelDistribuidor.adiciona(self, nome)
    	self.listar()

    def listar(self):
    	self.list_distribuidores.delete(0, END)
    	lista = ModelDistribuidor.lista(self)

    	for d in lista:
    	    self.list_distribuidores.insert(END, d)

    def remover(self, nome):
    	ModelDistribuidor.remove(self, nome)
    	self.listar()

    def alterar(self, nome, novo_nome):
    	ModelDistribuidor.altera(self, nome, novo_nome)
    	self.listar()
    
    def voltar(self):
    	self.destroy()
    	root.update()
    	root.deiconify()

class ModelDistribuidor:
    def adiciona(self, nome):
        arq = open('distribuidores.txt', 'a')
        arq.write(nome + '\n')
        arq.close()

        print('Nome adicionado com sucesso')

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

        print('removendo ' + nome)

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

        print('alterando ' + nome)
        
# -------------------- #

# classe ViewProduto

# -------------------- #

root = Tk()
sistema = ViewPrincipal(root)
root.geometry("340x300")
root.mainloop()