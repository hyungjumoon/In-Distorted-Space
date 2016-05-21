# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define mc = Character("Main Character") #chhange this, add color
define d = Character("Death")
define gol = Character("Goddess of Life")
define dk = Character("Dragon King")
define c1 = Character("Companion 1")
define c2 = Character("Companion 2")
define gd = Character("Good Dragon")
define pg = Character("Innkeeper")

#various variable names, to be tested
$male = False
$lovepoints = 1
$food = 0
$hp = 100
$time = 0
$goodDragTown=False

# The game starts here.
label start:
    mc "Abandon all hope ye "
    extend "who enter here"

    menu:
        "Ok, sure":
            "wise choice"
            jump introduction
        "Nah":
            jump crossroad

label forest:
    "You set out into the wild. It’s the first time you’ve seen the sky in ages since the remainder of humanity has been crammed into the walled city for protection."
    "The sky is surprising clear and beautiful. Around you is a green forest and you can see the komorebi as light filters through the leaves. Birds are chirping, and frankly, it looks like a typical idyllic fantasy forest."
    mc "Well I guess we set off now!"
    c1 "Y’all do realize this is like a suicide mission don’t you? We have no map, a limited supply of rations, and no leads. We volunteered to help with population control."
    cs "Yes, this is quite a hopeless quest. But look around you! The world is teeming with beauty. Don’t you want to share this sight with everyone who is stuck within the walls? And what’s the worst that could happen? After all, we can’t die!"
    mc "Indeed. It’s far too early to get discouraged now. Come, let us explore this beautiful world."
    "You wander through the forest for some time."
    #Insert boar image
    extend " Suddenly, a wild boar charges out of the forest and attacks!"
    "Luckily, all three of you are well equipped with tools and healthy."
    extend " However, the encounter with the boar proves much more difficult than one would anticipate because the boar cannot be killed, merely wounded."
    "Eventually you tire out the boar and he retreats."
    #Remove boar image
    "However, much time has passed and the sun is starting to set."
    extend " You eat some of the food rations that you set out with, which helps heal you from the wounds acquired during the boar fight."
    c2 "Hey guys, it’s been a long day. Why don’t we climb up into some trees and call it wraps?"
    c1 "Are you kidding? We can’t sleep in trees. That’s too close to the skies... and the dragons. We should continue on. MC, what do you think?"

    menu:
        "Sleep in the trees": #maybe increase the time counter?
            #tree image
            "You climb up onto a tree, and set up a hammock of sorts. It’s uncomfortable, but it’ll do."
            "The next morning, you wake up early and eat some breakfast and set out on your quest again."
            #abandoned city image
            "Wow! You stumbled upon an abandoned village."
            jump abandonedvillage
        "Continue forward":
            #abandoned city image
            "You reach an abandoned village just before the sun sets. How lucky! The three of you find a house to sleep in and spend the night."
            "The next morning, you wake up early and eat some breakfast and set out on your quest again."
            jump abandonedvillage
            

label abandonedvillage:
    "For the next few days, you wander around the area, making the abandoned village your base."
    extend " During one of those days, you find a shining rock and decide to take it for luck’s sake."
    "After several days with no leads, you are faced with the decision of continuing forwards, or staying at your mini basecamp and gathering supplies."

    menu:
        "Continue on":
            jump clearing
        "Stay at the abandoned village": #potential time counter +1
            "After wandering for another several days and finding nothing of interest, you decide to continue on."
            jump clearing

label clearing:
    "Eventually, you reach a clearing. It has been a long day of journeying, and you and your companions are all tired."
    extend " Suddenly, a giant centipede attacks you!"
    #Insert picture of giant centipede
    "You try to fight back, but the three of you are exhausted. You are less so trying to attack, and more so trying not to get mauled."

    #Insert DRAGON picture***
    "A dragon SWOOPS in from the sky. The three of you cower in fear."
    "Instead, the dragon grabs hold of the giant centipede, and you have been saved."
    "Your heart is still pounding from the sight of the giant beast. You can continue travelling towards..."

The jungle where the dragon was headed
//JUMP TO GOOD DRAGONS
Continue traveling in the direction that you were headed
After travelling, you find that you have reached a crossroads. 
//JUMP TO CROSSROADS



label refugeetown:
    "You arrive at a modest but dilapidated town. It appears to be inhabited by humans"
    c2 "Oh look! It's a town of people! It's been a while since we hmet other humans!"
    c1 "Eh. This area looks lawless to me. We're probably going to get robbed and murdered in our sleep."
    c2 "Well, at least we'll die in a comfortable bed instead of on the hard ground, I see an inn over there!"
    mc "Agreed, we need a place to spend the night. The town may look sketchy, but the inn looks safe."

    "Upon arriving in the inn, you are greeted by an attractive innkeeper."
    pg "Welcome to my inn? You don't look like you're from around here."
    mc "We would like a place to stay the night, along with some food."
    pg "I can provide all that but it'll cost you this much."
    c1 "What! That's outrageous! Why don't you just rob us instead?"
    "Upon hearing this, the pirate girl pulls out a gun from under the counter and points it at the companion."
    pg "if you don't like it, leave. However, good luck finding another honest inn like this one. Now pay me or get out."
    mc "Please calm down. And you, be quiet. We'll gladly pay to stay here."
    extend "With an innkeeper like you, this must be the safest place in town."
    pg "Haha, I used to be a pirate back in the day, until \"that event\" happened."
    pg "Well, actually I was kicked off for helping a stowaway."
    pg "Past aside, here are your keys, it's been a pleasure doing "

    jump testend

label baddragons:
    "bad drags"
    jump testend

label gooddragons:
    "good drags"
    jump otherend

label testend:
    d "You've reached the end of the game, congratulations"
    return

label otherend:
    gol "This is the other end"
    return