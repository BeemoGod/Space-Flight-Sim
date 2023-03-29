import pygame
import random


pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screen_x, screen_y = screen.get_size()
center_x, center_y = screen_x//2, screen_y//2

pygame.display.set_caption("Space Flight")


class Star:
  animation_speed = 10
  
  def __init__(self):
    self.x = random.randint(-screen_x, screen_x)
    self.y = random.randint(-screen_y, screen_y)
    self.z = random.randint(center_y, screen_x)
    self.pz = self.z
    self.color = (255,255,255)
  
  def update(self):
    self.z -= Star.animation_speed
    
    if self.z < 1:
      self.x = random.randint(-screen_x//1.5, screen_x//1.5)
      self.y = random.randint(-screen_y//1.5, screen_y//1.5)
      self.z = random.randint(center_y, screen_x)
      self.pz = self.z
    
    value = 255 - int((self.z * (255/screen_x)))
    self.color = (value, value, value)
  
  def draw(self):
    starx = self.x / self.z * center_y + center_x
    stary = self.y / self.z * center_y + center_y
    
    radius = maps(self.z, 0, screen_x, 6, 0)
    
    pygame.draw.circle(screen, self.color, (starx, stary), radius)
    
    prevx = self.x / self.pz * center_y + center_x
    prevy = self.y / self.pz * center_y + center_y
    
    self.pz = self.z
    
    pygame.draw.line(screen, self.color, (prevx, prevy), (starx, stary), round(radius/1.5))

def maps(num, in_min, in_max, out_min, out_max):
  return out_min + (out_max - out_min) * (num - in_min) / (in_max - in_min)


def render_cockpit():
  bottom_panel = [
    (0,screen_y),
    (0, screen_y/1.5),
    (screen_x/6, screen_y/1.8),
    (screen_x/3, screen_y/2),
    (screen_x-screen_x/3, screen_y/2),
    (screen_x-screen_x/6, screen_y/1.8),
    (screen_x, screen_y/1.5),
    (screen_x, screen_y)
  ]
  
  top_panel = [
    (0,0),
    (0, screen_y/9),
    (screen_x/2, screen_y/6),
    (screen_x, screen_y/9),
    (screen_x,0)
  ]
  
  pygame.draw.polygon(screen, (100,100,100), bottom_panel)
  pygame.draw.polygon(screen, (100,100,100), top_panel)
  pygame.draw.polygon(screen, (50,50,50), bottom_panel, 10)
  pygame.draw.polygon(screen, (50,50,50), top_panel, 10)
  pygame.draw.line(screen, (50,50,50), top_panel[2], (screen_x/2, screen_y/2), 10)
  pygame.draw.line(screen, (50,50,50), top_panel[1], bottom_panel[2], 10)
  pygame.draw.line(screen, (50,50,50), top_panel[3], bottom_panel[5], 10)


def main():
  clock = pygame.time.Clock()
  
  stars = []
  
  for i in range((screen_x+screen_y)//9):
    stars.append(Star())
  
  mouse_pressed = False
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        break
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pressed = True
      elif event.type == pygame.MOUSEBUTTONUP:
        mouse_pressed = False
    
    screen.fill("black")
    
    if mouse_pressed == True:
      if Star.animation_speed < screen_x/30:
        Star.animation_speed += 1
    else:
      Star.animation_speed = 3
    
    for star in stars:
      star.update()
      star.draw()
    
    render_cockpit()
    
    pygame.display.update()
    clock.tick(30)


if __name__ == "__main__":
  main()