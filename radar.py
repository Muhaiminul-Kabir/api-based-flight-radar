import tkinter as tk
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from geopy.distance import geodesic
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time
# Set central radar position
CENTER_LAT,CENTER_LON= 23.9984,90.4223
# Load and process CSV targets



targets = []
def load_targets():
    df = pd.read_csv("dhaka_airspace_flights.csv")
    global targets
    for _, row in df.iterrows():
        lat, lon = row['Latitude'], row['Longitude']
        distance = geodesic((CENTER_LAT, CENTER_LON), (lat, lon)).km
        bearing = calculate_bearing((CENTER_LAT, CENTER_LON), (lat, lon))
        alt = row['Altitude (m)']
        targets.append({
            'callsign': row['Callsign'],
            'distance': distance,
            'bearing_rad': np.deg2rad(bearing),
            'alt': alt
        })

def calculate_bearing(start, end):
    lat1, lon1 = map(math.radians, start)
    lat2, lon2 = map(math.radians, end)
    delta_lon = lon2 - lon1

    x = math.sin(delta_lon) * math.cos(lat2)
    y = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(delta_lon)
    bearing = math.atan2(x, y)
    return (math.degrees(bearing) + 360) % 360

# Setup radar GUI with animation
class RadarGUI:
    def __init__(self, root, targets):
        
        if targets:
            self.targets = targets
       
        self.root = root
        self.root.title("Radar Display")

        self.fig = plt.Figure(figsize=(6, 6), facecolor='black')
        self.ax = self.fig.add_subplot(111, polar=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.ax.set_facecolor('black')
        self.ax.set_theta_zero_location('N')
        self.ax.set_theta_direction(-1)
        if targets:
            self.ax.set_rmax(max(t['distance'] for t in targets) + 1)

        self.ax.grid(color='green', linestyle='--', linewidth=0.5)
        self.ax.tick_params(colors='green')
        self.ax.spines['polar'].set_color('green')

        # Plot persistent targets
        if targets:
            for t in self.targets:
                self.ax.plot(t['bearing_rad'], t['distance'], 'go')  # green dot
                self.ax.text(t['bearing_rad'], t['distance'] + 0.1, t['callsign']+"\n"+str(int(t['distance']))+'km away\n↑'+str(t['alt']), color='red', fontsize=7, va='top',ha='center')
        # Radar sweep line (initially zero)
        self.sweep_line, = self.ax.plot([], [], color='green', linewidth=1.5)

        self.angle = 0
        self.anim = FuncAnimation(self.fig, self.update, frames=np.linspace(0, 2*np.pi, 360), interval=20, blit=False)

    def update(self, frame):
        self.angle = frame
        self.sweep_line.set_data([self.angle, self.angle], [0, self.ax.get_rmax()])
        return self.sweep_line



def GUI_thread():
    global targets
    root = tk.Tk()
    app = RadarGUI(root, targets)
    root.mainloop()
def data_thread():
    while(1):
        print("refreshing data...")
        load_targets()
        time.sleep(10)




# Load targets and run GUI
if __name__ == "__main__":
    t2 = threading.Thread(target=data_thread, args=())
    t1 = threading.Thread(target=GUI_thread, args=())

    t1.start()
    t2.start()

