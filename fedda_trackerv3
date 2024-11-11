import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import facebook
import time
import threading

class FeddaTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fedda Tracker")
        self.root.geometry("400x200")
        
        # URL og tilgangstoken input
        tk.Label(root, text="Garmin URL:").pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()
        
        tk.Label(root, text="Facebook Access Token:").pack()
        self.token_entry = tk.Entry(root, width=50, show="*")
        self.token_entry.pack()
        
        # Start-knapp
        self.start_button = tk.Button(root, text="Start Tracking", command=self.start_tracking)
        self.start_button.pack(pady=10)
        
        # Status-label
        self.status_label = tk.Label(root, text="Status: Ikke startet")
        self.status_label.pack()

    def hent_posisjon(self, url):
        respons = requests.get(url)
        if respons.status_code == 200:
            soup = BeautifulSoup(respons.content, 'html.parser')
            latitude, longitude = "58.9700", "5.7331"  # Eksempelverdier
            return latitude, longitude
        else:
            return None, None

    def publiser_paa_facebook(self, tekst, access_token):
        graph = facebook.GraphAPI(access_token)
        graph.put_object(parent_object='me', connection_name='feed', message=tekst)

    def track_and_post(self):
        url = self.url_entry.get()
        access_token = self.token_entry.get()
        while True:
            latitude, longitude = self.hent_posisjon(url)
            if latitude and longitude:
                kartlenke = f"https://www.google.com/maps?q={latitude},{longitude}"
                self.publiser_paa_facebook(f'Min nåværende posisjon: {kartlenke}', access_token)
                self.status_label.config(text="Status: Posisjon publisert")
            time.sleep(43200)  # 12 timer

    def start_tracking(self):
        self.status_label.config(text="Status: Tracking pågår...")
        tracking_thread = threading.Thread(target=self.track_and_post)
        tracking_thread.daemon = True
        tracking_thread.start()

root = tk.Tk()
app = FeddaTrackerApp(root)
root.mainloop()
