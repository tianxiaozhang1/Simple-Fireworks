import pygame, sys, random
from math import sin, cos, radians

def setup_fireworks():
    fw_x_list = []
    fw_y_list = []
    # x axis spacing
    for i in range(0,6):
        fw_x_list.append(random.randint(120+280*i, 400+280*i))
    # y axis spacing
    for i in range(0,6):
        fw_y_list.append(1180+random.randint(-60,180))
    
    fw_colour = random.choice(colour_list)
    
    fireworks(fw_x_list, fw_y_list, fw_colour)

def fireworks(fw_x_list, fw_y_list, fw_colour):
    fw_time = 120

    while fw_time > 0:

        clock.tick(66)
        
        fw_time -= 1/4

        screen.fill(sapphire)
        skyline()

        #ascension
        if 90 < fw_time <= 120:
            for i in range(0, 6):
                for j in range(0,7):
                    pygame.draw.rect(screen, random.choice(hi_colour_list), pygame.Rect(fw_x_list[i]+3, int(fw_y_list[i] - 880 + 12 + 0.5*((953-10*j)/450)*((fw_time-90)**2))-8, 12, 12)) #flame
                pygame.draw.rect(screen, fw_colour, pygame.Rect(fw_x_list[i], int(fw_y_list[i] - 880 + 0.5*(88/45)*((fw_time-90)**2)), 18, 18)) #main particle
        
        #assembling fireworks
        while len(fw_quantity) < 6:     
            fw_quantity.append(random.randint(152,226))

        for i in range(0, 6):
            while len(fw_colour_list[i]) < fw_quantity[i]:
                #main particles
                fw_colour_list[i].append(random.choice(hi_colour_list))
                #trail particles
                fw_trail_list[i].append(random.choice(trail_list))
                #direction of particles
                fw_angle_list[i].append(random.randint(0,360))
                #length factor of particles
                fw_hyp_list[i].append(random.uniform(0.12, 1.02))

        #explosion
        if 50 < fw_time < 90:
            d1 = 600-(50/3)*(fw_time-66)+(1/2)*(-5/9)*((fw_time-66)**2)
            d1 *= 0.52

            for i in range(0, 6):
                for j in range(fw_quantity[i]):

                    #colour change
                    dc1 = fw_colour_list[i][j][0]
                    if dc1 < 26:
                        dc1 = 26
                    dc2 = fw_colour_list[i][j][1]
                    if dc2 < 40:
                        dc2 = 40
                    dc3 = fw_colour_list[i][j][2]
                    if dc3 < 72:
                        dc3 = 72

                    dt1 = fw_trail_list[i][j][0]
                    dt2 = fw_trail_list[i][j][1]
                    dt3 = fw_trail_list[i][j][2]

                    pygame.draw.rect(screen, (int(((dt1-26)/40))*(fw_time-50)+26, int(((dt2-40)/40))*(fw_time-50)+40, int(((dt3-72)/40))*(fw_time-50)+72), pygame.Rect(int(fw_x_list[i]+d1*fw_hyp_list[i][j]*(cos(radians(fw_angle_list[i][j])))), int(fw_y_list[i] - 880 + d1*fw_hyp_list[i][j]*(sin(radians(fw_angle_list[i][j])))+2-136+(0.5*(0.46)*(fw_time-66)**2)), 12, 12))
                    pygame.draw.rect(screen, (int(((dc1-26)/40))*(fw_time-50)+26, int(((dc2-40)/40))*(fw_time-50)+40, int(((dc3-72)/40))*(fw_time-50)+72), pygame.Rect(int(fw_x_list[i]+d1*fw_hyp_list[i][j]*(cos(radians(fw_angle_list[i][j]))))+6, int(fw_y_list[i] - 880 + d1*fw_hyp_list[i][j]*(sin(radians(fw_angle_list[i][j])))+8-136+(0.5*(0.46)*(fw_time-66)**2)), 12, 12))
                    
                    #constant colour
                    #pygame.draw.rect(screen, fw_trail_list[i][j], pygame.Rect(int(fw_x_list[i]+d1*fw_hyp_list[i][j]*(cos(radians(fw_angle_list[i][j])))), int(fw_y_list[i] - 880 + d1*fw_hyp_list[i][j]*(sin(radians(fw_angle_list[i][j])))+2-136+(0.5*(0.46)*(fw_time-66)**2)), 12, 12))
                    #pygame.draw.rect(screen, fw_colour_list[i][j], pygame.Rect(int(fw_x_list[i]+d1*fw_hyp_list[i][j]*(cos(radians(fw_angle_list[i][j]))))+6, int(fw_y_list[i] - 880 + d1*fw_hyp_list[i][j]*(sin(radians(fw_angle_list[i][j])))+8-136+(0.5*(0.46)*(fw_time-66)**2)), 12, 12))

        if fw_time < 49.9:
            fw_time = 120
            setup_fireworks()

        pygame.display.update()

def skyline():
    pygame.draw.rect(screen, midnight, pygame.Rect(280, 936, 120, 320))
    pygame.draw.rect(screen, midnight, pygame.Rect(360, 900, 180, 420))
    pygame.draw.rect(screen, midnight, pygame.Rect(860, 860, 160, 220))
    pygame.draw.rect(screen, midnight, pygame.Rect(580, 960, 760, 120))
    pygame.draw.rect(screen, midnight, pygame.Rect(1360, 920, 120, 320))
    pygame.draw.rect(screen, midnight, pygame.Rect(1560, 960, 120, 320))

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption('Fireworks!')

sapphire = (22, 36, 66)

midnight = (26, 40, 72)

textcolour = (236, 236, 236)

colour_list = [(168, 34, 38), (152, 80, 48), (198, 178, 38), (132, 168, 42), (32, 104, 100), (46, 88, 168), (108, 32, 108)]                     

hi_colour_list = [(200, 22, 28), (202, 112, 32), (216, 202, 72), (152, 182, 22), (62, 142, 134), (82, 112, 182), (138, 24, 116)]

trail_list = [(250, 212, 226), (255, 246, 152), (196, 218, 78), (220, 200, 226), (246, 176, 136), (212, 228, 238), (248, 198, 182), (212, 228, 212), (238, 196, 206), (212, 212, 192), (232, 202, 212), (248, 198, 182), (255, 252, 200)]

fw_colour_list = [[],[],[],[],[],[]]

fw_angle_list = [[],[],[],[],[],[]]

firework_distance_list = [[],[],[],[],[],[]]

fw_hyp_list = [[],[],[],[],[],[]]

fw_trail_list = [[],[],[],[],[],[]]

fw_quantity = []

pygame.draw.rect(screen, sapphire, pygame.Rect(0, 0, 1920, 1080))

skyline()

text_font = pygame.font.Font('freesansbold.ttf', 32)
new_game_surface_1 = text_font.render("Let's celebrate. Press SPACE for fireworks.", True, textcolour) 
new_game_surface_rect_1 = new_game_surface_1.get_rect(center = (960, 540))
screen.blit(new_game_surface_1, new_game_surface_rect_1)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                setup_fireworks()

    pygame.display.update()
    clock.tick(8)
