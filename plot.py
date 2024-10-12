import matplotlib.pyplot as plt
import pandas as pd
import locale
from datetime import datetime

# Establecer la localización a español (esto puede variar según el sistema operativo)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para Linux/Unix
# locale.setlocale(locale.LC_TIME, 'es_ES')  # Para Windows

# Lista de datos: (plain_text, cipher_text)
data = [
    ("11 de marzo", "Federación-Gloria-Argentina"),
    ("14 de marzo", "Federación-sistema-de América"),
    ("5 de junio", "Empleados-sin pudor-baldón"),
    ("6 de junio", "Nación-sin garantías-teoría"),
    ("1 de abril", "Quiroga-Ilustre-Invicto"),
    ("16 de abril", "Motín-mancha-unitaria"),
    ("8 de mayo", "Unitarios-mancharon-la Historia"),
    ("19 de mayo", "Federación-clamor-popular"),
    ("7 de junio", "Derechos-sin deberes-violencia"),
    ("17 de abril", "Centro-marchando-glorioso"),
    ("24 de abril", "De Bahía- corta-distancia"),
    ("26 de abril", "Del mar-sólo-una legua"),
    ("27 de abril", "Los indios-enemigos-se someten"),
    ("29 de abril", "Pronto-estaremos-en marcha"),
    ("5 de abril", "El otoño-se anuncia-húmedo"),
    ("29 de junio", "Chocory-corrido-deshecho"),
    ("24 de julio", "Pacheco-marchando-glorioso"),
    ("30 de julio", "Chocori-pagó-sus delitos"),
    ("2 de julio", "Codicia-envilece-el espíritu"),
    ("14 de abril", "Constancia-supera-imposibles"),
    ("7 de mayo", "Fanatismo-preocupación-infernal"),
    ("12 de mayo", "Orgullo-aleja-amistades"),
    ("12 de julio", "Crueldad-muestra-cobardía"),
    ("16 de julio", "Culto-sin Piedad-profanación"),
    ("19 de julio", "Trabajo-sin método-ruina"),
    ("17 de julio", "Amor-sin respeto-novela"),
    ("21 de julio", "Patriotismo-sin desprendimiento-conversación"),
    ("25 de mayo", "Salve-Mayo-Glorioso"),
    ("16 de marzo", "Al sud-está-la gloria"),
    ("15 de abril", "Patricios-virtuosos-guerreros"),
    ("23 de abril", "El ocio-enerva-al soldado"),
    ("5 de mayo", "Se desean-glorias-a la vanguardia"),
    ("10 de mayo", "Colorado-Negro-Federación o Muerte"),
    ("8 de abril", "Naturaleza-pródiga-en la sierra"),
    ("22 de diciembre", "Humilde-soledad-verde y sonora"),
]

# Crear DataFrame a partir de los datos
df = pd.DataFrame(data, columns=["plain_text", "cipher_text"])

# Convertir las fechas al formato datetime (asumiendo que el año es 2024)
df["date"] = pd.to_datetime(df["plain_text"], format="%d de %B", errors='coerce').map(lambda x: x.replace(year=1833))

# Ordenar el DataFrame por la fecha
df = df.sort_values(by="date")

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["cipher_text"], marker='o', linestyle='-', color='b')

# Añadir etiquetas y títulos
plt.title("Línea temporal de textos")
plt.xlabel("Fecha")
plt.ylabel("Texto")
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la gráfica
plt.show()

