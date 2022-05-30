# elkbledom-ha
Home Assistant integration for LED STRIP NAME ELK BLEDOM with app Duoco Strip

Supports controlling BLE based lights in HA

## Installation

### [HACS](https://hacs.xyz/) (recommended)

Installation can be done through [HACS custom repository](https://hacs.xyz/docs/faq/custom_repositories).

### Manual installation

You can manually clone this repository inside `config/custom_components/` HA folder.

## Setup

After installation, you should find elkbledom under the Configuration -> Integrations -> Add integration.

The setup step includes discovery which will list out all ELK BLEDOM lights discovered. The setup will validate connection by toggling the selected light. Make sure your light is in-sight to validate this.

The setup needs to be repeated for each light.

## Features
Discovery: Automatically discover ELK BLEDOM based lights without manually hunting for Bluetooth MAC address

On/Off/RGB/Brightness support

Emulated RGB brightness: Supports adjusting brightness of RGB lights

Multiple light support

## Not supported

Live state polling: External control (i.e. IR remote) state changes will reflect in Home Assistant

[Light modes] (blinking, fading, etc) is not yet supported.

## Known issues

1. Live state polling dont work.

3. Code in Work, not finnished, i am waiting for status write value:

            ```
            
            future = asyncio.get_event_loop().create_future()
            await self._device.start_notify(self._read_uuid, create_status_callback(future))
            # PROBLEMS WITH STATUS VALUE, I HAVE NOT VALUE TO WRITE AND GET STATUS
            await self._write(bytearray([0xEF, 0x01, 0x77]))
            await asyncio.wait_for(future, 5.0)
            await self._device.stop_notify(self._read_uuid)
            
            ```

## Credits
This integration will not be possible without the awesome work of this github repositories:

https://github.com/sysofwan/ha-triones

https://github.com/TheSylex/ELK-BLEDOM-bluetooth-led-strip-controller/

https://github.com/FreekBes/bledom_controller/

https://github.com/FergusInLondon/ELK-BLEDOM/

https://github.com/arduino12/ble_rgb_led_strip_controller

https://github.com/lilgallon/DynamicLedStrips

https://github.com/kquinsland/JACKYLED-BLE-RGB-LED-Strip-controller

https://linuxthings.co.uk/blog/control-an-elk-bledom-bluetooth-led-strip