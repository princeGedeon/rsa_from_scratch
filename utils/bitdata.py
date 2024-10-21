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
    def __repr__(self):

        return ''.join(self.bits)


# Test de la classe
bit_array = BitArray(10)
bit_array.set_from_int(18)
print(bit_array)
print(bit_array.estPair())