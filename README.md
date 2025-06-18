# ✈️ Real-Time API driven Flight Radar Scanner

A Python-based radar-style GUI that visualizes nearby aircraft using real-time data from the [OpenSky Network](https://opensky-network.org/). The radar display includes dynamic sweep animation, polar positioning of flights, and callsign annotations.

---

## 📦 Features
- 📡 Live flight tracking from OpenSky API  
- 🧭 Accurate bearing and distance calculation using geodesic methods  
- 🗺️ Radar-style polar plot using `matplotlib` in a `tkinter` window  
- 🛬 Displays callsign, altitude, and origin country  
- 📝 CSV export of live airspace data  
- 🔄 Animated sweep simulation for radar realism  

---

## 📄 Sample CSV Data 

```csv
Callsign,Altitude (m),Country,ICAO,Longitude,Latitude
BG071,11277,Bangladesh,S2-ABL,90.4072,23.9833
BG122,10668,Bangladesh,S2-AEV,90.4511,24.0350
BG391,9144,Bangladesh,S2-AJH,90.3857,24.1502
BG435,11887,Bangladesh,S2-AHO,90.4221,24.2201
```

## 🛠️ Requirements

- Python 3.x  
- Required packages:

```bash
pip install matplotlib pandas geopy requests
```

## 🖼️ Screenshot

![Radar Scanner Screenshot](./Screenshot(115).png)

*Radar GUI displaying live flights around Dhaka, Bangladesh.*
