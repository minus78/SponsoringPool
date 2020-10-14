from web3 import Web3
import json
from datetime import datetime

def findUSDLock2(w3, addr):
    RedirectAddr = "0x5ae7E199EC6ACfe1D7ee28401637a0AE897818c1"
    with open("ABI/atoken.json") as json_file:
        abiContract = json.load(json_file)
        
        USDLock = 0
        AContract = w3.eth.contract(address=addr, abi=abiContract)
        filtre = AContract.events.InterestStreamRedirected.createFilter(fromBlock="0x0", argument_filters={'_to': RedirectAddr})
        tab = filtre.get_all_entries()

        print("Nb event: {}".format(len(tab)))

        AddrActiveRedirect = []
        d = AContract.functions.decimals().call()

        for i in tab:
            AddrActive = i.args["_from"]
            red = AContract.functions.getInterestRedirectionAddress(AddrActive).call()

            if red == RedirectAddr:
                if AddrActive in AddrActiveRedirect:
                    pass
                else:
                    AddrActiveRedirect.append(AddrActive)
                    bal = AContract.functions.balanceOf(AddrActive).call()*1.0/10**d
                    USDLock = USDLock + bal

        print(USDLock)
        print(AContract.functions.getRedirectedBalance(RedirectAddr).call()*1.0/10**d)
        return AddrActiveRedirect
