
import random
import pygame


class Enemy:
    def __init__(self, x, y, width, height):
        self.x  = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
    def inc_speed(self, new_speed):
        self.speed = new_speed
    def move(self):
        self.x += self.speed
    
        
class Enemy_Manager:
    def __init__(self, car_width, car_height, screen_width, screen_height):
        self.car_width = car_width
        self.car_height = car_height
        self.max_width = screen_width
        self.min_height = 100
        self.max_height = screen_height
        self.lanes = 3
        self.car_height = car_height
        self.car_y_coords = self.calc_y_coords(car_height * 5)
        self.cars_per_lane = 5
        self.all_cars = []
        self.car_speed = 5
    
    def create_car(self, y_offset):
        possible_x_mults = [i * 50 for i in range(0, self.cars_per_lane * 2)]
        x_pos = 800 + possible_x_mults.pop(random.randint(0, self.cars_per_lane * 2 - 1))
        return Enemy(x_pos, self.car_y_coords[y_offset][0], self.car_width, self.car_height)
    
    def create_car_lanes(self):
        for lane in range(self.lanes):
            for car in range(self.cars_per_lane):
                self.all_cars.append(self.create_car(lane))

    def calc_y_coords(self, width_bw_lanes):
        lane_coord_list = []
        for y_offset in range(self.lanes):
            starting_coord = y_offset * width_bw_lanes + self.min_height
            ending_coord = starting_coord + self.car_height
            lane_coord_list.append((starting_coord, ending_coord))
        return lane_coord_list
    def update_cars(self):
        for car in self.all_cars:
            
                car.x -= self.car_speed
                if car.x < 0:
                    car.x = self.max_width
    def draw(self, win, img, rect):
        for car in self.all_cars:
                rect.center = (car.x, car.y)
                win.blit(img, rect)

    def detect_collision(self, player):
        for car in self.all_cars:
            if self.is_colliding(car, player):
                return True
        return False
    def is_colliding(self, enemy, player):
        return (player.x < enemy.x + enemy.width and \
        player.x + player.width > enemy.x and \
        player.y < enemy.y + enemy.height and \
        player.y + player.height > enemy.y)             
    def reset(self):
        self.all_cars = []
        

