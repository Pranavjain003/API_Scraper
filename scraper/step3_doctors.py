import requests
from bs4 import BeautifulSoup
import pandas as pd

# This function scrapes all doctors for each treatment and stores the output in an Excel file.
def scrape_doctors_by_treatment(treatment_excel_file, output_excel_file):
    df = pd.read_excel(treatment_excel_file)
    all_doctors = []

    seen_urls = set()  # to avoid duplicate doctor URLs

    for _, row in df.iterrows():
        treatment = row["Treatment"]
        url = row["URL"]

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")

            for a in soup.find_all("a", href=True):
                href = a["href"]
                name = a.get_text(strip=True)
                if "/specialist/" in href and name:
                    full_url = requests.compat.urljoin(url, href)
                    if full_url not in seen_urls:
                        seen_urls.add(full_url)
                        all_doctors.append({
                            "Treatment": treatment,
                            "Doctor Name": name,
                            "Doctor URL": full_url
                        })

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

    doctor_df = pd.DataFrame(all_doctors)
    doctor_df.to_excel(output_excel_file, index=False)
    print(f"✅ Saved {len(doctor_df)} unique doctors to {output_excel_file}")
