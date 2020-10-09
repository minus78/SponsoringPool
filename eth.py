from web3 import Web3
from function import *
from function2 import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
import numpy as np

ProviderAddr = 'wss://mainnet.infura.io/ws/v3/aaaaaaaaaaaaaaaaaaa'
w3 = Web3(Web3.WebsocketProvider(ProviderAddr))

# contract
aDaiAddr = w3.toChecksumAddress("0xfC1E690f61EFd961294b3e1Ce3313fBD8aa4f85d")
aBusdAddr = w3.toChecksumAddress("0x6Ee0f7BB50a54AB5253dA0667B0Dc2ee526C30a8")
aUSDCAddr = w3.toChecksumAddress("0x9ba00d6856a4edf4665bca2c2309936572473b7e")
aUSDTAddr = w3.toChecksumAddress("0x71fc860F7D3A592A4a98740e39dB31d25db65ae8")
aTUSDAddr = w3.toChecksumAddress("0x4da9b813057d04baef4e5800e36083717b4a0341")
asUSDAddr = w3.toChecksumAddress( "0x625ae63000f46200499120b906716420bd059240")
totalUSD = 0


print("== DAI ==")
USDLock, dateTab1, USDTab1 = findUSDLock(w3, aDaiAddr)
print(USDLock)
findUSDLock2(w3, aDaiAddr)

print("== BUSD ==")
USDLock, dateTab2, USDTab2 = findUSDLock(w3, aBusdAddr)
print(USDLock)
findUSDLock2(w3, aBusdAddr)

print("== USDC ==")
USDLock, dateTab3, USDTab3 = findUSDLock(w3, aUSDCAddr)
print(USDLock)
findUSDLock2(w3, aUSDCAddr)

print("== USDT ==")
USDLock, dateTab4, USDTab4 = findUSDLock(w3, aUSDTAddr)
print(USDLock)
findUSDLock2(w3, aUSDTAddr)

print("== TUSD ==")
USDLock, dateTab5, USDTab5 = findUSDLock(w3, aTUSDAddr)
print(USDLock)
findUSDLock2(w3, aTUSDAddr)

print("== SUSD ==")
USDLock, dateTab6, USDTab6 = findUSDLock(w3, asUSDAddr)
print(USDLock)
findUSDLock2(w3, asUSDAddr)

print("== Graph ==")

fig, ax = plt.subplots()
ax.plot(dateTab1, np.array(USDTab1))
ax.plot(dateTab2, np.array(USDTab2))
ax.plot(dateTab3, np.array(USDTab3))
ax.plot(dateTab4, np.array(USDTab4))
ax.plot(dateTab5, np.array(USDTab5))
ax.plot(dateTab6, np.array(USDTab6))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=WE))
ax.grid()
ax.set_title("Pool Sponsoring")
ax.legend(["aDAI", "aBUSD", "aUSDC", "aUSDT", "aTUSD", "aSUSD"], loc="best")
fig.autofmt_xdate()
plt.show()

# USDC = 484752.77 => +7559
# DAI = 412108.72 => +352
