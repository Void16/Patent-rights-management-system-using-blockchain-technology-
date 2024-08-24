import json
from web3 import Web3
from django.conf import settings

# Load your contract's ABI (replace with your contract ABI)
contract_abi = json.loads("""
[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "patentId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "patentId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "title",
				"type": "string"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "filingDate",
				"type": "uint256"
			}
		],
		"name": "PatentRegistered",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_documentHash",
				"type": "string"
			}
		],
		"name": "registerPatent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_patentId",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "_newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_patentId",
				"type": "uint256"
			}
		],
		"name": "getDocumentHash",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_patentId",
				"type": "uint256"
			}
		],
		"name": "getPatentDetails",
		"outputs": [
			{
				"internalType": "string",
				"name": "title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "documentHash",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "filingDate",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "patentCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
""")

# Connect to the Ethereum network (Infura or local node)
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/91b32027538544e9bcca51eddbfe14ba'))

# Specify the contract address
contract_address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"

# Create the contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def register_patent(title, description, document_hash, user_address, private_key):
    # Create the transaction
    nonce = w3.eth.getTransactionCount(user_address)
    transaction = contract.functions.registerPatent(title, description, document_hash).buildTransaction({
        'chainId': 11155111,  # Sepolia Testnet Chain ID
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction
    signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key)

    # Send the transaction
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return tx_hash.hex()

# Function to retrieve patent details
def get_patent_details(patent_id):
    return contract.functions.getPatentDetails(patent_id).call()

