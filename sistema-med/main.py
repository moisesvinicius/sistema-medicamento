import tkinter as tk
from datetime import datetime, timedelta

def calcular_proxima_dose():
    try:
        # Obtém a hora e o intervalo do usuário
        hora_tomada = entry_hora.get()
        intervalo = int(entry_intervalo.get())
        
        # Converte a hora para um objeto datetime
        hora = datetime.strptime(hora_tomada, "%H:%M")
        
        # Calcula a próxima hora
        proxima_dose = hora + timedelta(hours=intervalo)
        
        # Formata a próxima hora como string
        proxima_dose_str = proxima_dose.strftime("%H:%M")
        
        # Atualiza a área de texto com a próxima hora
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete(1.0, tk.END)  
        texto_resultado.insert(tk.END, f"🕒 Você deve tomar o remédio novamente às {proxima_dose_str}.", "resultado")
        texto_resultado.config(state=tk.DISABLED)

    except ValueError:
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete(1.0, tk.END)  
        texto_resultado.insert(tk.END, "⚠️ Por favor, insira a hora no formato HH:MM e um intervalo válido.", "erro")
        texto_resultado.config(state=tk.DISABLED)

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Medicamento")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Título
label_titulo = tk.Label(root, text="Sistema de Lembrete de Medicamento", font=("Arial", 16), bg="#f0f0f0")
label_titulo.pack(pady=20)

# Campo para hora tomada
label_hora = tk.Label(root, text="Hora que tomou o remédio (HH:MM):", bg="#f0f0f0")
label_hora.pack(pady=5)
entry_hora = tk.Entry(root, font=("Arial", 14))
entry_hora.pack(pady=5)

# Campo para intervalo
label_intervalo = tk.Label(root, text="Intervalo até a próxima dose (horas):", bg="#f0f0f0")
label_intervalo.pack(pady=5)
entry_intervalo = tk.Entry(root, font=("Arial", 14))
entry_intervalo.pack(pady=5)

# Botão para calcular a próxima dose
botao_calcular = tk.Button(root, text="Calcular Próxima Dose", command=calcular_proxima_dose, bg="#4CAF50", fg="white", font=("Arial", 14))
botao_calcular.pack(pady=20)

# Área de texto para mostrar o resultado
texto_resultado = tk.Text(root, height=4, width=40, font=("Arial", 12), bg="#ffffff", wrap=tk.WORD)
texto_resultado.pack(pady=10)
texto_resultado.config(state=tk.DISABLED)  # Desabilita a edição inicial


texto_resultado.tag_config("resultado", foreground="green")  
texto_resultado.tag_config("erro", foreground="red")         


root.mainloop()
