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

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pristyn-scraper-api.git
cd pristyn-scraper-api
````

---

### 2️⃣ Install Requirements

Make sure you're using Python 3.8 or higher. Then install the dependencies:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the App

Start the Flask server with:

```bash
python app.py
```

Once running, open your browser and go to:

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 4️⃣ Use the Scraper

* Enter the Pristyn Care URL (`https://www.pristyncare.com`) into the input box
* Click **Start Scraping**
* Wait a few moments as it scrapes the full website data

✅ Step 1: Scrape all **Specialties**
✅ Step 2: Scrape **Treatments** under each category
✅ Step 3: Scrape **Doctors** listed under each treatment
✅ Step 4: Scrape detailed **Doctor Profiles**

---

### 5️⃣ Output

After scraping is complete, you'll get four downloadable Excel files:

📁 `output/specialties.xlsx`
📁 `output/treatments.xlsx`
📁 `output/doctors.xlsx`
📁 `output/profiles.xlsx`

These files will also be available as clickable download links directly in the web interface ✅


