#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa scanner

# Programado por: Matthew Price
# Nick Lizard Squad
# Versão python utilizada: python2.7
# importação dos módulos necessários para ao funcionamento do programa

# modulo de interface gráfica " Tkinter "
from Tkinter import *
# modulo de sistema " sys "
import sys
# modulo para criar e manipular pacotes de rede em python " scapy "
from scapy.all import *
# importar o modulo system
from os import system

def help():
    # imprime o conjunto de  strings entre """  """ na tela
    print """  

____________________111¶¶¶¶1111___________________
_______________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_______________
__________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________
_______1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________
____1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1____________
_1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11____________
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶____________
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_1¶¶¶1___________
_1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶___________
__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶¶¶¶¶¶¶¶¶¶___________
___¶1111¶¶¶¶¶¶¶¶¶¶¶111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________
___1¶¶¶¶111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1__________
_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________
______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_________
______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1____
_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
_______1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶1
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1__¶¶¶¶¶¶¶¶
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_____¶¶¶¶¶¶¶¶¶
____1¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1______1¶¶¶¶¶¶¶¶¶1
___1¶¶¶¶¶1__1¶¶¶¶¶¶¶¶¶¶¶¶¶11_________1¶¶¶¶¶¶¶¶¶¶1_
___¶¶¶¶¶¶¶________________________1¶¶¶¶¶¶¶¶¶¶¶¶___
__¶¶¶¶¶¶¶¶¶¶1________________11¶¶¶¶¶¶¶¶¶¶¶¶¶1_____
__1¶¶¶¶¶¶¶¶¶¶¶¶¶111__1111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_______
___1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1__________
_____1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1______________
________111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111____________________


        ============================
        = Scanner via IP           =
        ============================
        = Criado por Matthew Price =
        ============================================================
        = Opções:                                                  =
        = [-t] Utilizar  o programa em modo texto                  =
        = EXEMPLO: python matthew.py -t <ip destino>               =
        =                                                          =
        = [-g] Utilizar o programa no modo interface gráfica       =
        = EXEMPLO: python matthew.py -g                            =
        =                                                          =
        = [--help ] ajuda do  programa                             =
        = EXEMPLO python matthew.py --help                         =
        =                                                          =
        = [--verion] exibe a versão do programa                    =
        = EXEMPLO: python matthew.py --version                     =
        ============================================================

    """
# se os argumentos passados forem menores do que 2,
# o programa apresentará uma mensagem de erro e chamará a função help()
# finalizando a execução.
if len(sys.argv) < 2:
    system('clear')
    print "ERRO !"
    print "Nenhum argumento foi passado"
    help()
    sys.exit()
elif sys.argv[1].startswith('--'): # se o 1º argumentos iniciar com --
    op = sys.argv[1][2:] # a variável op recebe o argumento sem os dois traços " -- "
    if op == 'help': # se a variável op for igual a 'help'
        help() # chama a função help()
        sys.exit() # encerra a execução do programa
    if op == 'version': # se a variável op for igual a 'version'
        # imprime a versão do programa
        # imprime a string entre " " na tela
        print """
            Scanner via IP
            Versão 2017

            Dados do programador:
            Matthew Price

        """
        sys.exit() # encerra a execução do programa
    else: # se não
        print "Opção inválida" # imprime a string entre " " na tela
        sys.exit() # encerra a execução do programa

elif sys.argv[1] == "-t":
    alvo = sys.argv[2] # a variável alvo recebe o segundo argumento
    ip = IP() # a variável ip recebe a função IP() pertencente ao scapy
    ping = ICMP() # a variável ping recebe a função ICMP() responsável em criar o pacote do ping
    ip.dst = alvo # o destino da variável ip recebe o alvo
    resp = sr1(ip/ping) # a variável resp recebe o pacote de envio
    res = sr1(ARP(pdst=sys.argv[2])) # envia o pacote ao alvo e permite a análise
    mac = res.hwsrc # a variável mac recebe o mac do alvo. Isso é muito simples através da linguagem python. :-)
    if resp.ttl < 65: # se resp.ttl, isto é o ttl do sistema do alvo for < 65, será Linux.
        '''
        Para quem não sabe fica uma dica abaixo sobre o ttl dos sistemas operacionais:
        ● Cyclades - Normalmente 30
        ● Linux - Normalmente 64
        ● Windows - Normalmente 128
        ● Cisco - Normalmente 255
        ● Linux + iptables - Normalmente 255
        '''
        # imprime o conjunto de  strings entre """  """ na tela
        print """
        SISTEMA OPERACIONAL
            =========
            = LINUX = MAC: %s
            =========
        """ %mac
    else:
        # imprime o conjunto de  strings entre """  """ na tela
        print """
        SISTEMA OPERACIONAL
            ===========
            = WINDOWS = MAC %s
            ===========
        """ %mac


