from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from bluetooth.fake_manager import FakeBluetoothManager

class HomeScreen(Screen):
    def __init__(self, history=None, **kwargs):
        super().__init__(**kwargs)
        self.bt = FakeBluetoothManager()
        self.history = history

    def start_error(self, error_type="error_low_water", message="Simulated error: Water too low"):
        self.ids.response_label.text = message
        self.history.add_entry(error_type)

    def start_cleaning(self):
        self.ids.response_label.text = "Connecting to system..."
        Clock.schedule_once(self._step2_send_cleaning_command, 1)

    def _step2_send_cleaning_command(self, dt):
        self.bt.connect()
        self.ids.response_label.text = "Sending cleaning command..."
        self.bt.send_command("START_CLEANING")
        Clock.schedule_once(self._step3_cleaning_read_response, 2)

    def _step3_cleaning_read_response(self, dt):
        self.ids.response_label.text = "Cleaning in progress..."
        response = self.bt.read_response()
        self.bt.disconnect()
        Clock.schedule_once(lambda dt: self._show_final_response(response, "cleaning"), 2)

    def start_oiling(self):
        self.ids.response_label.text = "Connecting to system..."
        Clock.schedule_once(self._step2_send_oil_command, 1)

    def _step2_send_oil_command(self, dt):
        self.bt.connect()
        self.ids.response_label.text = "Sending oiling command..."
        self.bt.send_command("START_OILING")
        Clock.schedule_once(self._step3_oil_read_response, 2)

    def _step3_oil_read_response(self, dt):
        self.ids.response_label.text = "Oiling in progress..."
        response = "Simulated oiling cycle complete"
        self.bt.disconnect()
        Clock.schedule_once(lambda dt: self._show_oiling_final_response(response, "oiling"), 2)

    def _show_final_response(self, response, action_type):
        self.ids.response_label.text = response
        self.history.add_entry(action_type)
