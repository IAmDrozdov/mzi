import binascii
from itertools import chain


class stb:
    @staticmethod
    def get_oct(value):
        if type(value) is not str:
            raise Exception("Value not string")
        return [ord(item) for item in value]

    def new_RotHi(self, value):
        return self.new_ShHi(value) ^ self.new_ShLo(value)

    @staticmethod
    def new_ShHi(value, k=1):
        return (value << k) ^ 2 ** 32

    @staticmethod
    def new_ShLo(value, k=31):
        return value >> k

    @staticmethod
    def to_int(values):
        shift = [24, 16, 8, 0]
        return sum([values[i] << shift[i] for i in range(4)])

    @staticmethod
    def to_list(value):
        shift = [24, 16, 8, 0]
        return [value >> item & 0xFF for item in shift]

    @staticmethod
    def to_int_l(values):
        shift = [0, 8, 16, 24]
        return sum([values[i] << shift[i] for i in range(4)])

    @staticmethod
    def to_list_l(value):
        shift = [0, 8, 16, 24]
        return [value >> item & 0xFF for item in shift]

    def plus(self, *args, base=2 ** 32):
        res = self.rev(args[0])
        for item in args[1:]:
            res = (res + self.rev(item)) % base
        return self.rev(res)

    def minus(self, a, b, base=2 ** 32):
        return self.rev((self.rev(a) - self.rev(b)) % base)

    @staticmethod
    def H(x):
        TABLE = [
            0xB1,
            0x94,
            0xBA,
            0xC8,
            0x0A,
            0x08,
            0xF5,
            0x3B,
            0x36,
            0x6D,
            0x00,
            0x8E,
            0x58,
            0x4A,
            0x5D,
            0xE4,
            0x85,
            0x04,
            0xFA,
            0x9D,
            0x1B,
            0xB6,
            0xC7,
            0xAC,
            0x25,
            0x2E,
            0x72,
            0xC2,
            0x02,
            0xFD,
            0xCE,
            0x0D,
            0x5B,
            0xE3,
            0xD6,
            0x12,
            0x17,
            0xB9,
            0x61,
            0x81,
            0xFE,
            0x67,
            0x86,
            0xAD,
            0x71,
            0x6B,
            0x89,
            0x0B,
            0x5C,
            0xB0,
            0xC0,
            0xFF,
            0x33,
            0xC3,
            0x56,
            0xB8,
            0x35,
            0xC4,
            0x05,
            0xAE,
            0xD8,
            0xE0,
            0x7F,
            0x99,
            0xE1,
            0x2B,
            0xDC,
            0x1A,
            0xE2,
            0x82,
            0x57,
            0xEC,
            0x70,
            0x3F,
            0xCC,
            0xF0,
            0x95,
            0xEE,
            0x8D,
            0xF1,
            0xC1,
            0xAB,
            0x76,
            0x38,
            0x9F,
            0xE6,
            0x78,
            0xCA,
            0xF7,
            0xC6,
            0xF8,
            0x60,
            0xD5,
            0xBB,
            0x9C,
            0x4F,
            0xF3,
            0x3C,
            0x65,
            0x7B,
            0x63,
            0x7C,
            0x30,
            0x6A,
            0xDD,
            0x4E,
            0xA7,
            0x79,
            0x9E,
            0xB2,
            0x3D,
            0x31,
            0x3E,
            0x98,
            0xB5,
            0x6E,
            0x27,
            0xD3,
            0xBC,
            0xCF,
            0x59,
            0x1E,
            0x18,
            0x1F,
            0x4C,
            0x5A,
            0xB7,
            0x93,
            0xE9,
            0xDE,
            0xE7,
            0x2C,
            0x8F,
            0x0C,
            0x0F,
            0xA6,
            0x2D,
            0xDB,
            0x49,
            0xF4,
            0x6F,
            0x73,
            0x96,
            0x47,
            0x06,
            0x07,
            0x53,
            0x16,
            0xED,
            0x24,
            0x7A,
            0x37,
            0x39,
            0xCB,
            0xA3,
            0x83,
            0x03,
            0xA9,
            0x8B,
            0xF6,
            0x92,
            0xBD,
            0x9B,
            0x1C,
            0xE5,
            0xD1,
            0x41,
            0x01,
            0x54,
            0x45,
            0xFB,
            0xC9,
            0x5E,
            0x4D,
            0x0E,
            0xF2,
            0x68,
            0x20,
            0x80,
            0xAA,
            0x22,
            0x7D,
            0x64,
            0x2F,
            0x26,
            0x87,
            0xF9,
            0x34,
            0x90,
            0x40,
            0x55,
            0x11,
            0xBE,
            0x32,
            0x97,
            0x13,
            0x43,
            0xFC,
            0x9A,
            0x48,
            0xA0,
            0x2A,
            0x88,
            0x5F,
            0x19,
            0x4B,
            0x09,
            0xA1,
            0x7E,
            0xCD,
            0xA4,
            0xD0,
            0x15,
            0x44,
            0xAF,
            0x8C,
            0xA5,
            0x84,
            0x50,
            0xBF,
            0x66,
            0xD2,
            0xE8,
            0x8A,
            0xA2,
            0xD7,
            0x46,
            0x52,
            0x42,
            0xA8,
            0xDF,
            0xB3,
            0x69,
            0x74,
            0xC5,
            0x51,
            0xEB,
            0x23,
            0x29,
            0x21,
            0xD4,
            0xEF,
            0xD9,
            0xB4,
            0x3A,
            0x62,
            0x28,
            0x75,
            0x91,
            0x14,
            0x10,
            0xEA,
            0x77,
            0x6C,
            0xDA,
            0x1D,
        ]
        return TABLE[x]

    def G(self, x, k):
        result = self.to_int([self.H(item) for item in self.to_list(x)])

        for _ in range(k):
            result = self.rev(self.new_RotHi(self.rev(result)))

        return result

    def encode(self, block, key):
        a, b, c, d, = [self.to_int(block[i:i + 4]) for i in range(0, len(block), 4)]
        keys = [self.to_int(key[i:i + 4]) for i in range(0, len(key), 4)]
        k = [keys[i % 8] for i in range(56)]
        for i in range(8):
            b = b ^ self.G(self.plus(a, k[7 * i + 0]), 5)
            c = c ^ self.G(self.plus(d, k[7 * i + 1]), 21)
            a = self.minus(a, self.G(self.plus(b, k[7 * i + 2]), 13))
            e = self.G(self.plus(self.plus(b, c), k[7 * i + 3]), 21) ^ self.to_int_l(
                self.to_list(i + 1)
            )
            b = self.plus(b, e)
            c = self.minus(c, e)
            d = self.plus(d, self.G(self.plus(c, k[7 * i + 4]), 13))
            b = b ^ self.G(self.plus(a, k[7 * i + 5]), 21)
            c = c ^ self.G(self.plus(d, k[7 * i + 6]), 5)
            a, b = b, a
            c, d = d, c
            b, c = c, b
        return self.to_list(b) + self.to_list(d) + self.to_list(a) + self.to_list(c)

    def decode(self, block, key):
        a, b, c, d, = [self.to_int(block[i:i + 4]) for i in range(0, len(block), 4)]
        keys = [self.to_int(key[i:i + 4]) for i in range(0, len(key), 4)]
        k = [keys[i % 8] for i in range(56)]
        for i in reversed(range(8)):
            b = b ^ self.G(self.plus(a, k[7 * i + 6]), 5)
            c = c ^ self.G(self.plus(d, k[7 * i + 5]), 21)
            a = self.minus(a, self.G(self.plus(b, k[7 * i + 4]), 13))
            e = self.G(self.plus(self.plus(b, c), k[7 * i + 3]), 21) ^ self.to_int_l(
                self.to_list(i + 1)
            )
            b = self.plus(b, e)
            c = self.minus(c, e)
            d = self.plus(d, self.G(self.plus(c, k[7 * i + 2]), 13))
            b = b ^ self.G(self.plus(a, k[7 * i + 1]), 21)
            c = c ^ self.G(self.plus(d, k[7 * i]), 5)
            a, b = b, a
            c, d = d, c
            a, d = d, a
        return self.to_list(c) + self.to_list(a) + self.to_list(d) + self.to_list(b)

    def rev(self, x):
        return self.to_int(self.to_list_l(x))


def unhex(value):
    return list(binascii.unhexlify(value))


if __name__ == '__main__':
    key_ = 'E9DEE72C8F0C0FA62DDB49F46F73964706075316ED247A3739CBA38303A98BF6'
    key = unhex(key_)
    text_ = 'B194BAC80A08F53B366D008E584A5DE48504FA9D1BB6C7AC252E72C202FDCE0D5BE3D61217B96181FE6786AD716B890B'
    text = unhex(text_)

    blocks = [text[i:i + 16] for i in range(0, len(text), 16)]
    r = [0 for _ in range(16 - len(blocks[-1]))]
    blocks[-1].extend(r)
    en_blocks = []
    for block in blocks:
        en_blocks.append(stb().encode(block, key))

    res = list(chain(*en_blocks))

    de_blocks = [stb().decode(block, key) for block in en_blocks]
    de_res = list(chain(*de_blocks))
    de_fin_res = [chr(item) for item in de_res]
    print('Key:', key_)
    print('Text:', text_)
    print('Encoded', ''.join(['%x' % item for item in res]))
