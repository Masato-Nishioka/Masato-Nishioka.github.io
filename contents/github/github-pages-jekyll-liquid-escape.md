# GitHub Pages × JekyllでMarkdownの`{{ }}`を壊さずに表示する方法

GitHub Pagesは、デフォルトで[Jekyll](https://jekyllrb.com/)という静的サイトジェネレーターを使用しています。  
Jekyllは、`.md`（Markdown）ファイルを自動的に`.html`ファイルに変換して公開できる便利な仕組みですが、**Liquidテンプレートエンジン**という仕組みを使っているために、Markdownに特定の構文を書くと意図しない変換が起こることがあります。

## なぜ変換ミスが起こるのか？

Jekyllは、Liquidというテンプレートエンジンを使用しており、以下のような構文をテンプレートとして解釈します。

- `{% raw %}{{ ... }}{% endraw %}` は **変数出力**
- `{% raw %}{% ... %}{% endraw %}` は **テンプレート構文**

つまり、Jekyllの目線では以下のような記述はすべてテンプレートの一部に見えてしまいます：

```markdown
{% raw %}${{ secrets.MY_SECRET }}{% endraw %}
```

この場合、Jekyllは{% raw %}{{ secrets.MY_SECRET }}{% endraw %}をLiquidテンプレートと解釈しようとしてしまうため、意図したとおりに表示されなくなります。表示が崩れる、もしくは空になる、などの不具合が出ます。

## 変換ミスの例

GitHub Actionsのサンプルなどで、Markdown中に以下のようなコードを含めたいことがあります。

```yaml
{% raw %}
app-id: ${{ vars.APP_ID }}
private-key: ${{ secrets.APP_PRIVATE_KEY }}
{% endraw %}
```

ところが、Jekyllは {% raw %}{{ vars.APP_ID }}{% endraw %} や {% raw %}{{ secrets.APP_PRIVATE_KEY }}{% endraw %} をテンプレートとして扱おうとするため、これが原因でページが正しく生成されず、**空になったりエラーになったり**することがあります。

## 解決方法：`raw`タグを使う

Jekyllのテンプレート構文に対して、「この部分はそのまま表示してね」と伝える方法があります。それが `raw` タグです。
`raw` タグを使用することで、Jekyllはその中をLiquidテンプレートとして解釈せず、そのまま出力してくれるようになります。

## 変換を自動化するPythonスクリプト

毎回手動で `raw` タグをつけるのは面倒なので、私は以下のPythonスクリプトで自動変換できるようにしました。

このスクリプトは、指定したディレクトリ内のMarkdownファイル内にある {% raw %}${{ ... }}{% endraw %} の構文を探して、自動的に `raw` タグで囲ってくれます。

### スクリプト

```python
import os

# ルートディレクトリを対象とする。適宜変換
markdown_dir = '.'

def wrap_raw_in_md_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # `${{` で始まり `}}` で終わる構文を `raw` タグで囲う
                updated_content = content.replace("${{", "{% raw %}${{").replace("}}", "}}{% endraw %}")

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

                print(f"Updated {file_path}")

wrap_raw_in_md_files(markdown_dir)
```

---

## 実行方法

1. 上記のコードを `wrap_raw.py` などのファイル名で保存します。
2. ターミナルでプロジェクトルートに移動し、次のコマンドで実行します：

```bash
python wrap_raw.py
```

## まとめ

- GitHub PagesはJekyllを使用しており、`.md` を自動で `.html` に変換する。
- しかし、Jekyllのテンプレートエンジン（Liquid）によって、{% raw %}{{ }}{% endraw %} の中が意図せず処理されてしまう。
- GitHub Actionsのような構文（{% raw %}${{ ... }}{% endraw %}）はそのまま書くと表示が崩れる。
- これを防ぐには `raw` タグで囲む必要がある。
- Pythonスクリプトを使えば、自動でこれを変換してくれるので、手間を減らすことができる。

---

これで、GitHub Actionsの構文を含んだMarkdownを、Jekyllを使ったGitHub Pagesでも安全に表示できるようになります。
