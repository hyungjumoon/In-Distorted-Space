﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg test = ".jpg"
image bg black = "black.png"
image bg forest = "forest.jpg"
image bg treetop = "treetop.jpg"
image bg abandonedvillage2 = "abandoned village.jpg"
image bg clearing2 = "clearing.jpg"
image bg crossroad2 = "crossroads.jpg"
image bg goodcityfront2 = "good dragon city gate.jpg"
image bg goodcityfar2 = "gdcd.jpeg"
image bg goodcityinterior2 = "good dragon city interior.jpg"
image bg throneroom = "throneroom.jpg"
image bg library2 = "library.jpg"
image bg indistortedspace2 = "distorted space.jpg"
image bg inn2 = "shop2.jpg"
image bg refugeetown2 = "rivertown3.jpg"
image bg crater = "Crater.png"
image bg templeoftime2 = "templeoftime.png"
image bg darktown = "darktown.jpg"
image bg treetopsunrise = "treetopsunrise.jpg"

image default test = "test.png"
image default flip = im.Flip ("test.png", horizontal=True)
image mcg neu = "maingirl.png"
image mcg neu flip = im.Flip ("maingirl.png", horizontal=True)
image desu neu = "death.png"
image desu neu flip = im.Flip ("death.png", horizontal=True)
image mcb neu = "mainboy.png"
image mcb neu flip = im.Flip ("mainboy.png", horizontal=True)
image inn neu = "innkeeper.png"
image inn neu flip = im.Flip ("innkeeper.png", horizontal=True)
image life neu = "life.png"
image life neu flip = im.Flip ("life.png", horizontal=True)
image kun neu = "tomokun.png"
image kun neu flip = im.Flip ("tomokun.png", horizontal=True)
image chan neu = "tomochan.png"
image chan neu flip = im.Flip ("tomochan.png", horizontal=True)
image pd neu = "plotdevice.png"
image pd neu flip = im.Flip ("plotdevice.png", horizontal=True)
image boar neu = im.Flip ("boar.png", horizontal=True)
image centipede neu = "centipede.png"
image ck neu = "Centipede killer.png"
image gdk neu = "gatekeeper.png"
image gk neu = "dragonruler.png"
image lib neu = "librarian.png"

# Declare characters used by this game.
define mc = Character("Main Character", color="#E68260") #chhange this, add color
define gol = Character("Goddess of Life", color="#A7F4FC")
define dk = Character("Dragon King", color="#7057FF")
define c1 = Character("Tomo-kun", color="#FC3030")
define c2 = Character("Tomo-chan", color="#7AFFAD")
define gd = Character("Good Dragon", color="#7057FF")
define pg = Character("Innkeeper", color="#EFF268")
define mg = Character("Mysterious Girl", color="#8DFCC1")
define gdr = Character("Good Dragon Ruler", color="#7057FF")
define gdl = Character("Dragon Librarian", color="#7057FF")
define death = Character("Death", color="#CFC7FF")

# Transform declarations
transform midleft:
    ypos 0.325
    xpos 0.0

transform midright:
    ypos 0.325
    xanchor 1.0
    xpos 1.0

transform midcenter:
    ypos 0.325
    xanchor 0.5
    xpos 0.5

transform midlefty:
    ypos 0.325
    xpos 0.25

transform midrighty:
    ypos 0.325
    xanchor 1.0
    xpos 0.75

transform boary:
    ypos 0.45
    xpos -0.1

transform centi:
    ypos 0.4
    xanchor 0.7
    xpos 1.0

transform ck1:
    ypos 0.35
    xanchor 0.7
    xpos 1.0

transform gate:
    ypos 0.325
    xanchor 0.5
    xpos 1.0

transform gking:
    ypos 0.15
    xanchor 0.7
    xpos 1.0

transform glib:
    ypos 0.15
    xanchor 0.7
    xpos 1.0

transform deathright:
    yanchor 0.4
    ypos 0.4
    xanchor 0.7
    xpos 1.0


# The game starts here.
label start:
    #various variable names, to be tested
    $ male = False
    $ lovepoints = 1
    $ food = 0
    $ hp = 100
    $ time = 0
    $ goodDragTown=False

