import numpy as np
import os, json
from web3 import Web3

chemin = os.path.join("sponsoring-pool_2020-10-14.tsv")
C = np.loadtxt(chemin, dtype=np.str,  delimiter="\t", skiprows=1)
Wallets = C[:,0]

ProviderAddr = 'wss://mainnet.infura.io/ws/v3/aaaaaaaaaaaaaa'
w3 = Web3(Web3.WebsocketProvider(ProviderAddr))

# contract
listContractCheck = []
listContractCheck.append(w3.toChecksumAddress("0xfC1E690f61EFd961294b3e1Ce3313fBD8aa4f85d"))
listContractCheck.append(w3.toChecksumAddress("0x6Ee0f7BB50a54AB5253dA0667B0Dc2ee526C30a8"))
listContractCheck.append(w3.toChecksumAddress("0x9ba00d6856a4edf4665bca2c2309936572473b7e"))
listContractCheck.append(w3.toChecksumAddress("0x71fc860F7D3A592A4a98740e39dB31d25db65ae8"))
listContractCheck.append(w3.toChecksumAddress("0x4da9b813057d04baef4e5800e36083717b4a0341"))
listContractCheck.append(w3.toChecksumAddress( "0x625ae63000f46200499120b906716420bd059240"))

# redirect Addresse
RedirectAddr = "0x5ae7E199EC6ACfe1D7ee28401637a0AE897818c1"

with open("ABI/atoken.json") as json_file:
    abiContract = json.load(json_file)
    lockUSD = 0
    for wallet in Wallets:
        print(wallet)
        wallet2 = w3.toChecksumAddress(wallet)
        for addrContract in listContractCheck:

            AContract = w3.eth.contract(address=addrContract, abi=abiContract)
            d = AContract.functions.decimals().call()
            red = AContract.functions.getInterestRedirectionAddress(wallet2).call()

            if red == RedirectAddr:
                bal = AContract.functions.balanceOf(wallet2).call()*1.0/10**d
                lockUSD = lockUSD + bal
print(lockUSD)  

