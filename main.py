from random import choice;

caracteres = int(input("Informe a quantidade de caracteres presentes na senha:"))
print("Sua senha é:")

senha = []
elementos = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J",
             "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T",
               "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z","Z" , "0", "1", "2", "3", "4", "5", "6", "7",
                 "8", "9"
            ]

for i in range(caracteres):
    algarismos = choice(elementos)
    senha.append(algarismos)

for j in senha:
    print(j, end = '')
