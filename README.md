# bank-reviews-analysis-task1
# data collection and processing step
# Ethiopian Banks App Review Analysis

## Methodology

- **Scraping**: Used `google-play-scraper` to collect 400+ reviews each for:
  - Commercial Bank of Ethiopia (com.combanketh)
  - Bank of Abyssinia (com.boa.bankapp)
  - Dashen Bank (com.m2i.dashen)

- **Preprocessing**:
  - Removed duplicate reviews.
  - Normalized dates to `YYYY-MM-DD`.
  - Filtered missing data.

- **Output**:
  - `bank_reviews_raw.csv` (raw scrape)
  - `bank_reviews_clean.csv` (final cleaned data)

