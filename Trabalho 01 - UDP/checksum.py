import hashlib

def checksum_gen(data):
    return hashlib.md5(data).hexdigest()

def checksum_chk(data, checksum):
    return hashlib.md5(data).hexdigest() == checksum