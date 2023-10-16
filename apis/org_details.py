import requests

CLEARBIT_API_KEY = 'sk_d757a879f699c344bc11970e3efaf263'
def search_organization_details(domain):
    url = f'https://company.clearbit.com/v2/companies/find?domain={domain}'
    headers = {
        'Authorization': f'Bearer {CLEARBIT_API_KEY}',
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # Extract and print relevant organization details
            print(f"Name: {data['name']}")
            print(f"Domain: {data['domain']}")
            print(f"Description: {data['description']}")
            print(f"Location: {data['location']}")
            print(f"Employees: {data['metrics']['employees']}")

        elif response.status_code == 404:
            print(f"Organization with domain '{domain}' not found.")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
