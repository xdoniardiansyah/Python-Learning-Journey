saldo_aktif = 10000000

while(True):

    print("\n=== MENU DOMPET DIGITAL ===")
    print("[1]. Cek Saldo")
    print("[2]. Tarik Dana")
    print("[3]. Keluar")

    try:
        pilihan_user = int(input("\nPilih menu (1/2/3): "))

    except ValueError:
        print(f"\n--> ERROR: Input tidak valid! Harap masukkan nominal dalam bentuk angka.")

    else:
        if pilihan_user == 1:
            print(f"\nSaldo anda: {saldo_aktif}")

        elif pilihan_user == 2:

            try:
                penarikan = int(input("\nBerapa nominal yang ingin ditarik? "))

                if penarikan > saldo_aktif:
                    print("\nSaldo anda tidak cukup!")
                else:
                    saldo_aktif -= penarikan
                    print(f"\nSisa saldo anda sekarang: {saldo_aktif}")

            except ValueError:
                print(f"\n--> ERROR: Input tidak valid! Harap masukkan nominal dalam bentuk angka.")
                
            
        else:
            print("\nAnda berhasil keluar dari Dompet Digital.\n")
            break