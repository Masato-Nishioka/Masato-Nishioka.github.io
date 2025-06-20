# GitHub Actionsのワークフローを作成する際のプロンプト

[なんとなくから脱却する GitHub Actionsグッドプラクティス11選](https://gihyo.jp/article/2024/10/good-practices-for-github-actions)で紹介されていたサンプルワークフローをもとに、  
AIにワークフローの作成を依頼する際に使えるプロンプトのテンプレートを作成した。

## プロンプト

以下をコピペしてAIに投げる。

```text
私は、「」を実現するGitHub Actionsのワークフローを作成したいと考えています。  
要件は以下の通りです。

- トリガーは  
-  
-  

ワークフローの作成にあたっては、以下の項目を遵守してください。

- タイムアウトを常に指定する  
- デフォルトのシェルを定義する  
- `actionlint`を使用する  
- `concurrency`で古いワークフローを自動キャンセルする  
- ランナーは `ubuntu-latest` を使用する  
- `GITHUB_TOKEN` のパーミッションはジョブレベルで定義する  
- `set -x` コマンドでログを詳細に出力する  
- `workflow_dispatch` イベントで手動実行もサポートする  

以下にサンプルのワークフローを記載します。  
このサンプルに追記する形でワークフローを生成してください。

  ```yaml
  name: Example
  on:

  permissions: {}

  defaults:
    run:
      shell: bash

  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true

  jobs:
    example:
      runs-on: ubuntu-latest
      timeout-minutes: 5
      permissions:
        contents: read
      steps:
        - name: Run actionlint
          run: |
            set -x
            docker run --rm -v "$(pwd):$(pwd)" -w "$(pwd)" rhysd/actionlint:1.7.3
  ```
```

## 留意事項

アクションをハッシュ値で指定するには、そのコードの中身を確認・精査する必要があるため、今回は省略。  
ワークフローの背景情報などのコメントは、必要に応じて自分で追加する。  
