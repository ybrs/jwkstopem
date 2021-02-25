import jwt
from cryptography.hazmat.primitives import serialization
import requests
from jwt import PyJWKClient
import sys

def to_rsa_pem(key):
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
    pubk_bytes = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return pubk_bytes.decode()

def get_key_from_url(url):
    for k in requests.get(url).json()['keys']:
        print(to_rsa_pem(k))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage: python jwkstopem.py https://dev-87evx9ru.auth0.com/.well-known/jwks.json")
    else:
        get_key_from_url(sys.argv[1])