class BluetoothManager:
    def connect(self):
        raise NotImplementedError

    def send_command(self, command: str):
        raise NotImplementedError

    def read_response(self) -> str:
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError