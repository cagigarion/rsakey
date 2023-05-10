from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from base64 import b64decode, b64encode
from Crypto.Util import asn1

ckd = '5ed7cdbf98749b2d484c50db635b5bab8631869b9a256251c0ff9f485a8a8d5a66b66ecc5adc83a1af5019bbec75eb817a4fc080d63aab208cf4f58d31ff0919138f5f57a3474dcefb73b09914849d373766427cdf0add264531ad0158a4737b3a6293f1ad626a00952510fba0cd07870fb209b406f802d1133765323c650849'

# code_bytes  = ckd.encode('UTF-8')
# bbb = b'f\xd8\xf4\xe4;\xce\x1e\xe9\xcb\x03\x1f\x94\x95\xd0\x02\xaa\xe0\xc9Z\xff?A\xe7\xf43\xbf\xd1-T\\Z\xa1\xa8\xdfF\xfd\xf9\x8dm\xb6\xbc2\xf8}\xb8Y\xea+\xae\x03\xd5\xd7\xaak\x16\x99\xefV/<\xb5\xafv\xb9\xa3\xbd3\xf5w\x99\x88\x16\xcd\x8a\xb8\xfa@\xfayiWY\xaej\xa7\x97&\xde\xaa(\xb4-\xbcs\xc1\x04\xff\xfc\xff\xc7\xcag\xc4O#\xa1\x96\x97\x89\xf4h\x98\xac\xeff\xf7(\xa7T\xd3\x050\x13\xac\x03O\xf7\xbe'

encrypted= bytes.fromhex(ckd)
print(encrypted)



key64Private = 'MIICXQIBAAKBgQC0Im4WeVxCrFNUv5+qqb7b8AxRpBnbfSRMcpAwqHJ5yCv/deCf\
aNFUWgNTESzG+54ER+GdIOWUlllWcagm7vEQ00QsolShECgKiUpR28KylOaqHlDm\
ZxlEsBNk6I26irFvKNR7pJ61FvoFm+b5q4SyiXrskBh0ImBmysXdDLfDcwIDAQAB\
AoGAJ6Q+Et8RUTDoQ8nJ4v5pHLC2nU7eS+G9178MgVDIpIlLOXRhAuPH0WbfvWuV\
rZKZAzsoaPJg47K0pWPsy+igjyLMusVTwklQomQITvcTh7dnTxS+SDufwDhTjZgR\
TDvKIxQDa7g5TCV9tyRImFd/uRjbKcfmlnrMzkeliGbvizUCQQDBSmkdM0fiFOkF\
8yHfGmXCO6oHOROZblJjpyGymlbOnpMyyj1cD2M4fVH7sklZDusHwXY5dkoIiWxt\
oPSVgpRdAkEA7pNYQWnPltY+nsLHhWdiC1WkAsxeUgVwYC7HHjiJ1WV6qVwev3eS\
kl5WfcjGb97pP4epfi7RY2HKcIfRvwQ6DwJBAKMVZFDV1p2jJOT3OanivN6/tnq3\
ppi641rfRehKnllgpDOjPVgyR3X/Dq/9wjMZCiaWDWj4LAi94jUxK4wGC6UCQQDq\
s8e6KncPY9uc4e/Y/JjGn8zG9/i+Zh1kcgBvaZ2ncrrWTArvv5lRJz+dZNxbCAec\
+UA0I6jYRUcbp3Ifoe/fAkAOTGZDtdfpI+nzz7YzUoeV/lXwhMrObcF9Dr6YzKKE\
hjEd+9KoWoPFeO1UZZprFY0GxsPE2ucCkNeVWk3WgoSd'
keyDERPrivate = b64decode(key64Private)
keyPrivate = RSA.importKey(keyDERPrivate)

decryptor = PKCS1_OAEP.new(keyPrivate)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)