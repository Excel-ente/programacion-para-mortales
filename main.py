print("🔍 Bienvenido a la Máquina de las Adivinanzas")
print("Tenés que adivinar una palabra secreta. Pista: es algo que usamos todos los días para buscar en internet.")

respuesta_correcta = "navegador"
intentos = 0
respuesta = ""

while respuesta != respuesta_correcta:
    respuesta = input("❓ ¿Cuál creés que es la palabra secreta? ").lower()
    intentos += 1

    if respuesta == "computadora":
        print("💻 Cerca... pero no es eso. Es algo que usás dentro de la computadora.")
    elif respuesta == "google":
        print("🌐 Mmm... estás en la zona correcta. ¡Pero pensá más general!")
    elif respuesta != respuesta_correcta:
        print("❌ Nope. ¡Intentá de nuevo!")

print("🎉 ¡Acertaste! La palabra era:", respuesta_correcta)
print("✨ Lo lograste en", intentos, "intento(s). ¡Sos un crack de la lógica!")
