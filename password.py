# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    if password == "":
        raise Exception("Chaine vide")
    else:
        pwd = list(password)  #On stock toute les lettres du mot de passe dans une liste de caractère
        found = False
        i=len(pwd)-1

        while not found:
            if pwd[i] < 'z':
                pwd[i] = chr(ord(pwd[i])+1)  #On augmente la valeur du caractère ASCII (uniquement si ce n'est pas 'z')
                found = True             
            else:
                pwd[i] = 'a'
                i = i-1 
        
        return ''.join(pwd) #Concatenation de la liste de caractère en chaine de caractère



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
