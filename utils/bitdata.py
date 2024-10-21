from utils.memorymanager import libererNombre


class BitArray:
    def __init__(self, x=100):
        self.size = x
        self.bits = ['0'] * x



    def to_int(self):

        binary_string = ''.join(self.bits)
        return int(binary_string, 2)

    def set_from_int(self, value):
        binary_representation = bin(value)[2:]  # Représentation binaire sans le préfixe '0b'
        if len(binary_representation) > self.size:
            raise ValueError(f"Le nombre dépasse la taille maximale de {self.size} bits")

        padded_representation = binary_representation.zfill(self.size)
        self.bits = list(padded_representation)

    def initialiser0(self):
        self.set_from_int(0)

    def initialiser1(self):
        self.set_from_int(1)

    def estPair(self):
        return True if self.bits[-1] == '0' else False

    def diviserPar2(self):
        """
        Divise le nombre représenté par le tableau de bits par 2.
        En supprimant le dernier bit.
        """
        self.bits.pop()  # Supprime le dernier bit
        self.bits.insert(0, '0')  # Ajoute un '0' au début pour garder la taille constante

    def reduireDe1(self):
        """
        Réduit le nombre représenté par le tableau de bits de 1.
        """
        value = self.to_int()  # Convertit en entier
        if value > 0:
            self.set_from_int(value - 1)  # Réduit de 1 et met à jour les bits
        else:
            raise ValueError("Le nombre est déjà à zéro, impossible de le réduire plus.")

    def multiplierPar2(self):

        self.size+=1
        if len(self.bits) < self.size:
            self.bits.append('0')  # Ajoute un '0' à la fin

        else:
            raise ValueError("Impossible de multiplier par 2, la taille maximale est atteinte.")


    def __repr__(self):

        return ''.join(self.bits)


# Test de la classe
bit_array = BitArray(10)
bit_array.set_from_int(18)
print(bit_array)
bit_array.diviserPar2()
print(bit_array)
bit_array.reduireDe1()
print(bit_array)
bit_array.multiplierPar2()
print(bit_array)

