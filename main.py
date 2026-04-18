def son_turini_aniqlash(son):
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"

son = int(input("Son kiriting: "))
print(son_turini_aniqlash(son))