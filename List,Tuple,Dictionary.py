# List, Tuple data is tipe data yang bisa menampung banyak nilai data dalam satu variable
# belajar List
# list merupakan kumpulan data terurut (ordered sequence)
# dapat dirubah
# boleh duplikat
# List dibuat dengan kurung siku dan setiap elemen dipisah dengan tanda koma
# setiap elemen memiliki no urut (index) yang dimulai dari 0,1,2,3 dst
# yuk mulai

x = [8,9,"OTKP","ATPH",True]
print(x) # hasilnya [8, 9, 'OTKP', 'ATPH', True]
print(x[2]) #(x[2]) maksudnya adalah mencetak index ke 2 yaitu hasilnya OTKP
print(x[-5]) # (x[-5]) maksudnya adalah mencetak tapi mulai dari belakang


# Fungsi fungsi pada list
x = [8,9,"OTKP","ATPH",True]

# mencari panjang list
print(len(x)) # hasilnya = 8 , (len(x)) ini untuk mendapatkan panjang list yang ada di variabel x
print(x)

# mengubah nilai pada index ke
x[2]= "tokyo"
print(x) # [8, 9, 'tokyo', 'ATPH', True]
x[3]= 25
print(x) # [8, 9, 'tokyo', 25, True]

# menambah element pada index terakhir
x.append("merah")
print(x) # [8, 9, 'tokyo', 25, True, 'merah']

# menambah element pada index ke-1
x.insert(1,"tomat")
print(x) #[8, 'tomat', 9, 'tokyo', 25, True, 'merah']

# menghapus element tertentu
x.remove("tomat")
print(x) #[8, 9, 'tokyo', 25, True, 'merah']

# menghapus element pada index ke 0
x.pop(0)
print(x) #[9, 'tokyo', 25, True, 'merah']

x.clear()
print(x)



