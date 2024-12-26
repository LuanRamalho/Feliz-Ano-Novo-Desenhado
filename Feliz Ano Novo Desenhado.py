import tkinter as tk
from tkinter import ttk

# Função para criar a interface gráfica
def criar_interface():
    # Janela principal
    root = tk.Tk()
    root.title("Feliz Ano Novo 2025")
    root.geometry("800x600")  # Define o tamanho da janela
    root.configure(bg="#000000")  # Cor de fundo preta para contraste

    # Título principal
    titulo = tk.Label(
        root,
        text="Feliz Ano Novo",
        font=("Helvetica", 48, "bold"),
        fg="#FFD700",  # Cor dourada
        bg="#000000"
    )
    titulo.pack(pady=30)

    # Subtítulo (ano 2025)
    subtitulo = tk.Label(
        root,
        text="2025",
        font=("Helvetica", 80, "bold"),
        fg="#FF4500",  # Cor laranja vibrante
        bg="#000000"
    )
    subtitulo.pack(pady=20)

    # Elementos decorativos - fogos de artifício simulados
    canvas = tk.Canvas(root, width=800, height=300, bg="#000000", highlightthickness=0)
    canvas.pack()

    # Desenhando fogos de artifício com círculos coloridos
    cores = ["#FF4500", "#FFD700", "#00FF00", "#00BFFF", "#FF1493"]
    for i in range(20):
        x = randint(50, 750)
        y = randint(50, 250)
        tamanho = randint(20, 50)
        cor = choice(cores)
        canvas.create_oval(
            x - tamanho, y - tamanho, x + tamanho, y + tamanho, fill=cor, outline=""
        )

    # Loop principal da interface
    root.mainloop()

# Chamando a função para executar o programa
if __name__ == "__main__":
    from random import randint, choice
    criar_interface()
