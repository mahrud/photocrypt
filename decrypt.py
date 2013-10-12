import binascii
import StringIO
import os, random, struct
from Crypto.Hash import SHA256 as SHA
from Crypto.Cipher import AES
 
class PKCS7Encoder(object):
    def __init__(self, k=16):
       self.k = k
 
    ## @param text The padded text for which the padding is to be removed.
    # @exception ValueError Raised when the input padding is missing or corrupt.
    def decode(self, text):
        '''
        Remove the PKCS#7 padding from a text string
        '''
        nl = len(text)
        val = int(binascii.hexlify(text[-1]), 16)
        if val > self.k:
            raise ValueError('Input is not padded or padding is corrupt')
 
        l = nl - val
        return text[:l]
 
    ## @param text The text to encode.
    def encode(self, text):
        '''
        Pad an input string according to PKCS#7
        '''
        l = len(text)
        output = StringIO.StringIO()
        val = self.k - (l % self.k)
        for _ in xrange(val):
            output.write('%02x' % val)
        return text + binascii.unhexlify(output.getvalue())

def encrypt(filename):
    h = SHA.new()
    file = open(filename, 'rb')
    plain = ''.join(file.readlines())
    file.close()
    h.update(plain)

    key = h.digest()

    enc = AES.new(key, AES.MODE_CBC, 16 * '\x00')

    encoder = PKCS7Encoder()
    padded = encoder.encode(plain)

    cipher = enc.encrypt(padded)

    file = open(filename + '.enc', 'wb')
    file.write(cipher.encode('base64'))
    file.close()

    return open(filename + '.enc', 'rb')
