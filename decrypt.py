#!/usr/bin/python

import os, random, struct
from Crypto.Hash import SHA256 as SHA
from Crypto.Cipher import AES

def convergent_decryption(in_filename, out_filename=None, sha_chunksize=64*1024):
    h = SHA.new()
    sha_chunksize = 8192 
    with open(in_filename, 'rb') as f:
        while True:
            chunk = f.read(sha_chunksize)
            if len(chunk) == 0:
                break
            h.update(chunk)

    return h.hexdigest()
#    return encrypt_file(h.digest(), in_filename, out_filename, sha_chunksize)

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]+'.jpg'

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
#    return open(out_filename, 'rb')
