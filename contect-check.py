from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.aljazeera.com/')
soup = BeautifulSoup(response.text, 'html.parser')

print("=== AL JAZEERA CONTENT ANALYSIS ===")

# 1. Website Title
title = soup.title.string
print(f"Website Title: {title}")

# 2. Header Navigation Links
header = soup.find('header') or soup.find('nav')
print("\nHeader Navigation:")
if header:
   header_links = header.find_all('a', href=True)
   for link in header_links:
       if link.text.strip() and len(link.text.strip()) < 20:
           print(f"  - {link.text.strip()}")
else:
   print("  Header navigation not found")

# 3. Article Headlines/Names
headlines = soup.find_all(['h1', 'h2', 'h3'])
print(f"\nArticles Found ({len(headlines)} total):")
article_count = 0
for headline in headlines:
   if headline.text.strip() and len(headline.text.strip()) > 10:
       print(f"  {article_count + 1}. {headline.text.strip()}")
       article_count += 1
       if article_count >= 5:  # Show only first 5 articles
           break

# 4. Basic Content
images = soup.find_all('img')
print(f"\nTotal Images: {len(images)}")
print(f"Total Headlines: {len(headlines)}")
