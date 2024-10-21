from utils.bitdata import BitArray


def comparer(bitarray1, bitarray2):

    if bitarray1.size != bitarray2.size:
        return False  # Les tailles sont différentes, donc les BitArray sont différents

    return bitarray1.bits == bitarray2.bits  # Compare les tableaux de bits

bitarray1 = BitArray(10)
bitarray1.set_from_int(25)
bitarray2 = BitArray(10)
bitarray2.set_from_int(25)
resultat = comparer(bitarray1, bitarray2)
if resultat:
    print("Les deux BitArray sont égaux.")
else:
    print("Les deux BitArray sont différents.")
