import requests
from bs4 import BeautifulSoup


def fetch_names(start_url):
    base_url = "https://en.wikipedia.org"
    names = []
    url = start_url
    while url:
        print(f"Scraping: {base_url}{url}")
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, "html.parser")
        for li in soup.select("div.mw-category div.mw-category-group ul li"):
            name = li.get_text(strip=True)
            # Only add if it's a single word (skip "Category:" etc.)
            if name.isalpha():
                names.append(name)
        next_link = soup.find("a", string="next page")
        if next_link:
            url = next_link["href"]
        else:
            url = None
    return names


# Fetch Polish masculine given names
polish_names = fetch_names("/wiki/Category:Polish_masculine_given_names")
# Fetch English masculine given names
english_names = fetch_names("/wiki/Category:English_masculine_given_names")

# Combine, deduplicate, and sort
all_names = sorted(set(polish_names + english_names))

# Save to Python file
with open("names.py", "w", encoding="utf-8") as f:
    f.write("names = (\n")
    for name in all_names:
        f.write(f'    "{name}",\n')
    f.write(")\n")

print(f"Saved {len(all_names)} names to names.py")
