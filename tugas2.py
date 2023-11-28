# deret angka 1-30
# tiap kelipatan angka 3 muncul dang
# tiap kelipatan 5 muncul dut
# tiap kelipatan 3 dan 5 muncul dangdut

"""
for i in range(1,31):
    if i%3 == 0 and i%5 ==0:
        print("dangdut")
    elif i%3 == 0:
        print("dang")
    elif i%5 == 0:
        print("dut")
    else:
        print(i)
"""
# belajar elif else
# nilai A = 100-90
# nilai B = 80-89
# nilai C = 70-79
# nilai D = 60-69
# nilai E = 0-59

nilai = int(input("masukan nilai :"))
if (nilai==100):
    print("nilai anda A")
elif (nilai>=90):
    print("nilai anda A")
elif (nilai>=80):
    print("nilai anda B")
elif (nilai>=70):
    print("nilai anda C")
elif (nilai>=60):
    print("nilai anda D")
elif (nilai>=50):
    print("nilai anda E")
elif (nilai>=0):
    print("selamat anda terdaftar dalam kategori parah sekali")
    print("anda harus bersabar bahwa hidup ini adalah ujian")





