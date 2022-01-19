# Cello

## Description
Cello is a blockchain-based instant messaging client. So far it has been tested on Ethereum test-network Ropsten.

## Caveats
Beware that end-to-end encryption has not yet been added, so your messages will not be secure unless you use your own encryption.

## Installation

Clone the repo and change into the directory:

	$ git clone https://github.com/sosli86/cello-pub
	$ cd cello-pub

Run the build script with your preferred RPC server as an argument (localhost running Ganache in the example):

	$ ./build.sh http://localhost:7545

To run the docker after it's been built, run the following command:

	$ ./cello

## Next steps

The next version of the app will store public keys and a corresponding encrypted private key, generated or encrypted and stored in plaintext locally.
