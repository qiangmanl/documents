import network
import time
test_id="CMCC-K6A6"
test_pw="15859105442"
try_connect_times=10

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()


def connect_wifi_with(times):
    for in range(times):
        wlan.connect(test_id, test_pw)
        if wlan.isconnected():
            return True
        time.sleep(1)
    return Flase
connect_wifi_with(try_connect_times)
if not connect_wifi_with(try_connect_times):
    exit()
else:
    print(f'success connected with wifi:{test_id},ip_set:{wlan.ifconfig()}')
