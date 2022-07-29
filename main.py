import pygame
import sys
import random
from platforms import Platforms
from pygame.locals import *
from player import Player

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


sprite_List = pygame.sprite.Group()
platforms = pygame.sprite.Group()
player = ''

def get_players_actions():
  p1_action = {}
  p1_action['p1_jump'] = pygame.image.load("images/p1_jump.png").convert()
  p1_action['p1_jump'].set_colorkey((0,0,0))
  p1_action['p1_hurt'] = pygame.image.load("images/p1_hurt.png").convert()
  p1_action['p1_hurt'].set_colorkey((0,0,0))
  return p1_action

def init(p1_action):
  global player
  for i in range(height // 100):
    for j in range(width // 410):
      plat = Platforms((random.randint(5, (width - 50) // 10) * 10, 120 * i), 'images/grassHalf.png', 70, 40)
      platforms.add(plat)
  player = Player((platforms.sprites()[-1].rect.centerx,platforms.sprites()[-1].rect.centery-300), p1_action)
  sprite_List.add(player)  



def main():
  global player
  p1_action = get_players_actions()
  init(p1_action)
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
            sys.exit()
      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                pygame.display.set_mode(size, FULLSCREEN)
            if event.key == pygame.K_ESCAPE:
                pygame.display.set_mode(size)
      keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      player.left()
    if keys[pygame.K_RIGHT]:
      player.right()
    screen.fill((0, 0, 100))
    platforms.draw(screen)
    sprite_List.draw(screen)
    pygame.display.flip()
    player.update(platforms)




if __name__ == '__main__':
  main()
