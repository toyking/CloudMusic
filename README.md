# CloudMusic
云音乐


# crontab
*/1 * * * * cd /data/NeteaseCloudMusicApi/ && PORT=8000 node app.js >> /data/NeteaseCloudMusicApi/logs/`date +'%Y-%m-%d'`.log 2>&1 &
