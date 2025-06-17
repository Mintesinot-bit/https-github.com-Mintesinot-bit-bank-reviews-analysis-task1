print ("hello world!")

from google_play_scraper import reviews_all, Sort
import pandas as pd
from datetime import datetime

# Updated bank apps with correct package names
BANK_APPS = {
    'com.combanketh.mobilebanking': 'CBE',
    'com.boa.boaMobileBanking': 'Bank of Abyssinia',
    'com.dashen.dashensuperapp': 'Dashen Bank'
}

def scrape_bank_reviews():
    all_reviews = []
    
    for package_name, bank_name in BANK_APPS.items():
        print(f"Scraping reviews for {bank_name} ({package_name})...")
        
        # Get reviews (400 per bank)
        reviews = reviews_all(
            package_name,
            lang='en',          # English reviews
            country='et',       # Ethiopia
            sort=Sort.NEWEST,   # Get newest first
            sleep_milliseconds=1000,  # Delay between requests
        )
        
        # Extract key data points
        for review in reviews[:400]:  # Limit to 400 per bank
            all_reviews.append({
                'review_text': review['content'],
                'star_rating': review['score'],
                'date_posted': datetime.fromisoformat(review['at'].replace('Z', '+00:00')).strftime('%Y-%m-%d'),
                'app_name': bank_name
            })
    
    return pd.DataFrame(all_reviews)

if __name__ == "__main__":
    # Scrape and save data
    df = scrape_bank_reviews()
    df.to_csv('ethiopian_bank_reviews.csv', index=False)
    print(f"Successfully saved {len(df)} reviews to 'ethiopian_bank_reviews.csv'")
    print("\nSample data:")
    print(df.head())  # Preview first 5 rows

./venv/Scripts/python.exe)

import pandas as pd

df = pd.read_csv("data/raw/reviews_raw.csv")

# Remove duplicates
df = df.drop_duplicates(subset=["review", "bank"])

# Handle missing data (<5% allowed)
missing_before = df.isnull().mean()
df = df.dropna(subset=["review", "rating", "date", "bank"])

# Normalize date
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Save cleaned data
df = df[["review", "rating", "date", "bank", "source"]]
df.to_csv("data/processed/reviews_clean.csv", index=False)

print(f"Missing data before cleaning:\n{missing_before}")

import pandas as pd

df = pd.read_csv("data/raw/reviews_raw.csv")

# Remove duplicates
df = df.drop_duplicates(subset=["review", "bank"])

# Handle missing data (<5% allowed)
missing_before = df.isnull().mean()
df = df.dropna(subset=["review", "rating", "date", "bank"])

# Normalize date
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Save cleaned data
df = df[["review", "rating", "date", "bank", "source"]]
df.to_csv("data/processed/reviews_clean.csv", index=False)

print(f"Missing data before cleaning:\n{missing_before}")
print(f"Rows after cleaning: {len(df)}")
scripts/scrape_reviews.py
