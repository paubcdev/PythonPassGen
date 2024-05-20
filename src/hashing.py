import hashlib


def hash_sha256(password):
    hash_type = "SHA2-256"

    hashed = password

    return hash_type, hashed


def hash_sha3_256(password):
    hash_type = "SHA3-256"
    hashed = password
    return hashed


def hash_blake2b(password):
    pass


def hasher(password, mode):
    if mode == 1:
        hash_type = "SHA2-256"
        return hash_type
    elif mode == 2:
        hash_type = "SHA3-256"
        return hash_type
    elif mode == 3:
        hash_type = "BLAKE2b"
        return hash_type
