#!/usr/bin/env python3


import pychromecast

print("Trying to find chromecasts")
chromecasts = pychromecast.get_chromecasts()

for cc in chromecasts:
    print(cc)
    print("\n")
exit()

cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Chromecast Device Name")
cast.wait()
mc = cast.media_controller


mc.play_media('http://webserver.local/sound/killer.mp3','audio/mpeg')
mc.block_until_active()

mc.stop()
