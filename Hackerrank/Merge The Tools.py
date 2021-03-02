def merge_the_tools(string, k):
    
    # String length
    n = len(string)

    # Builds a list of sequences u of unique elements (we use dicionaries for that)
    u_list = [dict.fromkeys(string[i:i+k]) for i in range(0, len(string), k)]

    # Prints it
    for u in u_list:
        print(''.join(list(dict.keys(u))))

"""
Alternative solution

# Divides the string into substrings of length k
sub_strings = [s[i:i+k] for i in range(0, len(s), k)]

# Scans all the sub-strings
for t in sub_strings:
    
    u = []
    
    # Adds novel characters into it
    for c in t:
        if c not in u: u.append(c) 
    
    # Prints the the sequence u
    print(''.join(u))
"""   

if __name__ == '__main__':