label introduction:
    scene bg black
    with fade
    play music "music/Intro SSY.mp3"

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
    extend " It was the best of times,"
    " it was the worst of times."
    extend " The churches faced revolt, collapse - their afterlife was lost to them forever." 
    "There were a few gruesome attempts at forcibly crossing that forbidden barrier between life and death, trying to claim their lives’ investment in holier things. But they were small bumps in the collective good feeling."
    "Still, perhaps it was then that we began to realize this immortality business wasn’t all roses..."
    
    scene bg darktown
    with fade
    show mcg neu flip at midleft
    with moveinleft

    "They watch you among the maze of planks that’s Main Street."
    "Grime-filled eyes sifting through the forest of dirty men and women to stare, a horde of bodies lined up alongside the weed-choked road."
    "Since the end of Death, maintaining the City had become difficult."
    "Grass would not be trampled - the fresh planks of new buildings would sprout branches and leaves every spring - the rats that gnawed at the fresh growth too multiplied without end."
    "They’d taken to dumping all the rats they could find into a fire-pit: even if fire couldn’t kill them, it’d burn away at their flesh."
    "Sure, the meat would regenerate as soon as you turned away (one of the many gifts that deathlessness had given to all creatures, human and rat alike), but that simply meant more fuel for the flames. It was a stasis of sorts."
    "You shake your head to clear the constant hissing screams of rat-pits out of your head, and smile for the crowd. You notice that the youngest looks no less than 14. "
    "When the old people stopped dying, they banned childbirths. It’s a sort of irony - when death died, so did all future generations of the human race."
    "When death died, so followed many things. You sweep your eyes across the shantytown that’s the outer edge of the City. This is all that is left of humanity."
    "Immortality for all, shockingly, meant immortality for all - the armored titan"
    "-ic dragons of the west, originally kept in check by their food supply, multiplied once they refused to die of starvation."
    "When their food supply also failed to die of starvation...well..."
    "There was a reason all remaining humanity was crammed inside a single walled city."
    extend " The reason might have been \"massive amounts of airbourne dragon-tanks.\""
    "Dragons and men had always been at war, having never managed to get past the racism inherent with the ability or lack thereof of breathing fire. But I digress."
    "We were discussing the losers that had nothing better to do with their lives except watch a boring bunch like you walk on the street."
    "They’re here to see the newest dispatch from the Excursion Council: you, Tomo-chan, and Tomo-kun."
    extend " The fifth such team off on a grand adventure to kick ass and unkill Death."
    "It just so happens that you’re all out of ass."
    "You grin at the sullen-looking populace. Their eyes speak of despair, hopelessness - they don’t believe in their salvation, their freedom from the oppression that is deathlessness."
    "They don’t think you can do it."
    "Must not make use of their brain cells on a regular basis. This is why you’re part of the elite and they aren’t. Sucks."
    "The gate looms open ahead of you - the exit from the last bastion of humanity, the walled city of Honno. From here on out, it’s all overgrown wilderness that just won’t die no matter how many times you kill it."
    "Just the way we like it."
    
    stop music
    scene bg darktown
    with moveoutleft

    jump forest

label crossroad:
    scene bg crossroad2
    with fade
    play music "music/crossroads NGNL.mp3"

    show kun neu at midright
    with moveinright
    show chan neu at midcenter
    with moveinright
    show mcg neu flip at midleft
    with moveinright
    "You arrive at a crossroads. You see different roads branching to differnt parts of the region."
    "One road, lined with trees, leads to a leafy jungle."
    extend " Another road cobbled with stones leads to some looming cliffs."
    extend " The final road follows a flowing river."
    "In which direction do you wish to go?"
    scene bg crossroad2
    with moveoutleft
    menu:      #add dialogue while travelling
        "The Jungle":
            "You decide to follow the leafy road."
            $ time += 1
            stop music
            jump gooddragons
        #"The Cliffs":
        #    "You decide to follow the rocky road."
        #    jump baddragons
        "The Stream":
            "You decide to follow the road next to the river."
            stop music
            jump refugeetown

