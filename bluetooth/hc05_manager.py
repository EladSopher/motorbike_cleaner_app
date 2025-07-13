import serial
import time
from bluetooth.base_manager import BluetoothManager

class HC05BluetoothManager(BluetoothManager):
    def __init__(self, port='COM5', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        self.connection = serial.Serial(self.port, self.baudrate, timeout=2)
        time.sleep(2)  # Wait for Arduino reset

    def send_command(self, command: str):
        if self.connection:
            self.connection.write((command + '\n').encode())

    def read_response(self) -> str:
        if self.connection and self.connection.in_waiting:
            return self.connection.readline().decode().strip()
        return ""

    def disconnect(self):
        if self.connection:
            self.connection.close()