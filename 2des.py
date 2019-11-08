import des


class _2DES():
    def __init__(self, key1, key2):
        self.des1 = des.DES(key1)
        self.des2 = des.DES(key2)

    def encrypt(self, block):
        return self.des2.encrypt(self.des1.encrypt(block))

    def decrypt(self, block):
        return self.des1.decrypt(self.des2.decrypt(block))


if __name__ == '__main__':
    _2des = _2DES('secret_k', 'secret_k')
    x = _2des.encrypt('kekkekke')
    print("Ciphered: %r" % x)
    print("Deciphered: ", _2des.decrypt(x))
