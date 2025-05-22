# #list
# x = []
# #dict
# y = {"key" : "value"}

# #dict -> list
# z = {
#     "nama" : [],
#     "umur" : []
# }

# #index dimulai dari 0

# buah = ["anggur", "mangga", "durian", "manggis"]

# # print(buah[1])

# biodata = {
#     "nama" : "Bintoro",
#     "umur" : 25
# }

# print(biodata["umur"])

# #nambah list append dan prepend
# buah.append("Cokelat")
# print(buah)

# biodata2 = {
#     "nama" : ["Bintoro","Ucup"],
#     "umur" : [25, 50]
# }
# print(biodata2["nama"][1])

#input dinamis
nama = []
for i in range(1,3):
    i_nama = input("Masukkan nama : ")
    nama.append(i_nama)
print(nama)

bio = {
    "nik" : [],
    "gender" : []
}

for i in range(1,3):
    i_nik = input("Masukkan NIK : ")
    bio["nik"].append(i_nik)
    i_gender = input("Masukkan gender : ")
    bio["gender"].append(i_gender)
print(bio)

print(bio["nik"][1])
print(bio["gender"][1])
