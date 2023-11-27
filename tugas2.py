# deret angka 1-30
# tiap kelipatan angka 3 muncul dang
# tiap kelipatan 5 muncul dut
# tiap kelipatan 3 dan 5 muncul dangdut

for i in range(1,31):
    if i%3 == 0 and i%5 ==0:
        print("dangdut")
    elif i%3 == 0:
        print("dang")
    elif i%5 == 0:
        print("dut")
    else:
        print(i)





