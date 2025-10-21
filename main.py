import pygame
import random
import json
import sys
pygame.init()
start_time = pygame.time.get_ticks()
enemy_time = pygame.time.get_ticks()
width = 1400
clock = pygame.time.Clock()
height = 820
high_score = 0
start = False
center_x = width // 2
center_y = height // 2
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RacingType")
running = True
letters_typed = 0
money = 10
finish_line = pygame.image.load("finish.png")
finish = pygame.transform.scale(finish_line, (width / 2, 324))
words_typed = letters_typed / 5
row = "Home Row"
names = [
    "HungryOcelote820",
    "SixSeventyGuy208",
    "DoughyReinderr23",
    "BloxBuilderBud99",
    "BuddhaBuddhy289",
    "FlyingLeapord284"
]
username = random.choice(names)

naming = False
running = False
adding = ""
def add_name():
    global adding, username, naming, running
    clock.tick(60)
    screen.blit(font.render("Enter Your Name :", True, (255, 255, 255)), (center_x - 350, center_y - 150))
    screen.blit(font.render(adding, True, (255, 255, 255)), (center_x - 250, center_y + 50))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                adding = adding[:-1]
            elif event.key == pygame.K_RETURN:
                username = adding
                naming = False
                adding = ""
            else:
                if len(adding) < 23:
                    adding += event.unicode
    pygame.display.update()





def get_rank(wpm):
    if wpm <= 10:
        return "Typing Trainee"
    elif wpm <= 20:
        return "Racing Rookie"
    elif wpm <= 30:
        return "Speed Starter"
    elif wpm <= 40:
        return "Key Cruiser"
    elif wpm <= 50:
        return "Speedster"
    elif wpm <= 60:
        return "Rapid Racer"
    elif wpm <= 70:
        return "Type Hero"
    elif wpm <= 80:
        return "Typing Titan"
    elif wpm <= 90:
        return "Keyboard King"
    else:
        return "Hyper Typer"

rank = None
backgrounds = [
    (0, 205, 0),
    (204, 153, 102)
]
background = random.choice(backgrounds)
cars = [
    
    {
        "image": "redthunder.png",
        "boost": 0,
        "name": "Red Thunder"
    },
    {
        "image": "Gt40_large.png",
        "boost": 1.4,
        "name": "Orange GT 1.5"
    },
    {
        "image": "largerainbow.png",
        "boost": 2.7,
        "name": "Rainbow RaceCar"
    },
    {
        "image": "tech.png",
        "boost": 4.0,
        "name": "Tech Car Prime"
    },
    {
        "image": "tron.png",
        "boost": 7.7,
        "name": "Turbo Tron"
    },
    {
        "image": "gold.png",
        "boost": 9.7,
        "name": "Godly Gold 2.0"
    }
]
car_image = cars[0]["image"]
boost = cars[0]["boost"]
scores = []


def roll():
    global car_image, money, boost
    if money > 150:
        money -= 150
        carr = random.choice(cars)
        if carr["image"] != car_image:
            car_image = carr["image"]
            boost = carr["boost"]
        else:
            carr = random.choice(cars)
            car_image = carr["image"]
            boost = carr["boost"]
        
        save()

filename = "Highscores.json"
def save():
    data = {
        "scores": scores,
        "rank": rank,
        "high_score": high_score,
        "money": money,
        "car_image": car_image,
        "boost": boost,
        "name": username
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)



def load():
    global high_score, rank, high_score, money, car_image, boost, username
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            scores_copy = data.get("scores", [])
            rank = data.get("rank", "Key Crawler")
            money = data.get("money", 10)
            username = data.get("name", random.choice(names))
            car_image = data.get("car_image", cars[0]["image"])
            boost = data.get("boost", cars[0]["boost"])
            if len(scores_copy) > 0:
                scores_copy.sort()
                if scores_copy[-1] > high_score:
                    high_score = scores_copy[-1]
    except(json.JSONDecodeError, FileNotFoundError):
        high_score = 0

def show_options():
    pygame.draw.rect(screen, (180, 180, 180), (center_x - 150, center_y - 150, 300, 400))
    pygame.draw.rect(screen, (140, 140, 140), (center_x - 100, center_y - 130, 180, 80))
    screen.blit(pygame.font.Font(None, 60).render("HOME", True, (255, 255, 255)), (center_x - 80, center_y - 110))
    pygame.draw.rect(screen, (140, 140, 140), (center_x - 100, center_y, 180, 80))
    screen.blit(pygame.font.Font(None, 80).render("TOP", True, (255, 255, 255)), (center_x - 80, center_y + 10))
    pygame.draw.rect(screen, (140, 140, 140), (center_x - 100, center_y + 140, 180, 80))
    screen.blit(pygame.font.Font(None, 50).render("BOTTOM", True, (255, 255, 255)), (center_x - 90, center_y + 160))
    pygame.draw.rect(screen, (255, 0, 0), (width - 80, 50, 50, 50), border_radius=3)
    screen.blit(pygame.font.Font(None, 45).render("X", True, (255, 255, 255)), (width - 65, 60))

