list2 = 0

def on_button_pressed_a():
    global list2
    list2 = 0
    led.plot(2, 3)
    basic.show_leds("""
        # # # . #
                # # # # .
                # . # . #
                . # . . .
                . # . # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
