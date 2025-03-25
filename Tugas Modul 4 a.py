row = int(input("Masukkan jumlah baris: "))
column = int(input("Masukkan jumlah kolom: "))

for n in range(row):
    for j in range(column):
        if (n + j) % 2 == 0:
            print("x", end=" ") 
        else:
            print("o", end=" ")

    print()