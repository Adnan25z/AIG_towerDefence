import pygame

goal_position = (27, 11)

spawn_positions = [(1, 5), (7, 1), (5, 13)]

path_positions = [
    [(4, 5), (4, 6), (5, 4), (6, 3), (11, 3), (25, 6), (21, 13), (12, 5), (11, 6), (10, 7), (9, 8), (7, 2), (9, 11), (10, 10), (9, 9), (5, 14)], #Normal Path
    [(2, 5), (3, 5), (6, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (19, 1), (20, 1), (26, 5), (21, 12), (10, 16), (9, 16),
        (6, 14), (13, 5), (14, 5), (15, 5), (17, 6), (18, 6), (19, 6), (8, 8), (7, 8), (6, 8), (7, 14)], #Top Covered
    [(3, 6), (7, 3), (8, 3), (9, 3), (10, 3), (20, 13), (17, 13), (12, 16), (6, 15),(7, 15), (9, 17), (7, 9), (8, 9),
        (16, 6), (19, 7), (18, 7), (15, 6), (14, 6), (13, 6), (12, 6), (22, 17), (26, 10)], #Bottom Covered
    [(5, 3), (6, 9), (20, 12), (8, 16), (19, 2), (11, 4), (11, 5), (21, 16), (25, 9), (25, 8), (25, 7), (8, 12), (9, 10), (4, 13)], #Left Covered
    [(5, 5), (5, 6), (12, 3), (26, 6), (22, 12), (10, 9), (20, 7), (20, 6), (20, 3), (20, 2), (12, 4), (10, 8), (5, 7), (21, 15)
    , (26, 9), (26, 8), (26, 7), (8, 14), (8, 15)], #Right Covered
    [(4, 4), (5, 2), (16, 1), (4, 10), (25, 5), (22, 6), (12, 13), (14, 15), (15, 10), (10, 6), (9, 7), (24, 13), (18, 15), (8, 11)], #Top_Left Covered
    [(27, 1), (16, 15), (25, 15), (12, 10), (17, 10), (16, 5), (22, 16), (16, 15), (27, 10)], #Top_Right Covered
    [(2, 6), (4, 7), (5, 8), (16, 17), (24, 15), (8, 17), (12, 11), (19, 3), (17, 7), (21, 17), (25, 10), (4, 14), (5, 15)], #Bottom_Left Covered
    [(6, 4), (16, 2), (27, 5), (22, 13), (14, 16), (25, 17), (10, 17), (6, 10), (15, 11), (11, 7), (27, 13), (18, 17), (9, 12), (10, 11)], #Bottom_Right Covered
    [(27, 2), (27, 3), (27, 4), (22, 7), (22, 8), (22, 9), (22, 10), (12, 14), (12, 16), (16, 16), (12, 15), (25, 16), (24, 14), (4, 11), (17, 11),
        (17, 12), (22, 11), (20, 11), (20, 10), (20, 9),(20, 8), (20, 5), (20, 4), (21, 14), (18, 16), (27, 12), (4, 12), (8, 13)], #Left_Right Covered
    [(13, 2), (14, 2), (15, 2), (5, 10), (17, 1), (18, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1), (24, 6), (23, 6), (19, 13),
        (18, 13), (16, 13), (15, 13),(14, 13), (13, 13), (13, 16), (11, 16), (15, 15), (11, 10), (13, 11), (14, 11), (16, 10), (26, 13), (25, 13), 
        (23, 17), (24, 17), (20, 15), (19, 15), (17, 17)] #Top-Bottom Covered
        ]

waves = [
    {0 : [1, 1, 1, 0, 0, 0], 1 : [2, 1, 0, 0, 0, 0], 2 : [2, 1, 0, 0, 0, 0]}, #Wave 1 - 5 Bug, 2 Fly, 1 Green Bug at Start 1
    {0 : [3, 1, 2, 0, 0, 0], 1 : [2, 2, 0, 0, 0, 0], 2 : [0, 2, 1, 0, 0, 0]},
    {0 : [3, 1, 1, 2, 0, 0], 1 : [0, 3, 2, 1, 0, 0], 2 : [0, 3, 2, 1, 0, 0]},
    {0 : [6, 0, 0, 0, 1, 0], 1 : [6, 0, 0, 3, 1, 0], 2 : [6, 0, 2, 2, 0, 0]},
    {0 : [0, 2, 1, 3, 1, 0], 1 : [4, 6, 0, 0, 1, 0], 2 : [0, 5, 3, 1, 1, 0]},
    {0 : [0, 2, 1, 1, 4, 0], 1 : [0, 0, 5, 2, 5, 0], 2 : [0, 0, 3, 5, 0, 1]},
    {0 : [0, 0, 7, 2, 0, 1], 1 : [0, 0, 7, 7, 1, 1], 2 : [0, 0, 2, 3, 3, 0]},
    {0 : [0, 0, 0, 0, 0, 1], 1 : [0, 0, 0, 0, 0, 1], 2 : [0, 0, 0, 0, 0, 1]},
    {0 : [0, 0, 1, 0, 5, 1], 1 : [0, 0, 0, 2, 1, 2], 2 : [0, 0, 0, 4, 0, 2]},
    {0 : [0, 0, 0, 0, 0, 3], 1 : [0, 0, 0, 0, 0, 3], 2 : [0, 0, 0, 0, 0, 3]}
]

tower1_stats = [
    [400, 20, (300, 300), 240, 1000], #Cost - 400, Damage - 20, Range - (300, 300), Rebuild CD - 240, Value - 1000
    [250, 35, (350, 350), 180, 600], 
    [650, 75, (450, 450), 120, 2000]
    ]

tower2_stats = [
    [800, 600, 5, 1800], #Cost - 800, Duration - 600, Overdrive Threshold - 5, Value - 1800
    [500, 750, 4, 1200],
    [550, 900, 3, 1500]
]

tower3_stats = [
    [600, 20, 10, (75, 75), 1550], #Cost - 600, Damage - 20, AOE Damage - 10, Range(75, 75), Value - 1550
    [700, 40, 30, (100, 100), 2050],
    [1050, 80, 60, (150, 150), 2700]
]

tree1 = pygame.transform.scale(pygame.image.load("assets/aesthetic/Tree_1.png"), (30, 25))
tree2 = pygame.transform.scale(pygame.image.load("assets/aesthetic/Tree_1-2.png"), (25, 30))
tree3 = pygame.transform.scale(pygame.image.load("assets/aesthetic/Tree_2.png"), (30, 25))
tree4 = pygame.transform.scale(pygame.image.load("assets/aesthetic/Tree_2-2.png"), (25, 30))

#Tree type and their coordinates
aesthetic_images = [
    [tree1, (63, 55)], [tree2, (147, 170)], [tree1, (630, 56)], [tree1, (808, 707)], [tree2, (1000, 140)], 
    [tree1, (88, 452)], [tree3, (1100, 353)], [tree1, (598, 367)], [tree3, (299, 223)], [tree3, (280, 545)], 
    [tree2, (155, 673)], [tree2, (1097, 682)], [tree2, (771, 216)], [tree3, (962, 343)], 
]