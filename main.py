distance = maqueen.ultrasonic(PingUnit.CENTIMETERS)

def on_forever():
    if distance > 20:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 100)
    else:
        if distance < 20:
            maqueen.motor_stop(maqueen.Motors.ALL)
            basic.show_icon(IconNames.HEART)
            music.play_melody("- G F - G C5 - - ", 120)
basic.forever(on_forever)
