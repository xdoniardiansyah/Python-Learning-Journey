# 🛡️ Sistem Dompet Digital Anti-Crash

**Topik:** Error Handling (Try/Except/Else), Nested If, dan Validasi Logika
**File Kode:** `sistem_dompet.py`  
**Status:** ✅ Selesai murni tanpa copas AI!

### 💡 Catatan Perjalanan Belajar
Challenge kali ini lumayan rumit dibanding challenge kemarin. Kali ini saya membuat menu dompet digital di mana ada 3 pilihan ketika kita menjalankan programnya: 1) Cek Saldo, 2) Tarik Dana, 3) Keluar.

Seperti biasa, saya langsung menuju YouTube dan mencari tutorial `try except` Python di channel Kelas Terbuka. Setelah itu, saya bisa menyimpulkan bahwa kode saya terhenti (*runtime error*) ketika input *integer* malah dimasukkan *string*. Untuk pilihan menu utama sebenarnya mudah saja karena bisa langsung saya `except` ketika input tidak sesuai dengan tipe data yang diinginkan.

Masalah kedua muncul ketika saya ingin melanjutkan kode jika `try` berhasil menjalankan perintah. Akhirnya saya *searching* lumayan lama di YouTube dan mendapati video dari Bro Code dan juga beberapa video dari *programmer* India. Jadi di situ bisa saya lihat modenya mirip seperti `if-else`. Ketika `except` di-skip (karena tidak ada error), maka kita bisa melanjutkannya dengan blok `else:`. Dengan cara ini, `try-except` bisa berjalan sesuai dengan *challenge*.

Dan yap, ternyata saya sempat menemukan *bug* ketika memilih nomor 2 untuk penarikan. Di situ awalnya saya tidak membungkus input *integer* untuk nominal uang dengan `try-except` lagi, jadi *runtime error* masih terjadi jika diisikan huruf. Tapi setelah saya tambal, sekarang sudah dipastikan semuanya amann!