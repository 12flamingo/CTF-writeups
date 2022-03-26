from random import randint
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

AES_KEY_SIZE = 16

flag = b"WH2022{fake_flag_for_testing}"

# Some say 0 is not a good number.
def get_new_key() -> bytes:
    digits = b"123456789"
    fav_event = b"wH1t3H@cK5_"

    while len(fav_event) < AES_KEY_SIZE:
        fav_event += bytes([digits[randint(0, 8)]])

    return fav_event


# Encrypting twice will make AES even stronger!
def encrypt(data, key1, key2):
    cipher1 = AES.new(key1, mode=AES.MODE_ECB)
    ct = cipher1.encrypt(pad(data, AES.block_size))
    cipher2 = AES.new(key2, mode=AES.MODE_ECB)
    ct = cipher2.encrypt(ct)

    ct = b64encode(ct).decode("utf-8")

    return ct

def decrypt(data, key):
    

def solve_me():
    key1 = get_new_key()
    key2 = get_new_key()

    ct = encrypt(flag, key1, key2)

    print(
        "Welcome to my personal encryption project\n"
        + "Where to meet next:\n"
        + ct 
        + "\n\nTest out this secure encryption scheme:\n> ",
        end="",
    )

    try:
        pt = input().strip()
        custom_enc = encrypt(pt.encode("utf-8"), key1, key2) #lets just say u put flag
        print(custom_enc + "\n")
        exit(1)
    except Exception as e:
        print(e)
        print("Error!\n")
        exit(1)


if __name__ == "__main__":
    solve_me()
