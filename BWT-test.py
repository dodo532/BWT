string = input("inserisci una parola: ")
print(string)
print("1--> aggiunta $")
string+="$"
print(string)
print()
rotations = []
for i in range(len(string)):
    rotations.append(string[i:] + string[:i])
print(rotations)