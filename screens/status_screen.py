from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
import random

class StatusScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_event = None  # Keep reference to auto-updater

    def on_pre_enter(self):
        self.refresh_status()
        self.refresh_event = Clock.schedule_interval(self.refresh_status, 1)

    def on_leave(self):
        if self.refresh_event:
            self.refresh_event.cancel()
            self.refresh_event = None

    def refresh_status(self, *args):
        # Simulated sensor values
        water_level = random.randint(0, 100)  # in mL
        speed = random.randint(0, 40)         # in km/h

        # --- Water Level Display ---
        if water_level > 50:
            water_color = "00ff00"  # Green
            water_status = "OK"
        elif 10 <= water_level <= 50:
            water_color = "ffaa00"  # Yellow
            water_status = "Low"
        else:
            water_color = "ff0000"  # Red
            water_status = "Too Low!"

        self.ids.water_label.text = f"[color={water_color}]Water Level: {water_level} mL - {water_status}[/color]"
        self.ids.water_label.markup = True

        # --- Speed Display ---
        if speed > 20:
            speed_color = "00ff00"
            speed_status = "OK"
        elif 5 <= speed <= 20:
            speed_color = "ffaa00"
            speed_status = "Too Low"
        else:
            speed_color = "ff0000"
            speed_status = "Critical!"

        self.ids.speed_label.text = f"[color={speed_color}]Speed: {speed} km/h - {speed_status}[/color]"
        self.ids.speed_label.markup = True