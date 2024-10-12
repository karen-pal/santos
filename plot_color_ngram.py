import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import locale
from datetime import datetime
import matplotlib.patches as mpatches

# Establecer la localización a español (esto puede variar según el sistema operativo)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para Linux/Unix
# locale.setlocale(locale.LC_TIME, 'es_ES')  # Para Windows

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
# Lista de colores predefinidos para asignar a las palabras
color_map2 = {
    "Federación": "green",            # ya definido
    "Gloria": "yellow",               # ya definido
    "Argentina": "blue",              # ya definido
    "sistema": "gray",                # ya definido
    "de América": "purple",           # ya definido
    "Empleados": "brown",
    "sin pudor": "orange",
    "baldón": "pink",
    "Nación": "gold",
    "sin garantías": "lightblue",
    "teoría": "lightgreen",
    "Quiroga": "crimson",
    "Ilustre": "navy",
    "Invicto": "lightcoral",
    "Motín": "olive",
    "mancha": "lightgray",
    "unitaria": "darkgreen",
    "Unitarios": "lime",
    "mancharon": "darkred",
    "la Historia": "cyan",
    "clamor": "maroon",
    "popular": "salmon",
    "Derechos": "darkblue",
    "sin deberes": "chocolate",
    "violencia": "black",
    "Centro": "turquoise",
    "marchando": "silver",
    "glorioso": "orchid",
    "De Bahía": "sienna",
    "corta": "coral",
    "distancia": "khaki",
    "Del mar": "darkorange",
    "sólo": "darkmagenta",
    "una legua": "beige",
    "Los indios": "peru",
    "enemigos": "tan",
    "se someten": "goldenrod",
    "Pronto": "darkslateblue",
    "estaremos": "darkkhaki",
    "en marcha": "lightpink",
    "El otoño": "firebrick",
    "se anuncia": "darksalmon",
    "húmedo": "lightseagreen",
    "Chocory": "steelblue",
    "corrido": "rosybrown",
    "deshecho": "mistyrose",
    "Pacheco": "slateblue",
    "pagó": "deepskyblue",
    "sus delitos": "mediumaquamarine",
    "Codicia": "springgreen",
    "envilece": "lavenderblush",
    "el espíritu": "forestgreen",
    "Constancia": "mediumblue",
    "supera": "paleturquoise",
    "imposibles": "palevioletred",
    "Fanatismo": "lightgoldenrodyellow",
    "preocupación": "thistle",
    "infernal": "mediumvioletred",
    "Orgullo": "indianred",
    "aleja": "slategray",
    "amistades": "mediumpurple",
    "Crueldad": "burlywood",
    "muestra": "dimgrey",
    "cobardía": "lightsteelblue",
    "Culto": "darkorchid",
    "sin Piedad": "royalblue",
    "profanación": "hotpink",
    "Trabajo": "mediumorchid",
    "sin método": "sandybrown",
    "ruina": "mediumseagreen",
    "Amor": "lightcyan",
    "sin respeto": "midnightblue",
    "novela": "darkslategray",
    "Patriotismo": "cadetblue",
    "sin desprendimiento": "navajowhite",
    "conversación": "tomato",
    "Salve": "lightgoldenrod",
    "Mayo": "aliceblue",
    "Glorioso": "chartreuse",
    "Al sud": "orangered",
    "está": "aquamarine",
    "la gloria": "seashell",
    "Patricios": "gainsboro",
    "virtuosos": "darkgreen",
    "guerreros": "dimgray",
    "El ocio": "gainsboro",
    "enerva": "lemonchiffon",
    "al soldado": "mintcream",
    "Se desean": "darkblue",
    "glorias": "peachpuff",
    "a la vanguardia": "lavenderblush",
    "Colorado": "snow",
    "Negro": "crimson",
    "Federación o Muerte": "darkslateblue",
    "Naturaleza": "darkseagreen",
    "pródiga": "cornflowerblue",
    "en la sierra": "plum",
    "Humilde": "slategray",
    "soledad": "lightgoldenrodyellow",
    "verde y sonora": "darkturquoise"
}

