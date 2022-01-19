import json
import sqlite3
from web3 import Web3

class ContactContract:

    def newContactContract(self, user_name, contract_name):
        try:
            print("Initializing new contract.")
            self.web3.eth.defaultAccount = self.user_address
            self.stagedContactContract = self.web3.eth.contract(abi=self.abi, bytecode=self.bc)
        except:
            print("Failed to stage the contract locally.")

        try:
            self.tx_hash = self.stagedContactContract.constructor().transact()
            self.tx_receipt = self.web3.eth.waitForTransactionReceipt(self.tx_hash)
            self.contract_address=self.tx_receipt.contractAddress
            print("Contract initialized successfully.")
        except:
            print("Failed to initialize the contract.")
        try:
            self.cur.execute('insert into contract values (?, ?)', (self.contract_name, self.contract_address))
            self.con.commit()
        except:
            print("Failed to update the database with the new contract.")
        return self.contract_address

    def addUserToContract(self):
        try:
            tx_hash = self.contract.functions.addUser(self.user_name).transact()
            tx_receipt = self.web3.eth.waitForTransactionReceipt(self.tx_hash)
            print("User added to contract.")
        except:
            print("Failed to add user to contract.")
        try:
            self.cur.execute('insert into user values (?, ?, ?)', (self.user_name, self.user_address, self.user_key))
            self.cur.execute('insert into user_membership values (?, ?)', (self.user_name, self.contract_name))
            self.con.commit()
        except: ("Failed to update database.")

    def initDB(self):
        try:
            print("Looking for local contract database...")
            self.con=sqlite3.connect("/app/db/contact_contract.db")
            self.cur=self.con.cursor()
            print("Database loaded.")
        except:
            print("Local contract database not found. Generating database...")
            open('/app/db/contact_contract.db', 'x')
            self.con = sqlite3.connect('contact_contract.db')
            self.cur = con.cursor
        try:
            self.cur.execute("CREATE TABLE user (user_name text not null unique primary key, user_address text not null unique, user_key text not null unique)")
            self.cur.execute("CREATE TABLE contract (contract_name text not null unique primary key, contract_address text not null unique)")
            self.cur.execute("CREATE TABLE user_membership (user_name text not null, contract_name text not null, foreign key (user_name) references user (user_name),foreign key (contract_name) references contract (contract_name))")
            print("Database populated with tables.")
        except:
            print("Database already populated with tables.")
        self.cur.execute
        self.con.commit()

    # This message can be run without an argument to collect the chat history.
    def addMessage(self, message_content):
        if message_content=="##retrieve":
            self.contract.functions.addMessage(self.user_name, "").transact()
        else:
            self.contract.functions.addMessage(self.user_name, message_content).transact()

    def showMessages(self):
        log = []
        for message in self.contract.functions.addMessage(self.user_name, "").call():
            try:
                if message[2][1] and message[3]:
                    log.append(f'{message[2][1]})', f'{message[3]}')
            except:
                print("oops")
        return log
    
    def showUserKeys(self):
    	log = []
    	for user in self.contract.functions.getUserList().call():
    		log.append(f'{user[2]}')

    def validateUser(self, user_name, user_cipher):
    	self.contract.functions.validateUser(user_name, user_cipher)

    def __init__(self, user_name='', user_address='', contract_name=''):
        self.abi=json.loads(open('/app/build/Contact.json').read())
        self.bc=open('/app/build/Contact').read()[:-1]
        self.initDB()
        if not user_name:
            self.user_name= input("Please enter your name. ")
        else:
            self.user_name=user_name
        if not user_address:
            if self.cur.execute('select user_address from user where user_name=(?)', (self.user_name,)).fetchone():
                self.user_address = self.cur.execute('select user_address from user where user_name=(?)', (self.user_name,)).fetchone()[0]
            else:
                self.user_address = input("User not found in database. Please enter your address. ")
                self.cur.execute('insert into user values (?, ?)', (self.user_name, self.user_address))

        else:
            self.user_address=user_address
        if not contract_name:
            self.contract_name=input("Please enter your contract name. ")
            try:
                self.contract_address=self.cur.execute('select contract_address from contract where contract_name = (?)', (self.contract_name,)).fetchone()[0]
                print("Found contract in database.")
            except:
                print("Couldn't find contract in database.")
                self.contract_address = input("No contract address found. Please specify contract or press enter to create new contract." )
        self.rpc = open('/app/etc/rpc').read()[:-1]
        self.web3 = Web3(Web3.HTTPProvider(self.rpc))

        if self.contract_address=='':
            try:
                self.contract_address=self.newContactContract(self.user_name, self.contract_name)
                print(f'New contract created: {self.contract_address}')
            except:
                print("Contract creation failed.")
        try:
            self.abi=open('/app/build/Contact.json').read()
            self.web3=Web3(Web3.HTTPProvider(self.rpc))
            self.web3.eth.defaultAccount = self.user_address
            try:
                self.contract = self.web3.eth.contract(
                    address=self.contract_address,
                    abi=self.abi,
                )
            except:
                print("failure in block 112")
        except:
            print("Contract instantiation failed.")
        try:
            self.cur.execute('insert into user_membership values (?, ?)', (self.user_name, self.contract_name))
            self.con.commit()
            self.con.close()
        except:
            print("Failed to add user membership to database.")
        try:
            print(self.showMessages())
        except:
            print("Failed to collect messages.")
        self.con.close()
