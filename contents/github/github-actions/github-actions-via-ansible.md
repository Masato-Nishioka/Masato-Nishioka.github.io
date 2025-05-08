# GitHub Actions を Ansible 経由で実行してみる

main ブランチじゃないのに `workflow_dispatch` が動いてた。ちょっと気になったので調べた。  
あと、Ansible で叩けそうだったので試してみたかった。

## ディレクトリ構成

以下ディレクトリ構造。  
ただ、`.github`, `ansible`ディレクトリは同じプロジェクトに存在する必要はない。

[こちら](/codes/github/github-actions/github-actions-via-ansible/)にサンプルコードを保管しています。

```tree
project-root/
├─ .github/
│   └─ workflows/
│        └─ sample.yml
└─ ansible/
     ├─ playbook.yml
     ├─ group_vars/
     │   └─ all.yml
     └─ roles/
         └─ trigger_workflow/
             ├─ tasks/
             │  └─ main.yml
             └─ vars/
                 └─ main.yml
```

## GitHub Actions の内容

### sample.yml

GitHub側にworkflowを認識させるため、一度workflowをトリガーする必要がある。  
`push`トリガーを設定してworkflowを実行し、GitHubに認識させる。  
一度トリガーさせた後はコメントアウト or 削除したほうがいいかも。

```yaml
name: Sample Workflow

on:
  push:
    branches:
      - sample-branch
  workflow_dispatch:
    inputs:
      name:
        description: 'Your name'
        required: true
      environment:
        description: 'Target environment'
        required: true

jobs:
  print-inputs:
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Hello, {% raw %}${{ github.event.inputs.name }}{% endraw %}"
          echo "Environment: {% raw %}${{ github.event.inputs.environment }}{% endraw %}"
```

## Ansible 側の内容

### group_vars/all.yml

```yaml
github_token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
repo_owner: "your-username"
repo_name: "your-repo"
branch_name: "sample-branch"
```

- `github_token` は **Personal Access Token (PAT)** を使う。
- GitHubの設定画面 → **Developer settings → Personal access tokens** で発行できる。
- スコープは `repo` と `workflow` を選べばOK。トリガーのPOSTが目的なら最小限でいい。

### playbook.yml

```yaml
- name: Trigger GitHub Actions via Ansible
  connection: local
  hosts: localhost
  gather_facts: false
  roles:
    - trigger_workflow

```

### roles/trigger_workflow/vars/main.yml

```yaml
workflow_file: ".github/workflows/sample1.yml"
inputs:
  name: "sample-name"
  environment: "staging"

```

### roles/trigger_workflow/tasks/main.yml

```yaml
- name: Trigger GitHub Actions workflow
  ansible.builtin.uri:
    url: "https://api.github.com/repos/{% raw %}{{ repo_owner }}{% endraw %}/{% raw %}{{ repo_name }}{% endraw %}/actions/workflows/{% raw %}{{ workflow_file | basename }}{% endraw %}/dispatches"
    method: POST
    headers:
      Accept: "application/vnd.github+json"
      Authorization: "Bearer {% raw %}{{ github_token }}{% endraw %}"
    body_format: json
    body:
      ref: "{% raw %}{{ branch_name }}{% endraw %}"
      inputs: "{% raw %}{{ inputs }}{% endraw %}"
    status_code: 204
  register: result

- name: Show result
  ansible.builtin.debug:
    var: result

```

## 実行コマンド

```bash
cd ansible
ansible-playbook -i localhost, playbook.yml
```

## 有用なケースの考察

- 特定ブランチや条件付きで Actions を叩きたいときに、入力変数込みで制御できて便利。
- インフラ構成管理のフローの一部として GitHub Actions を組み込みたいときに使える。
- CI/CD の実行を Ansible で管理したいケースに向いてる。

## やってみた結果

- `main` ブランチになくても `workflow_dispatch` トリガーで動く
- Ansible の `uri` モジュールで GitHub API 叩けることを確認

## 感想など

Ansible から GitHub Actions を操作できるの、けっこう便利だった。  
変数ファイルを分ければ複数のワークフローも使いまわせる。  
設定したらTower/AWX（Ansible Automation Platform）からボタンぽちぽちで実行できるのもいい。  
運用の仕組みに組み込んでおくと、GUI 経由でトリガーできて楽になると思う。
