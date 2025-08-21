import tkinter as tk
from tkinter import messagebox as mb

# -----------------------------
# Banco de preguntas (datos)
# -----------------------------
QUESTIONS = [
    {
        "q": "¿Qué enfatiza la programación estructurada?",
        "options": [
            "Lógica aleatoria y desordenada",
            "Uso de funciones y control lógico del flujo",
            "Optimización de hardware",
            "Programación de bajo nivel",
        ],
        "answer": 1,
        "explanation": "La programación estructurada organiza el código con funciones, condicionales y bucles para un flujo lógico claro.",
    },
    {
        "q": "¿Qué es un pseudocódigo?",
        "options": [
            "Un tipo de lenguaje compilado",
            "Un diagrama visual del código",
            "Una descripción del algoritmo en lenguaje natural",
            "Un componente gráfico de una interfaz",
        ],
        "answer": 2,
        "explanation": "El pseudocódigo expresa la lógica sin la sintaxis estricta de un lenguaje de programación.",
    },
    {
        "q": "¿Cuáles son las tres etapas básicas de un programa?",
        "options": [
            "Compilar - Ejecutar - Depurar",
            "Entrada - Proceso - Salida",
            "Planear - Codificar - Ejecutar",
            "Leer - Escribir - Cerrar",
        ],
        "answer": 1,
        "explanation": "El modelo EPS (Entrada-Proceso-Salida) describe el flujo fundamental de un algoritmo.",
    },
    {
        "q": "¿Cuál de los siguientes es un lenguaje compilado?",
        "options": ["Python", "JavaScript", "C++", "HTML"],
        "answer": 2,
        "explanation": "C++ se compila completamente a lenguaje máquina antes de ejecutarse.",
    },
    {
        "q": "¿Cuál es una característica clave de los lenguajes interpretados?",
        "options": [
            "El código se compila completamente antes de ejecutarse",
            "El código se ejecuta línea por línea",
            "No requieren traducción a lenguaje máquina",
            "Son más rápidos que los compilados",
        ],
        "answer": 1,
        "explanation": "Lenguajes como Python y JavaScript son interpretados línea por línea en tiempo de ejecución.",
    },
    {
        "q": "¿Qué se debe imprimir para el número 15 en FizzBuzz?",
        "options": ["Fizz", "Buzz", "FizzBuzz", "15"],
        "answer": 2,
        "explanation": "15 es múltiplo de 3 y de 5, por eso corresponde 'FizzBuzz'.",
    },
    {
        "q": "¿Cuál es el beneficio de modularizar la lógica FizzBuzz en una función?",
        "options": [
            "Evitar usar bucles",
            "Facilitar la depuración y reutilización del código",
            "Aumentar el tiempo de ejecución",
            "Imprimir los números más rápido",
        ],
        "answer": 1,
        "explanation": "Encapsular la lógica en una función la hace reutilizable y más fácil de probar.",
    },
    {
        "q": "¿Cómo puede el usuario aplicar la lógica FizzBuzz a rangos personalizados?",
        "options": [
            "Codificando valores fijos",
            "Importando librerías externas",
            "Usando entrada para definir el rango",
            "Eliminando las condiciones",
        ],
        "answer": 2,
        "explanation": "Pedir por entrada el inicio y fin permite aplicar FizzBuzz a cualquier rango.",
    },
    {
        "q": "¿Para qué se usa Tkinter en Python?",
        "options": [
            "Desarrollo web",
            "Programación de interfaces gráficas",
            "Gestión de bases de datos",
            "Diseño de videojuegos en C++",
        ],
        "answer": 1,
        "explanation": "Tkinter es el módulo estándar de Python para crear GUIs multiplataforma.",
    },
    {
        "q": "¿Qué hace ventana.geometry('300x150') en Tkinter?",
        "options": [
            "Añade un botón a la ventana",
            "Establece el título de la ventana",
            "Define las dimensiones de la ventana",
            "Cambia el texto de una etiqueta",
        ],
        "answer": 2,
        "explanation": "Define ancho x alto de la ventana principal en píxeles.",
    },
    {
        "q": "¿Qué hace el parámetro command en un botón de Tkinter?",
        "options": [
            "Cambia el color del botón",
            "Enlaza una función al botón",
            "Añade una etiqueta",
            "Ajusta el tamaño de la ventana",
        ],
        "answer": 1,
        "explanation": "command especifica la función que se ejecuta al hacer clic.",
    },
    {
        "q": "¿Qué describe mejor a una tupla en Python?",
        "options": [
            "Ordenada e inmutable",
            "Desordenada y mutable",
            "Mutable con claves duplicadas",
            "Usa pares clave-valor",
        ],
        "answer": 0,
        "explanation": "Las tuplas mantienen orden y no pueden modificarse tras su creación.",
    },
    {
        "q": "¿Cuál NO es verdadera sobre los diccionarios?",
        "options": [
            "Las claves deben ser únicas",
            "Se puede acceder a los valores mediante las claves",
            "Son inmutables",
            "Mantienen el orden de inserción",
        ],
        "answer": 2,
        "explanation": "Los diccionarios son mutables (por eso 'son inmutables' es falso).",
    },
    {
        "q": "¿Cuál de las siguientes afirmaciones sobre los sets es verdadera?",
        "options": [
            "Permiten elementos duplicados",
            "Se acceden por índice",
            "Son desordenados y mutables",
            "Almacenan pares clave-valor",
        ],
        "answer": 2,
        "explanation": "Los sets no mantienen orden, no permiten duplicados y son mutables.",
    },
]

