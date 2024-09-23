import string

"""## Exercice 1
text=input("Entrez un texte : ")
print(f"Texte non chiffré : {text}")
"""

## Exercice 2
import string

def format_exo_2(text):
    return "".join([c for c in text.lower() if c in string.ascii_letters])

#text=input("Entrez un texte : ")
# Parcourir chaque carateres vérifier s'il fait partir des lettres ascii
#print(f"Texte non chiffré : {format_exo_2(text)}")



## Exercice 3
def fonction_transforme(chiffre, cle):
    letters = string.ascii_lowercase
    position_cle = letters.find(cle)
    position_chiffre = letters.find(chiffre)
    new_position = (position_cle + position_chiffre ) % 26
    #print(letters)
    #print(position_chiffre, position_cle, new_position)

    return letters[new_position]

# Exercice 4
def normalise_cle(texte,cle):
    if len(texte)<len(cle):
        cle=cle[:len(texte)]
    elif len(texte)>len(cle):
        r=len(texte)%len(cle)
        n=len(texte)//len(cle)
        cle=cle*n + cle[:r]
    return cle
def big_chiffrement(texte,cle):
    texte=format_exo_2(texte)
    cle=format_exo_2(cle)
    cle=normalise_cle(texte,cle)
    #print(cle,texte)
    return "".join([fonction_transforme(t,c) for t,c in zip(texte,cle)])



# Exercice 5
## Déchiffrement
def dechiffre(tc,clec):
    letters = string.ascii_lowercase
    position_clec = letters.find(clec)
    position_tc = letters.find(tc)
    old_position = (position_tc - position_clec ) % 26
    # print(letters)
    # print(position_chiffre, position_cle, new_position)

    return letters[old_position]

def decode_vigenere_all(texte_c,cle):
    texte_c = format_exo_2(texte_c)
    cle = format_exo_2(cle)
    cle=normalise_cle(texte_c,cle)
    if len(texte_c) != len(cle):
        raise ("Doit être de même taille")
    else:
        return "".join([dechiffre(t, c) for t, c in zip(texte_c, cle)])



print(big_chiffrement("Bonjour a tous","python"))

print(decode_vigenere_all("qmgqchgymvif","python"))
