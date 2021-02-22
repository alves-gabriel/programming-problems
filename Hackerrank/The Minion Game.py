def minion_game(string):
    
    # Vower list and string size
    n = len(string)
    vowel = 'AIUEO'
    
    # Points initialization
    stuart = 0
    kevin = 0
    
    # What we should realize here is that the i-th letter contains
    # n - i subsequences starting at it (If i starts from 0). For example:
    # BANANA - The 3rd letter is an N
    #   ^
    # And there are 4 subsequences: NANA, NAN, NA and N.
    for i in range(n):
        
        if string[i] in vowel:
            kevin += n - i
        else:
            stuart += n - i
    
    # Compares the points
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
