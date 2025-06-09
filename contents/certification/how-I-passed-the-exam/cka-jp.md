# 認定Kubernetes管理者 (CKA-JP) 合格体験記

公式サイト：[認定Kubernetes管理者 (CKA-JP)](https://training.linuxfoundation.org/ja/certification/certified-kubernetes-administrator-cka-jp/)

## 前提

### 学習開始時点の知識・スキル

- 実務経験：12ヶ月(GitHub Actions, Terrform, Ansible, Google Cloud, AWS, Python)
- IT系保有資格：Google Cloud PCA, AWS SAA, LPIC-1

### 受験するモチベーション

Kubernetes関連の業務をすることが決まっており、事前に知識をつけておきたかった

## 学習内容

- [Certified Kubernetes Administrator (CKA) with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)
- Killer Shell
- [2025 Real CKA Exam Questions - New Pattern](https://www.udemy.com/course/real-cka-exam-questions-certified-kubernetes-administrator/?couponCode=ST12MT90625JP)

### 学習期間と時間

- 学習期間：81日（2025/3/20〜2025/6/9）
- 合計時間：約130〜150時間

内訳：

| 教材 | 時間 | 備考 |
|------|------|------|
| CKA Practice Tests（Udemy） | 約110〜120h | 2周＋苦手部分の復習 |
| Killer Shell | 約5h | 1回分のみ |
| Real CKA Questions（Udemy） | 約20〜30h | 苦手問題のみ（約0.5周） |

## 試験についての所感

CKAは実技形式の試験かつ自宅受験限定で、慣れないスタイルに戸惑いました。  
内容もKubernetesだけでなく、Linuxやコンテナ、ネットワーク、ストレージなど幅広く、正直かなり難しい試験でした。

特にネットワーク分野は業務経験が乏しく、独学もしていなかったため苦戦しました。

試験は2回分の受験資格が付いてきます。私は1回目（63/100）で不合格、2回目（84/100）で合格しました（合格基準：66%以上）。

## 教材レビュー

### Udemy：CKA Practice Tests

試験対策の中心として使用。  
Kubernetesの各リソース解説に加え、前提知識も丁寧に説明されており、理解を深めるのに非常に有用でした。

- 動画時間：約26時間（2025年6月時点）
- 仮想環境での演習付き
- 問題の質が高く、本試験を意識した構成

この教材だけで合格したという人もいるようです。

### Killer Shell

公式提供の模擬試験環境。  
本試験と非常によく似た構成で、2回分の模擬試験が利用できます。

私はUdemy教材を一周した後に一度挑戦しましたが、その時点では全く歯が立ちませんでした。その後は再挑戦していないため詳細は割愛します。

### Udemy：2025 Real CKA Exam Questions

1回目の不合格後に追加で購入。  
実際に出題された問題にかなり類似した内容が含まれており、非常に有益でした。

この教材を使って、スコアが63→84に向上しました。  
CKA Practice Testsだけで合格できなかった方には、強くおすすめできます。

## 試験時の注意点

### ネットワーク環境は要注意

試験は仮想環境上で行われ、操作のレスポンスにネットワーク品質が直結します。

私の場合、自宅のWi-Fi（下り300Mbps）で受験しましたが、レイテンシが1.5秒も発生し、試験中断となりました。  
**自宅＋有線接続での受験を強く推奨します。**

なお、試験前の部屋チェックは意外と緩めでした。「何もない部屋」が必須という訳ではありません。

### 試験予約時の名前入力に注意

試験予約時に政府発行の写真付き身分証明書が必要です。  
パスポートがない場合は運転免許証かマイナンバーカードを使うことになるかと思いますが、どちらも「日本語」で名前が書かれています。

予約画面でも名前を「日本語」で入力する必要があります。  
THE LINUX FOUNDATIONのアカウントがローマ字でも、**ローマ字で入力してしまうと再予約が必要になる**ので注意。

### バッテリーの消費量が多い

試験はCPU・ネットワークともに重いため、バッテリー消費が激しいです。  
M1 MacBook Airでバッテリー残量80%から開始したところ、途中で電源が落ちました。

**充電しながらの受験を強く推奨します。**

## 参考リンク

- [認定Kubernetes管理者 (CKA-JP) - 公式サイト](https://training.linuxfoundation.org/ja/certification/certified-kubernetes-administrator-cka-jp/)
- [PSI システム要件](https://helpdesk.psionline.com/hc/en-gb/articles/4409608794260-PSI-secure-browser-and-Chrome-Extension-System-Requirements)
- [認定資格の有効性確認](https://training.linuxfoundation.org/certification/verify/)