color_map = {
    "Federación": "#008000",          # green
    "Gloria": "#FFFF00",              # yellow
    "Argentina": "#0000FF",           # blue
    "sistema": "#808080",             # gray
    "de América": "#800080",          # purple
    "Empleados": "#A52A2A",           # brown
    "sin pudor": "#FFA500",           # orange
    "baldón": "#FFC0CB",              # pink
    "Nación": "#FFD700",              # gold
    "sin garantías": "#ADD8E6",       # lightblue
    "teoría": "#90EE90",              # lightgreen
    "Quiroga": "#DC143C",             # crimson
    "Ilustre": "#000080",             # navy
    "Invicto": "#F08080",             # lightcoral
    "Motín": "#808000",               # olive
    "mancha": "#D3D3D3",              # lightgray
    "unitaria": "#006400",            # darkgreen
    "Unitarios": "#00FF00",           # lime
    "mancharon": "#8B0000",           # darkred
    "la Historia": "#00FFFF",         # cyan
    "clamor": "#800000",              # maroon
    "popular": "#FA8072",             # salmon
    "Derechos": "#00008B",            # darkblue
    "sin deberes": "#D2691E",         # chocolate
    "violencia": "#000000",           # black
    "Centro": "#40E0D0",              # turquoise
    "marchando": "#C0C0C0",           # silver
    "glorioso": "#DA70D6",            # orchid
    "De Bahía": "#A0522D",            # sienna
    "corta": "#FF7F50",               # coral
    "distancia": "#F0E68C",           # khaki
    "Del mar": "#FF8C00",             # darkorange
    "sólo": "#8B008B",                # darkmagenta
    "una legua": "#F5F5DC",           # beige
    "Los indios": "#CD853F",          # peru
    "enemigos": "#D2B48C",            # tan
    "se someten": "#DAA520",          # goldenrod
    "Pronto": "#483D8B",              # darkslateblue
    "estaremos": "#BDB76B",           # darkkhaki
    "en marcha": "#FFB6C1",           # lightpink
    "El otoño": "#B22222",            # firebrick
    "se anuncia": "#E9967A",          # darksalmon
    "húmedo": "#20B2AA",              # lightseagreen
    "Chocory": "#4682B4",             # steelblue
    "corrido": "#BC8F8F",             # rosybrown
    "deshecho": "#FFE4E1",            # mistyrose
    "Pacheco": "#6A5ACD",             # slateblue
    "pagó": "#00BFFF",                # deepskyblue
    "sus delitos": "#66CDAA",         # mediumaquamarine
    "Codicia": "#00FF7F",             # springgreen
    "envilece": "#FFF0F5",            # lavenderblush
    "el espíritu": "#228B22",         # forestgreen
    "Constancia": "#0000CD",          # mediumblue
    "supera": "#AFEEEE",              # paleturquoise
    "imposibles": "#DB7093",          # palevioletred
    "Fanatismo": "#FAFAD2",           # lightgoldenrodyellow
    "preocupación": "#D8BFD8",        # thistle
    "infernal": "#C71585",            # mediumvioletred
    "Orgullo": "#CD5C5C",             # indianred
    "aleja": "#708090",               # slategray
    "amistades": "#9370DB",           # mediumpurple
    "Crueldad": "#DEB887",            # burlywood
    "muestra": "#696969",             # dimgrey
    "cobardía": "#B0C4DE",            # lightsteelblue
    "Culto": "#9932CC",               # darkorchid
    "sin Piedad": "#4169E1",          # royalblue
    "profanación": "#FF69B4",         # hotpink
    "Trabajo": "#BA55D3",             # mediumorchid
    "sin método": "#F4A460",          # sandybrown
    "ruina": "#3CB371",               # mediumseagreen
    "Amor": "#E0FFFF",                # lightcyan
    "sin respeto": "#191970",         # midnightblue
    "novela": "#2F4F4F",              # darkslategray
    "Patriotismo": "#5F9EA0",         # cadetblue
    "sin desprendimiento": "#FFDEAD", # navajowhite
    "conversación": "#FF6347",        # tomato
    "Salve": "#FAFAD2",               # lightgoldenrod
    "Mayo": "#F0F8FF",                # aliceblue
    "Glorioso": "#7FFF00",            # chartreuse
    "Al sud": "#FF4500",              # orangered
    "está": "#7FFFD4",                # aquamarine
    "la gloria": "#FFF5EE",           # seashell
    "Patricios": "#DCDCDC",           # gainsboro
    "virtuosos": "#006400",           # darkgreen
    "guerreros": "#696969",           # dimgray
    "El ocio": "#DCDCDC",             # gainsboro
    "enerva": "#FFFACD",              # lemonchiffon
    "al soldado": "#F5FFFA",          # mintcream
    "Se desean": "#00008B",           # darkblue
    "glorias": "#FFDAB9",             # peachpuff
    "a la vanguardia": "#FFF0F5",     # lavenderblush
    "Colorado": "#FFFAFA",            # snow
    "Negro": "#DC143C",               # crimson
    "Federación o Muerte": "#483D8B", # darkslateblue
    "Naturaleza": "#8FBC8F",          # darkseagreen
    "pródiga": "#6495ED",             # cornflowerblue
    "en la sierra": "#DDA0DD",        # plum
    "Humilde": "#708090",             # slategray
    "soledad": "#FAFAD2",             # lightgoldenrodyellow
    "verde y sonora": "#00CED1"       # darkturquoise
}


# Crear figura
fig, ax = plt.subplots(figsize=(12, len(data) * 0.6))

# Obtener el número de filas y columnas
num_rows = len(data)
num_cols = max(len(text.split('-')) for _, text in data)

# Crear una matriz para almacenar los colores
color_matrix = np.full((num_rows, num_cols), fill_value="#FFFFFF")  # Blanco por defecto
text_matrix = [["" for _ in range(num_cols)] for _ in range(num_rows)]  # Matriz para textos

# Rellenar la matriz con colores y textos
for i, (date, text) in enumerate(data):
    words = text.split('-')
    for j, word in enumerate(words):
        color = color_map.get(word, "#FFFFFF")  # Color por el color_map
        color_matrix[i, j] = color
        text_matrix[i][j] = word

# Dibujar la tabla
for i in range(num_rows):
    for j in range(num_cols):
        # Configurar celdas con colores
        ax.text(j, num_rows - i - 1, text_matrix[i][j], ha='center', va='center',
                color='black', fontsize=10,
                bbox=dict(facecolor=color_matrix[i, j], edgecolor='none', boxstyle='round,pad=0.5'))

# Añadir las fechas a la izquierda
for i, (date, _) in enumerate(data):
    ax.text(-0.5, num_rows - i - 1, date, ha='right', va='center', fontsize=10, color="black")

# Configurar límites y eliminar ejes
ax.set_xlim(-1, num_cols)
ax.set_ylim(-1, num_rows)
ax.set_xticks(np.arange(num_cols))
ax.set_yticks(np.arange(num_rows))
ax.spines[:].set_visible(False)

# Ocultar ticks
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

