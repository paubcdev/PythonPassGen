import hashlib


def hash_sha2_256(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


def hash_sha3_256(password):
    hashed = hashlib.sha3_256(password.encode()).hexdigest()
    return hashed


def hash_blake2b(password):
    hashed = hashlib.blake2b(password.encode()).hexdigest()
    return hashed


def hasher(password, mode):
    if mode == 1:
        hash_type = "SHA2-256"
        hashed = hash_sha2_256(password)
        return hash_type, hashed
    elif mode == 2:
        hash_type = "SHA3-256"
        hashed = hash_sha3_256(password)
        return hash_type, hashed
    elif mode == 3:
        hash_type = "BLAKE2b"
        hashed = hash_blake2b(password)
        return hash_type, hashed
