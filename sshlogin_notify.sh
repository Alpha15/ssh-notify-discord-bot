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

if [ -f ${LOGFILE_NAME} ]; then

	mv ${LOGFILE_NAME} /tmp/tmp_auth.log
	service rsyslog restart

	# Login success
	cat /tmp/tmp_auth.log | grep "sshd\[[0-9]*\]" | grep "Accepted" > /tmp/tmp_login.log
	cat /tmp/tmp_login.log | while read line
	do
		IP=$(echo $line | cut -f 11 -d " ")
		USER=$(echo $line | cut -f 9 -d " ")
		date_time $line
		echo "${IP}:allowed to access as ${USER}.(${TIME})"
	done

	# Login failed (wrong auth)
	cat /tmp/tmp_auth.log | grep "sshd\[[0-9]*\]" | grep "preauth" > /tmp/tmp_nologin.log
	cat /tmp/tmp_nologin.log | while read line
	do
		IP=$(echo $line | cut -f 12 -d " ")
		USER=$(echo $line | cut -f 11 -d " ")
		date_time $line
		echo "${IP}:denied to access as ${USER}.(${TIME})"
	done

	# Login failed (wrong protocol)
	cat /tmp/tmp_auth.log | grep "sshd\[[0-9]*\]" | grep "Did not receive identification string" > /tmp/tmp_noidentification.log
	cat /tmp/tmp_noidentification.log | while read line
	do
		IP=$(echo $line | cut -f 12 -d " ")
		date_time $line
		echo "Did not receive identification string from ${IP}.(${TIME})"
	done

	rm /tmp/tmp_auth.log
	rm /tmp/tmp_login.log
	rm /tmp/tmp_nologin.log
	rm /tmp/tmp_noidentification.log

fi
