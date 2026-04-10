以下の仕様に基づき、Wake-on-LAN Web アプリ「WolTile」の README.md を作成してください。

# README に含める内容

## 1. プロジェクト概要
- WolTile が何をするアプリか（タイル UI で Wake-on-LAN を送信）
- FastAPI + HTML/JS の構成であること

## 2. 必要環境
- Python 3.x
- pip
- Uvicorn
- GitHub からのクローン前提

## 3. インストール方法
- リポジトリのクローン手順
- requirements.txt のインストール手順

## 4. 起動方法
- Uvicorn を使った起動方法
- ブラウザでアクセスする URL（例: http://localhost:8000）

## 5. 設定ファイルの編集方法
- config/devices.json の説明
- デバイス名と MAC アドレスの追加方法
- UI には名前のみ表示されることを明記

## 6. 使い方（最重要）
- ブラウザでアクセスするとタイルが表示される
- タイルをクリックすると WOL パケットが送信される
- 成功/失敗時の挙動（トースト通知）

## 7. ディレクトリ構成
- config / app / static の役割を簡潔に説明

## 8. ライセンス（MIT で OK）
- 必要ならテンプレートで記載

# 出力形式
- 完成した README.md の全文を Markdown 形式で出力する
