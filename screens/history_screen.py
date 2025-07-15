from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class HistoryScreen(Screen):
    def __init__(self, history=None, **kwargs):
        super().__init__(**kwargs)
        self.history = history
        self.current_filter = "all"  # Options: 'all', 'cleaning', 'oiling'

    def on_pre_enter(self):
        self.update_log_display()

    def set_filter(self, filter_type):
        self.current_filter = filter_type
        self.update_log_display()

    def update_log_display(self):
        log_entries = self.history.get_entries()
        self.ids.log_box.clear_widgets()

        # Filter entries
        filtered = [
            entry for entry in reversed(log_entries)
            if (
                    self.current_filter == "all" or
                    (self.current_filter == "error" and entry["action"].startswith("error")) or
                    entry["action"] == self.current_filter
            )
        ]

        for entry in filtered:
            action = entry['action']
            color = {
                "cleaning": "0000ff",  # blue
                "oiling": "ffaa00",  # yellow/orange
                "error_low_water": "ff0000"  # red
            }.get(action, "ffffff")  # default: white

            text = f"[color={color}]{entry['timestamp']} - {action.capitalize()}[/color]"

            self.ids.log_box.add_widget(
                Label(
                    text=text,
                    size_hint_y=None,
                    height=30,
                    font_size=16,
                    markup=True  # enable color markup
                )
            )