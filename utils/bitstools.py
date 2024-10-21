from utils.bitdata import BitArray


def comparer(bitarray1, bitarray2):

    if bitarray1.size != bitarray2.size:
        return False  # Les tailles sont différentes, donc les BitArray sont différents

    return bitarray1.bits == bitarray2.bits  # Compare les tableaux de bits

def ajouter(bitarray1, bitarray2):
    """
    Additionne deux BitArray représentant des nombres binaires.
    Retourne un nouveau BitArray représentant le résultat.
    """
    # Vérifie si les deux BitArray ont la même taille
    if bitarray1.size != bitarray2.size:
        raise ValueError("Les BitArray doivent avoir la même taille pour être additionnés")
    result = BitArray(bitarray1.size)  # Résultat de la même taille
    carry = 0  # la retenue
    # Parcours des bits de droite à gauche (de l'indice le plus élevé à 0)
    for i in range(bitarray1.size - 1, -1, -1):
        bit1 = int(bitarray1.bits[i])
        bit2 = int(bitarray2.bits[i])
        total = bit1 + bit2 + carry
        result.bits[i] = str(total % 2)  # Le bit résultant est le modulo 2 de la somme
        carry = total // 2  # La retenue est le quotient de la somme par 2


    if carry:
        result.bits.insert(0, '1')  # Ajoute un '1' au début
        result.bits.pop()  # Supprime le dernier bit pour garder la taille constante

    return result

# Exemple d'utilisation
bitarray1 = BitArray(6)
bitarray2 = BitArray(6)

bitarray1.set_from_int(int('11001', 2))  # 11001 en binaire
bitarray2.set_from_int(int('01100', 2))  # 01100 en binaire

print("Nombre 1:", bitarray1)
print("Nombre 2:", bitarray2)

resultat = ajouter(bitarray1, bitarray2)

print("Résultat de l'addition:", resultat)

