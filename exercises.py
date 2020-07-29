def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """
    # Trier les deux chaines de caractères puis comparer les deux listes triées
    return "".join(sorted(s1)) == "".join(sorted(s2))

def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """
    #initialiser un compteur
    count = 0

    #on parcourt la chaine de caractères
    for x in string:
        if count >= 0:
            if x == '(':
            #si parenthèse ouvrante ajouter +1 au compteur 
                count += 1
            elif x == ')':
            #si parenthèse fermante ajouter -1 au compteur    
                count -= 1
    #return true si count = 0 et false si count != 0               
    return not count        

def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """
    #liste des coups à jouer
    queue = []

    possible = False
    nbreLigne = len(maze)
    nbreCol = len(maze[0])

    #liste des pères () initialiser à la taille du maze
    pere = [(-1,-1) for _ in range(nbreCol * nbreLigne)]
    
    #on commence au start
    queue.append(start)

    #fonction qui renvoie la liste des voisins à explorer, on regarde si le point à coté n'est pas un mur et n'a pas de père
    def searchMove(point):  
        close = []
        if(point[0] > 0 and maze[point[0]-1][point[1]] and pere[nbreCol * (point[0] - 1) + point[1]] == (-1,-1)):
            #ajouter le voisin du bas
            close.append((point[0]-1 , point[1]))   
        if(point[0] < nbreLigne -1 and maze[point[0]+1][point[1]] and pere[nbreCol * (point[0] + 1) + point[1]] == (-1,-1)):
            #ajouter le voisin du haut
            close.append((point[0]+1 , point[1]))
        if(point[1] > 0 and maze[point[0]][point[1]-1] and pere[nbreCol * point[0] + (point[1] - 1)] == (-1,-1)):
            #ajouter le voisin de gauche
            close.append((point[0] , point[1] - 1))
        if(point[1] < nbreCol - 1 and maze[point[0]][point[1]+1] and pere[nbreCol * point[0] + (point[1] + 1)] == (-1,-1)):
            #ajouter le voisin de droite 
            close.append((point[0] , point[1] + 1))    
        return close
    #parcours en largeur
    while len(queue) != 0:
        caseCour = queue.pop(0) 
        if caseCour == end:
        #on est sur l'arrivée    
            possible = True
            break
        else: 
        #on continue d'explorer    
            for x in searchMove(caseCour):
                queue.append(x)
                pere[x[0] * nbreCol + x[1]] = caseCour
    #verification si le chemin peut arriver jusqu'à la fin                               
    if possible:
        #construction du chemin à parcourir
        chemin = [end]
        #tant que le dernier élement n'est le départ on rajoute les pères de chaque points
        while chemin[-1] != start:
            chemin.append(pere[nbreCol * chemin[-1][0] + chemin[-1][1]])
        #on inverse le chemin pour l'avoir dans le bon ordre     
        chemin.reverse()  
        return chemin 
    else:
    #aucun chemin arrive jusqu'à la fin du maze    
        return False