label refugeetown:
    scene bg refugeetown2
    with fade
    play music "music/Refuge Town Utawarerumono.mp3"
    show kun neu at midright
    with moveinright
    show chan neu at midcenter
    with moveinright
    show mcg neu at midleft
    with moveinright
    "You arrive at a modest but dilapidated town. It appears to be inhabited by humans"
    c2 "Oh look! It's a town of people! It's been a while since we hmet other humans!"
    c1 "Eh. This area looks lawless to me. We're probably going to get robbed and murdered in our sleep."
    c2 "Well, at least we'll die in a comfortable bed instead of on the hard ground, I see an inn over there!"
    mc "Agreed, we need a place to spend the night. The town may look sketchy, but the inn looks safe."
    
    stop music
    scene bg refugeetown2
    with moveoutleft

    scene bg inn2
    with fade
    play music "music/Inn Shirobako.mp3"
    show kun neu at midright
    with moveinright
    show chan neu at midrighty
    with moveinright
    show mcg neu at midlefty
    with moveinright
    show inn neu flip at midleft #right facing left
    with moveinleft

    "Upon arriving in the inn, you are greeted by an attractive innkeeper."
    pg "Welcome to my inn? You don't look like you're from around here."
    mc "We would like a place to stay the night, along with some food."
    pg "I can provide all that but it'll cost you this much."
    c1 "What! That's outrageous! Why don't you just rob us instead?"
    "Upon hearing this, the pirate girl pulls out a gun from under the counter and points it at the companion."
    pg "if you don't like it, leave. However, good luck finding another honest inn like this one. Now pay me or get out."
    mc "Please calm down. And you, be quiet. We'll gladly pay to stay here."
    extend " With an innkeeper like you, this must be the safest place in town."
    pg "Haha, I used to be a pirate back in the day, until \"that event\" happened."
    pg "Well, actually I was kicked off for helping a stowaway."
    pg "Past aside, here are your keys, it's been a pleasure doing business with you."

    scene bg inn2
    with moveoutleft

    scene bg black
    with fade
    "You spend a pleasant night at the inn after a simple but hearty dinner."
    "You wake up in the morning and head to the fireplace in the lounge to warm up. You are joined by your companions"
    "You begin discussing what to do next in your mission to unkill death."
    
    scene bg inn2
    with fade
    show kun neu at midright
    with moveinright
    show chan neu at midrighty
    with moveinright
    show mcg neu at midlefty
    with moveinright

    mc "We need to find a lead about where Death went or disappeared to"
    c1 "There's no clues, we've been wandering aimlessly."
    c2 "Well, we've travelled far and wide. It's better than being stuck inside those walls."

    "Your innkeeper arrives with your breakfast of toast and marmalade."
    show inn neu flip at midleft #right facing left
    with moveinleft

    pg "Sorry I couldn't help but overhear your conversatoin. You're looking for Death?"
    c1 "It's none of your business."
    "Tomo-kun looks like he would like to say more, but upon seeing the innkeeper reach down, he backs off."
    mc "Do you have any information that might help?"
    pg "Well, not really. However, remember the stowaway I helped?"
    extend " After we were ousted from my ship, he went off with an acquaintance and I net either of them again."
    c2 "Why does that matter?"
    pg "That was the day of the event. They coudln't have died. But I couldn't find them no matter how hard I looked."
    pg "Furhtermore there was a flash of light from the area they went to. It all seems very mysterious doesn't it?"
    mc "Given the date, yea, it is. Can you please tell us where they went?"
    "The innkeeper gives you a map and marks the location."
    mc "Thank you, you've been a good help, please take payment."
    pg "It's fine, I've charged you enough as is. Go and fix this world."
    
    scene bg inn2
    show inn neu flip at midleft
    with moveoutright

    stop music

    jump templeoftime

label baddragons:
    "bad drags"
    jump testend

