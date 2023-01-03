HexToASCII db '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'

mov DL, [input]

mov AL, HexToASCII[DL]

mov [output], AL
