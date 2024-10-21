def libererNombre(obj):
    """
    Libère la mémoire associée à un objet en supprimant sa référence.
    Cela permet au garbage collector de récupérer la mémoire.
    """
    del obj