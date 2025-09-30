import serial
PortRF = serial.Serial('/dev/ttyAMA0',9600)

access_dict = {
    "5A0083F23C17":"MR Bean",
    "5B00AE4FEA50": "Ahmad",
    "5C009D668621": "Samuel"
}

while True:
    ID = ""
    read_byte = PortRF.read()
    if read_byte ==b"\x02":
        for i in range (0,12):
            read_byte=PortRF.read()
            ID += read_byte.decode('utf-8')
    if ID in access_dict.keys():
        print("Registered user")
        if access_dict.get(ID) == "MR Bean":
            print("Hello Mr Bean, you're allowed to access")
        else:
            print(f"Sorry Mr.{access_dict.get(ID)}, youre not allowed to access")
