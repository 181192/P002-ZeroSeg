import socket
import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.led_matrix.virtual import sevensegment
from luma.core.serial import spi, noop
from luma.core.virtual import viewport

def show_message_vp(device, msg, delay=0.6):
    # Implemented with virtual viewport
    width = device.width
    padding = " " * width
    msg = padding + msg + padding
    n = len(msg)

    virtual = viewport(device, width=n, height=8)
    sevensegment(virtual).text = msg
    for i in reversed(list(range(n - width))):
        virtual.set_position((i, 0))
        time.sleep(delay)


def clock(seg, seconds):
    """
    Display current time on device.
    """
    interval = 0.5
    for i in range(int(seconds / interval)):
        now = datetime.now()
        seg.text = now.strftime("%H-%M-%S")

        # calculate blinking dot
        if i % 2 == 0:
            seg.text = now.strftime("%H-%M-%S")
        else:
            seg.text = now.strftime("%H %M %S")

        time.sleep(interval)

def getIp():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        ip = s.getsockname()[0]
        s.close()
        return ip

def main():
	# create seven segment device
	serial = spi(port=0, device=0, gpio=noop())
	device = max7219(serial, cascaded=1)
	seg = sevensegment(device)

	show_message_vp(device, getIp())

    	clock(seg, seconds=60)

if __name__ == '__main__':
	main()
