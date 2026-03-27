from fastapi import FastAPI
from app.database import SessionLocal
from app.models import Article
from app.scrapers.youtube import fetch_ai_news
from app.services.llm import summarize
from app.services.db_services import save_article
from app.scheduler import start_scheduler

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI News Navigator API running 🚀"}

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/news")
def get_news():
    db = SessionLocal()

    try:
        articles = db.query(Article) \
            .order_by(Article.created_at.desc()) \
            .limit(10) \
            .all()

        return [
            {
                "title": a.title,
                "summary": a.summary,
                "link": a.link
            }
            for a in articles
        ]

    except Exception as e:
        return {"error": str(e)}

    finally:
        db.close()


# 🔥 THIS IS WHERE YOU LEVEL UP
@app.post("/run")
def run_pipeline():
    try:
        articles = fetch_ai_news(limit=5)

        for art in articles:
            summary = summarize(art["content"])
            art["summary"] = summary
            save_article(art)

        return {"status": "pipeline executed successfully"}

    except Exception as e:
        return {"error": str(e)}
