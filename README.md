## 立ち上げ方

1. `docker-compose up`
2. [8888 番ポート](http://localhost:8888/graphql)にアクセスする
3. Playground が立ち上がっているため、下記のクエリを実行できる

### 成功するクエリ

```
query {
  authenticateUser(request: {
    email: "user@example.com",
    password: "password"
  }) {
    isSuccess
    errorMessage
    data {
      id
      name
      email
    }
  }
}
```

### 失敗するクエリ

```
query {
  authenticateUser(request: {
    email: "user@example.com",
    password: "wrongpassword"
  }) {
    isSuccess
    errorMessage
    data {
      id
      name
      email
    }
  }
}
```

## Warning

- 実際のサーバーでは debug=False にして、middleware で CORS の設定をして起動する

参考記事

- [Notion](https://pinto-waltz-911.notion.site/Ariadne-122f3d9811d94bfd832c1e6dc88acc01#15c290b6126c4bfab0af9ce7db6ebb3c) ...変なテンションで書いたので語尾がおかしいです

---

## Alembic

- マイグレーションファイルを作成する

```
docker-compose run --rm app poetry run alembic revision --autogenerate -m "マイグレーションファイルの説明"
```

- 最新のマイグレーションファイルの状態を反映する

```
docker-compose run --rm app poetry run alembic upgrade head
```

---

その他必要なコマンドなど

- データベースの初期化

```
docker-compose run --rm app poetry run alembic downgrade base
```

- migrations/versions のファイルは不要（失敗した時など）になったら削除する

---
## memo
- .gitignoreに追加するだけでなく、ローカルで以下を実行すると__pyache__などのファイルを管理から除外できる
```
git rm -r --cached __pycache__/
git rm -r --cached *.py[cod]
git rm --cached *$py.class
```

`git rm --chached`ではインデックス（ステージング）からのみ消してくれるため、ワークツリーにはファイルが残るがgit管理から消すことができる便利なオプション
