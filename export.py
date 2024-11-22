import requests
import csv

url = 'https://geofeed.constant.com/'

output_file = 'ips.txt'

country_codes = {"NL", "DE", "PL", "GB"}

headers = {
    'User-Agent': 'FXtelekom IP Crawler (Contact: contact@fxtelekom.org)',
    'Accept': 'text/csv'
}

response = requests.get(url)

def main():
    if response.status_code == 200:
        data = response.text.splitlines()
        
        with open(output_file, 'w') as outfile:
            reader = csv.reader(data)
            for row in reader:
                if len(row) > 1 and row[1] in country_codes:
                    outfile.write(f"{row[0]}\n")
        print(f"IPcímek a {', '.join(country_codes)} országoknak elmentve: {output_file}")
    else:
        print(f"Hiba történt az IP lista letöltéskor: {response.status_code}")

if __name__ == "__main__":
    main()