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
            jump introduction
        "Nah":
            jump otherend

label introduction:
    "Nobody really noticed when Death died."
    "It was an end to a great universal truth, yes."
    extend " It was the end to the great question that dogged in our footsteps, sooner or later - when comes our time?"
    extend " It was, perhaps, even the end to that struggle we know as the human condition."
    "Immortality, as they say, is a hell of a drug."
    "But when that day came, when Death looked itself in the mirror and decided he was long overdue, nobody cared."

    "Maybe there was a little breeze, a little vibrant wind fluttering around our heels, new life breathed into our movements."
    extend " Maybe the sky lightened a bit."
    extend " Maybe we had a few miracles in our hospitals."
    "Who knows."
    "Death was the disquieting neighbor that we never liked. He moved out without much fanfare."
    "A few weeks down the line, though, the world started to feel his absence."
    extend " The terminally sick terminated their sickness."
    extend " War became drawn-out; muggings became shocking."
    "Life had become a fact"
    extend "- death, a mistake rectified."
    "There was no danger anymore of alcohol poisoning - so the celebrations became a bit more drunken."
    "To nearly all, life glittered with a sheen unseen, perhaps what it truly was: well and perfect, when the grime of certain death was scrubbed away."
    "So for weeks, we held Death a mighty funeral, banquets, games. Perhaps somebody mourned him, but the rest of us were merely freedmen."
    "Of course, behind all this, there were a few chinks needed smoothing out: the churches faced revolt, collapse - their afterlife was lost to them forever. There were a few gruesome attempts at forcibly crossing that forbidden barrier between life and death, trying to claim their lives’ investment in holier things. But they were small bumps in the collective good feeling."
    "Still, perhaps it was then that we began to realize this immortality business wasn’t all roses..."

    jump testend

label testend:
    d "You've reached the end of the game, congratulations"
    return

label otherend:
    gol "This is the other end"
    return