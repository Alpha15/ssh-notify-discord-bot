#!/bin/bash

LOGFILE_NAME="/tmp/shellscript_auth.log"

##発生日取得関数
date_time() {
	MONTH=$(echo $1 | cut -f 1 -d " ")
	DATE=$(echo $2 | cut -f 2 -d " ")
	HOUR=$(echo $3 | cut -f 1 -d ":")
	MINUTE=$(echo $3 | cut -f 2 -d ":")
	SECOND=$(echo $3 | cut -f 3 -d ":")

	## 英語の月名を数字に変換
	MONTH=$(date -d"${MONTH} ${DATE}" +%m)
	
	TIME="${MONTH}月${DATE}日${HOUR}時${MINUTE}分${SECOND}秒"
}

ip2contry(){
	COUNTRY=$(whois ${1} | grep "country:" | uniq | cut -f 2 -d ":" | sed 's/ //g')
	if [ -z $COUNTRY ]; then
		COUNTRY="不明"
	fi
}

if [ -f ${LOGFILE_NAME} ]; then

	mv ${LOGFILE_NAME} /tmp/tmp_auth.log
	service rsyslog restart

	cat /tmp/tmp_auth.log | grep "Accepted" > /tmp/tmp_login.log
	cat /tmp/tmp_login.log | while read line
do
	IP=$(echo $line | cut -f 11 -d " ")
	#ip2country $IP
	COUNTRY=$(whois ${IP} | grep "country:" | uniq | cut -f 2 -d ":" | sed 's/ //g')
	if [ -z $COUNTRY ]; then
		COUNTRY="不明"
	fi
	USER=$(echo $line | cut -f 9 -d " ")
	date_time $line
	echo "${IP}(${COUNTRY}):${USER} is accepted to login.($TIME)"
done

	cat /tmp/tmp_auth.log | grep "preauth" > /tmp/tmp_nologin.log
	cat /tmp/tmp_nologin.log | while read line
do
	IP=$(echo $line | cut -f 12 -d " ")
	COUNTRY=$(whois ${IP} | grep "country:" | uniq | cut -f 2 -d ":" | sed 's/ //g')
	if [ -z $COUNTRY ]; then
		COUNTRY="不明"
	fi
	USER=$(echo $line | cut -f 11 -d " ")
	date_time $line
	echo "${IP}($COUNTRY):denied to access as ${USER}.(${TIME})"
done

	rm /tmp/tmp_auth.log /tmp/tmp_login.log /tmp/tmp_nologin.log

fi
