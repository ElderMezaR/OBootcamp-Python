def bisiesto(año):
    if año% 400 == 0: return "Es bisiesto"
    elif año%4 == 0 and año%100 != 0: return "Es bisiesto"
    else: return "No es bisiesto"

print(bisiesto(1900))