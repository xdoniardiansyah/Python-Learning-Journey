import requests

url_target = input("Masukkan URL target (contoh: http://testphp.vulnweb.com/): ")
user_wordlist = input("Masukkan nama file wordlist beserta ekstensinya: ")

def open_file():
        hasil_teks = []
        try:
            with open(user_wordlist, mode="r") as file:
                    hasil_teks = file.read().splitlines()
                    
        except:
                pass
        
        return hasil_teks

daftar_kata = open_file()
total_kata = len(daftar_kata)

print("\n", 39*"=")
print("     SIMPLE DIRECTORY ENUMERATOR")
print(39*"=")
print(f"Target   : {url_target}")
print(f"Wordlist : {user_wordlist}")
print(39*"-")
print(f"[i] Membaca wordlist... {total_kata} kata ditemukan.")
print(f"[i] Memulai pemindaian...")
print(39*"-","\n")

for kata in daftar_kata:
       try:
        response = requests.get(url_target+kata)
        if response.status_code == 200:
                print(f"[+] Ditemukan : {url_target}{kata} (Status: {response.status_code})")
       except requests.exceptions.RequestException:
             print(f"[!] Peringatan: Koneksi terputus saat mencoba {url_target}{kata} Melewati kata ini...")