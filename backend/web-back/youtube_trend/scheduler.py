from apscheduler.schedulers.background import BackgroundScheduler
from .youtube_service import youtube_api_service

# 定期実行
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(youtube_api_service, 'cron', hour=0, minute=0)
    scheduler.start()