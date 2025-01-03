## ソースコードの構成、概要を説明するドキュメント

### ・app.py

フィボナッチ数列を計算し、それを画面表示させるプログラム。「nに値が入力されていないとき」「nに0以下の値が入力されているとき」「nに入力された値がint型以外のとき」の3通りでそれぞれのエラーを表示するように設定した。また、今回はFlaskというPythonのWebアプリケーションフレームワークで開発を行った。

### ・test_app.py

ユニットテスト用のプログラム。

### ・requirements.txt

Pythonプロジェクトの依存関係を記録するファイル。Renderや他のデプロイサービス（Heroku、AWS、Azureなど）でアプリケーションをデプロイする際に、必要なライブラリをインストールするために使われる。

### ・\_\_pycache\_\_

Pythonがスクリプトを効率的に実行するために自動的に作成するフォルダ。

## 実際に動いている環境のエンドポイントURL
```
https://fib-api-3ew7.onrender.com/fib?n=5
```
今回はRenderというデプロイサービスを用いてサーバー構築を行った。

## curlコマンド実行例
```
curl -X GET "https://fib-api-3ew7.onrender.com/fib?n=10"
```

上記のコマンドをコマンドプロンプトなどに入力すると結果が返ってくる。
