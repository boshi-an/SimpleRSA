from rsa import PrivateKey, PublicKey
import my_rsa

n, e = input('Your friend\'s public key: ').split(',')
message = input('Write your message here:')
n = int(n)
e = int(e)
print(n, e)
ciphertext = my_rsa.encrypt(message, PublicKey(n, e))

print("Your ciphertext: ", ciphertext)