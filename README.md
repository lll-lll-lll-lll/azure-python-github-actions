# 再現するには
やること
1. rootにrequirements.txtを用意<br>
2. Azure Functionの初期化設定 [参考URL](https://qiita.com/Futo_Horio/items/dd36e0ed7d674f3f226f)(この時にrequirements.txtが用意される)<br>
3. 仮想環境を構築
4. ```AZURE_FUNCTIONAPP_PUBLISH_PROFILE```をgithub のsecretに設定


**仮想環境構築**
```sh
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
```