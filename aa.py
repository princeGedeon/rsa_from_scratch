# Alphabet français
from collections import Counter

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt_vigenere(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    for i, letter in enumerate(ciphertext):
        if letter in alphabet:
            # Décalage avec la clé (ajustement spécial : -1 avant %26 pour décrypter)
            shift = (alphabet.index(key[i % key_length]) + 1) % len(alphabet)
            original_pos = (alphabet.index(letter) - shift) % len(alphabet)
            decrypted_text.append(alphabet[original_pos])
        else:
            decrypted_text.append(letter)  # Garder les caractères non alphabétiques
    return ''.join(decrypted_text)

def ask_user_for_mapping(ciphertext_letter):
    # Demander à l'utilisateur quelle est la lettre en clair correspondant à une lettre chiffrée
    clear_letter = input(f"Quelle est la lettre en clair correspondant à la lettre chiffrée '{ciphertext_letter}' ? ")
    return clear_letter

def find_key_from_user_input(subtexts):
    # Identifier la clé en demandant à l'utilisateur de fournir des correspondances entre le texte chiffré et le texte clair
    key = []
    for i, subtext in enumerate(subtexts):
        # Prendre la lettre la plus fréquente dans chaque sous-texte
        most_frequent_letter = Counter(subtext).most_common(1)[0][0]
        print(f"\nSous-texte {i+1} (lettres chiffrées) : {subtext[:10]}...")  # Montrer un aperçu du sous-texte
        clear_letter = ask_user_for_mapping(most_frequent_letter)
        # Calculer le décalage en prenant en compte l'ajustement de +1
        shift = (alphabet.index(most_frequent_letter) - alphabet.index(clear_letter) - 1) % len(alphabet)
        key.append(alphabet[shift])
    return ''.join(key)
"""salahsalah
   gpiowpoaxv"""

def break_vigenere(ciphertext, key_length):
    # Diviser le texte chiffré en sous-textes selon la longueur de la clé
    subtexts = ['' for _ in range(key_length)]
    for i, letter in enumerate(ciphertext):
        if letter in alphabet:
            subtexts[i % key_length] += letter

    # Trouver la clé en demandant à l'utilisateur
    key = find_key_from_user_input(subtexts)
    print(f"\nClé trouvée : {key}")

    # Déchiffrer le texte avec la clé trouvée
    return decrypt_vigenere(ciphertext, key)

# Exemple d'utilisation
ciphertext = input("Entrez le texte chiffré : ").lower()
key_length = int(input("Entrez la longueur de la clé : "))

decrypted_text = break_vigenere(ciphertext, key_length)
print(f"\nTexte déchiffré : {decrypted_text}")
