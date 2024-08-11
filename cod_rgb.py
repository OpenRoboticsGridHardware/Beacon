import asyncio
import RPi.GPIO as GPIO
import websockets
import json

LED1_PINS = {'red': 17, 'green': 27, 'blue': 22}
LED2_PINS = {'red': 23, 'green': 24, 'blue': 25}
LED3_PINS = {'red': 5, 'green': 6, 'blue': 13}
GPIO.setmode(GPIO.BCM)
leds = []
for pins in [LED1_PINS, LED2_PINS, LED3_PINS]:
    GPIO.setup(pins['red'], GPIO.OUT)
    GPIO.setup(pins['green'], GPIO.OUT)
    GPIO.setup(pins['blue'], GPIO.OUT)
    
    leds.append({
        'red': GPIO.PWM(pins['red'], 1000),  
        'green': GPIO.PWM(pins['green'], 1000),
        'blue': GPIO.PWM(pins['blue'], 1000)
    })

for led in leds:
    led['red'].start(0)
    led['green'].start(0)
    led['blue'].start(0)

def set_color(r, g, b):
    """Set the color of all RGB LEDs.
    
    Args:
        r (int): Red value (0-255)
        g (int): Green value (0-255)
        b (int): Blue value (0-255)
    """
    for led in leds:
        led['red'].ChangeDutyCycle(r / 255 * 100)
        led['green'].ChangeDutyCycle(g / 255 * 100)
        led['blue'].ChangeDutyCycle(b / 255 * 100)

async def handler(websocket, path):
    async for message in websocket:
        try:
            # Parse the JSON message
            data = json.loads(message)
            r = data.get("red", 0)
            g = data.get("green", 0)
            b = data.get("blue", 0)
            
            # Set the color of the LEDs
            set_color(r, g, b)
            
            # Send an acknowledgment back to the client
            response = json.dumps({"status": "OK"})
            await websocket.send(response)
        except json.JSONDecodeError:
            print("Failed to decode JSON")
            response = json.dumps({"status": "Error", "message": "Invalid JSON"})
            await websocket.send(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = json.dumps({"status": "Error", "message": str(e)})
            await websocket.send(response)

start_server = websockets.serve(handler, "0.0.0.0", 8765)

try:
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
finally:
    for led in leds:
        led['red'].stop()
        led['green'].stop()
        led['blue'].stop()
    GPIO.cleanup()
