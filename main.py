import tkinter as tk 
import tkinter as ttk
import controller as con

taxa_media_de_atendimento = 15 #hora mi
servidores = 5  #atendentes 
taxa_media_de_chegada = 500 #hora  lambda

janela_principal = tk.Tk()
janela_principal.title("Configuração de Filas")
janela_principal.resizable(True, True)

largura_janela = janela_principal.winfo_screenwidth() 
altura_janela = janela_principal.winfo_screenheight() 
janela_principal.geometry("%dx%d+0+0" % (largura_janela, altura_janela))

lambda_Frame = tk.LabelFrame(
    janela_principal,
    text="λ(Taxa Média de Chegada)=500/hora",
    width=270,
    height=75,
    borderwidth=0 
)

mi_Frame = tk.LabelFrame(
    janela_principal,
    text="μ(Taxa Média de atendimento)=15/hora",
    width=270,
    height=75,
    borderwidth=0 
)

c_Frame = tk.LabelFrame(
    janela_principal,
    text="c(Número de Servidores)=5",
    width=270,
    height=75,
    borderwidth=0 
)

Wq_Frame = tk.LabelFrame(
    janela_principal,
    text="Wq(Tempo médio de espera na fila)= "+str(con.tempo_de_espera_fila(taxa_media_de_chegada, taxa_media_de_atendimento))+"/horas",
    width=400,
    height=75,
    borderwidth=0
)


W_Frame = tk.LabelFrame(
    janela_principal,
    text="W(Tempo médio de espera no sistema)= "+str(con.tempo_de_espera_sistema(taxa_media_de_chegada, taxa_media_de_atendimento))+"/horas",
    width=400,
    height=75,
    borderwidth=0
)


tex: str = '''
     A configuração atual do sistema não vai conseguir atender todos os clientes já que λ>μ. \nNesse caso, mantendo as configurações de taxa média de chegada e de taxa de atendimento o ideal seria aumentar o número de atendentes para 33, já que: \n
                  
                  Capacidade de Atendimento Diária(Atual) = μ* Nº de atendentes * 24 = 15*5*24 = 1800\n
                  Chegada Diária no sistema = λ * 24 = 500 * 24 = 12000\n\n
                  
                  Nº de Atendentes ideal* 15 * 24 = 12000 => Nº de Atendentes ideal = 12000/15*24 = 33,33\n 

    Como alocar um número de atendentes tão alto pode ser inviável para o administrador, uma outra opção seria agendar os atendimentos para outros dias, fixando uma cota diária.\n    
    '''



Frame = tk.LabelFrame(
    janela_principal,
    text=str(tex),
    width=1100,
    height=300,
    borderwidth=0
)

lambda_Frame.place(in_=janela_principal, relx=0.2, rely=0.1, anchor=tk.CENTER)
mi_Frame.place(in_=janela_principal, relx=0.20, rely=0.15, anchor=tk.CENTER)
c_Frame.place(in_=janela_principal, relx=0.20, rely=0.20, anchor=tk.CENTER)
Wq_Frame.place(in_=janela_principal, relx=0.2, rely=0.25, anchor=tk.CENTER)
W_Frame.place(in_=janela_principal, relx=0.2, rely=0.30, anchor=tk.CENTER)
Frame.place(in_=janela_principal, relx=0.5, rely=0.6, anchor=tk.CENTER)


janela_principal.mainloop()

