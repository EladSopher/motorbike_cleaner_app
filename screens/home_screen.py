from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from bluetooth.fake_manager import FakeBluetoothManager
# from bluetooth.hc05_manager import HC05BluetoothManager

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bt = FakeBluetoothManager()

    def start_cleaning(self):
        self.ids.response_label.text = "Connecting to system..."
        Clock.schedule_once(self._step2_send_command, 1)

    def _step2_send_command(self, dt):
        self.bt.connect()
        self.ids.response_label.text = "Sending cleaning command..."
        self.bt.send_command("START_CLEANING")
        Clock.schedule_once(self._step3_read_response, 2)

    def _step3_read_response(self, dt):
        self.ids.response_label.text = "Cleaning in progress..."
        response = self.bt.read_response()
        self.bt.disconnect()
        Clock.schedule_once(lambda dt: self._show_final_response(response), 2)

    def _show_final_response(self, response):
        self.ids.response_label.text = response