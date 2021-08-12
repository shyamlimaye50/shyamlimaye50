def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
# Driver code
print(ispangram('the quick brown fox jumps over the lazy dog'))
