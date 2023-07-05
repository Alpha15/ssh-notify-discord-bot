【注意】  
**shellscript内は一部環境によって予期しない動作をする可能性があります.**

【概要】  
Discord botを動かしているLubuntu機にsshでの接続(または接続要求)があった時に、接続元IPとuser名,日時をdiscordの任意のチャンネルにて通知してくれる.
なお,sshは公開鍵のみの認証を想定している.

【準備】
 - discord.pyのインストール  
 - Discord botを作成できている(botのTOKENを取得できる)  
 - 通知を送信したいチャンネルのIDがわかっている  

「/etc/rsyslog.d」ディレクトリの下に60-tmp_auth.confを置く.  
ログを書き込んでいるデーモンをリスタートさせる.  
sudo systemctl restart rsyslog

【起動方法】  
sudo DISCORD_TOKEN=`cat lubuntu_bot_token.auth` CHANNEL=`cat lubuntu_ssh.ch` python3 lubuntu_bot.py

ファイルに格納したTOKENとチャンネルIDを環境変数に渡して起動している.


【参考】  
 - シェルスクリプトマガジン 最終回　不正アクセスを通知する  
> https://shell-mag.com/rensai-shellscript1-13/
 - discord botで定期的に処理をさせるためのLoop
> https://qiita.com/halglobe0108/items/a9d43a3eecabba06b5ef

