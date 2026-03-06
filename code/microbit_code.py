moisture = 0
humidifier = 0

dry_threshold = 450
wet_threshold = 650

pump_on = False
water_level = 1
light_level = 0

def on_button_pressed_a():
    global humidifier
    humidifier = 1 - humidifier
    
    if humidifier == 1:
        pins.digital_write_pin(DigitalPin.P2, 1)
    else:
        pins.digital_write_pin(DigitalPin.P2, 0)

input.on_button_pressed(Button.A, on_button_pressed_a)


def on_forever():
    global moisture, pump_on, water_level, light_level
    
    # Read sensors
    moisture = pins.analog_read_pin(AnalogPin.P0)
    water_level = pins.digital_read_pin(DigitalPin.P3)
    light_level = input.light_level()

    # Display moisture value
    basic.show_number(moisture)
    
    # Night mode
    if light_level < 50:
        pins.digital_write_pin(DigitalPin.P1, 0)
        pump_on = False
        basic.show_icon(IconNames.ASLEEP)
        basic.pause(5000)
        return
    
    # Water tank empty protection
    if water_level == 0:
        pins.digital_write_pin(DigitalPin.P1, 0)
        pump_on = False
        basic.show_icon(IconNames.SKULL)
        basic.pause(5000)
        return

    # Moisture hysteresis control
    if moisture < dry_threshold and pump_on == False:
        pump_on = True
        
    if moisture > wet_threshold and pump_on == True:
        pump_on = False

    # Pump control
    if pump_on:
        pins.digital_write_pin(DigitalPin.P1, 1)
        
        # Pump animation
        basic.show_leds("""
            0 0 1 0 0
            0 1 1 1 0
            1 0 1 0 1
            0 0 1 0 0
            0 0 1 0 0
        """)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.show_icon(IconNames.HAPPY)

    # Pump delay
    basic.pause(8000)

basic.forever(on_forever)