import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_specialties(base_url, output_path):
    response = requests.get(base_url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    specialties = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        text = a_tag.get_text(strip=True)
        if "/c/" in href and text:
            specialties.add(text)

    df = pd.DataFrame(sorted(specialties), columns=["Specialty"])
    df.to_excel(output_path, index=False)
    print(f"✅ Saved {len(df)} specialties to {output_path}")
