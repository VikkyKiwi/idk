import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,pos, images):
    super().__init__()
    self.jump_speed = -17
    self.images = images
    self.image = images['p1_jump']
    self.rect =self.image.get_rect()
    self.rect.center = pos
    self.xy_speed = pygame.math.Vector2(0,0)
    self.facing = 'R'

  def update(self, platforms):
        screen_info = pygame.display.Info()
        self.image = self.images['p1_jump']
        if self.facing == "L":
          self.image = pygame.transform.flip(self.image, True,False)
        if self.rect.right<0:
          self.rect.left = screen_info.current_w
        elif self.rect.left> screen_info.current_w:
          self.rect.right = 0

        if self.rect.top<100:
          self.rect.top = 100
          for plat in platforms.sprite():
            plat.scroll(-1*self.xy_speed[1])
        elif self.rect.top>screen_info.current_h-80:
          self.rect.top = screen_info.current_h-80
          for plat in platforms.sprite():
            if plat.rect.bottom>0:
              plat.scroll(-1*self.xy_speed[1])
            else:
              plat.kill()
          return True
          

          
        self.rect.move_ip(self.xy_speed)
        hitlist = pygame.sprite.spritecollide(self, platforms,False)
        for platforms in hitlist:
          if self.xy_speed[1]>0 and abs(self.rect.bottom -platforms.rect.top) <= self.xy_speed[1]:
            self.rect.bottom = platforms.rect.top
            self.xy_speed[1] = self.jump_speed
        self.xy_speed[0] = 0
        self.xy_speed[1] +=.5
  def left(self):
    self.facing = 'L'
    self.xy_speed[0] = -5
  def right(self):
    self.facing = 'R'
    self.xy_speed[0] = 5


   
 
    