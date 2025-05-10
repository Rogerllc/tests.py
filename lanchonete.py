#Biblioteca tkinter
#Para criar uma interface gráfica
import tkinter as tk
from tkinter import messagebox
#cardapio como dicionario
cardapio = {
      "Cachorro Quente": 10.00,
      "X-Salada": 15.00,
      "X-Bacon": 20.00,
      "Misto Quente": 8.00,
      "Refrigerante": 5.00,
      "Suco": 7.00,
      "Água": 3.00
}
#Lista para armazenar os pedidos
pedido = []
#função para adicionar um item ao pedido
def adicionar_pedido(item):
    pedido.append(item)
    atualizar_pedido()

def atualizar_pedido():
    texto_pedido.delete("1.0", tk.END)
    total = 0 
    for item in pedido:
        preco = cardapio[item]
        texto_pedido.insert(tk.END, f"{item}: R$ {preco:.2f}\n")
        total += preco
    texto_pedido.insert(tk.END, f"Total: R$ {total:.2f}\n")
    
def finalizar_pedido():
    if not pedido:
        messagebox.showinfo("Peido", "Seu pedido esta vazio.")
    else:
        atualizar_pedido()
        messagebox.showinfo("Pedido", "Seu pedido foi finalizado com sucesso!")
        # Limpar o pedido
        pedido.clear()
        atualizar_pedido()

#criando janela
janela = tk.Tk()
janela.title("Jack Lanches")
janela.geometry("400x500")

#Titulo
titulo = tk.Label(janela, text= "Cardapio", font=("Arial", 20))
titulo.pack(pady=10)

#Criando os botoes
for item, preco in cardapio.items():
    botao = tk.Button(janela, text=f"{item} R$ {preco:.2f}", width= 20,
                      command=lambda item=item: adicionar_pedido(item))
    botao.pack(pady=5)

#Criando o texto do pedido
label_pedido = tk.Label(janela, text="\nSeu pedido:", font=("Arial", 12))
label_pedido.pack()

texto_pedido= tk.Text(janela, width=40, height=10)
texto_pedido.pack(pady=10)

#Criando o botao de finalizar pedido
botao_finalizar = tk.Button(janela, text="Finalizar Pedido", width=20,
                            command=finalizar_pedido)
botao_finalizar.pack(pady=10)

#loop de janela
janela.mainloop()