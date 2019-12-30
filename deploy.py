from web3 import Web3
from eth_account import Account
from eth_keys import keys
from eth_utils import keccak
import rlp

def createAccount(name):
    account = Account.create(name)
    private_key = account.privateKey
    address = account.address
    print(private_key,address)
    return account

url = "https://ropsten.infura.io/v3/58196e7733be426ca1564fb66eaaf575"

w3 = Web3(Web3.HTTPProvider(url))

print(w3.isConnected())

'''
A = Account.create('gordon')
private_key_A = A.privateKey
address_A = A.address
print(private_key_A,A.privateKey.hex())
print(address_A)

B = Account.create('bitch')
private_key_B = B.privateKey
address_B = B.address
print(private_key_B.hex())
print(address_B)

C = Account.create('ggininder')
private_key_C = C.privateKey
address_C = C.address
print(private_key_B.hex())
print(address_C)

balance_A = w3.eth.getBalance(address_A)
balance_B = w3.eth.getBalance(address_B)
balance_C = w3.eth.getBalance(address_C)

print('A:',balance_A)
print('B:',balance_B)
print('C:',balance_C)
'''

# test
private_key_A = bytes.fromhex('5d43a01075ccbaf8207d1c739e1a4f41b81cd68a009bd2fc0374d09b478fe0ff')
address_A = '0x3140c5cC6194dB5De7A005c2465879E3464De54E'

print(w3.eth.getBalance(address_A))

# deploy

import json
with open('./SABI.json', encoding='utf-8-sig') as f:
    info_json = json.load(f)
abi = info_json

file = open('./Sbytecode.txt')
bytecode = file.read()
file.close()


Token = w3.eth.contract(abi=abi, bytecode=bytecode)
Token_tx = Token.constructor().buildTransaction({
    'from':address_A,
    'nonce': w3.eth.getTransactionCount(address_A),
    'gas': 1728712,
    'gasPrice' : w3.toWei('21','gwei')})
    
signed = w3.eth.account.signTransaction(Token_tx,private_key_A)

Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
print(Token_Tx_hash.hex())

#contrat_address = ''
#Token_instance = w3.eth.contract(address = Web3.toChecksumAddress(contract_address),abi = abi)

