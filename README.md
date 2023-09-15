# Coding challenge
## Task
RGB color code convert to HEX color code

## decimalToHex function
Convert the decimal number to a two digit hex number
### input => decimal number (int)
### output => two digit Hex number (string)
* If the input = 0, then return 00
* If the input < 16, then return 0 + Remainder of division by 16, which choose this one in convert table
* If the input > 16, then return Remainder of division by 16, which choose this one in convert table
* Run while remainder of division by 16, equals 0 or smaller

## rgbToHex function
### input => 3 decimal number (int)
### output => the 3 decimal number convert to hex (string)
* Check the input is bigger than -1 and small than 255
