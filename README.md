Simple Blockchain Simulation

Overview

This is a basic blockchain simulation implemented in Python. It demonstrates core blockchain features such as:

Block structure with indexing, timestamps, transactions, and cryptographic hashes.

Hashing using SHA-256 to ensure data integrity.

A simple Proof-of-Work mechanism.

Blockchain validation to detect tampering.

Features

Genesis Block: The first block in the blockchain.

Adding Blocks: New blocks are added with dummy transactions.

Proof-of-Work: Blocks are mined with a difficulty level.

Blockchain Integrity Check: Ensures hashes are correctly linked.

Tampering Demonstration: Shows how modifications can break the chain.

Installation

Ensure you have Python installed, then clone the repository and run:
python blockchain.py

Example Output
Block mined: 0000267db264db2be7ea162e583938c7b0f5aea555e2a8718271cefcd124012d
Block mined: 0000dfb7a307bf0eda915974f44668ab104bccbcf39880c2dacfe0aa7aee2d37

Blockchain:
Block 0 [Hash: dc13ae40781419b56ee89046ff176d50678382b4ba62c11039a7a0f14df2f2ef, Previous Hash: 0, Transactions: ['Genesis Block'], Nonce: 0]
Block 1 [Hash: 0000267db264db2be7ea162e583938c7b0f5aea555e2a8718271cefcd124012d, Previous Hash: dc13ae40781419b56ee89046ff176d50678382b4ba62c11039a7a0f14df2f2ef, Transactions: ['Transaction 1'], Nonce: 2691]
Block 2 [Hash: 0000dfb7a307bf0eda915974f44668ab104bccbcf39880c2dacfe0aa7aee2d37, Previous Hash: 0000267db264db2be7ea162e583938c7b0f5aea555e2a8718271cefcd124012d, Transactions: ['Transaction 2'], Nonce: 173867]

Validating blockchain...
Blockchain is invalid: Current block hash is incorrect.

Tampering with blockchain...
Blockchain after tampering:
Block 0 [Hash: dc13ae40781419b56ee89046ff176d50678382b4ba62c11039a7a0f14df2f2ef, Previous Hash: 0, Transactions: ['Genesis Block'], Nonce: 0]
Block 1 [Hash: 0000267db264db2be7ea162e583938c7b0f5aea555e2a8718271cefcd124012d, Previous Hash: dc13ae40781419b56ee89046ff176d50678382b4ba62c11039a7a0f14df2f2ef, Transactions: ['Tampered Transaction'], Nonce: 2691]
Block 2 [Hash: 0000dfb7a307bf0eda915974f44668ab104bccbcf39880c2dacfe0aa7aee2d37, Previous Hash: 0000267db264db2be7ea162e583938c7b0f5aea555e2a8718271cefcd124012d, Transactions: ['Transaction 2'], Nonce: 173867]

Validating blockchain after tampering...
Blockchain is invalid: Current block hash is incorrect.
