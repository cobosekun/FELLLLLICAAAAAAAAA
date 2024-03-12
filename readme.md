# 手順
1. pipenv install && pipenv shell

2. brew install swig
pyscardのinstallに必須

3. pip install pyscard

# 学習
1. まずNFCとFelicaの仕組みを知らないと話にならない。 
下記で記載
2. 手持ちのFelicaからデータを読み取る。
RTAは読み取れた。デバイスも読み取れた。

## NFC
国際標準の通信規格を用いた技術
* カードエミュレーション機能  
ICカードやICタグの代わりになる機能  
* R/W機能
データの読み書きができること。
* 端末貫通新機能
NFC対応デバイス同士を近づけるだけでデータの送受信ができる機能

### 種類
上記の技術要件を満たしたNFCには、規格が３つありタイプによって分けられている。
1. Type-F(Felica)
2. Type-A
3. Type-B

### etc
NFCとFelica,おサイフケータイの違いは、いずれもNFC技術を使っていながら、FelicaはSonyが開発したNFC規格を用いて開発されたキャッシュレスサービスの一部のため、おサイフケータイはFelicaの一部と言える。
Felica本体はICカードであり、PaSoRi(RC-S300)はそのICカードをR/Wする機器である。

### ???
FelicaってICカードって認識だけど、NFC規格的にICカードの代わりになる機能であることってことは、FelicaはNFCではないってこと？NFCは何かをかざしてデータをR/Wできれば形を問わなくて、形を持ったのがFelicaって理解でいいのか？？

## Felica
1. カードの検出
かざせばいい
2. カードとリーダーの接続を確立
接続が確立されるとATR(Answer To Reset)を取得できる。  
ATRとは、カードの状態やプロトコル（カードの規格）等の情報が含まれる。わかりやすく言うと、Felicaの読み取り以前にR/WデバイスはNFC規格を用いたどんなICカードが来るかわからないのでR/WデバイスにかざすとICカードから自己紹介してくれるってことです。自己紹介リストは、https://pcsc-tools.apdu.fr/smartcard_list.txtを参考にしてください。ATRの構造を知りたい人は、https://en.wikipedia.org/wiki/Answer_to_reset のGeneral Structureの項目を見てください。01のビットデータをビット単位でパースしてどれがどの情報かをICカードに保存していてそれを返してくれているみたいです。なんとなくATRについて分かったら、https://smartcard-atr.apdu.fr/ で自分のNFCのATRを解析してみてもらってください。

## 参考ページ
https://service.smt.docomo.ne.jp/keitai_payment/corporation/shop/tips/ID40.html
https://www.docomo.ne.jp/binary/pdf/corporate/technology/rd/technical_journal/bn/vol29_2/vol29_2_008jp.pdf
https://ramble.impl.co.jp/2114/
