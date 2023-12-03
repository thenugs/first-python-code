# funtion/methode
def bilangan_prima(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return "bukan prima"
        else:
            return "prima"
    else:
        return "bukan prima"

x = int(input('Masukkan bilangan: '))
hasil = bilangan_prima(x)
print(hasil)
