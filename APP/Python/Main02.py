import tkinter as tk

def func_botao1():
    label.config(text="Execultando...")

def func_botao2():
    label.config(text="Execultando...")

def func_botao_Sair():
    label.config(text="Execultando...")
    janela.destroy()

# Criando a janela principal
janela = tk.Tk()
janela.title("App de Execulções Rápida.")

# definir tamanho de janela
janela.geometry("400x300")

# Definir cor de janela
janela.configure(bg="#352640")

# Criando os componentes da interface
botao1 = tk.Button(janela, text="Verificaçao Rápida de Upgrade.", command=func_botao1, bg="#059b9a")
botao2 = tk.Button(janela, text="Auto localizador de Pastas.", command=func_botao2, bg="#059b9a")
botao_Sair = tk.Button(janela, text="Exit", command=func_botao_Sair, bg="#FF0000")
label = tk.Label(janela, text="Selecione um botão de execulção", bg="#352640")

# Posicionando os componentes na janela
botao1.pack(pady=15)
botao2.pack(pady=15)
botao_Sair.place(x=100, y=100)
label.pack(pady=25)

# Iniciando o loop principal da interface
janela.mainloop()
 