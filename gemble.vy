# Token

# Token params

owner: address
balances: map(address, uint256)
randomNumber : uint256
players: map(uint256, address)
playersLen: uint256
winner: address
MAX_PLAYERS: constant(int128) = 100


@public
def __init__(amount: uint256):
    self.owner = msg.sender
    self.balances[msg.sender] = amount
    self.playersLen = 0
    
@private
def random(time: timestamp, down: uint256, top: uint256) -> uint256 :
    return convert(keccak256(convert(time,bytes32)),uint256) % (top-down+1) + down

@public    
def deposit(account: address, amount: uint256):
    assert self.owner == msg.sender
    assert self.owner != account
    
    self.balances[self.owner] += amount

    
@public
def issue(account: address, amount: uint256):
    assert self.owner == msg.sender
    assert self.owner != account
    assert self.balances[self.owner] >= amount

    self.balances[self.owner] -= amount
    self.balances[account] += amount
    
    
@public
def transfer(to: address, amount: uint256):
    assert self.balances[msg.sender] >= amount
    assert self.owner != msg.sender
    assert to != msg.sender

    self.balances[msg.sender] -= amount
    self.balances[to] += amount
    
    
@public
def withdraw(account: address):
    assert self.owner == msg.sender
    assert self.owner != account
    self.balances[self.owner] += self.balances[account]
    self.balances[account] = 0

@public
def pull(amount: uint256):
    assert self.balances[msg.sender] >= amount
    assert self.owner != msg.sender
    
    self.balances[msg.sender] -= amount
    
    self.randomNumber = self.random(block.timestamp,111,999)
    if self.randomNumber == 111 :
        self.balances[msg.sender] += amount * 1
    elif self.randomNumber == 222 :
        self.balances[msg.sender] += amount * 2
    elif self.randomNumber == 333 :
        self.balances[msg.sender] += amount * 3
    elif self.randomNumber == 444 :
        self.balances[msg.sender] += amount * 4
    elif self.randomNumber == 555 :
        self.balances[msg.sender] += amount * 5
    elif self.randomNumber == 666 :
        self.balances[msg.sender] += amount * 6
    elif self.randomNumber == 777 :
        self.balances[msg.sender] += amount * 7
    elif self.randomNumber == 888 :
        self.balances[msg.sender] += amount * 8
    elif self.randomNumber == 999 :
        self.balances[msg.sender] += amount * 9


@public
def bet(amount: uint256):
    assert self.balances[msg.sender] >= amount * 10
    assert self.playersLen < MAX_PLAYERS
    assert amount > 0
    
    iter: uint256 = 0
    for i in range(MAX_PLAYERS):
        if self.playersLen + 1 > MAX_PLAYERS or iter >= amount:
            break
        self.players[self.playersLen] = msg.sender
        self.playersLen += 1
        self.balances[msg.sender] -= 10
        
        iter += 1
    if self.playersLen == 100:
        n: uint256 = self.random(block.timestamp,0,99)
        self.winner = self.players[n]
        self.balances[self.winner] += self.playersLen * 9
        self.playersLen = 0 
        
@public
@constant
def getWinner() -> address:
    return self.winner

@public
@constant
def getPlayersNumber() -> uint256:
    return self.playersLen
    
@public
def pickWinner():
    assert msg.sender == self.owner
    n: uint256 = self.random(block.timestamp, 0,self.playersLen-1)
    self.winner = self.players[n]
    self.balances[self.winner] += self.playersLen * 9
    self.playersLen = 0

@public
def reset():
    assert msg.sender == self.owner
    self.playersLen = 0    
        
    
@public
@constant
def getRandom() -> uint256 :
    return self.randomNumber

    

    


@public
@constant
def getBalabce() -> uint256:
    return self.balances[msg.sender]