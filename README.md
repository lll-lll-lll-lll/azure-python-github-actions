# 再現するには
必要なこと
- requirements.txtの用意<br>
- Azure Functionの初期化 [参考URL](https://qiita.com/Futo_Horio/items/dd36e0ed7d674f3f226f)(この時にrequirements.txtが用意される)<br>
- .venv/ の用意
- AZURE_FUNCTIONAPP_PUBLISH_PROFILEをgithub のsecretに設定

**仮想環境構築**
```sh
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
```
