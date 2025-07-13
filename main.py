from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.home_screen import HomeScreen
from screens.history_screen import HistoryScreen

class WindowManager(ScreenManager):
    pass

from kivy.lang import Builder
Builder.load_file("ui/widgets.kv")

class MotorbikeApp(App):
    def build(self):
        sm = WindowManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(HistoryScreen(name="history"))
        return sm

if __name__ == '__main__':
    MotorbikeApp().run()