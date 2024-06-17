import pygame as py 
import sys,random
from pygame.locals import *



class snake():

	def __init__(self):
		#screen edition 
		py.display.set_caption("SNAKE GAME !")

		self.width,self.height = 800,800
		self.screen = py.display.set_mode((self.width,self.height)) 
		self.black = py.Color(0,0,0)

		self.running = True
		self.fps = py.time.Clock()

		#apple edit
		self.range_apple = [n for n in range(40,760+1,20)]
		self.apple_x = [random.choice(self.range_apple),random.choice(self.range_apple)]
		
		#snake structure
		self.snake_body = [[40,20]] 
		self.direction = "r"
       


	def again(self):
		return snake().main_game()
		

	def apple_spawn(self):

		self.apple_x = [random.choice(self.range_apple), random.choice(self.range_apple)]
		return self.apple_x

#celdas del tablero
	def main_board(self):

		self.screen.fill(self.black)

		self.squares = self.height // 20 

		self.dim_x = [n*20 for n in range(self.squares)] #c.dim
		self.dim_y = [n*20 for n in range(self.squares)]

		for x in self.dim_x:
			for y in self.dim_y:

				self.x = py.draw.line(self.screen,(150,150,150),(x, 0),(x,self.width),1)
				self.y = py.draw.line(self.screen,(150,150,150),(0, y),(self.height,y),1)

#juego
	def main_game(self): 
		py.init()
		
		while self.running:
			
			self.x_head = [self.snake_body[0][0],self.snake_body[0][1]]
			snake().main_board()
			
			for event in py.event.get():
				sys.exit() if event.type == py.QUIT else None

				if event.type == py.KEYDOWN:
					if event.key == py.K_RIGHT:
						self.direction = "r"
					elif event.key == py.K_LEFT:
						self.direction = "l"
					elif event.key == py.K_UP:
						self.direction = "u"
					elif event.key == py.K_DOWN:
						self.direction = "d"

			if self.direction == "u":
				self.x_head[1] -= 20
			elif self.direction == "d":
				self.x_head[1] += 20
			elif self.direction == "r":
				self.x_head[0] += 20
			elif self.direction == "l":
				self.x_head[0] -= 20


			for x,y in self.snake_body[1:]: snake().again() if self.x_head == [x,y] else None #lose


			self.snake_body.insert(0, list(self.x_head) ) #iterator 

			for pos in self.snake_body: #snake draw
				pos[0] = pos[0] % self.width 
				pos[1] = pos[1] % self.height 
				py.draw.rect(self.screen ,(204,0,0), py.Rect(pos[0], pos[1], 20, 20))
		

			if self.x_head == self.apple_x : # add cube
				self.snake_body.append(self.apple_x)
				self.apple_x = snake().apple_spawn()
			else:
				self.snake_body.pop()



			py.draw.rect(self.screen ,(0,204,102), py.Rect(self.apple_x[0], self.apple_x[1] , 20, 20)) #apple draw 



			py.display.flip()
			self.fps.tick(30)
def pex3():
	snake().main_game()