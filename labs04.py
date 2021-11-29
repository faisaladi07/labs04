list = ["m", "o", "b", "i", "l"]


print("Tampilkan elemen ke 3:", list[2])
print("ambil element ke 2 sampai 4:", list[1:4])
print("ambil element terakhir:", list[-1])


# Merubah elemen ke 4 dengan nilai lainya
list[3] = "s"
print("merubah elemen ke 4 dengan nilai lain :", list)

# Merubah elemen ke 4 sampai terakhir
list[3:] = "a", "l"
print("Merubah elemen ke 4 sampai terakhir:", list)
