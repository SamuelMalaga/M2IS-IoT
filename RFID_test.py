import serial
PortRF = serial.Serial('/dev/ttyAMA0',9600)

while True:
    ID = ""
    read_byte = PortRF.read()
    if read_byte ==b"\x02":
        for i in range (0,12):
            read_byte=PortRF.read()
            ID += read_byte.decode('utf-8')

    print(ID)