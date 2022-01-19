import math
import random
import os, sys
import gnupg
import json
from base64 import b64encode
from Crypto.Cipher import AES

# Establishes the PKI for a new user.
def newUserKey(user_name, user_email):
	os.mkdir('.' + user_name)
	gpg = gnupg.GPG(gnupghome='./.' + user_name)
	input_data = gpg.gen_key_input(key_type="RSA", key_length=1024, name_real=user_name, name_email=user_email)
	key = gpg.gen_key(input_data)
	return gpg.export_keys(user_name)

# Creates the private key for a new contract.
def newContract(contract_name):
	os.mkdir('.' + contract_name)
	keyFile = open('./.' + contract_name + '/contract.key', "x")
	key = ''.join(random.choice(string.printable) for i in range (128))
	keyFile.write(key)
	keyFile.close()
	return key

# Encrypts the contract key with a new user's public key, which is also added to the PKI
def addNewUser(user_key, contract_name)
	newUserPubKey = gpg.import_keys(user_key)
	keyFile = open('./.' + contract_name + '/contract.key', "r")
	encrypted_key = gpg.encrypt(keyFile.read(), newUserPubKey)
	keyFile.close()
	return encrypted_key
	
# Encrypts a new message
def encrypt(user_name, message_text, contract_name):
	header = b"%s", user_name
	keyFile = (open('./.' + contract_name + '/contract.key', "r")
	contract_key = keyFile.read()
	keyFile.close()
	cipher = AES.new(contract_key, AES.MODE_CCM)
	cipher.update(header)
	cipher_text, tag = cipher.encrypt_and_digest(message_text)
	json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
	json_v = [ b64encode(x).decode('utf-8') for x in cipher.nonce, header, cipher_text, tag ]
	result = json.dumps(dict(zip(json_k, json_v)))
	return result
	
# Decrypts a new message
def decrypt(cipher_text, contract_name):
	try:
		b64 = json.loads(json_input)
		json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
		jv = {k:b64decode(b64[k]) for k in json_k}
		cipher = AES.new(key, AES.MODE_CCM, nonce=jv['nonce'])
		cipher.update(jv['header'])
		plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
		return plaintext
	except: (ValueError, KeyError):
		return "Whoops!"
