import des


class _3DES():
    def __init__(self, key1, key2, key3):
        self.des1 = des.DES(key1)
        self.des2 = des.DES(key2)
        self.des3 = des.DES(key3)

    def encrypt(self, block):
        return self.des3.encrypt(self.des2.decrypt(self.des1.encrypt(block)))

    def decrypt(self, block):
        return self.des1.decrypt(self.des2.encrypt(self.des3.decrypt(block)))


if __name__ == '__main__':
    _3des = _3DES('secret_k', 'secret_k', 'secret_k')
    x = _3des.encrypt('kekkekke')
    print("Ciphered: %r" % x)
    print("Deciphered: ", _3des.decrypt(x))
