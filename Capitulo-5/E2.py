def primo(a):
    if a == 2 or a == 3: return True
    if a%2 == 0 or a<2: return False
    for i in range(3, int(a**0.5)+1,2):
        if a%i ==0:
            return False
    return True

print(primo(13))