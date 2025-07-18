import os
import json

class ThemeManager:
    def __init__(self):
        self.theme_file = os.path.join(os.path.dirname(__file__), "theme_config.json")
        self.current_theme = "light"
        self.load_theme()

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.save_theme()

    def save_theme(self):
        with open(self.theme_file, "w") as f:
            json.dump({"theme": self.current_theme}, f)

    def load_theme(self):
        if os.path.exists(self.theme_file):
            with open(self.theme_file, "r") as f:
                data = json.load(f)
                self.current_theme = data.get("theme", "light")

    def get_colors(self):
        if self.current_theme == "light":
            return {
                "bg_color": [1, 1, 1, 1],
                "text_color": [0, 0, 0, 1],
                "button_color": [.9, .9, .9, 1]
            }
        else:
            return {
                "bg_color": [0.1, 0.1, 0.1, 1],
                "text_color": [1, 1, 1, 1],
                "button_color": [0.2, 0.2, 0.2, 1]
            }
