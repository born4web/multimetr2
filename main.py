def zobraz_teplotu():
    global teplota
    teplota = input.temperature()
    basic.show_string("" + str(teplota))
    basic.pause(2000)
    basic.clear_screen()
def zobraz_svetlo():
    global svetlost
    svetlost = input.light_level()
    basic.show_string("" + str(svetlost))
    basic.pause(2000)
    basic.clear_screen()

def on_button_pressed_a():
    global aktivni_prikaz
    aktivni_prikaz += 1
    if prikazy[aktivni_prikaz]:
        aktivni_prikaz = 0
    basic.show_string("")
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if aktivni_prikaz == 0:
        zobraz_teplotu()
    if aktivni_prikaz == 1:
        zobraz_svetlo()
    if aktivni_prikaz == 2:
        basic.show_string("TONIK")
input.on_button_pressed(Button.B, on_button_pressed_b)

aktivni_prikaz = 0
svetlost = 0
teplota = 0
prikazy: List[str] = []
prikazy = ["T", "S", "J"]
basic.show_icon(IconNames.HAPPY)
basic.pause(1000)
basic.clear_screen()