pragma solidity ^0.4.16;

contract gamble{
    address owner;
    address[] players;
    mapping (address => uint256) balances;
    uint256 private randomNumber;
    address winner;
    uint256 playersNumber;
    
    function gamble(){
        owner = msg.sender;
        balances[msg.sender] = 50000;
    }
    
    
    function random(uint256 down,uint256 top) internal returns(uint256){
        return uint256(sha3(now,block.blockhash(block.number-1))) % (top - down + 1) + down;
    }
    
    function deposit(address account,uint256 amount)
    {
        require(owner == msg.sender);
        balances[account] += amount;
    }
    
    function pull(uint256 amount){
        
        require(balances[msg.sender] >= amount);
        require(owner != msg.sender);

        balances[msg.sender] -= amount;
        balances[owner] += amount;
        
        
        randomNumber = random(111,999);
        uint256 temp = 0;
        if(randomNumber == 111)
            temp = amount;
        else if(randomNumber == 222)
            temp = amount*2;
        else if(randomNumber == 333)
            temp = amount*3;
        else if(randomNumber == 444)
            temp = amount*4;
        else if(randomNumber == 555)
            temp = amount*5;
        else if(randomNumber == 666)
            temp = amount*6;
        else if(randomNumber == 777)
            temp = amount*7;
        else if(randomNumber == 888)
            temp = amount*8;
        else if(randomNumber == 999)
            temp = amount*9;
        
        balances[msg.sender] += temp;
        balances[owner] -= temp;
    }
    
    function getRandom() constant returns(uint256)
    {
        return randomNumber;
    }
    
    function issue(address account, uint amount){
        require(msg.sender == owner);

        balances[account] += amount;
    }
    
    
    function getBalabce() constant returns(uint256){
        return balances[msg.sender];
    }
    
    function bet(uint256 amount){
        require(balances[msg.sender] > 10 * amount);
        require(players.length < 100);
        
        for(uint i = 1 ; i <= amount ; i++)
        {
            if(players.length+1 > 100)
                break;
            playersNumber = players.push(msg.sender);
            balances[msg.sender] -= 10;
        }
        if(players.length == 100)
        {
            uint256 n = random(0,players.length-1);
            winner = players[n];
            balances[winner] += players.length * 9 ;
            players = new address[](0);
            playersNumber = 0;
        }
    }
    
    function getWinner() constant returns(address)
    {
        return winner;
    }
    
    
    function getPlayersNumber() constant returns(uint256)
    {
        return playersNumber;
    }
    
    function getPlayers() public view returns (address[]) {
      return players;
    }
    
    function pickWinner()
    {
        require(msg.sender == owner);
        uint256 n = random(0,players.length);
        winner = players[n];
        balances[winner] += players.length * 9;
        players = new address[](0);
        playersNumber = 0;
    }
    function reset()
    {
        require(msg.sender == owner);
        players = new address[](0);
        playersNumber = 0;
    }
}