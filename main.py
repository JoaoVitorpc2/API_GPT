import tkinter as tk
import requests
import json

def enviar_mensagem():
    mensagem = entrada.get()
    mensagens_listbox.insert(tk.END, "Você: " + mensagem)
    entrada.delete(0, tk.END)

    from senha import API_KEY

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        "model": id_modelo,
        "messages": [
            {"role": "system", "content": "Você: " + mensagem},
            {"role": "user", "content": mensagem}
        ]
    }

    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    resposta = requisicao.json()
    mensagem_resposta = resposta['choices'][0]['message']['content']
    mensagens_listbox.insert(tk.END, "Bot: " + mensagem_resposta)

# Cria a janela principal
janela = tk.Tk()
janela.title("Interface para Rodar Código")
janela.geometry("400x400")

# Configuração de estilo
bg_color = "#F0F0F0"  # Cor de fundo
fonte = ("Arial", 12)  # Fonte

# Cria uma listbox para exibir as mensagens do chat
mensagens_listbox = tk.Listbox(janela, width=50, height=15, bg=bg_color, font=fonte)
mensagens_listbox.pack(pady=10)

# Cria um campo de entrada para digitar as mensagens
entrada = tk.Entry(janela, width=50, font=fonte)
entrada.pack(pady=10)

# Cria um botão para enviar as mensagens
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem, bg=bg_color, font=fonte)
botao_enviar.pack(pady=5)

# Configuração de cores e estilo
janela.configure(bg=bg_color)
mensagens_listbox.configure(selectbackground="#A9A9A9")  # Cor de fundo do item selecionado na listbox

# Inicia o loop principal da interface gráfica
janela.mainloop()
