import requests
import json

def check_pwned_data(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "User-Agent": "Your App Name",
        "hibp-api-key": "YOUR_API_KEY"  # Get your API key from https://haveibeenpwned.com/API/Key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"Your data has been leaked in {len(data)} platforms:")
        for breach in data:
            print(f"- {breach['Title']}")
            print("\tData classes: ", ", ".join(breach["DataClasses"]))
            print("\tBreach date: ", breach["BreachDate"])
            print("\tDescription: ", breach["Description"])
            print("\tIs verified by HIBP: ", breach["IsVerified"])
            print("\tIs sensitive: ", breach["IsSensitive"])
            print("\tIs retired: ", breach["IsRetired"])
            print("\tPwnCount: ", breach["PwnCount"])
    elif response.status_code == 404:
        print("No breached data found for this email.")
    else:
        print("Error occurred while checking for breached data.")

def capture_leaked_data(email):
    url = f"https://haveibeenpwned.com/api/v3/pasteaccount/{email}"
    headers = {
        "User-Agent": "Your App Name",
        "hibp-api-key": "YOUR_API_KEY"  # Get your API key from https://haveibeenpwned.com/API/Key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"Leaked data found in pastes:")
        for paste in data:
            print(f"- Source: {paste['Source']}")
            print(f"  Date: {paste['Date']}")
            print(f"  Title: {paste['Title']}")
            print(f"  EmailCount: {paste['EmailCount']}")
    elif response.status_code == 404:
        print("No leaked data found in pastes.")
    else:
        print("Error occurred while checking for leaked data in pastes.")

if __name__ == "__main__":
    email = input("Enter the email address to check for data breaches: ")
    check_pwned_data(email)
    capture_leaked_data(email)
