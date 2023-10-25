# 【概要】  
Discord botを動かしているUbuntu機にsshでの接続(または接続要求)があった時に,接続元IPとuser名,日時をdiscordの任意のチャンネルにて通知してくれる.
なお,sshは公開鍵のみの認証を想定している.

# 【準備】
 - discord.pyのインストール  
 - Discord botを作成できている(botのTOKENを取得できる)  
 - 通知を送信したいチャンネルのIDがわかっている  

「/etc/rsyslog.d」ディレクトリの下に60-tmp_auth.confを置く.  
  
## 想定される出力ログ  
> MONTH DD HH:mm:ss SERVER_NAME sshd[XXXX]: Accepted publickey for USER_NAME from XXX.XXX.XXX.XXX port XXXX ssh2: KEY HOGEHOGE  

必要に応じてテンプレートを変更してください.  

ログを書き込んでいるデーモンをリスタートさせる.  
`sudo systemctl restart rsyslog`

# 【起動方法】  
sudo DISCORD_TOKEN=\`cat token.auth\` CHANNEL=\`cat channel_id.ch\` python3 main.py  
ファイルに格納したTOKENとチャンネルIDを環境変数に渡して起動している.  

## 【コマンド】  
 - `!who`コマンドによりログイン中のユーザ一覧を取得できます.  

# 【免責事項】  
Ubuntu環境を想定しています。  
全ての環境での動作は保証されません。  

# 【参考】  
 - シェルスクリプトマガジン 最終回　不正アクセスを通知する  
> https://shell-mag.com/rensai-shellscript1-13/
 - discord botで定期的に処理をさせるためのLoop
> https://qiita.com/halglobe0108/items/a9d43a3eecabba06b5ef

