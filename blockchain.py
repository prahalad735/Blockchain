import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        """
        Initialize a new block.
        :param index: The block's position in the blockchain.
        :param previous_hash: The hash of the previous block in the chain.
        :param transactions: A list of transactions (dummy data in this case).
        :param timestamp: The time the block was created.
        :param nonce: A value used in mining (for proof-of-work).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block using SHA-256.
        :return: The hash of the block.
        """
        # Convert the block's data into a string and encode it
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        # Compute the SHA-256 hash of the encoded data
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        """
        Mine the block by finding a hash that meets the difficulty requirement.
        :param difficulty: The number of leading zeros required in the hash.
        """
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4):
        """
        Initialize the blockchain with a genesis block.
        :param difficulty: The difficulty level for proof-of-work.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (genesis block).
        :return: The genesis block.
        """
        return Block(0, "0", ["Genesis Block"], time.time())

    def get_latest_block(self):
        """
        Get the latest block in the blockchain.
        :return: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the blockchain.
        :param new_block: The block to be added.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.
        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print("Blockchain is invalid: Current block hash is incorrect.")
                return False

            # Check if the previous block's hash matches the current block's previous_hash
            if current_block.previous_hash != previous_block.hash:
                print("Blockchain is invalid: Previous block hash mismatch.")
                return False

        print("Blockchain is valid.")
        return True

    def print_chain(self):
        """
        Print the entire blockchain.
        """
        for block in self.chain:
            print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Transactions: {block.transactions}, Nonce: {block.nonce}]")

# Example Usage
if __name__ == "__main__":
    # Create a new blockchain with a difficulty of 4
    blockchain = Blockchain(difficulty=4)

    # Add blocks with dummy transactions
    blockchain.add_block(Block(1, "", ["Transaction 1"], time.time()))
    blockchain.add_block(Block(2, "", ["Transaction 2"], time.time()))

    # Print the blockchain
    print("\nBlockchain:")
    blockchain.print_chain()

    # Validate the blockchain
    print("\nValidating blockchain...")
    blockchain.is_chain_valid()

    # Tamper with the blockchain
    print("\nTampering with blockchain...")
    blockchain.chain[1].transactions = ["Tampered Transaction"]
    print("Blockchain after tampering:")
    blockchain.print_chain()

    # Validate the blockchain after tampering
    print("\nValidating blockchain after tampering...")
    blockchain.is_chain_valid()