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

                # `${{` で始まり `}}` で終わる構文を `{% raw %}` で囲う
                updated_content = content.replace("${{", "{% raw %}${{").replace("}}", "}}{% endraw %}")

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

                print(f"Updated {file_path}")

wrap_raw_in_md_files(markdown_dir)