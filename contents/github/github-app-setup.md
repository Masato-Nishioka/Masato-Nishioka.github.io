# GitHub Appを使用して他組織のリポジトリをクローン

GitHub Actionsのワークフロー内で他組織に存在するリポジトリをクローンする際に  
PAT(personal access token)を使用していたが、セキュリティと管理工数の観点から、  
GitHub Appを使用することになったため、ナレッジを記載する。

## 確認事項

以下に記載する条件に当てはまる場合、この手順がそのまま使用できます。

- GitHub Appを使用して、組織内のワークフローから別組織のリポジトリをクローンしたい

## 前提条件

- Owner権限を持っている組織がある(GitHub App作成のために必要)

## 手順

ここからGitHub Appを使用し、ワークフロー内で他組織に存在するリポジトリをクローンする実装方法を記載します。  
なお、組織名を区別するために、実行するワークフローが存在する組織を**組織A**  
クローンしたいリポジトリが存在する組織を**組織B**と記載します。

### GitHub Appの作成

以下のページからGitHub Appの作成を行います。  
<https://github.com/organizations/{組織名}/settings/apps/new>

> [!NOTE]  
>`{組織名}`はGitHub Appを管理したい組織名に置換してください。組織A, Bどちらでも大丈夫です。  
>GitHub Appの作成には組織のOwner権限が必要です。

設定項目は以下の通りです。(必須項目のみ記載しています)

- Register new GitHub App
  - GitHub App name: **任意の名前**
  - Homepage URL: **ダミーURLでOK**(例: <https://example.com>)
- Webhook
  - **Activeのチェックマークを外す**
- Permissions
  - Repository permissions
    - Contents: **Read-only**
    - Metadata: **Read-only**
- Where can this GitHub App be installed: **This enterprise**

### GitHub AppのIDと秘密鍵を生成・保存

作成が完了すると、以下のページに作成したGithub Appが表示されます  
<https://github.com/organizations/{組織名}/settings/apps>

> [!NOTE]  
>`{組織名}`はGitHub Appを作成した組織名に置換してください。  
>Organization > settings > Developer Settings > GitHub Appから作成したGitHub Appを参照できます。

作成したGitHub Appを選択後、[Generate a private key]を選択し、秘密鍵を生成して保存します。  
また、App IDも後に使用するので書き留めておいてください。

### GitHub Appのインストール

作成したGitHub Appをインストールします。
以下のページから組織A,Bの対象リポジトリにインストールしてください。  
<https://github.com/organizations/{組織名}/settings/apps/{GitHub_APP名}installations>

> [!NOTE]  
>`{組織名}`はGitHub Appを作成した組織名に置換してください。  
>`{GitHub_APP名}`は作成したGitHub App名に置換してください。  
>対象リポジトリとは、ワークフローを実行するリポジトリ、ワークフロー内でクローンしたいリポジトリを指します。  
>インストールにはOwner権限が必要です。もし権限を所有していない場合は権限付与依頼 or インストール依頼をしてください。

### GitHub AppのIDと秘密鍵をVariablesとSecretに保存

組織AにGitHub AppのIDと秘密鍵をVariablesとSecretに保存します。  
<https://github.com/organizations/{組織A名}/{リポジトリ名}/settings/secrets/actions>

> [!NOTE]  
>`{組織A名}`は組織A名に置換してください。  
>`{リポジトリ名}`はsecretを保存するリポジトリ名に置換してください。  

なお、[GitHub公式][1]では、App IDは「Variables」、秘密鍵は「Secrets」に保存すると記載されているので、ここでもそうしています

### ワークフローの作成

以下は組織Aから組織Bのリポジトリをクローンするワークフローのサンプルです。  
組織A内のリポジトリに作成してください。

```yaml
name: Git clone with GitHub App

on: workflow_dispatch # 適宜変更

jobs:
  git_clone_check:
    runs-on: ubuntu-latest
    steps:
      - name: Generate GitHub App Token
        id: app_token
        uses: actions/create-github-app-token@v1
        with:
          app-id: ${{ vars.APP_ID }}
          private-key: ${{ secrets.APP_PRIVATE_KEY }}
          owner: {組織B名}

      - name: Clone private repository
        env:
          GH_TOKEN: ${{ steps.app_token.outputs.token }}
        run: |
          git clone https://x-access-token:"$GH_TOKEN"@github.com/{組織B名}/{リポジトリ名}.git

      - name: Check repository
        run: ls -la
```

> [!NOTE]  
>`{組織B名}`はクローンしたいリポジトリが属している組織Bの名前に置換してください。  
>`{リポジトリ名}`はクローンしたいリポジトリ名に置換してください。  

### ワークフローの実行

ワークフローを実行します。  
結果がを確認し、`Check repository`の`step`でリポジトリの存在が確認できていれば成功です。

```log
>☑︎ Set up job
>☑︎ Generate GitHub App Token
>☑︎ Clone private repositoty

∨☑︎ Check repository
  ▼Run ls -la
  ls -la
  shell: /usr/bin/bash -e {0}
total 0
drwxr-xr-x 3 runner runner  38 Apr 14 02:06 .
drwxr-xr-x 3 runner runner  48 Apr 14 02:06 ..
drwxr-xr-x 3 runner runner 138 Apr 14 02:06 {リポジトリ名}

>☑︎ Post Generate GitHub App Token
>☑︎ Complete job
```

---
[1]:https://docs.github.com/ja/enterprise-cloud@latest/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow
