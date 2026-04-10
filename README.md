# WolTile - Wake-on-LAN Web UI

## プロジェクト概要

**WolTile** は、ブラウザ上でタイルをクリックして Wake-on-LAN（WOL）マジックパケットを送信できるシンプルな Web アプリケーションです。

複数のネットワークデバイスをタイル UI で一元管理でき、タイルクリック一つでリモートからデバイスを起動できます。

**技術スタック：**
- バックエンド：**FastAPI** + Python
- フロントエンド：**HTML** + **CSS** + **Vanilla JavaScript**
- サーバー起動：**Uvicorn**

---

## 必要環境

- **Python 3.x**（3.8 以上推奨）
- **pip**（Python パッケージマネージャー）
- **Git**（リポジトリをクローンする場合）

---

## インストール方法

### 1. リポジトリのクローン

```bash
git clone <リポジトリURL>
cd woltile
```

### 2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

このコマンドで以下がインストールされます：
- `fastapi` - Web フレームワーク
- `uvicorn` - ASGI サーバー
- `pydantic` - データバリデーション

---

## 起動方法

プロジェクトディレクトリで以下のコマンドを実行します：

```bash
uvicorn app.main:app --reload
```

**起動確認：**

ブラウザで以下の URL を開きます：

```
http://localhost:8000
```

WolTile のUI が表示されれば成功です。

---

## 設定ファイルの編集方法

### config/devices.json について

このファイルに Wake-on-LAN の送信対象デバイスを定義します。

**ファイル場所：** `config/devices.json`

### デバイスの追加方法

`config/devices.json` を編集して、デバイス情報を JSON 配列形式で追加します：

```json
[
  {
    "name": "NAS",
    "mac": "AA:BB:CC:DD:EE:FF"
  },
  {
    "name": "Living Room PC",
    "mac": "11:22:33:44:55:66"
  },
  {
    "name": "Media Server",
    "mac": "77:88:99:AA:BB:CC"
  }
]
```

**各項目の説明：**

| キー | 説明 | 例 |
|------|------|-----|
| `name` | デバイスの表示名（UI に表示されます） | `"NAS"`, `"Living Room PC"` |
| `mac` | デバイスの MAC アドレス（WOL パケット送信先） | `"AA:BB:CC:DD:EE:FF"` |

### 重要な注意

- **UI に表示されるのはデバイス名のみです**。MAC アドレスは内部処理に使用され、ブラウザには送信されません。
- MAC アドレスのフォーマットは `"AA:BB:CC:DD:EE:FF"` または `"AABBCCDDEEFF"` 形式に対応しています。

---

## 使い方

### 基本的な操作フロー

1. **ブラウザでアクセス**

   ```
   http://localhost:8000
   ```

2. **タイルが表示される**

   `config/devices.json` に登録されたデバイスがタイル状に表示されます。
   各タイルには **デバイス名のみ** が表示されます。

3. **タイルをクリック**

   目的のデバイスのタイルをクリックします。

4. **結果の確認**

   画面右上にトースト通知が表示されます：

   - ✅ **成功時**：緑色の通知が表示され、「Wake-on-LAN パケットが送信されました」というメッセージが表示されます。
   - ❌ **失敗時**：赤色の通知が表示され、エラー内容が表示されます。

### レスポンシブ対応

- **PC（1200px 以上）**：3 列グリッド
- **タブレット（641px～900px）**：2 列グリッド
- **スマートフォン（640px 以下）**：1 列表示

---

## ディレクトリ構成

```
woltile/
├── config/
│   └── devices.json          # デバイス設定ファイル（MAC アドレスと名前を管理）
├── app/
│   ├── main.py               # FastAPI アプリケーションメイン
│   ├── routers.py            # API ルート定義（/api/devices, /api/wake）
│   ├── models.py             # Pydantic モデル定義（Device クラス）
│   └── wol.py                # Wake-on-LAN マジックパケット送信ロジック
├── static/
│   ├── index.html            # HTML UI
│   ├── style.css             # スタイル定義
│   └── app.js                # JavaScript フロントエンドロジック
├── docs/
│   ├── copilot_prompt_woltile.md     # プロジェクト仕様書
│   └── copilot_prompt_readme.md      # README 作成指示書
├── requirements.txt          # Python パッケージ依存関係
└── README.md                 # このファイル
```

### 各ディレクトリ・ファイルの役割

| パス | 説明 |
|------|------|
| `config/` | アプリケーション設定ファイル置き場 |
| `app/` | FastAPI バックエンド実装 |
| `static/` | フロントエンド（HTML / CSS / JS） |
| `requirements.txt` | pip インストール対象パッケージ一覧 |

---

## API リファレンス

### GET /api/devices

登録されたすべてのデバイス情報を取得します。

**レスポンス例：**

```json
[
  {
    "name": "NAS",
    "mac": "AA:BB:CC:DD:EE:FF"
  },
  {
    "name": "Living Room PC",
    "mac": "11:22:33:44:55:66"
  }
]
```

### POST /api/wake

指定した MAC アドレスのデバイスに Wake-on-LAN パケットを送信します。

**リクエストボディ：**

```json
{
  "mac": "AA:BB:CC:DD:EE:FF"
}
```

**レスポンス（成功時）：**

```json
{
  "success": true,
  "message": "Wake-on-LAN packet sent."
}
```

---

## トラブルシューティング

### ブラウザでアクセスできない

1. Uvicorn が起動しているか確認
2. ターミナルに以下のコマンドを入力：

```bash
uvicorn app.main:app --reload
```

### デバイスが起動しない

1. `config/devices.json` の MAC アドレスが正確か確認
2. 対象デバイスが Wake-on-LAN に対応しているか確認
3. ネットワーク接続を確認

### パッケージのインストールに失敗

以下を確認してください：

- Python バージョンが 3.8 以上か
- pip がアップデートされているか：

```bash
pip install --upgrade pip
```

---
