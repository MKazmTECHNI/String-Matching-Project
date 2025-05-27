import requests
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org"
start_url = "/wiki/Category:English-language_surnames"
english_surnames = []

url = start_url
while url:
    print(f"Scraping: {base_url}{url}")
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract surnames from the current page
    for li in soup.select("div.mw-category div.mw-category-group ul li"):
        surname = li.get_text(strip=True)
        english_surnames.append(surname)

    # Find the "next page" link
    next_link = soup.find("a", text="next page")
    if next_link:
        url = next_link["href"]
    else:
        url = None

# Now, read your existing Polish surnames
from surnames import surnames as polish_surnames

# Combine and deduplicate
all_surnames = tuple(sorted(set(polish_surnames) | set(english_surnames)))

# Save to surnames.py
with open("surnames.py", "w", encoding="utf-8") as f:
    f.write("surnames = (\n")
    for surname in all_surnames:
        f.write(f'    "{surname}",\n')
    f.write(")\n")

print(f"Saved {len(all_surnames)} surnames (Polish + English) to surnames.py")
