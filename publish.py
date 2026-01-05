
import os
import requests
import frontmatter
from dotenv import load_dotenv

# Load environment variables from the parent directory where .env typically resides
# Adjust path as necessary to find the .env file
load_dotenv(dotenv_path="../../.env")

API_KEY = os.getenv("DEVTO_API_KEY")
ARTICLE_PATH = "generated_article.md"

def publish_article():
    if not API_KEY:
        print("❌ DEVTO_API_KEY not found in environment. Cannot publish.")
        return

    if not os.path.exists(ARTICLE_PATH):
        print(f"❌ Article file {ARTICLE_PATH} not found.")
        return

    print(f"📖 Reading article from {ARTICLE_PATH}...")
    with open(ARTICLE_PATH, 'r') as f:
        article_content = frontmatter.load(f)

    # Prepare payload
    # Dev.to API expects 'article' object
    # We strip the frontmatter from the content string as we send metadata separately, 
    # or we can send the raw markdown with frontmatter to the 'body_markdown' field?
    # The simpler way: send body_markdown with frontmatter included, usually works.
    
    # Let's verify frontmatter has published: true
    if article_content.get('published') is not True:
        print("⚠️ 'published: true' not found in frontmatter. Forcing it...")
        article_content['published'] = True
    
    # Re-dump to string to ensure the frontmatter is correct
    final_markdown = frontmatter.dumps(article_content)
    
    payload = {
        "article": {
            "title": article_content['title'],
            "body_markdown": final_markdown,
            "published": True,
            "tags": article_content.get('tags', []),
            "series": article_content.get('series'),
            "main_image": article_content.get('cover_image'),
            "canonical_url": article_content.get('canonical_url'),
            "description": article_content.get('description')
        }
    }

    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }

    print("🚀 Publishing to Dev.to...")
    response = requests.post("https://dev.to/api/articles", json=payload, headers=headers)

    if response.status_code == 201:
        data = response.json()
        print(f"✅ Successfully published!")
        print(f"🔗 URL: {data['url']}")
    else:
        print(f"❌ Failed to publish. Status: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    publish_article()
