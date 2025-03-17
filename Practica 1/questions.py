import random
import sys 

# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]

puntaje_total = 0.0

# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

for question, options, correct_index in questions_to_ask:
    print(question)
    for i, option in enumerate(options, start = 1):
        print(f"{i}) {option}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
            if not (0 <= user_answer < len(options)):
                raise ValueError
        except ValueError:
            print("Respuesta no valida." , flush=True)
            sys.exit(1)

        if (user_answer == correct_index):
            print("¡Correcto!\n")
            puntaje_total += 1.0
            break
        else:
            puntaje_total -= .5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correctas
        print(f"Incorrecto. La respuesta correcta es: {correct_index + 1}) {options[correct_index]}\n")

print(f"El puntaje total es: {puntaje_total}")