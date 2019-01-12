# CloudMusic
网易云音乐NodeJS版API：https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=mv-%e8%af%84%e8%ae%ba


# crontab
*/1 * * * * cd /data/NeteaseCloudMusicApi/ && PORT=8000 node app.js >> /data/NeteaseCloudMusicApi/logs/`date +'%Y-%m-%d'`.log 2>&1 &