label templeoftime:
    scene bg crater
    with fade
    play music "music/Temple of Time F0 Grief.mp3"
    "After a long and arduous travel, the party arrives at the location marked on the map."
    "Once there, the party is struck silent by the sight of an aging massive crater."
    show kun neu flip at midleft
    with moveinleft
    show chan neu flip at midcenter
    with moveinleft
    show mcg neu flip at midright
    with moveinleft
    c2 "What happened here?"
    c1 "Nothing good, I bet"
    mc "I can see a person over there, we should ask them for any leads."
    
    scene bg crater
    with moveoutright
    show pd neu at midright
    with moveinright

    "The party approaches a mysterious girl staring morosely at the crater."

    show kun neu flip at midleft
    with moveinleft
    show chan neu flip at midlefty
    with moveinleft
    show mcg neu flip at midrighty
    with moveinleft    
    
    mg "..it's been over twenty years since then, huh"
    mc "Excuse me, what are you talking to yourself about? Perhaps \"that event\"?"

    "Startled, the girl looks up."

    mg "I'm sorry, I didn't realize there were people here."
    c2 "Can you help us? Do you know anything about what happened here?"
    mg "This crater predates the event you are referring to."
    extend " Although to say that it is was unrelated is incorrect."
    c1 "Stop twisting your words and get to the point. We're looking for the truth of what happened and how to fix it."
    mg "Mmm, is that so? That's nice..."
    extend "Heroes trying to right the worongs of this world."
    mg "Although, the world was reduced to this state by one trying to right the worng behind this crater."
    mg "Tell me, are you sure that you are in the right?"
    mc "Right or wrong, this world must change. With no end, there are no beginnings either."
    mg "True..."
    "The girl ponders for a bit."
    mg "Very well, I will help you. "
    mg "I have certain...connections with an individual. I can take you to the place Death vanquished himself."
    mc "What?! Who are you?! \"Vanquished himself\"?!"
    mg "Find the truth yourself..."
    
    stop music
    scene bg crater
    with moveouttop

    play music "music/GOL SSS.mp3"
    "After a blur and dizzying sway, you and your companions find yourself on the floor of the Temple of Time. The mysterious girl has disappeared."
    
    scene bg templeoftime2
    with fade

    show mcg neu flip at midleft
    with moveintop
    mc "Oof!"
    show chan neu flip at midcenter
    with moveintop
    c2 "Ouch!"
    show kun neu flip at midright
    with moveintop
    c1 "Tch!"
    c2 "Where are we?"

    scene bg templeoftime2
    show mcg neu flip at midleft
    show chan neu flip at midlefty
    show kun neu flip at midrighty
    with move

    "\"You're at the Temple of Time,\" a voice responds"
    show life neu at midright
    with moveinright
    
    mc "Who are you?"
    gol "I am the Goddess of Life. I know why you have come."  
    
    c2 "Who? Never heard of you?"
    
    gol "I am the counterpart to Death. Since the dawn of time, we struggle against each other, each not being able to best the other."
    gol "Then a new avatar of Death appeared. This one was different. This one was unwilling to harm others for his benefit."
    gol "I told him that this world needed for him to disappear. Selflessly, he agreed."
    gol "However, now as time passes, I realize that the world is suffering without Death. The world needs us both to function."
    gol "Heroes, if you wish to bring Death back, you must go where none have gone, not even I."
    gol "when Death died, the paradox left a distortion in space. Enter this dsitorted space and bring him back!"
    
    c1 "How can we trust you? For all we know, you're insane!"
    mc "We got this far, show us where this space is."

    scene bg templeoftime2
    show life neu at midright
    with fade
    stop music
    jump indistortedspace

