def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """
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
    count = 0

    for x in string:
        if x == '(':
            count += 1
        elif x == ')':
            count -= 1        
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
    queue = []
    possible = False
    nbreLigne = len(maze)
    nbreCol = len(maze[0])
    pere = [(-1,-1) for _ in range(nbreCol * nbreLigne)]
    queue.append(start)

    def searchMove(point):
        close = []
        if(point[0] > 0 and maze[point[0]-1][point[1]] and pere[nbreCol * (point[0] - 1) + point[1]] == (-1,-1)):
            #bas
            close.append((point[0]-1 , point[1]))
            
        if(point[0] < nbreLigne -1 and maze[point[0]+1][point[1]] and pere[nbreCol * (point[0] + 1) + point[1]] == (-1,-1)):
            #haut
            close.append((point[0]+1 , point[1]))

        if(point[1] > 0 and maze[point[0]][point[1]-1] and pere[nbreCol * point[0] + (point[1] - 1)] == (-1,-1)):
            #droite
            close.append((point[0] , point[1] - 1))

        if(point[1] < nbreCol - 1 and maze[point[0]][point[1]+1] and pere[nbreCol * point[0] + (point[1] + 1)] == (-1,-1)):
            #gauche
            close.append((point[0] , point[1] + 1))    
        return close

    while len(queue) != 0:
        caseCour = queue.pop(0)
        
        if caseCour == end:
            possible = True
            break
        else: 
            for x in searchMove(caseCour):
                queue.append(x)
                pere[x[0] * nbreCol + x[1]] = caseCour                  
    if possible:
        chemin = [end]

        while chemin[-1] != start:
            chemin.append(pere[nbreCol * chemin[-1][0] + chemin[-1][1]]) 
        chemin.reverse() 
        print(chemin)   
        return chemin 
    else:
        print(pere) 
        return False

