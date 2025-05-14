# GitHub Appとはなにか、どのようなメリットがあるのか

>GitHub App は、GitHub の機能を操作して拡張するために構築できる統合の一種です。  
>GitHub App を構築して、ユーザーのサインインやサービス アカウントの作成を必要とせずに、  
>柔軟性を提供し、プロセスの摩擦を軽減できます。

引用：[GitHub Apps について](https://docs.github.com/ja/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps#github-apps-%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)

## GitHub APIに対する認証

GitHub APIを落ちいて操作を行う際、多くのケースで認証が必要です。  
GitHub APIの認証方法はいくつかありますが、主に以下の2つの認証方法がよく使われている印象です。

- [personal access token](https://docs.github.com/ja/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#personal-access-token)
- [アプリによって生成されたトークンを使用した認証](https://docs.github.com/ja/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#authenticating-with-a-token-generated-by-an-app)

引用：[REST API に対する認証](https://docs.github.com/ja/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28)

## personal access tokenとGitHub Appのメリットデメリット

- personal access token
  - メリット
    - 手軽さ：簡単な設定で即時利用可能
    - シンプルさ：理解しやすい認証方式
  - デメリット
    - セキュリティリスク：トークン漏えいのリスク
    - アカウント依存：アカウント削除・権限変更で無効化
    - 権限の限界：ユーザー権限を超える操作不可
- GitHub App
  - メリット
    - セキュリティリスク：アクセス範囲を限定
    - 運用：アカウント削除の影響を受けない。
    - 組織利用：組織全体で一貫した認証
    - 権限独立：ユーザーに依存しない
  - デメリット
    - 複雑さ：設定・開発が複雑
    - 工数：設定に時間がかかる