elif sys.argv[1] == '-g':
    # INTERFACE GRÁFICA
    class Programa:
        def __init__(self, toplevel):
            self.frame1=Frame(toplevel.title(" Scanner via IP"))
            self.frame1.pack()
            self.frame2=Frame(toplevel)
            self.frame2.pack()
            self.frame3=Frame(toplevel)
            self.frame3.pack()
            self.frame4=Frame(toplevel)
            self.frame4.pack()
            self.frame5=Frame(toplevel)
            self.frame5.pack()
            self.frame6=Frame(toplevel)
            self.frame6.pack()

            Label(self.frame1,text='matthew_price', fg='darkblue',font=('Verdana','10','bold'), height=2).pack() # cria uma Label
            fonte1=('Negrito','10','bold') # define a fonte

            Label(self.frame2,text='IP: ',font=fonte1,width=20).pack(side=LEFT) # cria uma Label

            self.ip=Entry(self.frame2,width=15,font=fonte1) # cria uma entrada, onde o usuário ira digitar numa caixa de texto
            self.ip.focus_force() # força o foco em self.ip
            self.ip.pack(side=LEFT) # define a posição do objeto


            Label(self.frame3,font=fonte1,height=1,text='SO: ').pack(side=LEFT) # cria uma Label
            self.msg1=Label(self.frame3,font=fonte1,height=3,text='AGUARDANDO...') # cria uma Label
            self.msg1.pack(side=RIGHT)  # define a posição do objeto
            Label(self.frame4,font=fonte1,height=3,text='MAC: ').pack(side=LEFT)  # cria uma Label
            self.msg2=Label(self.frame4,font=fonte1,height=1,text='AGUARDANDO...')
            self.msg2.pack(side=RIGHT)  # define a posição do objeto

            self.conferir=Button(self.frame5, font=fonte1, text="Iniciar", bg="Silver", command=self.conf) # cria um botão que chama a função conf
            self.conferir.pack(side=LEFT)

            self.conferir=Button(self.frame5, font=fonte1, text="Limpar", bg="Silver", command=self.limpa)# cria um botão que chama a função limpa
            self.conferir.pack(side=RIGHT)

        # função confi
        # Todos os componentes dentro de conf são os mesmos explicados no início do código.
        # O que há de diferente aqui é o uso da interface gráfica
        def conf(self):
            alvo=self.ip.get()
            ip = IP()
            ping = ICMP()
            ip.dst = alvo
            resp = sr1(ip/ping)
            if resp.ttl == 64:
                self.msg1['text'] = "LINUX"
                self.msg1['fg']='darkgreen'
            elif resp.ttl == 128:
                self.msg1['text'] = "Windows"
                self.msg1['fg']='red'
            elif resp.ttl == 30:
                self.msg1['text'] = "Cyclades"
                self.msg1['fg']='darkgreen'
            else:
                self.msg1['text'] = "Desconhecido"
                self.msg1['fg']='darkgreen'
            res = sr1(ARP(pdst=self.ip.get()))
            self.msg2['text'] = res.hwsrc
            self.msg2['fg']='red'
        #função limpa
        # o objetivo desta função é limpar todos os componentes visíveis do programa (Label)
        def limpa(self):
            self.ip.delete(INSERT, END)
            self.msg1['text'] = " "
            self.msg2['text'] = " "





    instancia=Tk()          #################################################################################
    Programa(instancia)     # Mantém o programa aberto até que um evento seja chamado e finalize a execução #
    instancia.mainloop()        #################################################################################

else:
    print ("Opção inválida !")