import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Temperature C:", cpx.temperature)
    print((cpx.temperature),)
    time.sleep(1)
