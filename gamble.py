from web3 import Web3
from eth_account import Account
from eth_keys import keys
from eth_utils import keccak
import rlp


url = "https://ropsten.infura.io/v3/58196e7733be426ca1564fb66eaaf575"

w3 = Web3(Web3.HTTPProvider(url))
######
import json
with open('./ABI.json', encoding='utf-8-sig') as f:
    info_json = json.load(f)
abi = info_json

'''
file = open('./Sbytecode.txt')
bytecode = file.read()
file.close()
'''

vyper = '0x18b17ecc84d92745a62962e2e743d0ec933bb2cd'
#'0x586f798518adf847e3C23073bBda303A301FA3d0'
solidity = '0x1ee31fa0c6588e1a0d5bb5168fa9a6589c6e080a'

contract_address = vyper
Token_instance = w3.eth.contract(address = Web3.toChecksumAddress(contract_address),abi = abi)
######
private_key_A = bytes.fromhex('5d43a01075ccbaf8207d1c739e1a4f41b81cd68a009bd2fc0374d09b478fe0ff')
address_A = '0x3140c5cC6194dB5De7A005c2465879E3464De54E'

private_key_B = bytes.fromhex('1f967cdb8950a2eb987488bed2d0fcd0a1ea3abb9cd3acbd780f722b3c7ed8e6')
address_B = '0xE37793f19BE9a5Aa809c5C2eA0957a780D184164'

class account():
    def __init__(self,privateKey,address):
        self.privateKey = privateKey
        self.address = address
        
    def deposit(self,to_address,amount):
        
        Token_tx = Token_instance.functions.deposit(Web3.toChecksumAddress(to_address), amount).buildTransaction({
            'from': self.address,
            'nonce': w3.eth.getTransactionCount(self.address),
            'gas': 1728712,
            'gasPrice': w3.toWei('21', 'gwei')})

        signed = w3.eth.account.signTransaction(Token_tx, self.privateKey)

        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

        print(Token_Tx_hash.hex())
        receipt = w3.eth.waitForTransactionReceipt(Token_Tx_hash)
        print(receipt)   
        
    def issue(self,to_address,amount):
        
        Token_tx = Token_instance.functions.issue(Web3.toChecksumAddress(to_address), amount).buildTransaction({
            'from': self.address,
            'nonce': w3.eth.getTransactionCount(self.address),
            'gas': 1728712,
            'gasPrice': w3.toWei('21', 'gwei')})

        signed = w3.eth.account.signTransaction(Token_tx, self.privateKey)

        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

        print(Token_Tx_hash.hex())
        receipt = w3.eth.waitForTransactionReceipt(Token_Tx_hash)
        print(receipt)

    def pull(self,amount):
        address = self.address
        private_key = self.privateKey
        
        Token_tx = Token_instance.functions.pull(amount).buildTransaction({
            'from': address,
            'nonce': w3.eth.getTransactionCount(address),
            'gas': 1728712,
            'gasPrice': w3.toWei('21', 'gwei')})
            
        signed = w3.eth.account.signTransaction(Token_tx, private_key)
        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
        #print(Token_Tx_hash.hex())
        receipt = w3.eth.waitForTransactionReceipt(Token_Tx_hash)
        #print(receipt)
        randomNumber = Token_instance.functions.getRandom().call({'from': self.address})
        return randomNumber
    
    def bet(self,amount):
        address = self.address
        private_key = self.privateKey
        
        Token_tx = Token_instance.functions.bet(amount).buildTransaction({
            'from': address,
            'nonce': w3.eth.getTransactionCount(address),
            'gas': 1728712,
            'gasPrice': w3.toWei('21', 'gwei')})
            
        signed = w3.eth.account.signTransaction(Token_tx, private_key)
        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
        print(Token_Tx_hash.hex())
        receipt = w3.eth.waitForTransactionReceipt(Token_Tx_hash)
    
    def reset(self):
        address = self.address
        private_key = self.privateKey
        
        Token_tx = Token_instance.functions.reset().buildTransaction({
            'from': address,
            'nonce': w3.eth.getTransactionCount(address),
            'gas': 1728712,
            'gasPrice': w3.toWei('21', 'gwei')})
            
        signed = w3.eth.account.signTransaction(Token_tx, private_key)
        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
        #print(Token_Tx_hash.hex())
        receipt = w3.eth.waitForTransactionReceipt(Token_Tx_hash) 
        
    def getPlayersNumber(self):
        return Token_instance.functions.getPlayersNumber().call({'from': self.address})
        
    def getWinner(self):
        return Token_instance.functions.getWinner().call({'from': self.address})
    def getBalance(self):
        return Token_instance.functions.getBalabce().call({'from': self.address})

A = account(private_key_A,address_A)
B = account(private_key_B,address_B)
#issue(B,1000)
#pull(A,100)
