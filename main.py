# Librerias importadas
import pygame as pg
import sys, random
from pygame.locals import *
import constants as c

# Clases de objetos 
class Player(pg.sprite.Sprite): # Clase de nave
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("nave.png").convert()
		self.image.set_colorkey(c.black)
		self.rect = self.image.get_rect()
		self.speed_x = 0

	def changespeed(self, x):
		self.speed_x += x

	def update(self):
		self.rect.x += self.speed_x
		player.rect.y = 595

class Bullet(pg.sprite.Sprite): # Clase de disparo
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("bullet.png").convert()
		self.image.set_colorkey(c.blue)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 4


class Enemy(pg.sprite.Sprite): # Clase de enemigo
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("enemy.png").convert()
		self.image.set_colorkey(c.black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 2 
		if self.rect.y > 720:
			self.rect.y = -10
			self.rect.x = random.randrange(900)

score = 0

velocidad = 5

# Iniciar pygame
pg.init()

# Ventana 
screen = pg.display.set_mode(c.size)

# Título
pg.display.set_caption("SpaceInvaders")

# Cargar imagen de fondo
background = pg.image.load("bg.png").convert()

# 
sprite_list = pg.sprite.Group()
bullet_list = pg.sprite.Group()
enemy_list = pg.sprite.Group()

# Musica del juego
pg.mixer.music.load("music.wav")
pg.mixer.music.play(-1)

player = Player()
sprite_list.add(player)

for i in range(10):
	enemy = Enemy()
	enemy.rect.x = random.randrange(1280 - 20)
	enemy.rect.y = random.randrange(450) 

	enemy_list.add(enemy)
	sprite_list.add(enemy)

health = 3

fuente = pg.font.Font(None, 26)



# Bucle de juego
while health >= 0:

	screen.blit(background, (0,0))
	
	# Salida del juego
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		
		# Keyboard
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT:
				player.changespeed(-5)
			if event.key == pg.K_RIGHT:
				player.changespeed(5)
			if event.key == pg.K_SPACE:
				bullet = Bullet()
				bullet.rect.x = player.rect.x + 45
				bullet.rect.y = player.rect.y - 20

				bullet_list.add(bullet)
				sprite_list.add(bullet)

				sound = pg.mixer.Sound("bullet.wav")
				sound.play()

		elif event.type == pg.KEYUP:
			if event.key == pg.K_LEFT:
				player.changespeed(5)
			if event.key == pg.K_RIGHT:
				player.changespeed(-5)
	
	sprite_list.update() 

	for bullet in bullet_list:
		enemy_hit_list = pg.sprite.spritecollide(bullet, enemy_list, True)	
		for enemy in enemy_hit_list:
			sprite_list.remove(bullet)
			bullet_list.remove(bullet)
			score += 1
			print(score)
		if bullet.rect.y < -10:
			sprite_list.remove(bullet)
			bullet_list.remove(bullet)

	for enemy in enemy_list:
		player_hit_list = pg.sprite.spritecollide(player, enemy_list, True)	
		if player_hit_list:
			health -= 1

	score_text= f"Enemigos muertos: {score}"
	score_text_render = fuente.render(score_text, 1, (255, 255, 255))
	health_text= f"Vidas: {health}"
	health_text_render = fuente.render(health_text, 1, (255, 255, 255))

	screen.blit(score_text_render, (15, 10))
	screen.blit(health_text_render, (15, 30))
	

	sprite_list.draw(screen)

	clock = pg.time.Clock()
	clock.tick(c.fps)

	pg.display.flip()









