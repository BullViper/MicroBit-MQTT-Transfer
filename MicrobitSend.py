# micro:bit MicroPython - Radio Timer Sender
# A: start/stop toggle
# B: reset timer (when stopped)
# A+B: send elapsed time over radio (milliseconds + seconds)

from microbit import *
import radio

# --- Radio setup (match receiver channel/group as needed) ---
radio.config(channel=53, power=7, length=251)
radio.on()

# --- Timer state ---
running = False
start_ms = 0          # running start timestamp (ms)
elapsed_ms = 0        # accumulated elapsed time (ms)

def format_time(ms):
    # returns (seconds as float string, mm:ss.mmm)
    s = ms / 1000.0
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    millis = ms % 1000
    return "{:.3f}".format(s), "{:02d}:{:02d}.{:03d}".format(minutes, seconds, millis)

def update_display(ms):
    # show seconds (integer) while running/stopped, quick and readable
    display.show(str((ms // 1000) % 10))  # single digit to keep it snappy

# Optional: set a group if your receiver uses groups
# radio.config(group=1)  # uncomment if needed (note: group is for MakeCode radio; MicroPython uses channel)

# --- Main loop ---
while True:
    now = running_time()

    # Button A: start/stop toggle
    if button_a.was_pressed():
        if not running:
            running = True
            start_ms = now
            display.show("▶")   # start icon-ish
        else:
            # stop and accumulate
            elapsed_ms += now - start_ms
            running = False
            display.show("■")   # stop icon-ish
        sleep(200)  # debounce

    # Button B: reset (only when stopped)
    if button_b.was_pressed():
        if not running:
            elapsed_ms = 0
            display.show("0")
        else:
            display.show("!")   # indicate you can't reset while running
        sleep(200)

    # Buttons A+B: send current elapsed time over radio
    if button_a.is_pressed() and button_b.is_pressed():
        # compute current elapsed
        current_ms = elapsed_ms + (now - start_ms) if running else elapsed_ms
        sec_str, mmss_str = format_time(current_ms)

        # Send a compact payload; receiver can print/log it
        # Example: "TIMER ms=12345 s=12.345 mmss=00:12.345"
        payload = "TIMER ms={} s={} t={}".format(current_ms, sec_str, mmss_str)
        radio.send(payload)

        display.show("S")  # sent
        sleep(500)         # avoid repeated sends while holding
        display.clear()

    # Update display while running (or show last value when stopped)
    current_ms = elapsed_ms + (now - start_ms) if running else elapsed_ms
    update_display(current_ms)

    sleep(50)