garage = False
options = False
def show_garage():
    screen.fill((100, 100, 100))
    imagey = pygame.image.load(car_image)
    screen.blit(pygame.transform.scale(imagey, (imagey.get_width() * 3, imagey.get_height() * 3)), (150, center_y - 120))
    screen.blit(pygame.font.Font(None, 70).render(f"HIGH SCORE : {int(high_score)}", True, (255, 255, 255)), (720, center_y + 60))
    screen.blit(pygame.font.Font(None, 35).render(rank, True, (255, 255, 0)), (720, center_y - 60))
    screen.blit(pygame.font.Font(None, 50).render(username, True, (255, 255, 255)), (720, center_y - 100))
    screen.blit(pygame.font.Font(None, 40).render(f"${money}", True, (0, 245, 0)), (width - 200, 80))
    pygame.draw.rect(screen, (255, 0, 0), (width - 80, 50, 50, 50), border_radius=3)
    screen.blit(pygame.font.Font(None, 45).render("X", True, (255, 255, 255)), (width - 65, 60))
enemy_image = random.choice(cars)["image"]
sentences = [
    [
        "Ask dads salad ads add salsa gall.",
        "Ads as glass salad salsa fag.",
        "A glad lad had a salad at gala.",
        "A glad lad had a salad at gala.",
        "A glad lad had a salad at gala.",
        "Had a lass dash as all fell?",
        "Jack had a salad, Jill had salsa."
    ],
    [
        "Get out of here you ugly rat.",
        "Are you a good guy or are you?",
        "Jake tried to sell weird stuff.",
        "He tried to sell a fake jewel.",
        "A tired joker sells fake stuff.",
        "Sharks will always eat sweet food."
    ],
    [
        "The biggest ocean is Pacfic ocean.",
        "Jack went to Middle School League!",
        "Brown fox jumped over the lazy dog."
    ]
]
indexy = 0
if row == "Home Row":
    indexy = 0
elif row == "Top Row":
    indexy = 1
elif row == "Bottom Row":
    indexy = 2
sentence = sentences[indexy][random.randint(0, len(sentences[indexy]) - 1)]
index = 0
player = ""
font = pygame.font.SysFont("Arial", 70)
running = True
clicked = False
car_x = -pygame.image.load(car_image).get_width() // 5
enemy_x = -pygame.image.load(enemy_image).get_width() // 5
playing = False
wpm = 0
load()
box = pygame.image.load("box.png")

