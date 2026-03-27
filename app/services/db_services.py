from app.database import SessionLocal
from app.models import Article

def save_article(data):
    db = SessionLocal()

    existing = db.query(Article).filter(Article.link == data["link"]).first()
    if existing:
        db.close()
        return

    article = Article(
        title=data["title"],
        content=data["content"],
        summary=data["summary"],
        link=data["link"]
    )

    db.add(article)
    db.commit()
    db.close()