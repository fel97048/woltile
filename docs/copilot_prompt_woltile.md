以下の仕様に基づき、Wake-on-LAN パケットを送信する Web アプリケーション「WolTile」を構築するため、
複数ファイルをまとめて生成してください。

# 目的
Web UI 上でタイルをクリックすると、指定されたデバイスに Wake-on-LAN マジックパケットを送信できるアプリケーションを作成する。

# 使用技術
- Python 3.x
- FastAPI
- Uvicorn
- フロントエンドは HTML + CSS + JavaScript（Vanilla）
- 設定ファイルは JSON 形式でサーバー側に配置

# UI 仕様（重要）
- 画面にはデバイス名のみをタイル状に表示する
- MAC アドレスは UI に表示しない（内部的には API に渡す）
- タイルはクリック可能で、クリックすると WOL パケットを送信する
- タイルは CSS Grid で並べる（PC: 3列、タブレット: 2列、スマホ: 1〜2列）
- ホバー時に軽い影または色変化をつける
- 成功時・失敗時は画面右上にトースト通知を表示する
- ページ読み込み時に /api/devices を取得し、タイルを動的に生成する

# ディレクトリ構成
/config
  - devices.json
/app
  - main.py
  - wol.py
  - models.py
  - routers.py
/static
  - index.html
  - style.css
  - app.js
requirements.txt

# 各ファイルの要件

## config/devices.json
- Wake-on-LAN 送信先デバイスの一覧を定義
- 各デバイスは { "name": "NAS", "mac": "AA:BB:CC:DD:EE:FF" } の形式
- 配列で複数デバイスを保持

## app/wol.py
- send_wol(mac_address: str) を実装
- マジックパケットを生成し UDP ブロードキャスト（ポート 9）で送信
- 成功/失敗を bool または例外で返す

## app/models.py
- Device モデルを Pydantic BaseModel で定義
- name: str, mac: str

## app/routers.py
- FastAPI APIRouter を使用
- GET /api/devices: devices.json を読み込み返す
- POST /api/wake: body.mac を受け取り send_wol() を実行
- 成功/失敗を JSON で返す

## app/main.py
- FastAPI アプリを初期化
- routers.py を include_router で読み込む
- /static を静的ファイルとして提供
- index.html をルート("/")で返す

## static/index.html
- タイル一覧を表示する UI
- タイルには「デバイス名のみ」を表示する
- app.js を読み込む
- タイルクリックで wake API を呼び出す

## static/style.css
- タイルレイアウト（CSS Grid）
- タイルは角丸カード
- ホバー時に影または色変化
- トースト通知のスタイルも定義する

## static/app.js
- ページ読み込み時に /api/devices を取得
- デバイス名のみをタイルとして生成
- タイルクリックで /api/wake に POST
- 成功/失敗をトースト通知で表示

## requirements.txt
- fastapi
- uvicorn
- pydantic

# 出力形式
- 各ファイルを「```ファイル名\nコード```」の形式でまとめて提示する
- すべてのファイルを一度に出力する
