#### Fonction secondaire
'''
Fonction palindrome
'''
def ispalindrome(p):
    '''
    Méthode qui teste si la chaine de caractère passé en paramètre est un palindrome
    return : True si c'est un palindrome
    '''
    p=p.lower()
    special= str.maketrans("éëêèàçùô","eeeeacuo")
    p=p.translate(special)
    for char in ["?", "!", ",", " ", ".", ":", "-","'"]:
        p = p.replace(char, "")
    n=p[::-1]
    if n==p:
        return True
    return False

#### Fonction principale


def main():
    '''
    Méthode principale qui teste la fonction secondaire
    '''

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
