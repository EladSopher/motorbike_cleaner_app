from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class HistoryScreen(Screen):
    def __init__(self, history=None, **kwargs):
        super().__init__(**kwargs)
        self.history = history
        self.current_filter = "all"  # Options: 'all', 'cleaning', 'oiling'

    def on_pre_enter(self):
        self.update_log_display()
        self.ids.export_status.text = ""  # ✅ clear status when entering

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

    def export_log_to_csv(self):
        filepath = self.history.export_to_csv()
        self.ids.export_status.text = f"Exported to: {filepath}"

    def clear_log(self):
        # Inner function: called if user confirms
        def confirm_clear(instance):
            self.history.clear_history()
            self.update_log_display()
            self.ids.export_status.text = "History cleared."
            popup.dismiss()

        # Inner function: cancel action
        def cancel(instance):
            popup.dismiss()

        # Create popup content
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Label(text="Are you sure you want to clear the history?"))

        buttons = BoxLayout(spacing=10, size_hint_y=None, height=50)
        btn_cancel = Button(text="Cancel", on_release=cancel)
        btn_clear = Button(text="Clear", on_release=confirm_clear)
        buttons.add_widget(btn_cancel)
        buttons.add_widget(btn_clear)

        layout.add_widget(buttons)

        popup = Popup(title="Confirm Clear", content=layout,
                      size_hint=(None, None), size=(400, 200))
        popup.open()