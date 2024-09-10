print("Starting")


import busio
import board
from kmk.kmk_keyboard import KMKKeyboard; keyboard = KMKKeyboard()
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.holdtap import HoldTap; keyboard.modules.append(HoldTap())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.adxl345 import adxl345
from kmk.modules.macros import Macros

from kmk.hid import HIDModes
from kmk.hid import BLEHID


from kmk.handlers.stock import passthrough
macros = Macros()
keyboard.modules.append(macros)

adxl = adxl345()
keyboard.modules.append(adxl)

def stepReport(*args, **kwargs):
    temp = "You have walked: " + str(adxl.steps)
    print(temp) #print to serial console
    keyboard.tap_key(KC.MACRO(repr(temp)+" ")) #type it on keyboard

make_key(names=('STEPS',), on_press=stepReport, on_release=passthrough)

bluetoothInterface = BLEHID()
def BT(*args, **kwargs):
    bluetoothInterface.clear_bonds()
    bluetoothInterface.start_advertising()

make_key(names=('CLEARBT',), on_press=BT, on_release=passthrough)

keyboard.col_pins = (board.D6, board.D3, board.D2, board.D1, board.D0,)
keyboard.row_pins = (board.D7, board.D8, board.D9, board.D10,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.BLE,  # Defaults to UART
)
keyboard.modules.append(split)


keyboard.keymap = [
# BASE
[
KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT,
KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.R, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.S, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.T, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.M, KC.HT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.E, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.I, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.O, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),
KC.Z, KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.SLSH,
KC.NO, KC.CLEARBT, KC.ESC, KC.LT(1, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.TAB, KC.ENT, KC.LT(2, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.DEL
],
# NAV
[
KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.TD(KC.NO, KC.CAPS, tap_time=200), KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,
KC.NO, KC.RALT, KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.NO, KC.INS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.DEL, KC.NO, KC.NO
],
# NUM
[
KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.RALT, KC.NO,
KC.NO, KC.STEPS, KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
],

]

layer_names_list = [
"Base", "Nav", "Num",
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='2Pocket')

