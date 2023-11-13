import requests

# API key read from hidden file not in git repository
with open("apis/.org_clearbit_secrets", "r") as file:
    CLEARBIT_API_KEY  = file.read().rstrip()

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
            return '\n'.join([
            f"Name: {data['name']}",
            f"Domain: {data['domain']}",
            f"Description: {data['description']}",
            f"Location: {data['location']}",
            f"Employees: {data['metrics']['employees']}"])

        elif response.status_code == 404:
            print(f"Organization with domain '{domain}' not found.")

        else:
            return (f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        return (f"An error occurred: {str(e)}")

