# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg test = ".jpg"
image bg default = ".jpg"

image mc test = ".jpg"
image mc defauklt = ".jpg"

# Declare characters used by this game.
define mc = Character("Main Character") #chhange this, add color
define d = Character("Death")
define gol = Character("Goddess of Life")
define dk = Character("Dragon King")

#various variable names, to be tested
$male = False
$lovepoints = 1
$food = 0
$hp = 100

# The game starts here.
label start:
    mc "Abandon all hope ye "
    extend "who enter here"

    menu:
        "Ok, sure":
            jump testend
        "Nah":
            jump otherend



label testend:
    d "You've reached the end of the game, congratulations"
    return

label otherend:
    gol "This is the other end"
    return