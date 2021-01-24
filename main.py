# Librerias importadas

import pygame as pg
import sys, random
from pygame.locals import *
import constants as c
import imagenes as img


# Iniciar pygame
pg.init()

# Ventana 
screen = pg.display.set_mode(c.size)

# FPS
clock = pg.time.Clock()
clock.tick(c.fps)

# Título
pg.display.set_caption("Ejemplo")


# Bucle de juego
while True:

	screen.blit(img.background, (0,0))
	
	# Salida del juego
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		
		# Keyboard
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT:
				c.Velocidad = -0.85
			if event.key == pg.K_RIGHT:
				c.Velocidad = 0.85
			if event.key == pg.K_SPACE:
				c.disparo = True
		elif event.type == pg.KEYUP:
			if event.key == pg.K_LEFT:
				c.Velocidad = 0
			if event.key == pg.K_RIGHT:
				c.Velocidad = 0
	
	

	

	# Movimiento
	c.Posicion_nave += c.Velocidad 


	if c.disparo:
		pos_bullet_x = c.Posicion_nave
		for i in range(0, len(c.pos_bullet_y)):
			screen.blit(img.bullet, (pos_bullet_x+45, c.pos_bullet_y[i]))
			

	# Nave

	screen.blit(img.nave,(c.Posicion_nave, 590)) 



	pg.display.flip()









