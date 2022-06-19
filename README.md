# 再現するには
やること
- requirements.txtを用意<br>
- Azure Functionの初期化設定 [参考URL](https://qiita.com/Futo_Horio/items/dd36e0ed7d674f3f226f)(この時にrequirements.txtが用意される)<br>
- 仮想環境を構築
- AZURE_FUNCTIONAPP_PUBLISH_PROFILEをgithub のsecretに設定


**仮想環境構築**
```sh
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
```