def A(string):
    
    if string.islower():
        return list(string) == list(reversed(string))
    else:
        return ""
        
def B(phrase):
    
    phrase = phrase.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_phrase = ""
    for char in phrase:
        if char in alphabet:
            new_phrase += char
            
    return A(new_phrase)
        
def C(string, index):
    
    if string.islower():
        manip = ''
        distance_from_end = len(string) - index
        if distance_from_end < index:
            count = distance_from_end
        else:
            count = index
        for spot in range(1, count + 1):
            candidate = (string[index - spot: index + spot + 1])
            if A(candidate) and len(candidate) > len(manip):
                manip = candidate
        return manip
    else:
        return ""