label forest:
    scene bg forest
    with fade
    play music "music/Forest Kimi ga Yobu Namae.mp3"
    show kun neu at midright
    with moveinright
    show chan neu at midcenter
    with moveinright
    show mcg neu at midleft
    with moveinright
    "You set out into the wild. It’s the first time you’ve seen the sky in ages since the remainder of humanity has been crammed into the walled city for protection."
    "The sky is surprising clear and beautiful. Around you is a green forest and you can see the komorebi as light filters through the leaves. Birds are chirping, and frankly, it looks like a typical idyllic fantasy forest."
    mc "Well I guess we set off now!"
    c1 "Y’all do realize this is like a suicide mission don’t you?"
    extend " We have no map, a limited supply of rations, and no leads. We volunteered to help with population control."
    c2 "Yes, this is quite a hopeless quest."
    extend " But look around you! The world is teeming with beauty."
    extend " Don’t you want to share this sight with everyone who is stuck within the walls?"
    extend " And what’s the worst that could happen? After all, we can’t die!"
    mc "Indeed. It’s far too early to get discouraged now. Come, let us explore this beautiful world."
    "You wander through the forest for some time."
    
    scene bg forest
    show kun neu at midright
    show chan neu at midrighty
    show mcg neu at midlefty
    with move
    stop music
    play music "music/Boar Katanagatari.mp3"
    show boar neu at boary #right, facing left
    with moveinleft

    extend " Suddenly, a wild boar charges out of the forest and attacks!"
    "Luckily, all three of you are well equipped with tools and healthy."
    extend " However, the encounter with the boar proves much more difficult than one would anticipate because the boar cannot be killed, merely wounded."
    "Eventually you tire out the boar and he retreats."
    stop music
    play music "music/Post boar Bakemonogatari.mp3"
    scene bg forest
    show kun neu at midright
    show chan neu at midrighty
    show mcg neu at midlefty
    with moveoutleft
    "However, much time has passed and the sun is starting to set."
    extend " You eat some of the food rations that you set out with, which helps heal you from the wounds acquired during the boar fight."
    c2 "Hey guys, it’s been a long day. Why don’t we climb up into some trees and call it wraps?" #turns left towards c1
    c1 "Are you kidding? We can’t sleep in trees. That’s too close to the skies... and the dragons. We should continue on. MC, what do you think?"

    scene bg forest
    with moveoutright

    menu:
        "Sleep in the trees": #maybe increase the time counter?
            scene bg treetop
            with fade
            "You climb up onto a tree, and set up a hammock of sorts. It’s uncomfortable, but it’ll do."
            scene bg treetopsunrise
            with fade
            "The next morning, you wake up early and eat some breakfast and set out on your quest again."
            scene bg abandonedvillage2
            with fade
            show kun neu at midright
            show chan neu at midcenter
            show mcg neu flip at midleft
            with moveinright
            "Wow! You stumbled upon an abandoned village."
            scene bg black
            with fade
            stop music
            jump abandonedvillage
        "Continue forward":
            scene bg abandonedvillage2
            with fade
            show kun neu at midright
            show chan neu at midcenter
            show mcg neu flip at midleft
            with moveinright
            "You reach an abandoned village just before the sun sets. How lucky! The three of you find a house to sleep in and spend the night."
            scene bg black
            with fade
            "The next morning, you wake up early and eat some breakfast and set out on your quest again."
            stop music
            jump abandonedvillage
            
label abandonedvillage:
    play music "music/Abandoned Village 2 SAW.mp3"
    scene bg abandonedvillage2
    show kun neu at midright
    show chan neu at midcenter
    show mcg neu flip at midleft
    with fade
    "For the next few days, you wander around the area, making the abandoned village your base."
    extend " During one of those days, you find a shining rock and decide to take it for luck’s sake."
    "After several days with no leads, you are faced with the decision of continuing forwards, or staying at your mini basecamp and gathering supplies."

    scene bg abandonedvillage2
    with moveoutright
    menu:
        "Continue on":
            stop music
            jump clearing
        "Stay at the abandoned village": #potential time counter +1
            "After wandering for another several days and finding nothing of interest, you decide to continue on."
            stop music
            jump clearing

