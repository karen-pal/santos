# Let's break down the plaintext dates and the corresponding cipher texts
plain_text = [
    "11 de marzo", "14 de marzo", "5 de junio", "6 de junio", "1 de abril", "16 de abril", 
    "8 de mayo", "19 de mayo", "7 de junio", "17 de abril", "24 de abril", "26 de abril", 
    "27 de abril", "29 de abril", "5 de abril", "29 de junio", "24 de julio", "30 de julio", 
    "2 de julio", "14 de abril", "7 de mayo", "12 de mayo", "12 de julio", "16 de julio", 
    "19 de julio", "17 de julio", "21 de julio", "25 de mayo", "16 de marzo", "15 de abril", 
    "23 de abril", "5 de mayo", "10 de mayo", "8 de abril", "22 de diciembre"
]

cipher_text = [
    "Federación-Gloria-Argentina", "Federación-sistema-de América", "Empleados-sin pudor-baldón", 
    "Nación-sin garantías-teoría", "Quiroga-Ilustre-Invicto", "Motín-mancha-unitaria", 
    "Unitarios-mancharon-la Historia", "Federación-clamor-popular", "Derechos-sin deberes-violencia", 
    "Centro-marchando-glorioso", "De Bahía- corta-distancia", "Del mar-sólo-una legua", 
    "Los indios-enemigos-se someten", "Pronto-estaremos-en marcha", "El otoño-se anuncia-húmedo", 
    "Chocory-corrido-deshecho", "Pacheco-marchando-glorioso", "Chocori-pagó-sus delitos", 
    "Codicia-envilece-el espíritu", "Constancia-supera-imposibles", "Fanatismo -preocupación-infernal", 
    "Orgullo-aleja-amistades", "Crueldad-muestra-cobardía", "Culto- sin Piedad-profanación", 
    "Trabajo-sin método-ruina", "Amor- sin respeto-novela", "Patriotismo-sin desprendimiento-conversación", 
    "Salve-Mayo -Glorioso", "Al sud-está-la gloria", "Patricios-virtuosos-guerreros", 
    "El ocio-enerva-al soldado", "Se desean-glorias-a la vanguardia", "Colorado-Negro-Federación o Muerte", 
    "Naturaleza-pródiga-en la sierra", "Humilde-soledad-verde y sonora"
]

# Let's create a dictionary to map the plain text to cipher text
cipher_pairs = dict(zip(plain_text, cipher_text))

# Check for common words in cipher_text that may correspond to specific parts of the dates
from collections import Counter

# Tokenize all the cipher_text to analyze word frequency
all_cipher_words = [word for text in cipher_text for word in text.split("-")]
word_frequencies = Counter(all_cipher_words)

word_frequencies.most_common()  # Find the most common words
print("frequency count:>>>>>>>")
print(word_frequencies.most_common())  # Find the most common words


# Let's try to group the pairs where "Federación", "marchando", and "glorioso" appear to analyze them

# Filter cipher pairs with key phrases like "Federación", "marchando", and "glorioso"
key_phrases = ["Federación", "marchando", "glorioso"]

filtered_pairs = {pt: ct for pt, ct in cipher_pairs.items() if any(phrase in ct for phrase in key_phrases)}
print("\n")
print(filtered_pairs)  # Output filtered pairs

# Let's examine the corresponding days of the month for pairs containing "Federación"
# and see if "Federación" is linked to specific days.

# Extract the days from the plain text for pairs containing "Federación"
federacion_dates = [pt.split()[0] for pt, ct in filtered_pairs.items() if "Federación" in ct]

print("federacion_dates")  # Output the days for "Federación" occurrences
print(federacion_dates)  # Output the days for "Federación" occurrences


# Let's extract the words that accompany "Federación" in the cipher text
federacion_context = [ct.split("-") for pt, ct in cipher_pairs.items() if "Federación" in ct]

print(federacion_context)  # Output the context where "Federación" appears


