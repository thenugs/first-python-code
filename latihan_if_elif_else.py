'''
latihan if else termasuk dalam percabangan
 if else ini, jika di materi matematika sama dengan logika matematika, ada konjungsi, implikasi, biimplikasi
# contoh 1
p = 0.5
q = 21.5

if p>q:
    print("p lebih besar dari q")
else:print("q lebih besar dari p")

#contoh2
berat_badan = float(input("masukan angka :"))
if berat_badan > 100 :
    print("anda gendut")
    print("segera diet ya gaes")
else:print("anda langsing sekali")
print("kamu sangat ideal")
'''

#contoh3
# masih butuh penyempurnaan bagaimana jika ifnya bertingkat
#gen Z  <25 tahun
#gen Y  <25-35 tahun
#gen X  <36-55 tahun
#gen bomber >55 tahun

usia = float(input("masukan usia anda :"))
if usia > 55 :
    print("baby boomer")
elif(usia>36):
    print("gen X")
elif(usia>25):
    print("gen Y")
elif(usia<=25):
    print("gen Z")