label clearing:
    scene bg clearing2
    with fade
    play music "music/Clearing Kara no Kyoukai.mp3"
    show kun neu flip at midleft #most left, facing right
    show chan neu flip at midcenter #mid, facing right
    show mcg neu flip at midright #least left, facing right
    with moveinright
    
    "Eventually, you reach a clearing. It has been a long day of journeying, and you and your companions are all tired."
    
    scene bg clearing2
    show kun neu flip at midleft #most left, facing right
    show chan neu flip at midlefty #mid, facing right
    show mcg neu flip at midrighty #least left, facing right
    with move
    stop music
    extend " Suddenly, a giant centipede attacks you!"
    play music "music/CENTIPEDE AOT.mp3"
    show centipede neu at centi #facing left on the right
    with moveinright
    
    "You try to fight back, but the three of you are exhausted. You are less so trying to attack, and more so trying not to get mauled."
    "A dragon SWOOPS in from the sky. The three of you cower in fear."
    "Instead, the dragon grabs hold of the giant centipede, and you have been saved."       
    scene bg clearing2
    show kun neu flip at midleft #most left, facing right
    show chan neu flip at midlefty #mid, facing right
    show mcg neu flip at midrighty #least left, facing right
    with fade
    show ck neu at ck1
    with moveinright
    "Your heart is still pounding from the sight of the giant beast."
    
    scene bg clearing2
    show kun neu flip at midleft #most left, facing right
    show chan neu flip at midlefty #mid, facing right
    show mcg neu flip at midrighty #least left, facing right
    with moveouttop

    extend " You can continue travelling towards..."
    scene bg clearing2
    with moveoutleft
    menu: 
        "The jungle where the dragon was headed":
            stop music
            jump gooddragons
        "Continue traveling in the direction that you were headed":
            "After travelling, you find that you have reached a crossroads."
            stop music
            jump crossroad

label gooddragons:
    scene bg goodcityfar2
    with fade
    play music "music/Good City Far Madoka.mp3"
    "You find yourself faced with a majestic marble city in the Jungle... with dragons flying around it. The sight amazes and terrifies you at the same time. Do you..."
    menu:
        "Flee from the city":
            $ time += 1 
            "After travelling, you find that you have reached a crossroads."
            stop music
            jump crossroad
        "Approach the city":
            c1 "Are you crazy? You know that dragons EAT PEOPLE right? God you must be insane."
            c2 "Oh, maybe they’re friendly. After all, that one dragon back then saved our lives!"
            stop music
            jump goodcityfront

label goodcityfront:
    scene bg goodcityfront2
    with fade
    play music "music/Good city Front Owari no Seraph OST.mp3"
    show kun neu flip at midleft #most left, facing right
    with moveinright
    show chan neu flip at midcenter #mid, facing right
    with moveinright
    show mcg neu flip at midright #least left, facing right
    with moveinright
    "Nevertheless, you decide to cautiously approach the city."
    scene bg goodcityfront2
    show kun neu flip at midleft #most left, facing right
    show chan neu flip at midlefty #mid, facing right
    show mcg neu flip at midrighty #least left, facing right
    with move
    "At the front you meet a gatekeeper who ROARS FEROCIOUSLY at you"
    show gdk neu at gate
    with moveinright
    menu:
        "FLEE":
            scene bg goodcityfront2
            show gdk neu at gate
            with moveoutleft
            stop music
            jump deadend
        "Present the Glowing Rock":
            "The dragon seems pleased, and escorts you into the city."
            scene bg goodcityfront2
            with moveoutright
            stop music
            jump goodcityinterior
        #"Leave behind c1, whose whining was not helpful anyway and FLEE"
        #    "After running away for your life, you and c2 find that you have arrived in front of a crossroads."
        #    jump crossroad

label goodcityinterior:
    scene bg goodcityinterior2
    with fade
    play music "music/Good City Interior Soredemo.mp3"
    "You are inside the gorgeous marble city. Magestic dragons fly all around you and you marvel at their horrible beauty."
    "You follow the gatekeeper towards what appears to be the center spire of the city."
    "You approach a regal looking dragon. Suddenly, a voice appears in your head"
    scene bg throneroom
    with fade
    show mcg neu flip at midrighty #least left, facing right
    with moveinleft
    show chan neu flip at midlefty #mid, facing right
    with moveinleft
    show kun neu flip at midleft #most left, facing right
    with moveinleft
    show gk neu at gking
    with moveinright

    gdr "Hello tiny young ones."
    c2 "Wow! How are you talking to us?"
    gdr "You know, not all dragons hate humans. Honestly, your kind is really small and bony. Really quite a pain to eat."
    extend " Ages ago, we once were friends even."
    c1 "Hah as if we would believe you who have so terrorized us."
    c2 "(((SHHHH DO YOU WANT THEM TO EAT YOU?)))"
    gdr "Heh. We won't eat you, not having presented us with such a lovely gift. I will gladly accept it into our collection."
    extend " And truly, the dragons here do not hate humanity, even though our mindset is a rare one."
    mc "Well perhaps we can bring back history and  befriend you too."
    gdr "Perhaps. We will see how the fates play out. You are free to stay in our city for as long as you would like."
    mc "Thank you so much for your offer."
    gdr "None of the dragons here actively hate humans, but it has been ages since we have seen any of your kind."
    extend " So realize that many of the dragons will be cautious. In fact, some of our youngsters may never have seen any humans at all."
    c2 "Will do! I can't believe we're in a dragon city!"
    gdr "Indeed. Here, let me show you to the city center."

    scene bg throneroom
    with moveoutright

    jump goodcitycenter

