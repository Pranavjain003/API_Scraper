import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_doctor_profiles(input_excel_file, output_excel_file):
    df = pd.read_excel(input_excel_file)
    unique_urls = df["Doctor URL"].drop_duplicates()

    all_data = []
    seen = set()

    for url in unique_urls:
        if url not in seen:
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.content, 'html.parser')
                data = {"url": url}

                h1 = soup.find("h1")
                data["name"] = h1.get_text(strip=True) if h1 else None

                about_heading = soup.find("h3", class_="doctorDetailsHeading", string=lambda x: x and "About" in x)
                if about_heading:
                    para = about_heading.find_next("p")
                    about_text = para.get_text(separator=" ", strip=True) if para else None
                    if about_text and "Read More" in about_text:
                        about_text = about_text.replace("Read More", "").strip()
                    data["about"] = about_text
                else:
                    data["about"] = None

                reg_heading = soup.find("h3", string=lambda x: x and "Medical Registration" in x)
                if reg_heading:
                    reg_div = reg_heading.find_next("div", class_="registrationDetailsContainer")
                    reg_text = reg_div.get_text(strip=True) if reg_div else None
                    if reg_text:
                        reg_fixed = re.sub(r"([a-zA-Z])(\d)", r"\1 \2", reg_text)
                        data["registration"] = reg_fixed
                    else:
                        data["registration"] = None
                else:
                    data["registration"] = None

                data["education"] = []
                edu_ul = soup.find("ul", class_="doctorDetailsDataContainer")
                if edu_ul:
                    for li in edu_ul.find_all("li"):
                        span = li.find("span")
                        if span:
                            data["education"].append(span.get_text(strip=True))

                data["treatments"] = []
                treat_ul = soup.find("ul", class_="doctorInterlinkingDetails")
                if treat_ul:
                    for li in treat_ul.find_all("li"):
                        a = li.find("a")
                        if a:
                            data["treatments"].append(a.get_text(strip=True))

                all_data.append(data)
                seen.add(url)

            except Exception as e:
                all_data.append({"url": url, "error": str(e)})

    df_final = pd.DataFrame(all_data)
    df_final.to_excel(output_excel_file, index=False)
    print(f"✅ Saved doctor profiles to {output_excel_file}")
