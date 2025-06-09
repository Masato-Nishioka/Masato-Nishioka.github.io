# 認定Kubernetes管理者 (CKA-JP) 合格体験記

公式サイト：[認定Kubernetes管理者 (CKA-JP)](https://training.linuxfoundation.org/ja/certification/certified-kubernetes-administrator-cka-jp/)

## 前提

### 学習開始時点の知識

- 実務経験：12ヶ月(GitHub Actions, Terrform, Ansible, Google Cloud, AWS, Python)
- IT系保有資格：Google Cloud PCA, AWS SAA, LPIC-1

### 受験するモチベーション

Kubernetes関連の業務をすることが決まっており、事前に知識をつけておきたかった

## 学習内容

- [Certified Kubernetes Administrator (CKA) with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)
- Killer Shell
- [2025 Real CKA Exam Questions - New Pattern](https://www.udemy.com/course/real-cka-exam-questions-certified-kubernetes-administrator/?couponCode=ST12MT90625JP)

## 学習時間

所用日数：81d( 2025/3/20~2025/06/09 )  
合計時間：約130h~150h

- [Certified Kubernetes Administrator (CKA) with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/): 約110h~120h(2周+わからない部分を適宜)
- Killer Shell: 約5h(1回分)
- [2025 Real CKA Exam Questions - New Pattern](https://www.udemy.com/course/real-cka-exam-questions-certified-kubernetes-administrator/?couponCode=ST12MT90625JP): 約20h~30h(わからない問題のみ 約0.5周)

## 所感

選択形式ではなく実技形式という点と、自宅受験のみという点で、慣れない試験だった。  
Kubernetes自体、Linux、コンテナ、ネットワーク、ストレージなどを包括しているので、正直難しかったし、相当な勉強期間となった。  
特にネットワーク関連の部分については業務で本格的に扱ったことがないし、別途学習したこともほとんどなかったため、難儀した。  
本試験は申し込みをすると2回分の受験資格を得られる。  
私は1度目を63/100で落ち、2度目を84/100で合格した。(66%以上で合格)

### 教材について

試験の教材として、[Certified Kubernetes Administrator (CKA) with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)をメインに使用した。  
Kubernetesの各種リソースの説明はもちろんのこと、それに必要な前提知識から説明してくれるので、大変助かった。動画の時間だけで26時間(2025/06時点)だし、仮想環境でのテストもあるので、一周するだけで相当な時間がかかる。  
ただ、その分詳しく説明がされており、Kubernetesの基礎を固めることができたと感じている。  
仮想環境でのテストに関しては、本試験の問題を意識した問題が出題され、質の高さを感じた。  
人によってはこの教材だけで試験に受かってしまうらしい。  

追加の教材としてKiller Shellも使用した。  
これは、公式が提供している仮想環境上で解く模擬試験であり、本試験に近い問題がほぼ同じ環境が提供されている。  
試験に申し込みすると2回分の模擬試験の受験資格が得られる。  
上で記載したUdemy教材を1周した後に1度模擬試験にチャレンジしたが、その時点では手も足も出ず。  
またそれ以降受けていないので、正直詳細は覚えていない。

1度目の本試験では、上の2つだけで挑んだが、不合格だった。  
Udemyで他教材を探したところ、[2025 Real CKA Exam Questions - New Pattern](https://www.udemy.com/course/real-cka-exam-questions-certified-kubernetes-administrator/?couponCode=ST12MT90625JP)が見つかった。  
1度目の試験で出た問題に非常に類似している問題を取り扱っている。  
[Certified Kubernetes Administrator (CKA) with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)だけでは合格できない人はこれに頼ると良いかもしれない。  
実際私はこの教材のおかげで63→84まで点数が伸びた。

### 試験を受ける際の注意点

#### ネットワーク

本試験は仮想環境上で問題に沿ったKubernetesリソースの状態にする実技形式の試験。  
[システム要件](https://helpdesk.psionline.com/hc/en-gb/articles/4409608794260-PSI-secure-browser-and-Chrome-Extension-System-Requirements)を満たしている場合でも、無線接続が相当レイテンシが発生する恐れがある。  
無線接続で安定して300Mbps出ていた状態で受験したが、レイテンシが1500msec(1.5秒)発生し、試験を中断したほど、試験の環境のネットワーク問題は深刻。  
個室ブースを借りるのではなく、できれば自宅受験＆有線接続で受験した方がいい。  
なお、部屋の環境チェックが試験前に入るが、結構緩く感じた。  
何もない部屋じゃないと受験できないって訳ではないので、特別な事情がない限りは自宅受験がいい。

#### 試験の予約と受験に必要な手順

試験予約をする際に、自分の名前を入力する必要がある。  
ここでは、政府発行の写真付き身分証明書が必要。  
私のようにパスポートを持っていない人は、恐らく運転免許書 or マイナンバーカードになると思うが、どちらも名前が日本語で記載されている。  
この時、予約画面では、日本語の名前を入力する必要がある。  
THE LINUX FOUNDATIONのアカウントはローマ字だったから、ここもローマ字で入力してしまうかもしれないが、そうした場合、受験時間になっても受験スケジュールを再設定するハメになる

#### バッテリーの消費

試験はえげつないくらいバッテリーを食う。  
M1 Macbook Airに80%バッテリー残量がある状態で受験をしたが、試験中に充電が切れた。  
幸い、その試験は再受験可能となったが、充電しながらの受験を推奨する。

## 参考

- 公式サイト：[認定Kubernetes管理者 (CKA-JP)](https://training.linuxfoundation.org/ja/certification/certified-kubernetes-administrator-cka-jp/)
- システム要件: [PSI secure browser and Chrome Extension System Requirements](https://helpdesk.psionline.com/hc/en-gb/articles/4409608794260-PSI-secure-browser-and-Chrome-Extension-System-Requirements)
- 資格が有効か確認するURL: [The Linux Foundation Certification Verification Tool](https://training.linuxfoundation.org/certification/verify/)