# -----------------------------
# Lógica de la aplicación
# -----------------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz de Fundamentos de Programación")
        self.root.geometry("720x420")
        self.root.minsize(600, 380)

        self.index = 0
        self.answered = [None] * len(QUESTIONS)    # guarda índice de opción marcada
        self.correct = [False] * len(QUESTIONS)    # guarda si acertó

        # Variables UI
        self.selected = tk.IntVar(value=-1)

        # Encabezado
        self.header = tk.Label(
            root, text="Quiz de Fundamentos de Programación",
            font=("Segoe UI", 16, "bold")
        )
        self.header.pack(pady=(12, 6))

        # Número de pregunta
        self.progress = tk.Label(root, text="", font=("Segoe UI", 10))
        self.progress.pack()

        # Marco principal
        self.container = tk.Frame(root, padx=16, pady=10)
        self.container.pack(fill="both", expand=True)

        # Enunciado
        self.question_lbl = tk.Label(
            self.container, text="", wraplength=660, justify="left", anchor="w",
            font=("Segoe UI", 12, "bold")
        )
        self.question_lbl.pack(anchor="w", pady=(4, 10))

        # Opciones
        self.options_frame = tk.Frame(self.container)
        self.options_frame.pack(anchor="w", fill="x")

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame,
                text="", variable=self.selected, value=i, anchor="w",
                justify="left", wraplength=640, font=("Segoe UI", 11)
            )
            rb.pack(anchor="w", pady=3)
            self.option_buttons.append(rb)

        # Feedback
        self.feedback_lbl = tk.Label(
            self.container, text="", wraplength=660, justify="left",
            font=("Segoe UI", 10)
        )
        self.feedback_lbl.pack(anchor="w", pady=(8, 4))

        # Barra de botones
        self.btns = tk.Frame(root, pady=8)
        self.btns.pack(fill="x")

        self.prev_btn = tk.Button(self.btns, text="⟵ Anterior", command=self.prev_q)
        self.submit_btn = tk.Button(self.btns, text="Responder", command=self.submit)
        self.next_btn = tk.Button(self.btns, text="Siguiente ⟶", command=self.next_q)
        self.reset_btn = tk.Button(self.btns, text="Reiniciar", command=self.reset)

        self.prev_btn.pack(side="left", padx=6)
        self.reset_btn.pack(side="left", padx=6)
        self.submit_btn.pack(side="right", padx=6)
        self.next_btn.pack(side="right", padx=6)

        self.refresh()

    def refresh(self):
        q = QUESTIONS[self.index]
        self.progress.config(text=f"Pregunta {self.index + 1} de {len(QUESTIONS)}")
        self.question_lbl.config(text=q["q"])

        # Cargar opciones
        for i, text in enumerate(q["options"]):
            self.option_buttons[i].config(text=text, state="normal")

        # Estado según si ya fue respondida
        if self.answered[self.index] is None:
            self.selected.set(-1)
            self.feedback_lbl.config(text="", fg="#333")
            self.submit_btn.config(state="normal")
            for rb in self.option_buttons:
                rb.config(state="normal")
        else:
            self.selected.set(self.answered[self.index])
            # mostrar feedback previo
            if self.correct[self.index]:
                self.feedback_lbl.config(
                    text=f"✔ Correcto. {q['explanation']}", fg="#0A8A0A"
                )
            else:
                ans_text = q["options"][q["answer"]]
                self.feedback_lbl.config(
                    text=f"✖ Incorrecto. Respuesta: '{ans_text}'. {q['explanation']}",
                    fg="#B00020"
                )
            # bloquear edición
            self.submit_btn.config(state="disabled")
            for rb in self.option_buttons:
                rb.config(state="disabled")

        # Habilitar/deshabilitar navegación
        self.prev_btn.config(state="normal" if self.index > 0 else "disabled")
        self.next_btn.config(state="normal" if self.index < len(QUESTIONS) - 1 else "disabled")

    def submit(self):
        choice = self.selected.get()
        if choice == -1:
            mb.showinfo("Aviso", "Selecciona una opción antes de responder.")
            return
        if self.answered[self.index] is not None:
            # Ya estaba respondida
            return

        q = QUESTIONS[self.index]
        self.answered[self.index] = choice
        is_correct = choice == q["answer"]
        self.correct[self.index] = is_correct

        if is_correct:
            self.feedback_lbl.config(
                text=f"✔ Correcto. {q['explanation']}", fg="#0A8A0A"
            )
        else:
            ans_text = q["options"][q["answer"]]
            self.feedback_lbl.config(
                text=f"✖ Incorrecto. Respuesta: '{ans_text}'. {q['explanation']}",
                fg="#B00020"
            )

        # Bloquear cambios
        self.submit_btn.config(state="disabled")
        for rb in self.option_buttons:
            rb.config(state="disabled")

        # Si es la última pregunta y todas están respondidas, mostrar resultado
        if all(a is not None for a in self.answered):
            self.show_results()

    def next_q(self):
        if self.index < len(QUESTIONS) - 1:
            self.index += 1
            self.refresh()

    def prev_q(self):
        if self.index > 0:
            self.index -= 1
            self.refresh()

    def reset(self):
        if mb.askyesno("Reiniciar", "¿Quieres reiniciar el cuestionario? Se perderán tus respuestas."):
            self.index = 0
            self.answered = [None] * len(QUESTIONS)
            self.correct = [False] * len(QUESTIONS)
            self.refresh()

    def show_results(self):
        total = len(QUESTIONS)
        score = sum(self.correct)
        pendientes = self.answered.count(None)
        msg = f"Puntaje: {score}/{total}\n"
        if pendientes:
            msg += f"Preguntas pendientes: {pendientes}\n"
        else:
            msg += "¡Has respondido todas las preguntas!\n"
        mb.showinfo("Resultados", msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()