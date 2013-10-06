#!/usr/bin/python

import os, random, struct
from Crypto.Hash import SHA256 as SHA
from Crypto.Cipher import AES

def convergent_encryption(in_filename, out_filename=None, sha_chunksize=64*1024):
    h = SHA.new()
    sha_chunksize = 8192 
    with open(in_filename, 'rb') as f:
        while True:
            chunk = f.read(sha_chunksize)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return encrypt_file(h.digest(), in_filename, out_filename, sha_chunksize)

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(0) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

    outfile.close()

    return open(out_filename, 'rb')
