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
#gen X  <25
#gen Y  <30
#gen Z  < 20
#gen tua  >30

usia = float(input("masukan usia anda :"))
if usia <= 25 :
    print("kamu gen x")
else:print("gen tua")
if usia >= 30 :
    print("gen tua")
else:print("gen gak jelas")

