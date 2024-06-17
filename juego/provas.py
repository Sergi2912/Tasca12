"""
import pygame

"""
Constantes globales
"""

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Dimensiones de la pantalla
LARGO_PANTALLA = 800
ALTO_PANTALLA = 600

class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa la barra inferior que controla el protagonista. """

    # Función Constructor
    def __init__(self, x, y):
        # Llama al constructor padre
        super().__init__()

        # Establecemos el alto y largo
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLANCO)

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Establecemos el vector velocidad
        self.cambio_x = 0
        self.cambio_y = 0
        self.paredes = None

    def cambiovelocidad(self, x, y):
        """ Cambia la velocidad del protagonista. """
        self.cambio_x += x
        self.cambio_y += y

    def update(self):
        """ Cambia la velocidad del protagonista. """
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x

        # Hemos chocado contra la pared después de esta actualización?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right

        # Desplazar arriba/abajo
        self.rect.y += self.cambio_y

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:
            # Reseteamos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom

class Pared(pygame.sprite.Sprite):
    """ Pared con la que el protagonista puede encontrarse. """
    def __init__(self, x, y, largo, alto):
        """ Constructor para la pared con la que el protagonista puede encontrarse """
        # Llama al constructor padre
        super().__init__()

        # Construye una pared azul con las dimensiones especificadas por los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(AZUL)

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Serpiente(pygame.sprite.Sprite):
    """ Serpiente que persigue al jugador """
    def __init__(self, x, y):
        """ Constructor de la serpiente """
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(VERDE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self, jugador):
        """ Persigue al jugador """
        if self.rect.x < jugador.rect.x:
            self.rect.x += 3
        elif self.rect.x > jugador.rect.x:
            self.rect.x -= 3
        if self.rect.y < jugador.rect.y:
            self.rect.y += 3
        elif self.rect.y > jugador.rect.y:
            self.rect.y -= 3

# Llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
pygame.init()

# Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([LARGO_PANTALLA, ALTO_PANTALLA])

# Creamos el título de la ventana
pygame.display.set_caption('Test')

# Lista que almacena todos los sprites
listade_todoslos_sprites = pygame.sprite.Group()

# Construimos las paredes. (x_pos, y_pos, largo, alto)
pared_list = pygame.sprite.Group()

pared = Pared(0, 0, 10, 600)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(10, 0, 790, 10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(10, 200, 100, 10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

# Creamos al objeto protagonista
protagonista = Protagonista(50, 50)
protagonista.paredes = pared_list

listade_todoslos_sprites.add(protagonista)

# Crear serpiente
serpiente = Serpiente(400, 300)
listade_todoslos_sprites.add(serpiente)

# Reloj para controlar la tasa de fotogramas
reloj = pygame.time.Clock()

# Bucle principal
terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                protagonista.cambiovelocidad(-3, 0)
            elif evento.key == pygame.K_RIGHT:
                protagonista.cambiovelocidad(3, 0)
            elif evento.key == pygame.K_UP:
                protagonista.cambiovelocidad(0, -3)
            elif evento.key == pygame.K_DOWN:
                protagonista.cambiovelocidad(0, 3)
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                protagonista.cambiovelocidad(3, 0)
            elif evento.key == pygame.K_RIGHT:
                protagonista.cambiovelocidad(-3, 0)
            elif evento.key == pygame.K_UP:
                protagonista.cambiovelocidad(0, 3)
            elif evento.key == pygame.K_DOWN:
                protagonista.cambiovelocidad(0, -3)

    # Actualizar sprites
    listade_todoslos_sprites.update()
    serpiente.update(protagonista)

    # Comprobar colisiones entre la serpiente y el jugador
    if pygame.sprite.collide_rect(protagonista, serpiente):
        print("¡La serpiente te atrapó!")
        terminado = True

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar todos los sprites
    listade_todoslos_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar a 60 fotogramas por segundo
    reloj.tick(60)

pygame.quit()"""
