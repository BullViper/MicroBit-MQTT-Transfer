# micro:bit MicroPython - Radio Receiver -> Serial
# Receives text over radio and writes it to USB serial

from microbit import *
import radio

# --- Radio setup (MUST match the sender) ---
radio.config(channel=53, power=7, length=251)
radio.on()

display.show("R")  # Receiver ready

while True:
    msg = radio.receive()
    if msg:
        # Write to serial (newline-terminated for easy reading)
        serial.write_line(msg)

        # Optional visual feedback
        display.show("•")
        sleep(100)
        display.clear()

    sleep(20)
