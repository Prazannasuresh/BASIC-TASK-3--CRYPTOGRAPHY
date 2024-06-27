import rsa
def genkey():
    (pubkey,privkey)=rsa.newkeys(1024)
    with open("pubkey.pem","wb") as f:
        f.write(pubkey.save_pkcs1("PEM"))
    with open("privkey.pem","wb") as f:
        f.write(privkey.save_pkcs1("PEM"))
def loadkey():
    with open("pubkey.pem","rb") as f:
        pubkey=rsa.PublicKey.load_pkcs1(f.read())
    with open("privkey.pem","rb") as f:
        privkey=rsa.PrivateKey.load_pkcs1(f.read())
    return pubkey,privkey
def encrypt(msg,key):
    return rsa.encrypt(msg.encode("ascii"),key)
def decrypt(ciphertext,key):
    try:
        return rsa.decrypt(ciphertext,key).decode("ascii")
    except:
        return False
def sign(msg, key):
    return rsa.sign(msg.encode("ascii"),key,"SHA-1")
def verify(msg,signature,key):
    try:
        return rsa.verify(msg.encode("ascii"),signature,key)=="SHA-1"
    except:
        return False
genkey()
pubkey,privkey=loadkey()
import os
path=input("Enter the path(working directory path):")
os.chdir(path)
u=input("Enter the file to read:")
a=u + ".txt"
if os.path.exists(a):
    f=open(a,"r")
    msg=f.read()
    f.close()
else:
    print("File does not exist")
ciphertext=encrypt(msg,pubkey)
signature=sign(msg,privkey)
oritext=decrypt(ciphertext,privkey)
print(f"Cipher text: {ciphertext}")
print(f"Signature: {signature}")
if oritext:
    print(f"original text: {oritext}")
else:
    print("Couldn't decrypt the file.")
if verify(oritext,signature,pubkey):
    print("Signature verified.")
    print("File has not been tampered.")
else:
    print("File signature could not be verified.")
    print("File has been tampered.")


    
