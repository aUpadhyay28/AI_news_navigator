from app.scrapers.youtube import fetch_ai_news
from app.services.llm import summarize
from app.services.db_services import save_article


def run_pipeline():
    print("Fetching AI news...\n")

    articles = fetch_ai_news(limit=5)

    for art in articles:
        try:
            summary = summarize(art["content"])
            art["summary"] = summary

            save_article(art)

            print("Saved:", art["title"])

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    run_pipeline()