xyz=True
while xyz:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check=False
    speed=2
    KeyBoardKey=pygame.key.get_pressed()
    if KeyBoardKey[pygame.K_LEFT]:
        char.x -=speed
    if KeyBoardKey[pygame.K_RIGHT]:
        char.x +=speed
    pygame.display.flip()
    pygame.time.delay(30)