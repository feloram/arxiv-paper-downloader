import arxiv
import os
import requests

# ایجاد پوشه برای داده‌ها
os.makedirs("data", exist_ok=True)

# تعریف موضوعات جستجو
search_queries = [
    "Retrieval-Augmented Generation", 
    "Large Language Models agents", 
    "Hallucination detection in LLMs"
]

client = arxiv.Client()

for query in search_queries:
    print(f"Searching for: {query}")
    search = arxiv.Search(
        query=query,
        max_results=5,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    for result in client.results(search):
        # ساخت یک نام فایل تمیز بر اساس آیدی مقاله
        paper_id = result.entry_id.split('/')[-1]
        filename = f"data/{paper_id}.pdf"
        
        # اگر قبلاً دانلود نشده بود، دانلودش کن
        if not os.path.exists(filename):
            print(f"Downloading: {result.title}...")
            try:
                # استفاده از requests برای دانلود مستقیم از لینک PDF
                response = requests.get(result.pdf_url)
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"Successfully saved to {filename}")
            except Exception as e:
                print(f"Failed to download {result.title}: {e}")
        else:
            print(f"Already exists: {filename}")

print("عملیات به پایان رسید.")