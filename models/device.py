class Device:
    def __init__(self, ID, name, imei, uuid, manufacturer, model, imsi, androidId, simSerial, macAddress, facebook):
        self.ID = ID
        self.name = name
        self.imei = imei
        self.uuid = uuid
        self.manufacturer = manufacturer
        self.model = model
        self.imsi = imsi
        self.androidId = androidId
        self.simSerial = simSerial
        self.macAddress = macAddress
        self.facebook = facebook

    def display_info(self):
        print(f"Device ID: {self.ID}")
        print(f"Device Name: {self.name}")
        print(f"IMEI: {self.imei}")
