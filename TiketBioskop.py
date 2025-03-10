print('             =====DAFTAR FILM DI ENHY CINEMA====='
'\n \n---------------------------------------------------------------'

' \nKode Film     Judul Film                            Harga Tiket'
'\n---------------------------------------------------------------'
' \n01            Siksa Kubur                           50.000'
' \n02            Ipar Adalah Maut                      50.000'
' \n03            Vina : Sebelum 7 Hari                 30.000'
' \n04            Moana 2                               40.000'
' \n05            Attack On Titan : The Last Attack     40.000'
' \n06            Kuasa Gelap                           40.000 \n ')

name = input("Masukkan nama anda: ")
code = input("Pilih kode film yang ingin anda tonton: ")
summ = int(input("Berapa jumlah tiket yang ingin anda pesan? "))

if code == '01' :
    price = 50000
    title = "Siksa Kubur"
elif code == '02' :
    price = 50000
    title = "Ipar Adalah Maut"
elif code == '03' :
    price = 30000
    title = "Vina : Sebelum 7 Hari"
elif code == '04' :
    price = 40000
    title = "Moana 2"
elif code == '05' :
    price = 40000
    title = "Attack On Titan : The Last Attack"
elif code == '06' :
    price = 40000
    title = "Kuasa Gelap"
else :
    print("Kode yang dimasukkan tidak valid. Silahkan coba lagi.")

total_price = summ*price

if total_price <= 100000 :
    discount = 0
    discount_price = total_price
elif 100000 <total_price <= 250000 :
    discount = int(15/100*total_price)
    discount_price = int(85/100*total_price)
else :
    discount = int(35/100*total_price)
    discount_price = int(65/100*total_price)

print("\n \n=====STRUK PEMESANAN TIKET ENHY CINEMA=====")
print(
    f"\nNama           : {name}"
    f"\nJudul Film     : {title}"
    f"\nJumlah Tiket   : {summ}"
    f"\nHarga Satuan   : {price}"
    f"\nPotongan Harga : {discount}"
    f"\nTotal Harga    : {discount_price}"
)
print("\n \n~Selamat Menonton~")
