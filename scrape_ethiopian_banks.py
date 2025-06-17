scrape_reviews.py
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
    
    for package_name, bank_name in BANK_APPS.i tems():
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
    # Check for missing data
print("\nMissing values per column:")
print(df.isnull().sum())
from google_play_scraper import app, Sort, reviews_all
import pandas as pd

def scrape_app_reviews(package_name, bank_name):
    reviews = reviews_all(
        package_name,
        sleep_milliseconds=1000,  # Avoid rate-limiting
        lang='en',                # Language
        country='et',             # Ethiopia
        sort=Sort.NEWEST,         # Get newest reviews first
    )
    
    df = pd.DataFrame(reviews)
    df['bank'] = bank_name
    df['source'] = 'Google Play'
    
    return df[['content', 'score', 'at', 'bank', 'source']].rename(columns={
        'content': 'review',
        'score': 'rating',
        'at': 'date'
    })

# Scrape 400+ reviews per bank
cbe_reviews = scrape_app_reviews('com.cbe.cbe', 'CBE')
awash_reviews = scrape_app_reviews('com.awashbank.mobilebanking', 'Awash Bank')
dashen_reviews = scrape_app_reviews('com.dashenmobile', 'Dashen Bank')

# Combine & save
all_reviews = pd.concat([cbe_reviews, awash_reviews, dashen_reviews])
all_reviews.to_csv('bank_reviews_raw.csv', index=False)

from google_play_scraper import reviews
import pandas as pd

bank_apps = {
    "BankA": "com.bankA.app",
    "BankB": "com.bankB.app",
    "BankC": "com.bankC.app"
}

all_reviews = []

for bank, package_name in bank_apps.items():
    result, _ = reviews(
        package_name,
        lang='en',
        country='us',
        count=410,  # Slightly more to cover duplicates/missing
        filter_score_with=None
    )
    for r in result:
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'],
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)
df.to_csv("data/raw/reviews_raw.csv", index=False)
# Check for missing data
print("\nMissing values per column:")
print(df.isnull().sum())
