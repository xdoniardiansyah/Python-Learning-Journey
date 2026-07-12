# 🔍 Simple Directory Enumerator

**Topik:** File Handling, HTTP Requests, Perulangan (For Loop), dan Error Handling (Try/Except)
**File Kode:** `enumerator.py`  
**Status:** ✅ Selesai murni tanpa copas AI!

### 💡 Catatan Perjalanan Belajar

Kali ini saya mencoba membuat kode enumerasi atau *fuzzing website*. Untuk membuat tampilan CLI yang oke rasanya cukup mudah, namun ternyata tidak dengan logika di belakangnya, hahaha.

Saya cukup kesusahan di bagian pembacaan file yang berisi *wordlist*. Di awal, saya sempat senang karena program berhasil mengeluarkan *output* "12 kata ditemukan". Namun, setelah saya cek dan hitung ulang secara manual, isi *wordlist* tersebut sebenarnya ada 20 kata. Kenapa malah keluar angka 12? Usut punya usut, ternyata yang dihitung oleh kode saya adalah jumlah karakter dari nama filenya, alias "wordlist.txt" (yang kebetulan pas berjumlah 12 huruf)!

Akhirnya, saya mulai mencari tutorial lagi untuk mencari tahu bagaimana cara menghitung isi *wordlist* dengan benar. Ternyata solusinya cukup simpel: saya hanya perlu membuat variabel, membaca file, dan menambahkan `.splitlines()` di belakangnya. Dengan begitu, isi *wordlist* otomatis terpotong per baris dan berubah menjadi *list*. Barulah setelah itu saya bisa menghitung isinya dengan membuat variabel baru yang memanggil fungsi `len()` untuk mengukur *list* tersebut.

Setelah urusan membaca file selesai, barulah saya memikirkan cara mengambil isi *wordlist* tersebut satu per satu, menggabungkannya ke belakang `url_target`, dan melihat *request response*-nya. Tak berselang lama, saya akhirnya bisa menyelesaikan kode ini dengan tangan saya sendiri! Tentu saja dibantu AI yang bertindak sebagai mentor: hanya menjelaskan langkah logikanya tanpa menyuapi *full code*-nya.

---

## ⚠️ Disclaimer

**ATTENTION:** This project is created for educational purposes and ethical hacking practice only. 

Segala kode yang ada di dalam repositori ini ditujukan untuk pembelajaran mengenai cara kerja enumerasi direktori dan penanganan jaringan pada Python. Penulis tidak bertanggung jawab atas segala penyalahgunaan, kerugian, atau implikasi hukum yang disebabkan oleh tindakan pengguna lain yang memodifikasi atau menjalankan *script* ini pada target yang tidak sah (*unauthorized*). Pengguna bertanggung jawab penuh atas tindakan mereka masing-masing.