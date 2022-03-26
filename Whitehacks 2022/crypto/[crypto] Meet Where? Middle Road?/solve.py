from random import randint
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fav_event = "wH1t3H@cK5_"
pt = 'aaaaaaaaaaaaaaaa' #my input
ct = b64decode("l3sGI8MveiL31mhmINTJtIPYKZkgFIGNGWFOGyr6NCg=".encode("utf-8")) #my input, encrypted

##STEP ONE: List all possible keys 
def possible_keys():
    poss_keys = []
    for a in digits:
        for b in digits:
            for c in digits:
                for d in digits:
                    for e in digits:
                        key = fav_event + str(a) + str(b) + str(c) + str(d) + str(e)
                        poss_keys.append(key)

    return poss_keys

##STEP TWO: Using all the possible keys, encode plaintext and store in map ciphertext -> key1
def enc_pt(possible_keys):
    result = {}
    for key in possible_keys:
        key1 = key
        cipher1 = AES.new(key1.encode("utf-8"), mode=AES.MODE_ECB)
        c1 = cipher1.encrypt(pad(pt.encode("utf-8"), AES.block_size))
        result[c1] = key1
        
    return result

##STEP THREE: Similarly, decode ciphertext and look up in the map from enc_pt
def denc_ct(possible_keys, enc_pt):
    for key in possible_keys:
        key2 = key           
        cipher2 = AES.new(key2.encode("utf-8"), mode=AES.MODE_ECB)
        result = cipher2.decrypt(ct)
        if result in enc_pt: #if we find a pair that matches
            key1 = enc_pt[result] 
            return key1, key2 #we win! here is our key


def main():
    keys = possible_keys()
    enc_plaintext = enc_pt(keys)
    denc_ciphertext = denc_ct(keys, enc_plaintext)
    print(denc_ciphertext)

if __name__ == "__main__":
    main()

   
