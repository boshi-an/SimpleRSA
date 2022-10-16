import my_rsa

my_rsa.generateKeys()

publicKey, privateKey = my_rsa.loadKeys()

print("Using: ", publicKey)

print("Please tell your friend your public key, and input the ciphertext from your friend.")

ciphertext = int(input())

text = my_rsa.decrypt(ciphertext, privateKey)

print("text: ", text)