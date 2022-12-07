import math 

def padel_cost_court(court_type):
    if court_type == 'indoor':
        idk = 30 

    if court_type == 'outdoor':
        idk = 20

    return idk

def rackets_cost(racket_brand):
    if racket_brand == 'Bullpadel':
        price = 100

    if racket_brand == 'Nox':
        price = 140
    
    if racket_brand == 'Siux':
        price = 200
    
    return price

def padel_balls_cost(balls_boxes):
    balls_price = 2
    if int(balls_boxes) > 1:
        # it suposed to minus 0.5 for each ball if the balls > 1
        balls_price = ( 2 - ((0.5 * int(balls_boxes)) - 0.5) )

    return balls_price

def padel_game_cost():
    court_cost = input("indoor or outdoor ?: ")
    racket = input("Racket brand? (Bullpadel - Nox - Siux: ")
    ball_boxs = input("How many ball boxs would you like?: ")
    hours = input("For how many hours?: ")

    court_cost = padel_cost_court(court_cost)
    racket = rackets_cost(racket.title())
    ball_boxs = padel_balls_cost(ball_boxs)
    

    if int(hours) >=3:
        # it make a 20% discount if hours more than 2
        total = (court_cost + racket + ball_boxs) * (int(hours) * (20/100))
    
    else:
        total = (court_cost + racket + ball_boxs) * int(hours)

    return(total)

print("Total price is: " + str(math.ceil(padel_game_cost())) + "KD")