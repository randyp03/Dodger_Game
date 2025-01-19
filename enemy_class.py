import pygame

class Enemy():
    def __init__(self, spawn_position, target_position, speed = 200):
        self.pos = pygame.Vector2(spawn_position) # enemy's position
        self.direction = (target_position - self.pos).normalize() # direction vector to target
        self.speed = speed # movement speed (pixels/second)
        self.radius = 20 # enemy's size

    def update(self, dt):
        # update enemy's position
        self.pos += self.direction * self.speed * dt
    
    def is_off_screen(self, WIDTH, HEIGHT):
        # check if the enemy is off screen
        return (
            self.pos.x < -self.radius or self.pos.x > WIDTH + self.radius or
            self.pos.y < -self.radius or self.pos.y > HEIGHT + self.radius
        )
    
    def draw(self, surface, color="white"):
        # draw the enemy as a circle
        pygame.draw.circle(surface, color, (self.pos.x, self.pos.y), self.radius)
    
    def collides_with_player(self, player_rect):
        # check collision with player
        # closest point on the rectangle to circle's center
        closest_x = max(player_rect.left, min(self.pos.x, player_rect.right))
        closest_y = max(player_rect.top, min(self.pos.y, player_rect.bottom))

        # distance between the closest point and the enemy's center
        distance = pygame.Vector2(closest_x, closest_y).distance_to(self.pos)
        return distance <= self.radius