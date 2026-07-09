"""
File: 01_cek_portofolio_v1.py
Topik: Dictionary, List, dan Control Flow (If-Else)

Catatan Perjalanan Belajar:
Jadi, code ini saya buat untuk memantau aset portofolio dari berbagai platform 
seperti Binance, Tokocrypto, dan Stockbit.

Saat merakitnya, saya mencoba mengeksplorasi merangkai kode demi kode sampai 
saya melihat tutorial menggunakan `itertools` untuk mengambil key dari dictionary. 
Tanpa disadari, explore ini terlalu explore ternyata, karena kodenya jadi panjang 
sekali untuk hal yang simpel.

Namun, itu semua menjadi pengalaman untuk saya di awal journey Python ini. 
Saya memang ingin mempelajari pemrograman Python dengan memahami kode dan logikanya, 
serta menghilangkan kebiasaan copas AI, karena untuk pemula seperti saya hasilnya 
tidak akan ada jika saya hanya copas dari AI.

Saya senang sekali bisa membuat kode ini dari awal sampai akhir tanpa copas AI. 
AI hanya saya pergunakan untuk mengajari saya dan memberi tahu materi apa yang 
harus saya baca atau tonton untuk menyelesaikan challenge Python ini.
"""

import itertools

Crypto = {
  "Binance" : [
    {
      "Aset":"BTC",
      "Jumlah":"0.5"
    },
    {
      "Aset":"ETH",
      "Jumlah":"2.1"
    }
  ],
  "Tokocrypto" : [
    {
      "Aset":"BNB",
      "Jumlah":"5.0"
    },
    {
      "Aset":"TKO",
      "Jumlah":"121"
    }
  ],
  "Stockbit" : [
    {
      "Aset":"BBCA",
      "Jumlah":"1000"
    },
    {
      "Aset":"GOTO",
      "Jumlah":"50000"
    }
  ]
}

binance_platform = "Binance"
tokocrypto_platform = "Tokocrypto"
stockbit_platform = "Stockbit"

pilihan_platform = input("Masukkan nama platform yang ingin dicek: ")

input_value = pilihan_platform.lower()
  
if len(Crypto) >= 2:
  binance = next(itertools.islice(Crypto, 0, None))
  tokocrypto = next(itertools.islice(Crypto, 1, None))
  stockbit = next(itertools.islice(Crypto, 2, None))

if input_value == "binance":
  print(f"=== Portofolio Di {binance} ===")

  for cex in Crypto[binance_platform]:
    print(f"-> Koin/Saham: {cex['Aset']} (Total: {cex['Jumlah']}")
elif input_value == "tokocrypto":
  print(f"=== Portofolio Di {tokocrypto} ===")

  for cex in Crypto[tokocrypto_platform]:
    print(f"-> Koin/Saham: {cex['Aset']} (Total: {cex['Jumlah']}")
elif input_value == "stockbit":
  print(f"=== Portofolio Di {stockbit} ===")

  for cex in Crypto[stockbit_platform]:
    print(f"-> Koin/Saham: {cex['Aset']} (Total: {cex['Jumlah']}")
else:
  print("Platform tidak terdaftar")