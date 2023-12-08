import network
test_id="CMCC-K6A6"
test_pw="15859105442"
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()