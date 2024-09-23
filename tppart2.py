from collections import defaultdict


def find_repeating_sequences(cipher_text):
    sequence_counts = defaultdict(int)
    #  cherche toutes les séquences possibles
    for i in range(len(cipher_text)):
        for j in range(i + 3, len(cipher_text) + 1):
            sequence = cipher_text[i:j]
            #print(sequence)
            sequence_counts[sequence] += 1
    #Filtrage
    sequence_counts={key: value for key, value in sequence_counts.items() if value > 1}

    # Affiche ceux font il a plus de 2
    for sequence, count in sequence_counts.items():
        if count > 1:
            print(f"{sequence} trouvé {count} fois")

    return sequence_counts


def find_occurrences(sequence, text):
    occurrences = []
    start = 0
    # Boucle pour trouver toutes les occurrences de la séquence dans le texte
    while True:
        # Utilise la méthode find pour trouver l'index de la séquence dans le texte
        index = text.find(sequence, start)
        # Si la séquence n'est plus trouvée, on arrête la recherche
        if index == -1:
            break
        # Ajouter l'index à la liste des occurrences
        occurrences.append(index)
        # Mettre à jour la position de départ pour la prochaine recherche
        start = index + 1  # Incrément pour ne pas retomber sur la même occurrence
    return occurrences


if __name__ == "__main__":
    cipher_text = input("cipher: ")
    seqs=find_repeating_sequences(cipher_text)
    print(seqs)
    distance_dict = {}
    for seq in seqs:
        # print(seq)
        # print("--->")
        seq_ids = find_occurrences(seq, cipher_text)
        # Calcul difference
        diff = []
        #print(seq_ids)
        for i in range(len(seq_ids)-1):
            diff.append(seq_ids[i + 1] - seq_ids[i])
        distance_dict[seq] = diff
    print(distance_dict)