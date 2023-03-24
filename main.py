def on_button_pressed_a():
    robotbit.servo(robotbit.Servos.S6, 180)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S4, 90)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S5, 90)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S7, 90)
    basic.pause(200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    robotbit.servo(robotbit.Servos.S6, 90)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S5, 90)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S5, 90)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S7, 90)
    basic.pause(200)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    robotbit.servo(robotbit.Servos.S6, 0)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S4, 90)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S5, 90)
    basic.pause(200)
    robotbit.servo(robotbit.Servos.S7, 90)
    basic.pause(200)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("1")

def on_forever():
    pass
basic.forever(on_forever)
