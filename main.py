# Vector Test for EccoPY
from DATA.EPShortFunctions import *
from pygame import *
from math import *


class UI(object):
    def __init__(self):
        SIZES = [
            [1920, 1080], # Window
            [512, 512] # Surface
        ]

        init()

        self.WINDOW = display.set_mode(SIZES[0])
        self.SCREEN = Surface(SIZES[1]).convert()


class CODE(object):
    def __init__(self):
        # Linkers!
        self.UP = UI()

        # Vars
        self.Running = 1

        #   Keyboard Controlls
        self.keyb = KEYDOWN
        self.prke = key.get_pressed()

        #       Bindings
        self.end = K_ESCAPE
        self.up = K_UP
        self.down = K_DOWN
        self.left = K_LEFT
        self.right = K_RIGHT
        self.upscale = K_KP_MINUS
        self.downscale = K_KP_PLUS

        #               Controller
        self.joysticks = [joystick.Joystick(i) for i in range(joystick.get_count())]


var = CODE()

class testvect(sprite.Sprite):
    def __init__(self):
        # Linkers!
        sprite.Sprite.__init__(self)
        self.vector = math.Vector2
        self.keys = CODE()

        # Attributes
        #   Image
        self.image = Surface((128, 128))
        self.image.fill((22, 46, 95))
        #   TriggerBox
        self.rect = self.image.get_rect()
        #   Vars
        self.pos = self.vector(0, 0)
        self.vel = self.vector(0, 0)
        self.acc = self.vector(0, 0)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel + (self.acc) / 2
        self.rect.center = self.pos

    def render(self, surface):
        surface.blit(self.image, self.pos)
        self.update()


vec = testvect()

while var.Running == 1:
    var.prke = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()
        if e.type == var.keyb:
            if e.key == var.up:
                vec.vel.x = round(cos(1))

            elif e.key == var.end:
                var.Running = 0


    var.UP.SCREEN.fill((255, 0, 0))

    vec.render(var.UP.SCREEN)

    var.UP.WINDOW.blit(transform.scale(var.UP.SCREEN, (var.UP.WINDOW.get_width(), var.UP.WINDOW.get_height())), (0, 0))

    display.set_caption("ECCOPY_TEST_VECTOR")
    display.update()
