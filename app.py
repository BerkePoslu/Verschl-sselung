import tkinter as tk


window = tk.Tk()
# grössi definiere
window.geometry("300x500")
label = tk.Label(window, text="Message", )
entry = tk.Entry(window)

label2 = tk.Label(window, text="Verschiebung")
entry2 = tk.Entry(window)

alphabet = "abcdefghijklmnopqrstuvwxyzäöü"


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

# encrypte knopf funktion
def encrypt_message():
    message = entry.get()
    verschiebung = int(entry2.get())
    encrypted_message = caesarVerschlusselung(message, verschiebung)
    encrypted_result.configure(text=encrypted_message)

# nur decrypte wenn de encrypted im message feld staht
def decrypt_message():
    message = entry.get()
    verschiebung = int(entry2.get())
    decrypted_message = caesarVerschlusselung_rev(message, verschiebung)
    decrypted_result.configure(text=decrypted_message)

# reverse tued de text wo scho encrypted worde isch decrypte
# wird meh zum teste benutzt
def reverse_message():
    message = encrypted_result.cget("text")
    verschiebung = int(entry2.get())
    decrypted_message = caesarVerschlusselung_rev(message, verschiebung)
    decrypted_result.configure(text=decrypted_message)

encrypt_label = tk.Label(window, text="Encrypted Message:")
encrypted_result = tk.Label(window, text="")

decrypt_label = tk.Label(window, text="Decrypted Message:")
decrypted_result = tk.Label(window, text="")

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message)
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message)

reverse_button = tk.Button(window, text="Reverse", command=reverse_message)

label.pack()
entry.pack()
label2.pack()
entry2.pack()
encrypt_button.pack()
decrypt_button.pack()
reverse_button.pack()
encrypt_label.pack()
encrypted_result.pack()
decrypt_label.pack()
decrypted_result.pack()

window.mainloop()
# Erjon: de input vo de zahl wird in 3 teil ufgteilt
part1, part2, part3 = entry2

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

# Erjon: da tuen ich dafür sorge das message mehrmals 
#        durch die funktion ghat mit dene 3 separate teil vo de verschlüsselig

test_string1 = caesarVerschlusselung(entry, key1)
test_string2 = caesarVerschlusselung(test_string1, key2)
test_string3 = caesarVerschlusselung(test_string2, key3)

print(test_string3)