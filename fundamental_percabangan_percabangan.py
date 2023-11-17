# sekuensial
print('ibu berkata, "pergi ke toko"')
print('budi berkata, "baik apa yang harus saya lakukan di toko?"')
print('ibu menjawab, "beli satu botol susu"')
print("maka budi berangkat ke toko")
print("dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f'jumlah botol susu {jumlah_botol_susu} botol')
print(f'jumlah telur {jumlah_telur} butir')

if jumlah_botol_susu > 0:
    print('Anak mengecek harganya, dan ternyata cukup uangnya')
    if jumlah_telur >= 6:
        print('Anak membeli 6 butir telur')
    else:
        print('Anak tidak membeli telur')
    print('Anak membeli 1 botol susu')
else:
    print('Anak tidak jadi membeli susu')

print('Anak pulang kerumah')
print('Anak menyampaikan hasilnya kepada ibu')