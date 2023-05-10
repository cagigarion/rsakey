from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from base64 import b64decode
from Crypto.Util import asn1
import base64


keyPair = RSA.generate(1024)

# print("keyPair > " + keyPair.exportKey().decode('ascii'))

# pubKey = keyPair.publickey()

# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

# pubKeyPEM = pubKey.exportKey()
# print(pubKeyPEM.decode('ascii'))

# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
# privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('ascii'))

key64 = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC0Im4WeVxCrFNUv5+qqb7b8AxR\
pBnbfSRMcpAwqHJ5yCv/deCfaNFUWgNTESzG+54ER+GdIOWUlllWcagm7vEQ00Qs\
olShECgKiUpR28KylOaqHlDmZxlEsBNk6I26irFvKNR7pJ61FvoFm+b5q4SyiXrs\
kBh0ImBmysXdDLfDcwIDAQAB'
keyDER = b64decode(key64)
keyPub = RSA.importKey(keyDER)


msg = b'{ "name":"John", "age":30, "city":"New York"}'
encryptor = PKCS1_OAEP.new(keyPub)
encrypted = encryptor.encrypt(msg)

# listTestByte = list(encrypted)
# print(listTestByte)

print("Encrypted:", binascii.hexlify(encrypted))
print("--------------------------------")

# print("Encrypted:", encrypted)

# print("--------------------------------------------------")

# key64Private = 'MIICXQIBAAKBgQC0Im4WeVxCrFNUv5+qqb7b8AxRpBnbfSRMcpAwqHJ5yCv/deCf\
# aNFUWgNTESzG+54ER+GdIOWUlllWcagm7vEQ00QsolShECgKiUpR28KylOaqHlDm\
# ZxlEsBNk6I26irFvKNR7pJ61FvoFm+b5q4SyiXrskBh0ImBmysXdDLfDcwIDAQAB\
# AoGAJ6Q+Et8RUTDoQ8nJ4v5pHLC2nU7eS+G9178MgVDIpIlLOXRhAuPH0WbfvWuV\
# rZKZAzsoaPJg47K0pWPsy+igjyLMusVTwklQomQITvcTh7dnTxS+SDufwDhTjZgR\
# TDvKIxQDa7g5TCV9tyRImFd/uRjbKcfmlnrMzkeliGbvizUCQQDBSmkdM0fiFOkF\
# 8yHfGmXCO6oHOROZblJjpyGymlbOnpMyyj1cD2M4fVH7sklZDusHwXY5dkoIiWxt\
# oPSVgpRdAkEA7pNYQWnPltY+nsLHhWdiC1WkAsxeUgVwYC7HHjiJ1WV6qVwev3eS\
# kl5WfcjGb97pP4epfi7RY2HKcIfRvwQ6DwJBAKMVZFDV1p2jJOT3OanivN6/tnq3\
# ppi641rfRehKnllgpDOjPVgyR3X/Dq/9wjMZCiaWDWj4LAi94jUxK4wGC6UCQQDq\
# s8e6KncPY9uc4e/Y/JjGn8zG9/i+Zh1kcgBvaZ2ncrrWTArvv5lRJz+dZNxbCAec\
# +UA0I6jYRUcbp3Ifoe/fAkAOTGZDtdfpI+nzz7YzUoeV/lXwhMrObcF9Dr6YzKKE\
# hjEd+9KoWoPFeO1UZZprFY0GxsPE2ucCkNeVWk3WgoSd'
# keyDERPrivate = b64decode(key64Private)
# keyPrivate = RSA.importKey(keyDERPrivate)


# decryptor = PKCS1_OAEP.new(keyPrivate)
# decrypted = decryptor.decrypt(encrypted)
# print('Decrypted:', decrypted)