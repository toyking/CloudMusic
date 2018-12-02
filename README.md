# CloudMusic
云音乐


# crontab
*/10 * * * * cd /data/release/NeteaseCloudMusicApi/ && PORT=80 node app.js >> /data/logs/NeteaseCloudMusicApi/`date +'%Y-%m-%d'`.log 2>&1 &