from web3 import Web3
import json
from datetime import datetime

def findUSDLock(w3, addr):
    RedirectAddr = "0x5ae7E199EC6ACfe1D7ee28401637a0AE897818c1"
    with open("ABI/atoken.json") as json_file:
        abiContract = json.load(json_file)

        # BUSD
        USDLock = 0
        AContract = w3.eth.contract(address=addr, abi=abiContract)
        filtre = AContract.events.RedirectedBalanceUpdated.createFilter(fromBlock="0x0", argument_filters={'_targetAddress': RedirectAddr})
        tab = filtre.get_all_entries()
        d = AContract.functions.decimals().call()

        print("Nb event: {}".format(len(tab)))

        dateTab = []
        USDTab = []
        for i in tab:
            ajout = float(i.args["_redirectedBalanceAdded"])
            enleve = float(i.args["_redirectedBalanceRemoved"])
            USDLock = USDLock - enleve*(1.0/10**d) + ajout*(1.0/10**d)
            timestamp = w3.eth.getBlock(i.blockNumber).timestamp
            dateTab.append(datetime.fromtimestamp(timestamp))
            USDTab.append(USDLock)

        return USDLock, dateTab, USDTab
