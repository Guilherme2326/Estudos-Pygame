#codigo demostração de deslocamento pela tela 
import pygame 

pygame.init()

screem = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screem.get_width() / 2, screem.get_height() / 2)

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screem.fill("red")

    pygame.draw.circle(screem, "blue", player_pos, 10) #tamanho da bola

    keys = pygame.key.get_pressed() #movimentação do circulo
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt           

    pygame.display.flip()


    dt = clock.tick(60) / 1000


pygame.quit()



