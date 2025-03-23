from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class MyWrapper(EWrapper):
    def __init__(self):
        super().__init__()
    def nextValidId(self, orderId: int):
        print(f"Next valid order ID: {orderId}")

    def error(self, reqId: int, errorCode: int, errorString: str):
        print(f"Error: {errorCode}, Message: {errorString}")

class Myclient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

app = Myclient(MyWrapper())
app.connect("127.0.0.1", 7497, clientId=1)
app.run()