from flask import Flask, request, render_template, redirect, url_for, send_file, jsonify
import os
import traceback
from scraper.step1_specialties import scrape_specialties
from scraper.step2_treatments import scrape_treatments
from scraper.step3_doctors import scrape_doctors_by_treatment
from scraper.step4_profiles import scrape_doctor_profiles

app = Flask(__name__)
OUTPUT_DIR = "output"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return render_template("index.html", error="Please enter a valid URL.")

        try:
            os.makedirs(OUTPUT_DIR, exist_ok=True)

            print("✅ Step 1: Scraping specialties...")
            scrape_specialties(url, os.path.join(OUTPUT_DIR, "specialties.xlsx"))

            print("✅ Step 2: Scraping treatments...")
            scrape_treatments(url, os.path.join(OUTPUT_DIR, "treatments.xlsx"))

            print("✅ Step 3: Scraping doctors by treatment...")
            scrape_doctors_by_treatment(
                os.path.join(OUTPUT_DIR, "treatments.xlsx"),
                os.path.join(OUTPUT_DIR, "doctors.xlsx")
            )

            print("✅ Step 4: Scraping doctor profiles...")
            scrape_doctor_profiles(
                os.path.join(OUTPUT_DIR, "doctors.xlsx"),
                os.path.join(OUTPUT_DIR, "profiles.xlsx")
            )

            # Check all files exist before offering download
            all_paths = [
                "specialties.xlsx",
                "treatments.xlsx",
                "doctors.xlsx",
                "profiles.xlsx"
            ]
            for name in all_paths:
                if not os.path.exists(os.path.join(OUTPUT_DIR, name)):
                    raise FileNotFoundError(f"{name} was not created.")

            return render_template("index.html", download_link="/download/all")

        except Exception as e:
            print("❌ Scraping error:", e)
            traceback.print_exc()
            return render_template("index.html", error=f"Scraping failed: {e}")

    return render_template("index.html")

@app.route("/download/all")
def download_all():
    zip_path = os.path.join(OUTPUT_DIR, "pristyn_data.zip")
    import zipfile

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for name in ["specialties.xlsx", "treatments.xlsx", "doctors.xlsx", "profiles.xlsx"]:
            full_path = os.path.join(OUTPUT_DIR, name)
            if os.path.exists(full_path):
                zipf.write(full_path, arcname=name)

    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
