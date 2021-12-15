import json
import pygame


class Node:
    def __init__(self, id, pos):
        self.id = id
        self.pos = (pos['x'], pos['y'])

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = {(e['src'], e['dest']): e['w'] for e in edges}

def load_graph(dict):
    if 'nodes' in dict:
        nodes = {n.id: n for n in dict['nodes']}
        return Graph(nodes, dict['edges'])
    if 'id' in dict:
        return Node(**dict)
    return dict

def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen



with open('graph_triangle.json', 'r') as file:
    graph : Graph = json.load(file, object_hook=load_graph)

WIDTH, HEIGHT = 800, 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), depth=32, flags=pygame.constants.RESIZABLE)

FONT = pygame.font.SysFont('Arial', 20)


min_x = min(graph.nodes.values(), key= lambda n: n.pos[0]).pos[0]
max_x = max(graph.nodes.values(), key= lambda n: n.pos[0]).pos[0]
min_y = min(graph.nodes.values(), key= lambda n: n.pos[1]).pos[1]
max_y = max(graph.nodes.values(), key= lambda n: n.pos[1]).pos[1]

r = 15
margin = 50

while True:
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill(pygame.Color(25,150,120))

    # draw nodes
    for n in graph.nodes.values():
        scale_x = scale(n.pos[0], margin, screen.get_width() - margin, min_x, max_x)
        scale_y = scale(n.pos[1], margin, screen.get_height() - margin, min_y, max_y)
        pygame.draw.circle(screen, pygame.Color(22,58,205), (scale_x, scale_y), r)

        id_srf = FONT.render(str(n.id), True, pygame.Color(255,255,255))
        rect = id_srf.get_rect(center=(scale_x, scale_y))
        screen.blit(id_srf, rect)

    for (src, dest) in graph.edges:
        src_node: Node = graph.nodes[src]
        dest_node: Node = graph.nodes[dest]

        src_x = scale(src_node.pos[0], margin, screen.get_width() - margin, min_x, max_x)
        src_y = scale(src_node.pos[1], margin, screen.get_height() - margin, min_y, max_y)
        dest_x = scale(dest_node.pos[0], margin, screen.get_width() - margin, min_x, max_x)
        dest_y = scale(dest_node.pos[1], margin, screen.get_height() - margin, min_y, max_y)

        pygame.draw.line(screen, pygame.Color(109, 73, 92), (src_x, src_y), (dest_x, dest_y))

    pygame.display.update()
    # refresh rate
    clock.tick(60)



