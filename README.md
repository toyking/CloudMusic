# CloudMusic
网易云音乐NodeJS版API：https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=mv-%e8%af%84%e8%ae%ba


# crontab
*/1 * * * * cd /data/NeteaseCloudMusicApi/ && export PORT=8000 && nohup node app.js >> /data/NeteaseCloudMusicApi/logs/run.log 2>&1 &


# django
*/1 * * * * cd /data/CloudMusic/ && nohup python manage.py runserver 0.0.0.0:80 >> /data/CloudMusic/logs/run.log 2>&1 &