label goodcitycenter:
    scene bg goodcityinterior2
    with fade
    show mcg neu flip at midright #least left, facing right
    with moveinleft
    show chan neu flip at midcenter #mid, facing right
    with moveinleft
    show kun neu flip at midleft #most left, facing right
    with moveinleft
    menu:
        "Fountain":
            "You see many dragons gathered around a giant fountain."
            jump goodcitycenter
        "Library":
            stop music
            play music "music/Library Steins Gate.mp3"
            scene bg goodcityinterior2
            with moveoutright
            scene bg library2
            with fade
            show mcg neu flip at midrighty #least left, facing right
            with moveinleft
            show chan neu flip at midlefty #mid, facing right
            with moveinleft
            show kun neu flip at midleft #most left, facing right
            with moveinleft
            show lib neu at glib
            with moveinright
            #*** INSERT DRAGON PICTURE ***
            "The smell of ancient books hits you as light filters in from above. The library emanates a feeling of ancient wisdom and power."
            gdl "Humans! I have not seen any of your kind in eons."
            c2 "Heehee that makes me feel kinda special." #smiling ^^ sprite
            gdl "So, you must be here to seek wisdom."
            c1 "Indeed. We want to restore Death to this world."
            gdl "Death... Death was a concept much more real to humans than to dragons before the event. Why would you want to do such a thing?"
            c1 "Your kind terrorizes all other animals on Earth. Before, at least there was balance."
            gdl "I see. Well, I am not the judge of Morality. That role goes to my brother whom you already met."
            extend " I am simply the guardian of knowledge. And if my brother decided that you were worthy, then so be it."
            "The dragon flies to a high perch and retreives a scroll."
            gdl "On this scroll there is a map."
            extend " I have indicated a location which many reports have indicated there was a brilliant flash of light on the day of the event."
            mc "Thank you greatly. We truly appreciate your wisdom."
            "You set off towards the marked location on the map."
            $ time -= 1 
            scene bg library2
            show lib neu at glib
            with moveoutleft
            stop music
            jump templeoftime
        "Nursery":
            "You see a bunch of baby dragons. D'awww how cute."
            jump goodcitycenter
        "Leave the city":
            c1 "We had nothing to do in a city of DRAGONS anyway. Good riddance."
            "You walk away from the magestic city and wander until you reach a crossroads."
            scene bg goodcityinterior2
            with moveoutright
            stop music
            jump crossroad

