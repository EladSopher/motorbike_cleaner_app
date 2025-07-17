from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.history_screen import HistoryScreen
from screens.status_screen import StatusScreen
from utils.history_log import HistoryLog
from kivy.core.window import Window
Window.size = (360, 640)  # Simulate typical phone screen (in dp)

class WindowManager(ScreenManager):
    pass

from kivy.lang import Builder
Builder.load_file("ui/widgets.kv")

class MotorbikeApp(App):
    def build(self):
        self.history = HistoryLog()
        sm = WindowManager()
        sm.add_widget(HomeScreen(name="home", history=self.history))
        sm.add_widget(StatusScreen(name="status"))
        sm.add_widget(HistoryScreen(name="history", history=self.history))
        return sm

if __name__ == '__main__':
    MotorbikeApp().run()