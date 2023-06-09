from tkinter import *
import customtkinter as tk
import random

alphabet = "abcdefghijklmnopqrstuvwxyzäöü"

# TDES oder Caesar switch-boolean
caesar_mode = True

### Verschluesslungsfunktionen

## en kurze funktion für de caesar verschlüsselig
def caesarVerschlusselung(string, verschiebung):
    # de verschiebig: tued die erste (a - d, b - c usw) mache und die zweite (:verschiebig) lösst das problem
    # für die erstiDreifachEntschlüsselungsmodus (a, b, c) (mit verschiebig 4 zb)
    shifted_alphabet = alphabet[verschiebung:] + alphabet[:verschiebung]
    # mir mached mit translation table en comparison table fürs normale alphabet zum geheimschrift alphabet
    # upper() wird verwendet um die gröss gschriebeni buechstabe au zu verschlüssle
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    normal_list = []
    modified_list = []

    for char in string:
        # id liste appende
        normal_list.append(char)
        # translate
        modified_letter = [char.translate(translation_table) for i in normal_list]
        # das [0] burcht es suscht isch es komisch
        modified_list.append(modified_letter[0])

    # liste id string konvertiere
    modified_string = "".join(modified_list)

    return modified_string


## Caesar Verschluesselung-entschluessung
def caesarVerschlusselung_rev(string, verschiebung):
    shifted_alphabet = alphabet[verschiebung:] + alphabet[:verschiebung]
    # mir mached alles glich eif reverse
    translation_table = str.maketrans(
        shifted_alphabet + shifted_alphabet.upper(), alphabet + alphabet.upper()
    )
    normal_list = []
    modified_list = []

    for char in string:
        # id liste appende
        normal_list.append(char)
        # translate
        modified_letter = [char.translate(translation_table) for i in normal_list]
        # das [0] burcht es suscht isch es komisch
        modified_list.append(modified_letter[0])

    # liste id string konvertiere
    modified_string = "".join(modified_list)

    return modified_string

## TDES Verschluesselung
def TripleDataEncryptionStandards(String, Verschiebung):

    message = entry.get("1.0", "end-1c")
    verschiebung = entry2.get("1.0", "end-1c")
    
    # Erjon: de input vo de zahl wird in 3 teil ufgteilt
    part_length = len(verschiebung) // 3
    
    key1 = int(verschiebung[:part_length])
    key2 = int(verschiebung[part_length:2*part_length])
    key3 = int(verschiebung[2*part_length:])

    # Erjon: will wend zahl grösser isch als ahzal symbol im alphabet 
    #        tuets die zahl um 29(ahzahl symbol im alphabet) verchlinere 
    #        dammit eusi funktion wieder ghat


    if key1 >= 29:
        while key1 >= 29:
            key1-=29       

    if key2 > 29:
        while key2 >= 29:
            key2-=29 

    if key3 > 29:
        while key3 >= 29:
            key3-=29

    test_string1 = caesarVerschlusselung(message, key1)
    test_string2 = caesarVerschlusselung(test_string1, key2)
    test_string3 = caesarVerschlusselung(test_string2, key3)

    return test_string3

## TDES Verschluesselung-entschluesselung
def TripleDataEncryptionStandards_rev(String, Verschiebung):

    message = entry.get("1.0", "end-1c")
    verschiebung = entry2.get("1.0", "end-1c")
    
    # Erjon: de input vo de zahl wird in 3 teil ufgteilt
    part_length = len(verschiebung) // 3
    
    key1 = int(verschiebung[:part_length])
    key2 = int(verschiebung[part_length:2*part_length])
    key3 = int(verschiebung[2*part_length:])

    # Erjon: will wend zahl grösser isch als ahzal symbol im alphabet 
    #        tuets die zahl um 29(ahzahl symbol im alphabet) verchlinere 
    #        dammit eusi funktion wieder ghat


    if key1 >= 29:
        while key1 >= 29:
            key1-=29       

    if key2 > 29:
        while key2 >= 29:
            key2-=29 

    if key3 > 29:
        while key3 >= 29:
            key3-=29

    test_string1 = caesarVerschlusselung_rev(message, key1)
    test_string2 = caesarVerschlusselung_rev(test_string1, key2)
    test_string3 = caesarVerschlusselung_rev(test_string2, key3)

    return test_string3

### knopf funktione

## encrypt funktion
 
