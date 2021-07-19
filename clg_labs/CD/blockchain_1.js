const SHA256 = require('crypto-js/sha256')

class block{
    constructor(index, timestamp, data, previous_hash=''){
        this.index = index;
        this.timestamp = timestamp;
        this.data = data;
        this.previous_hash = previous_hash;
        this.hash = this.calculate_hash();
        this.nonce = 0
    }

    calculate_hash(){
        return SHA256(this.index + this.timestamp + this.previous_hash + JSON.stringify(this.data) + this.nonce).toString();
    }

    mine_block(difficulty){
        while(this.hash.substring(0, difficulty) != Array(difficulty + 1).join("0")){
            this.nonce++;
            this.hash = this.calculate_hash();
        }
    }

}

class blockchain{
    constructor(){
        this.chain = [this.genesis_block()];
        this.difficulty = 2
    }

    genesis_block(){
        return new block(0, '11/01/1999', "Not confused !", "0");
    }

    get_latest_block(){
        return this.chain[this.chain.length-1];
    }

    add_block(newblock){
        newblock.previous_hash = this.get_latest_block().hash;
        newblock.mine_block(this.difficulty);
        this.chain.push(newblock);
    }

    is_chain_valid(){
        for(let i = 1; i < this.chain.length; i++){
            const currunt_block = this.chain[i];
            const previous_block = this.chain[i-1];

            if(currunt_block.hash != currunt_block.calculate_hash()){
                return false;
            }

            if(currunt_block.previous_hash != previous_block.hash){
                return false;
            }
        }
        return true;
    }
}

let me = new blockchain();
console.log('mining first block !!')
me.add_block(new block(1, "06/03/2000", { confused : 1 }));
console.log('mining second block !!')
me.add_block(new block(2, "10/08/1994", { idontknow : 1 }));


//console.log(me, null, 4)