label indistortedspace:
    scene bg indistortedspace2
    with fade
    "You feel like you are floating, yet CRUSHED by the pressure at the same time."
    extend " You are burning and freezing."
    extend " You are in pain, but also numb."
    extend " The world is dark, but blindingly bright."
    "You are In Distorted Space,"
    extend " stuck In Broken Time."
    "You wander around blindly... Well as much as you could consider it 'wandering'"
    extend " It's more like swimming in some sort of jello. Your limbs feel heavy and given that you can't see anything, you can't actually tell if you're moving or not."
    "And you slug on..."
    extend " and on..."
    extend " and on..."
    extend " and on..."
    extend " and on..."
    c2 "EEK! I bumped into something."
    show chan neu flip at midleft
    with fade
    "\"Who has entered this dreary realm, the graveyard for gods?\""
    c1 "More like we should be asking who YOU are."
    show kun neu flip at midlefty
    with fade
    mc "Relax c1. We are here to restore death."
    show mcg neu flip at midrighty
    with fade
    "The figure laughes a slightly maniacal laugh. \"You what?\" Ahahahahaha"
    "\"You all must be mad. Entirely mad.\""
    "\"People search to banish death for ages, and within 20 years, people want to bring death back?\""
    "\"Mad. Entirely mad. The entire lot of you.\""
    death " I came here out of self-sacrifice and you humans are telling me that you want me BACK?"
    show desu neu at deathright
    extend " But you know what? I'll entertain you."
    death "Luckily for you, this place is horribly uncomfortable and I'm getting quite bored."
    death "So how are you going to get us out?"
    mc "Uhhhhh... RIP WE DIDN'T THINK THAT FAR. (In fact, the writers of this plot did not think of that either)"
    death "HAHAHA AS IF you mortals could possibly have that power."
    extend " Please, of course I can get us out of here. I only stayed In Distorted Space because I thought that humanity wanted it."
    death "Apparently in this day and age, humans don't even know how to appreciate my great self-sacrifice."
    extend " But yes I'll come with you. Perhaps a touch of Death will make you remember how kind my actions were."
    death "Let's begin. Brace yourselves."
    death "I am the MIGHTY and ALL POWERFUL DEATH."
    extend " TIME, hear my cry. The balance of the world must be restored."
    extend " For in truth, the goddess was wrong. It is not \"Neither can live while the other survives,\""
    extend " but \"Earth. Fire. Air. Water. Only the Avatar can master all four elements and bring balance to the world.\""
    death "Wait that's not it."
    extend " ROW ROW FIGHT THE POWAH."
    death "Wait that's not it either."
    extend " Wait it's this one, I'm sure it's this one."
    extend " The world needs darkness and light, shadow and illumination, because without the two there can be no balance."
    "Suddenly, A blinding light envelops you, and the warmth of existance once again fills your limbs. You can feel again, you can breathe again. You are alive again. You are back in the real world."
    if time>0:
        jump failend
    else:
        jump goodend

label deadend:
    scene bg black
    with fade
    "The dragon eats you and you exist in its stomach acid for all of eternity."
    return

label failend:
    scene bg black
    with fade
    play music "music/Fail End Angel Beats.mp3"
    "You failed. You took so long that by the time death was revived, the entire planetary ecosystem had collapsed. The dragons captured all the humans and placed them in farms."
    extend " The tenuous reliance by dragons on human farms for sustenance meant that when humans started dying again, the dragons died of starvation."
    "Every human on earth was hunted down until there were none left. And the remaining dragons scavenged for prey until they were driven to cannibalism."
    stop music
    jump credits

label goodend:
    scene bg black
    with fade
    play music "music/Good End Ebb and Flow.mp3"
    "With Death returning to the world, balance has been restored. The Dragon population ceases being the main predator, and many will die out because they don't have enough sustenance."
    extend "Meanwhile, in the last stronghold of humanity there will be a decrease in population because the elderly and sick have died."
    "However, as per usual, the resilient race known as humanity will bounce back, and everything eventually returns to the status quo before In Broken Time."
    stop music
    jump credits

label credits:
    play music "music/Credits ODDS&ENDS (piano).mp3"
    "Credits"
    extend " Hyugnju (Hector) Moon - \"Plot\" Developer, Writer, Spriter, Hacky Animator"
    extend " Stella Yang - \"Plot\" Developer, Writer, Spriter, Background Fixer, Music Picker"
    extend " Bill Tang - Intro writer, Edgemaster, Best known for leaving before finishing his route"
    extend " Jason Thomas - AFK"
    extend " Chelsea Li - Less AFK than Jason since she actually chatted with us at midnight xD"
    return

label deocide:
    scene bg black
    with fade
    "gol dies"
    return

label testend:
    scene bg black
    with fade
    death "You've reached the end of the game, congratulations"
    return

label otherend:
    scene bg black
    with fade
    gol "This is the other end"
    return