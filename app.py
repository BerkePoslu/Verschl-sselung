import tkinter as tk

alphabet = "abcdefghijklmnopqrstuvwxyzäöü"

mode = True
modusStatus = "Caesar"

# Erjon: das wechselt de Wert für mode False isch 3DES funtion True isch Caesar funktion
def toggle_mode():
    if mode == False:
        mode = True
        modusStatus = "Caesar"
    else: 
        mode == False
        modusStatus = "3DES"


# en kurze funktion für de caesar verschlüsselig
def caesarVerschlusselung(string, verschiebung):
    # de verschiebig: tued die erste (a - d, b - c usw) mache und die zweite (:verschiebig) lösst das problem
    # für die ersti 3 (a, b, c) (mit verschiebig 4 zb)
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
        print(normal_list)
        # translate
        modified_letter = [char.translate(translation_table) for i in normal_list]
        # das [0] burcht es suscht isch es komisch
        modified_list.append(modified_letter[0])

        print(modified_list)

    # liste id string konvertiere
    modified_string = "".join(modified_list)

    return modified_string



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
        print(normal_list)
        # translate
        modified_letter = [char.translate(translation_table) for i in normal_list]
        # das [0] burcht es suscht isch es komisch
        modified_list.append(modified_letter[0])

        print(modified_list)

    # liste id string konvertiere
    modified_string = "".join(modified_list)

    return modified_string

def TripleDataEncryptionStandards(String, Verschiebung):

    message = entry.get("1.0", "end-1c")
    verschiebung = entry2.get("1.0", "end-1c")
    
    # Erjon: de input vo de zahl wird in 3 teil ufgteilt
    part1, part2, part3 = verschiebung.split(' ')

    key1 = int(part1)
    key2 = int(part2)
    key3 = int(part3)

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

def TripleDataEncryptionStandards_rev(String, Verschiebung):

    message = entry.get("1.0", "end-1c")
    verschiebung = entry2.get("1.0", "end-1c")
    
    # Erjon: de input vo de zahl wird in 3 teil ufgteilt
    part1, part2, part3 = verschiebung.split(' ')

    key1 = int(part1)
    key2 = int(part2)
    key3 = int(part3)

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

# encrypte knopf funktion
# 1.0 isch in tkinter erste character und end-1c isch de character bevor newline /n
def encrypt_message():
    message = entry.get("1.0", "end-1c")
    if mode == True:
        verschiebung = int(entry2.get("1.0", "end-1c"))
        # Erjon: Das sorgt dafür das de Key nie grösser als 29 isch will denn verschiebig nöd ghat. 
        if verschiebung >= 29:
            while verschiebung >= 29:
                verschiebung-=29
        encrypted_message = caesarVerschlusselung(message, verschiebung)
    else:
        verschiebung = entry2.get("1.0", "end-1c") 
        encrypted_message = TripleDataEncryptionStandards(message, verschiebung)
    encrypted_result.configure(text=encrypted_message)



# nur decrypte wenn de encrypted im message feld staht
def decrypt_message():
    message = entry.get("1.0", "end-1c")
    if mode == True:
        verschiebung = int(entry2.get("1.0", "end-1c"))
        # Erjon: Das sorgt dafür das de Key nie grösser als 29 isch will denn verschiebig nöd ghat. 
        if verschiebung >= 29:
            while verschiebung >= 29:
                verschiebung-=29
        decrypted_message = caesarVerschlusselung_rev(message, verschiebung)
    else:
        verschiebung = entry2.get("1.0", "end-1c")
        decrypted_message = TripleDataEncryptionStandards_rev(message, verschiebung)
    decrypted_result.configure(text=decrypted_message)

# Erjon: das wechselt de Wert für mode False isch 3DES funtion True isch Caesar funktion
def toggle_mode():
    if mode == False:
        mode = True
        modusStatus = "Caesar"
    else: 
        mode == False
        modusStatus = "3DES"

# Erjon: Bestimmt dfrabene fürs GUI
primary_color = "#293E4D"
secondary_color = "#F0F0F0"
button_color = "#447DBA"
button_text_color = "#FFFFFF"

# Erjon: Machts Window fürs tkInter
window = tk.Tk()
window.title("Tkinter GUI")
window.geometry("700x700")
window.configure(bg=primary_color)

# Erjon: Erstellt Konfigurations Labels
label = tk.Label(window, text="Message", bg=primary_color, fg=secondary_color, font=("Arial", 12))
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label2 = tk.Label(window, text="Verschiebung", bg=primary_color, fg=secondary_color, font=("Arial", 12))
label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

encrypt_label = tk.Label(window, text="Encrypted Message:", bg=primary_color, fg=secondary_color, font=("Arial", 12))
encrypt_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

decrypt_label = tk.Label(window, text="Decrypted Message:", bg=primary_color, fg=secondary_color, font=("Arial", 12))
decrypt_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")

# Erjon: Erstehlt Konfigurations eingabe Felder
entry = tk.Text(window, width=30, height=5, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Text(window, width=30, height=3, font=("Arial", 12))
entry2.grid(row=1, column=1, padx=10, pady=10)


# Erjon: Erstellt Knöpf

modus_button = tk.Button(window, text = modusStatus, command=toggle_mode, bg=button_color, fg=button_text_color, font=("Arial", 12))
modus_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="we")

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message, bg=button_color, fg=button_text_color, font=("Arial", 12))
encrypt_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message, bg=button_color, fg=button_text_color, font=("Arial", 12))
decrypt_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")


# Feld für das Ergebnis bi Encryption
encrypted_result = tk.Label(window, width=40, height=5, bg=primary_color, fg=secondary_color, font=("Arial", 12))
encrypted_result.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Feld für das Decryption bi Encryption
decrypted_result = tk.Label(window, width=40, height=5, bg=primary_color, fg=secondary_color, font=("Arial", 12))
decrypted_result.grid(row=5, column=1, padx=10, pady=10, sticky="w")

# Erjon: das wechselt de Wert für mode False isch 3DES funtion True isch Caesar funktion
def toggle_mode():
    if mode == False:
        mode = True
        modusStatus = "Caesar"
    else: 
        mode == False
        modusStatus = "3DES"

# Function to copy encrypted text to the message field
def copy_encrypted_to_message():
    encrypted_text = encrypted_result["text"]
    entry.delete("1.0", "end")
    entry.insert("1.0", encrypted_text)

def copy_decrypted_to_message():
    decrypted_text = decrypted_result["text"]
    entry.delete("1.0", "end")
    entry.insert("1.0", decrypted_text)
# Erställt en Knopf zum de text ufs feld obe zum witer bruche. 
copy_button = tk.Button(window, text="Copy", command=copy_encrypted_to_message, bg=button_color, fg=button_text_color, font=("Arial", 12))
copy_button.grid(row=3, column=2, padx=10, pady=10, sticky="w")

copy_button = tk.Button(window, text="Copy", command=copy_decrypted_to_message, bg=button_color, fg=button_text_color, font=("Arial", 12))
copy_button.grid(row=5, column=2, padx=10, pady=10, sticky="w")


window.mainloop()