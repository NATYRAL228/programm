import pygame as pg
from sql_bd import DateBaseSQL
score = 'Score 0'
bd = DateBaseSQL
clock = pg.time.Clock()
apl = pg.image.load('apl.png')
a = pg.image.load('pngwing.com.png')
pga = pg.image.load('sergeyjpg.jpg')
pg.init()
font_name = pg.font.match_font('arial') #поиск шифта arial
size = 18 #размер шрифта
W,H = 600,600
win = pg.display.set_mode((W, H)) # переменная чтобы создать игровое окно
name = ' '
class Apple(pg.sprite.Sprite):
    def __init__(self, x,y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.image = pg.image.load('apl.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.bottom = self.y
class Player(pg.sprite.Sprite):
    def __init__(self, x,y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 0
        self.image = pg.image.load('zm.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.bottom = self.y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.speed_x = -1
        if key[pg.K_RIGHT]:
            self.speed_x = +1
        if key[pg.K_DOWN]:
            self.speed_y = +1
        if key[pg.K_UP]:
            self.speed_y = -1
all_sprites = pg.sprite.Group()
apple = Apple(50,50)
player = Player(300,300)
all_sprites.add(player,apple)
def draw_text(surf, text, x,y, size=size, color=(255,255,255)):
    font = pg.font.Font(font_name, size) #определяет шрифт
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
def user_name(surf,text,x,y,size,color=(255,255,255)):
    font = pg.font.Font(font_name, size)  # определяет шрифт
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
mainloop = True
while mainloop:
  for i in pg.event.get():
    if i.type == pg.QUIT:
      exit()
    elif i.type == pg.KEYDOWN:
       if  i.key == pg.K_BACKSPACE:
           name = name[:-1]
       elif i.key == pg.K_RETURN:
           mainloop = False
       else:
           name += i.unicode
    win.fill((0,0,0))
    win.blit(a,(0,0))
    draw_text(win, 'Введите имя:', W//2,H//2)
    draw_text(win,name,W//2,H//2 + 20)
    pg.display.update()

while 1:
  for i in pg.event.get():
    if i.type == pg.QUIT:
      exit()
  win.fill((0, 0, 0))
  win.blit(pga, (0, 0))
  all_sprites.update()
  all_sprites.draw(win)
  clock.tick(60)
  str(score)



  for vertic in range(0,600,20):
      pg.draw.line(win,(255,0,0),(0,vertic),(600,vertic))
  for horiz in range(0, 600, 20):
      pg.draw.line(win, (0, 255, 0), (horiz, 0), (horiz, 600))
  draw_text(win,name,W//2, 10,color=(255,0,0))
  draw_text(win,str(score),W//6, 10,color=(0,255,0))
  pg.display.update()
