Crypto = {
    "Bitcoin": 1100000000,
    "Etherium": 31000000,
    "Solana": 1400000
}



while True:
    print("")
    print("=== SISTEM CEK ASET DIGITAL ===")

    user_input = input("Ketik nama koin yang ingin anda cek. (ketik 'keluar' untuk tutup): ")
    nama_coin = user_input.title()

    if nama_coin=="Keluar":
        print("--> Menutup sistem... Terima kasih!")
        exit()

    while nama_coin in  Crypto or nama_coin not in Crypto:

        if nama_coin not in Crypto:
            print(f"--> ERROR: Koin {nama_coin} tidak ditemukan dalam database kami.")
            break

        jumlah_coin = int(input("Berapa banyak koin yang anda miliki? "))

        total_aset = jumlah_coin * Crypto[nama_coin]

        print(f"--> SUKSES: {jumlah_coin} {nama_coin} setara dengan {total_aset}")
        break