while running:
    elapsed = (pygame.time.get_ticks() - start_time) / 1000
    enemy_elapsed = pygame.time.get_ticks() - enemy_time
    minutes = elapsed / 60
    if naming:
        add_name()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            clicked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not playing:
                if not start:
                    
                    if pygame.Rect(center_x - 55, center_y + 55, 180, 60).collidepoint(event.pos):
                        if not garage and not options:
                            playing = True
                            background = random.choice(backgrounds)
                            start = True
                            player = ""
                            letters_typed = 0
                            index = 0
                            
                            words_typed = 0
                            car_x = -pygame.image.load(car_image).get_width() // 5
                            enemy_x = -pygame.image.load(enemy_image).get_width() // 5
                            start_time = pygame.time.get_ticks()
                    if pygame.Rect(width - 80, 50, 50, 50).collidepoint(event.pos):
                        garage = False
                        playing = False
                        start = False
                        options = False
                    if pygame.Rect(20, center_y, 140, 70).collidepoint(event.pos) and not options:
                        garage = True
                    if pygame.Rect(width - 180 - 20, height - 200, 180, 70).collidepoint(event.pos) and not garage and not start:
                        options = True
                    if options:
                        if pygame.Rect(center_x - 100, center_y - 130, 180, 80).collidepoint(event.pos):
                            row = "Home Row"
                        if pygame.Rect(center_x - 100, center_y, 180, 80).collidepoint(event.pos):
                            row = "Top Row"
                        if pygame.Rect(center_x - 100, center_y + 140, 180, 80).collidepoint(event.pos):
                            row = "Bottom Row"
                    if pygame.Rect(width - 150, center_y - 25, box.get_width(), box.get_height()).collidepoint(event.pos):
                        roll()
                    
                if pygame.Rect(center_x - 250, center_y + 40, 200, 80).collidepoint(event.pos):
                    if not garage:
                        if start:
                            start = False
                            playing = False
                            garage = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n and not clicked:
                if not start and not playing:
                    if not garage and not options:
                        clicked = True
                        naming = not naming
            if event.key == pygame.K_BACKSPACE:
                if player:
                    index -= 1
                    player = player[:-1]
            else:
                if playing:
                    if index <= len(sentence) - 1 and event.unicode == sentence[index]:
                        
                        index += 1
                        player += event.unicode
                        car_x += (39 + boost)
                        
                    if car_x >= center_x + center_x / 2 + 30:
                        letters_typed += len(player)
                        words_typed = letters_typed / 5
                        wpm = words_typed // minutes
                        scores.append(wpm)
                        if wpm > high_score:
                            high_score = wpm
                        money += 25
                        save()
                        sentence = sentences[indexy][random.randint(0, len(sentences[indexy]) - 1)]
                        playing = False
                    
    
    clock.tick(60)
    if start:
        screen.fill(background)
    elif not start:
        screen.fill((50, 50, 50))
    words_typed = letters_typed / 5
    key = pygame.key.get_pressed()
    if row == "Home Row":
        indexy = 0
    elif row == "Top Row":
        indexy = 1
    elif row == "Bottom Row":
        indexy = 2
    if start and not garage and not naming:
        pygame.draw.rect(screen, (225, 0, 0), (0, center_y - pygame.image.load(car_image).get_height() - 40, width, 20))
        pygame.draw.rect(screen, (225, 0, 0), (0, center_y + 170 + pygame.image.load(car_image).get_height() - 40, width, 20))
        pygame.draw.rect(screen, (100, 100, 100), (0, center_y - pygame.image.load(car_image).get_height() - 20, width, 300))
        screen.blit(finish, (center_x + center_x / 2 + 30, center_y - pygame.image.load(car_image).get_height() - 31))
         
        screen.blit(pygame.image.load(car_image), (car_x, center_y - pygame.image.load(car_image).get_height() // 2))
        screen.blit(pygame.image.load(enemy_image), (enemy_x, center_y + pygame.image.load(enemy_image).get_height()))
    if not naming and not playing and not start:
        pygame.draw.rect(screen, (150, 150, 150), (20, center_y, 180, 70))
        f = pygame.font.Font(None, 65)
        screen.blit(f.render("Garage", True, (255, 255, 255)), (30, center_y + 10))
        pygame.draw.rect(screen, (210, 210, 0), (width - 180 - 20, height - 200, 180, 70))
        screen.blit(f.render("Rows", True, (255, 255, 255)), (width - 160 - 20, height - 190))
    if not playing:
        if garage:
            show_garage()

    if not naming and not playing and not garage:
        if start:
            if car_x < center_x + center_x / 2 + 30:
                string = font.render(f"You Lost! HIGH SCORE : {int(high_score)}", True, (255, 0, 0))
            elif car_x >= center_x + center_x / 2 + 30:
                string = font.render(f"You Won! HIGH SCORE : {int(high_score)}", True, (255, 255, 0))
            screen.blit(string, (center_x - 350, center_y - 50))
            pygame.draw.rect(screen, (0, 0, 255), (center_x - 250, center_y + 40, 200, 80))
            screen.blit(font.render("Home", True, (255, 255, 255)), (center_x - 245, center_y + 45))
        else:
            screen.blit(pygame.font.SysFont('arial', 90, bold=True, italic=True).render("RacingType", True, (255, 0, 0)), (center_x - 300, 120))
            pygame.draw.rect(screen, (255, 0, 0), (center_x - 55, center_y + 55, 140, 60))
            string = pygame.font.Font(None, 35).render(">>RACE<<", True, (255, 255, 255))
            screen.blit(string, (center_x - 50, center_y + 70))
            screen.blit(box, (width - 150, center_y - 25))
        wpm_text = font.render(f"WPM: {int(wpm)}", True, (0, 0, 0))
        if start:
            screen.blit(wpm_text, (50, 50))
        rank = get_rank(high_score)
        if options:
            show_options()
     
   
    if playing:
        string = font.render(sentence, True, (255, 255, 255))
        screen.blit(string, (50, height - 100))
        string = font.render(player, True, (100, 100, 100))
        screen.blit(string, (50, height - 100))
        cursor_x = font.size(player)[0] + 40
        screen.blit(font.render("|", True, (0, 0, 200)), (cursor_x, height - 100))
        if letters_typed > 0 and minutes > 0.01:
            wpm = words_typed / minutes
        else:
            wpm = 0

        if minutes >= 0.02 and enemy_elapsed >= 190:
            if row == "Home Row":
                x = random.randint(36, 40)
            elif row == "Top Row":
                x = random.randint(40, 44)
            elif row == "Bottom Row":
                x = random.randint(47, 56)
            if enemy_x + x < center_x + center_x / 2 + 39:
                enemy_x += x
                enemy_time = pygame.time.get_ticks()
            else:
                letters_typed += len(player)
                words_typed = letters_typed / 5
                wpm = words_typed / minutes
                scores.append(wpm)
                if wpm > high_score:
                    high_score = wpm
                save()
                if letters_typed > 0:
                    wpm = words_typed / minutes
                money += 15
                sentence = sentences[indexy][random.randint(0, len(sentences[indexy]) - 1)]
                playing = False

    pygame.display.update()

save()
pygame.quit()