# 1.0 isch in tkinter erste character und end-1c isch de character bevor newline /n
def encrypt_message():
    message = entry.get("1.0", "end-1c")
    if caesar_mode == True:
        verschiebung = int(entry2.get("1.0", "end-1c"))
        # Erjon: Das sorgt dafür das de Key nie grösser als 29 isch will denn verschiebig nöd ghat. 
        if verschiebung >= 29:
            while verschiebung >= 29:
                verschiebung-=29
        encrypted_message = caesarVerschlusselung(message, verschiebung)
    else:
        verschiebung = entry2.get("1.0", "end-1c") 
        encrypted_message = TripleDataEncryptionStandards(message, verschiebung)
    encrypted_result.delete("1.0", "end")
    encrypted_result.insert("1.0", encrypted_message)



## decrypt funktion

def decrypt_message():
    message = entry.get("1.0", "end-1c")
    if caesar_mode == True:
        verschiebung = int(entry2.get("1.0", "end-1c"))
        # Erjon: Das sorgt dafür das de Key nie grösser als 29 isch will denn verschiebig nöd ghat. 
        if verschiebung >= 29:
            while verschiebung >= 29:
                verschiebung-=29
        decrypted_message = caesarVerschlusselung_rev(message, verschiebung)
    else:
        verschiebung = entry2.get("1.0", "end-1c")
        decrypted_message = TripleDataEncryptionStandards_rev(message, verschiebung)
    decrypted_result.delete("1.0", "end")
    decrypted_result.insert("1.0", decrypted_message)

## switch menu funktion

# *args will mir tuend unbestimmti ahzahl vo arguments verschicked
def switch_modes(*args):
    global caesar_mode
    selected_option = switch_variable.get()
    if selected_option == "3DES":
        caesar_mode=False
    else:
        caesar_mode=True


### GUI

# Erjon: Bestimmt dfrabene fürs GUI
tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

# Erjon: Machts Window fürs tkinter
window = tk.CTk()
window.title("Verschlüsselung von Berke und Erjon")
window.geometry("900x700")

# Erjon: Erstellt Konfigurations Labels
label = tk.CTkLabel(window, text="Message")
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label2 = tk.CTkLabel(window, text="Verschiebung")
label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

encrypt_label = tk.CTkLabel(window, text="Encrypted Message:")
encrypt_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

decrypt_label = tk.CTkLabel(window, text="Decrypted Message:")
decrypt_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")

# Erjon: Erstehlt Konfigurations eingabe Felder
entry = tk.CTkTextbox(window, width=400)
entry.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.CTkTextbox(window, width=400, height=10)
entry2.grid(row=1, column=1, padx=10, pady=10)


# Erjon: Erstellt Knöpf
encrypt_button = tk.CTkButton(window, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

decrypt_button = tk.CTkButton(window, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")


# Feld für das Ergebnis bi Encryption
encrypted_result = tk.CTkTextbox(window, width=400, height=100)
encrypted_result.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Feld für das Decryption bi Encryption
decrypted_result = tk.CTkTextbox(window, width=400, height=100)
decrypted_result.grid(row=5, column=1, padx=10, pady=10, sticky="w")

# Erjon: Key generator 
def key_gen():
    random_number = random.randint(100000000, 999999999)
    entry2.delete("1.0", "end")
    entry2.insert("1.0", random_number)
    
# Function to copy encrypted text to the message field
def copy_encrypted_to_message():
    encrypted_text = encrypted_result.get("1.0", "end")
    entry.delete("1.0", "end")
    entry.insert("1.0", encrypted_text)

def copy_decrypted_to_message():
    decrypted_text = decrypted_result.get("1.0", "end")
    entry.delete("1.0", "end")
    entry.insert("1.0", decrypted_text)

# Erjon: tuet de Schlüssel generiere
gen_button = tk.CTkButton(window, text="Generate Key", command=key_gen)
gen_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="we")

# Erställt en Knopf zum de text ufs feld obe zum witer bruche. 
copy_button = tk.CTkButton(window, text="Copy", command=copy_encrypted_to_message)
copy_button.grid(row=3, column=2, padx=10, pady=10, sticky="w")

copy_button = tk.CTkButton(window, text="Copy", command=copy_decrypted_to_message)
copy_button.grid(row=5, column=2, padx=10, pady=10, sticky="w")

switch_variable = tk.StringVar(value="off")
# Mode switch Knopf
switch_menu = tk.CTkSwitch(window, text="Dreifach-Entschlüsselungsmodus", command=switch_modes, onvalue="3DES", offvalue="off", variable=switch_variable)
switch_menu.grid(row=0, column=2, padx=10, pady=10, sticky="w")


window.mainloop()