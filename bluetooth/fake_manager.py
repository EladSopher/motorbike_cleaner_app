from bluetooth.base_manager import BluetoothManager
import time

class FakeBluetoothManager(BluetoothManager):
    def connect(self):
        print("Simulated Bluetooth connected")

    def send_command(self, command: str):
        print(f"Simulated sending: {command}")
        time.sleep(1)  # Simulate delay

    def read_response(self) -> str:
        time.sleep(2)  # Simulate processing time
        return "Simulated: Cleaning cycle complete"

    def disconnect(self):
        print("Simulated Bluetooth disconnected")
