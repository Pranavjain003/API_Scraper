import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

def scrape_treatments(base_url, output_path):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")

    treatments = []

    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        text = a_tag.get_text(strip=True)
        if "/treatment/" in href and text:
            full_url = urljoin(base_url, href)
            treatments.append((text, full_url))

    df = pd.DataFrame(treatments, columns=["Treatment", "URL"]).drop_duplicates()
    df.to_excel(output_path, index=False)
    print(f"✅ Saved {len(df)} treatments to {output_path}")
