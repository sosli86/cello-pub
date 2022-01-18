# Cello

## Description
Cello is a blockchain-based instant messaging client. So far it has been tested on Ethereum test-network Ropsten.

## Caveats
Beware that end-to-end encryption has not yet been added, so your messages will not be secure unless you use your own encryption.

## Installation

Clone the repo and change into the directory:

	$ git clone https://github.com/sosli86/cello
	$ cd cello

Run the build script:

	$ ./build.sh

To run the docker after it's been built, run the following command:

	$ ./cello

## Next steps

The encryption infrastructure still needs to be added.

Each contract will have its own private key, generated locally when the contract is created.

Each user will have a private key and a public key, generated locally when the user is created.

Three-pass protocol will be used to securely transfer the private contract key to new users.

All messages sent to the contract will be encrypted and decrypted locally using the private contract key.
