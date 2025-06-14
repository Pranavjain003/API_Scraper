# 🏥 Pristyn Care Web Scraper API

A Python Flask-based API that scrapes treatment, doctor, and profile data from [Pristyn Care](https://www.pristyncare.com). You simply input the base URL, and the scraper will generate downloadable Excel files containing structured medical data.

---

## 📌 Features

- ✅ Extracts **specialties** listed on homepage
- ✅ Scrapes **treatments** under each specialty
- ✅ Scrapes **doctors** listed per treatment
- ✅ Extracts **full doctor profile** info from each doctor page
- ✅ Returns **Excel files** for download via a simple web interface

---

## 📁 Output Files

After scraping, the following Excel files will be generated:

- `specialties.xlsx`: List of all medical specialties offered
- `treatments.xlsx`: All treatments with links
- `doctors.xlsx`: Doctors associated with each treatment
- `profiles.xlsx`: Full doctor profiles (name, about, registration, education, treatments, etc.)

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pristyn-scraper-api.git
cd pristyn-scraper-api
