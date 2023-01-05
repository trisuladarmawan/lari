# membuka text dan menjadikannya list
input = open("tubes_input.txt")
data = input.readlines()

#Contoh pembacaan file: 
# 21/12/2021 5 artinya pada tanggal 21 bulan desember 2021 
# saya berlari sejauh 25 km


# membuat dictionary kosong
catatan = {}

# membuat list kosong untuk menampung 
# jarak lari setiap bulannya
januari = []
februari = []
maret = []
januari = []
april = []
mei = []
juni = []
juli = []
agustus = []
september = []
oktober = []
november = []
desember = []

# memindahkan jarak lari dari text ke list
# menggunakan perulangan for
for dt in data:
    list_bulan = dt.split('/')
    list_jarak = dt.split(" ")
    bulan = int(list_bulan[1])
    jarak_lari = int(list_jarak[1])
    if bulan == 1:
        januari.append(jarak_lari)
    elif bulan == 2:
        februari.append(jarak_lari)
    elif bulan == 3:
        maret.append(jarak_lari)
    elif bulan == 4:
        april.append(jarak_lari)
    elif bulan == 5:
        mei.append(jarak_lari)
    elif bulan == 6:
        juni.append(jarak_lari)
    elif bulan == 7:
        juli.append(jarak_lari)
    elif bulan == 8:
        agustus.append(jarak_lari)
    elif bulan == 9:
        september.append(jarak_lari)
    elif bulan == 10:
        oktober.append(jarak_lari)
    elif bulan == 11:
        november.append(jarak_lari)
    elif bulan == 12:
        desember.append(jarak_lari)


# membuat list yang lebih besar untuk menampung 
# list jarak lari setiap bulannya 
jarak_tiap_bulan = [januari, februari, maret, april, mei, juni, juli, agustus, september, oktober, november, desember]

# mengisi key dan value dictionary catatan menggunakan perulangan while
i = 1
while i <= 12:
    catatan[i] = sum(jarak_tiap_bulan[i-1])
    i += 1

# membuat fungsi rekor untuk mengembalikkan (return) 
# bulan dengan total jarak terjauh yang berhasil ditempuh selama 2021.
def rekor(dict):
    value = []
    for v in dict.values():
        value.append(v)
    return value.index(max(value)) + 1

# membuat fungsi report yang digunakan untuk menampilkan 
# rata-rata jarak yang berhasil ditempuh setiap bulannya.
def report(dict):
    jumlah_jarak = 0
    banyak_bulan = 0
    for v in dict.values():
        jumlah_jarak += v
        banyak_bulan += 1
    return jumlah_jarak/banyak_bulan

# main program
print(catatan)
print(rekor(catatan))
print(report(catatan))

input.close()