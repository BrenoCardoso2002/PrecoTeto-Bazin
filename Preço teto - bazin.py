# Importações:
import tkinter as tk
import tkinter.messagebox as messagebox

# Função que fecha janela:
def close_window(event):
  if event.char == chr(27):  # Verifica se o "esc" foi pressionado
    janela.destroy() # fecha a janela

# Função que limpa todos os campos:
def limpar():
    input01.delete(0, tk.END)
    input02.delete(0, tk.END)
    input03.delete(0, tk.END)
    input04.delete(0, tk.END)
    input05.delete(0, tk.END)
    input06.delete(0, tk.END)
    input01.focus()

# Função que calcula o preço teto:
def calcular():
    # Verifica a inserção de dados:
    try:
        # Obtém os valores das caixas de texto:
        proventos = []
        proventos.append(float(input02.get().replace(",", ".")))
        proventos.append(float(input03.get().replace(",", ".")))
        proventos.append(float(input04.get().replace(",", ".")))
        proventos.append(float(input05.get().replace(",", ".")))
        proventos.append(float(input06.get().replace(",", ".")))

        # calcula a média e preço teto:
        media = sum(proventos) / len(proventos)
        preco_teto = media / 0.06

        # Verifica se o ticker foi recebido e exibe o resultado:
        if input01.get().replace(" ", "") == "":
            messagebox.showerror(title="Erro!", message="Os valores inseridos não são válidos.")
        else:
            messagebox.showinfo(title="Preço teto - Décio Bazin!", message=f"Ticker: {input01.get().upper()}\nPreço teto: R${preco_teto:.2f}\nYield: 6%")

    # Tratamento do erro:
    except ValueError:
        messagebox.showerror(title="Erro!", message="Os valores inseridos não são válidos.")

# Cria a janela:
janela = tk.Tk()
janela.title("Preço teto - Décio Bazin")
janela.geometry("330x220")

# Label 01 - Titulo:
label01 = tk.Label(janela, text="Preço teto - Décio Bazin", font=("Arial", 14))
label01.grid(row=0, columnspan=3)

# Label 02 - Ticker:
label02 = tk.Label(janela, text="Ticker do ativo:", font=("Arial", 12))
label02.grid(row=1, column=0)

# Label 03 - Dividendo ano 01:
label03 = tk.Label(janela, text="Provento do ano 01:", font=("Arial", 12))
label03.grid(row=2, column=0)

# Label 04 - Dividendo ano 02:
label04 = tk.Label(janela, text="Provento do ano 02:", font=("Arial", 12))
label04.grid(row=3, column=0)

# Label 05 - Dividendo ano 03:
label05 = tk.Label(janela, text="Provento do ano 03:", font=("Arial", 12))
label05.grid(row=4, column=0)

# Label 06 - Dividendo ano 04:
label06 = tk.Label(janela, text="Provento do ano 04:", font=("Arial", 12))
label06.grid(row=5, column=0)

# Label 07 - Dividendo ano 05:
label07 = tk.Label(janela, text="Provento do ano 05:", font=("Arial", 12))
label07.grid(row=6, column=0)

# Label 08 - Espaco entre Label e Caixa de texto:
label08 = tk.Label(janela, text=" ", font=("Arial", 12))
label08.grid(row=1, column=1)

# Input 01 - Ticker:
input01 = tk.Entry(janela)
input01.grid(row=1, column=2)
input01.focus()

# Input 02 - Ticker:
input02 = tk.Entry(janela)
input02.grid(row=2, column=2)

# Input 03 - Ticker:
input03 = tk.Entry(janela)
input03.grid(row=3, column=2)

# Input 04 - Ticker:
input04 = tk.Entry(janela)
input04.grid(row=4, column=2)

# Input 05 - Ticker:
input05 = tk.Entry(janela)
input05.grid(row=5, column=2)

# Input 06 - Ticker:
input06 = tk.Entry(janela)
input06.grid(row=6, column=2)

# Label 09 - Espaco entre as caixas de texto e os botões:
label09 = tk.Label(janela, text=" ", font=("Arial", 6))
label09.grid(row=7, column=0)

# Botão 01 - Calcular:
button01 = tk.Button(janela, text="CALCULAR", command=calcular)
button01.grid(row=8, column=0)

# Botão 02 - Limpar:
button02 = tk.Button(janela, text="LIMPAR", command=limpar)
button02.grid(row=8, column=2)

# Associa a tecla "esc" à função de fechar janela
janela.bind("<Escape>", close_window)

# Loop principal da janela:
janela.mainloop()
