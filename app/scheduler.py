from apscheduler.schedulers.background import BackgroundScheduler
from app.scrapers.youtube import fetch_ai_news
from app.services.llm import summarize
from app.services.db_services import save_article


def run_pipeline():
    print("⚡ Running scheduled pipeline...")

    articles = fetch_ai_news(limit=5)

    for art in articles:
        try:
            summary = summarize(art["content"])
            art["summary"] = summary
            save_article(art)

            print("Saved:", art["title"])

        except Exception as e:
            print("Error:", e)


def start_scheduler():
    scheduler = BackgroundScheduler()

    # 🔥 Runs every 1 hour (change later)
    scheduler.add_job(run_pipeline, "interval", hours=1)

    scheduler.start()