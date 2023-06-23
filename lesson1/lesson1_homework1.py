def palindrom(string): 
    reversed_string = ''.join(reversed(string))
    if string == reversed_string:
        return True
    else:
        return False
    
print(palindrom(input("String: ")))