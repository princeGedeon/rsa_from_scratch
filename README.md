# crypto_security
# RSA From ScRATCH

**RSA** est un algorithme de chiffrement asymétrique basé
sur deux clés publics et privée

Une fonction modulo qui prends en paramètre a , n et calcule a[n]

La création des clés dans RSA se fait de la manière suivante :
-  Choisir deux nombres p et q distincts, aléatoirement et tous les deux premiers.
- Calculer n = p x q.
-  Calculer phi(n) = (p-1) x (q-1).
-  Choisir arbitrairement un nombre e, compris entre 1 et phi(n), et premier avec phi(n).
-  Calculer d, l’inverse de e modulo phi(n).


### Clés
- **Clé public :** (e, n)
- **Clé privé :**  (d , n)



By **Prince Gédéon GUEDJE**