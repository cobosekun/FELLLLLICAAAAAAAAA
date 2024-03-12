from smartcard.CardType import AnyCardType
from smartcard.CardConnection import CardConnection
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString

# インスタンス作成
cardtype = AnyCardType()

# timeoutで指定された時間分、カード読み取りを待機
cardrequest = CardRequest(timeout=5, cardType=cardtype)
cardservice = cardrequest.waitforcard()

# ATRを取得
cardservice.connection.connect(CardConnection.T1_protocol)
print(toHexString(cardservice.connection.getATR()))
# >>> 3B 8F 80 01 80 4F 0C A0 00 00 03 06 11 00 3B 00 00 00 00 42
#   smartcardlist参照↓
# 	RFID - FeliCa (汎用) (PCSC 標準パート 3 による)
# 	公共交通カード Suica (日本の IC システム) 
# 	(別名: はやかけん、ICOCA、Kitaca、manaca、nimoca、PASMO、PiTaPa、SUGOCA、TOICA) 
# 	https://en.wikipedia.org/wiki/Suica 
# 	Octopus、香港の MTR ネットワーク、2014 
# 	e-Amusement カード (その他) 
# 	https://en.wikipedia.org/wiki/E-Amusement 

# R/Wデバイスを取得
print(cardservice.connection.getReader())
# >>> SONY FeliCa Port/PaSoRi 4.0