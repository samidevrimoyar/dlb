import requests
import sys

BASE_URL = "http://127.0.0.1:8000/api"
EMAIL = "test@superisi.net"
PASSWORD = "securepassword123"

def run_test():
    # 1. Login
    print("Logging in...")
    resp = requests.post(f"{BASE_URL}/users/login/", json={"email": EMAIL, "password": PASSWORD})
    if resp.status_code != 200:
        print("Login failed", resp.text)
        sys.exit(1)
    
    tokens = resp.json()
    access_token = tokens['access']
    headers = {"Authorization": f"Bearer {access_token}"}
    print("Login success.")

    # 2. Create Trip
    print("Creating Trip...")
    trip_data = {
        "name": "Aegean Adventure",
        "status": "active"
    }
    resp = requests.post(f"{BASE_URL}/logbook/trips/", json=trip_data, headers=headers)
    if resp.status_code != 201:
        print("Create trip failed", resp.text)
        sys.exit(1)
    trip = resp.json()
    print(f"Trip created: {trip['id']} - {trip['name']}")

    # 3. Create Entry
    print("Creating Logbook Entry...")
    entry_data = {
        "trip": trip['id'],
        "timestamp": "2023-10-27T10:00:00Z",
        "latitude": "38.4237",
        "longitude": "27.1428",
        "sog": 5.5,
        "cog": 180.0,
        "notes": "Leaving the marina."
    }
    resp = requests.post(f"{BASE_URL}/logbook/entries/", json=entry_data, headers=headers)
    if resp.status_code != 201:
        print("Create entry failed", resp.text)
        sys.exit(1)
    entry = resp.json()
    print(f"Entry created: {entry['id']} at {entry['latitude']}, {entry['longitude']}")

    # 4. List Entries
    print("Listing Entries...")
    resp = requests.get(f"{BASE_URL}/logbook/entries/", headers=headers)
    entries = resp.json()
    print(f"Total entries: {len(entries)}")

if __name__ == "__main__":
    run_test()
