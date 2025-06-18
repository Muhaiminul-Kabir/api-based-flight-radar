import requests
import csv


# Define the bounding box parameters
params = {
    "lamin": 23.924438,
    "lamax": 24.371363,
    "lomin": 90.064959,
    "lomax": 90.758423
}

url = "https://opensky-network.org/api/states/all"
res = requests.get(url, params=params)

if res.status_code == 200:
    data = res.json()
    flights = data.get("states", [])

    # Print header
    print("Callsign | Altitude | Country")

    # Write to CSV
    with open("dhaka_airspace_flights.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Callsign", "Altitude (m)", "Country", "ICAO", "Longitude", "Latitude"])
        try:
            for s in flights:
                callsign = s[1].strip() if s[1] else "N/A"
                altitude = s[7] if s[7] is not None else "N/A"
                country = s[2] or "N/A"
                icao = s[0]
                lon = s[5]
                lat = s[6]
                print(f"{callsign} | {altitude} | {country} | {lat} | {lon}")
                writer.writerow([callsign, altitude, country, icao, lon, lat])
        except:
            print("No flights in range")
else:
    print(f"Failed to fetch data: {res.status_code}")
