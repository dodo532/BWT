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
n = len(rotations)
for i in range (n-1):
    for j in range(n - 1 - i):
        if rotations[j] > rotations[j + 1]:
            var = rotations[j]
            rotations[j] = rotations [j+1]
            rotations[j+1] = var
print()
print("2--> si ordina l'output")
print()
print(rotations)

bwt = ""
for i in rotations:
    bwt += i[-1]
print("[",bwt,"[")
