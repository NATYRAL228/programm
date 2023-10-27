import pygame as pg
a = pg.image.load('C:/Users/Ученик_8/Downloads/programm-main/pngwing.com.png')
pga = pg.image.load('C:/Users/Ученик_8/Downloads/sergeyjpg.jpg')
pg.init()
font_name = pg.font.match_font('arial') #поиск шифта arial
size = 18 #размер шрифта
W,H = 600,600
win = pg.display.set_mode((W, H)) # переменная чтобы создать игровое окно
name = ' '
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

  for vertic in range(0,600,20):
      pg.draw.line(win,(255,0,0),(0,vertic),(600,vertic))
  for horiz in range(0, 600, 20):
      pg.draw.line(win, (0, 255, 0), (horiz, 0), (horiz, 600))
  draw_text(win,name,W//2, 20,color=(255,0,0))
  pg.display.update()
