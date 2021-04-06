let distance = maqueen.Ultrasonic(PingUnit.Centimeters)
basic.forever(function () {
    if (distance >= 5) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 100)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 100)
    } else if (distance < 5) {
        maqueen.motorStop(maqueen.Motors.All)
        basic.showIcon(IconNames.Heart)
        music.playMelody("- G F - G C5 - - ", 120)
    }
})
