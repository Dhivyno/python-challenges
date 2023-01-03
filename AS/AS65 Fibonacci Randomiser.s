mov EAX, 0
mov EBX, 1
mov ECX, 10

fibonacci_loop:
    mov [output], EAX
    add EAX, EBX
    mov EBX, EAX
    dec ECX
    jnz fibonacci_loop
