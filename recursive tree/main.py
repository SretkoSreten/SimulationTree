import pygame
import math

WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recusive Tree")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

h = 100
w = 5


class node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def draw_line(self):
        pygame.draw.line(win, (255, 255, 255), (self.start[0], self.start[1]),(self.end[0], self.end[1]))
    def draw_circle(self):
        r = 5
        pygame.draw.circle(win, (255, 255, 255), (int(self.end[0]), int(self.end[1])), r)

class tree:
    def __init__(self):
        self.root = []
        self.nodes = []
        self.dis = 50
        self.start = [WIDTH // 2, HEIGHT - 50]
        self.end = [int(WIDTH // 2), int(HEIGHT - self.dis - 50)]
        self.dis_x = 30
        self.h = 0
        self.width = 0
        self.dis_y = math.sqrt(self.dis**2 - self.dis_x**2)
        self.angle = 0
        self.len = 5

    def add_root(self):
        self.root.append(node(self.start, self.end))

    def add_node(self):

        self.angle += 0.5

        dis = self.dis
        dis_x = self.dis_x
        dis_y = self.dis_y

        self.start = self.end
        self.end = [int(self.start[0] - dis_x), int(self.start[1] - dis_y)]

        end_left = [self.start[0] - dis_x, self.start[1] - dis_y]
        end_right = [self.start[0] + dis_x, self.start[1] - dis_y]

        self.root.append(node(self.start, end_left))
        self.root.append(node(self.start, end_right))  

        for i in range(1, len(self.root)):

            end = self.root[i].end
            self.start = end
            self.end = [int(self.start[0] - dis_x), int(self.start[1] - dis_y)]

            end_left = [self.start[0] - dis_x, self.start[1] - dis_y]
            end_right = [self.start[0] + dis_x, self.start[1] - dis_y]

            self.root.append(node(self.start, end_left))
            self.root.append(node(self.start, end_right))        

    def add_nodes(self):
        for i in range(self.len):
            self.add_node()

    def draw_nodes(self):
        for node in self.root:
            node.draw_line()
            node.draw_circle()
    
def main():
    run = True
    tree_ = tree()
    tree_.add_root()
    tree_.add_nodes()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        tree_.draw_nodes()
        pygame.display.update()

    pygame.quit()

main()