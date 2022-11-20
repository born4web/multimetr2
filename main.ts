function zobraz_teplotu () {
    teplota = input.temperature()
    basic.showString("" + teplota)
    basic.pause(2000)
    basic.clearScreen()
}
function zobraz_svetlo () {
    svetlost = input.lightLevel()
    basic.showString("" + svetlost)
    basic.pause(2000)
    basic.clearScreen()
}
input.onButtonPressed(Button.A, function () {
    aktivni_prikaz += 1
    if (prikazy[aktivni_prikaz]) {
        aktivni_prikaz = 0
    }
    basic.showString("")
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (aktivni_prikaz == 0) {
        zobraz_teplotu()
    }
    if (aktivni_prikaz == 1) {
        zobraz_svetlo()
    }
    if (aktivni_prikaz == 2) {
        basic.showString("TONIK")
    }
})
let aktivni_prikaz = 0
let svetlost = 0
let teplota = 0
let prikazy: string[] = []
prikazy = ["T", "S", "J"]
basic.showIcon(IconNames.Happy)
basic.pause(1000)
basic.clearScreen()
