# =====================================================
# Election MVP - Attribution des points
# =====================================================


# Fonction Test
# Vérifie si une chaîne contient seulement des lettres et des espaces
def Test(ch):

    if ch.strip() == "":
        return False

    for c in ch:

        if not (c.isalpha() or c == " "):
            return False

    return True



# Fonction Existe
# Cherche une chaîne dans un tableau
# Retourne son indice ou -1
def Existe(ch, T, n):

    for i in range(n):

        if T[i].lower() == ch.lower():
            return i

    return -1



# =====================================================
# Procédure Saisir_Dimensions
# =====================================================

def Saisir_Dimensions():

    while True:

        n = int(input("Donner le nombre de joueurs n (5 à 30) : "))

        if 5 <= n <= 30:
            break


    while True:

        m = int(input("Donner le nombre de journalistes m (2 à 50) : "))

        if 2 <= m <= 50:
            break


    return n, m



# =====================================================
# Procédure Remplir_Joueurs
# =====================================================

def Remplir_Joueurs(TJ, n):

    for i in range(n):

        while True:

            nom = input(f"Saisir le nom du joueur N°{i+1} : ")


            if Test(nom) and Existe(nom, TJ, i) == -1:

                TJ[i] = nom
                break



# =====================================================
# Procédure Voter
# =====================================================

def Voter(TJ, TS, n, m):


    # Initialisation des scores

    for i in range(n):

        TS[i] = 0



    # Votes des journalistes

    for j in range(1, m + 1):

        print("\n--- Vote du journaliste", j, "---")


        # Choix 1 : 5 points

        while True:

            ch1 = input("Choix 1 (5 pts) : ")

            pos1 = Existe(ch1, TJ, n)


            if pos1 != -1:
                break


        TS[pos1] += 5



        # Choix 2 : 3 points

        while True:

            ch2 = input("Choix 2 (3 pts) : ")

            pos2 = Existe(ch2, TJ, n)


            if pos2 != -1 and ch2.lower() != ch1.lower():

                break


        TS[pos2] += 3



        # Choix 3 : 1 point

        while True:

            ch3 = input("Choix 3 (1 pt) : ")

            pos3 = Existe(ch3, TJ, n)


            if (pos3 != -1 and
                ch3.lower() != ch1.lower() and
                ch3.lower() != ch2.lower()):

                break


        TS[pos3] += 1



# =====================================================
# Procédure Afficher_MVP
# =====================================================

def Afficher_MVP(TJ, TS, n):


    # Recherche du score maximal

    max_score = TS[0]


    for i in range(1, n):

        if TS[i] > max_score:

            max_score = TS[i]



    # Recherche des joueurs MVP

    MVP = []


    for i in range(n):

        if TS[i] == max_score:

            MVP.append(TJ[i])



    # Affichage final

    print("\nLe score MVP est :", max_score)

    print("Le(s) joueur(s) MVP :", ", ".join(MVP))



# =====================================================
# Programme Principal
# =====================================================

def Election_MVP():


    # 1. Saisie des dimensions

    n, m = Saisir_Dimensions()



    # 2. Remplissage du tableau des joueurs

    TJ = [""] * n

    Remplir_Joueurs(TJ, n)



    # 3. Votes et calcul des scores

    TS = [0] * n

    Voter(TJ, TS, n, m)



    # 4. Affichage du MVP

    Afficher_MVP(TJ, TS, n)

# Lancement

Election_MVP()