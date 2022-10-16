import rsa
import os
from rsa import transform

def generateKeys(path = "keys"):

    if not os.path.exists(path):
        os.makedirs(path)
    
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open(os.path.join(path, "publickey.pem"), 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open(os.path.join(path, "privateKey.pem"), 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys(path = "keys"):
    with open(os.path.join(path, "publickey.pem"), 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open(os.path.join(path, "privateKey.pem"), 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return publicKey, privateKey

def encrypt(message, key):
    ciphertext = rsa.encrypt(message.encode('ascii'), key)
    int_cipher = transform.bytes2int(ciphertext)
    return int_cipher

def decrypt(ciphertext, key):
    try:
        byte_cipher = transform.int2bytes(ciphertext)
        return rsa.decrypt(byte_cipher, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False