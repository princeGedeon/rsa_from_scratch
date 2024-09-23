def decrypt_with_key(ciphertext, probable_word, position):
    key = probable_word[position:] + probable_word[:position]  # Ajuste la clé pour la position
    decrypted_text = []

    # Parcourt le texte chiffré et la clé pour déchiffrer
    for i in range(len(ciphertext)):
        key_letter = key[i % len(key)]
        ciphertext_letter = ciphertext[i]
        # Calcul de la lettre déchiffrée
        decrypted_letter = chr(((ord(ciphertext_letter) - ord(key_letter)) % 26) + ord('A'))
        decrypted_text.append(decrypted_letter)

    return ''.join(decrypted_text)

def test_all_positions(ciphertext, probable_word):
    for position in range(len(probable_word)):
        result = decrypt_with_key(ciphertext, probable_word, position)
        print(f"Position {position}: {result}")

# Exemple d'utilisation :
ciphertext = "ONKSEOV"  # Ton texte chiffré
probable_word = "ATTAQUE"  # Ton mot probable
position = 1  # Position où commencer
result = decrypt_with_key(ciphertext, probable_word, position)
print(result)



# Exemple d'utilisation :
test_all_positions(ciphertext, probable_word)
