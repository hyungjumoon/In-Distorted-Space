# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

define gdr = Character("Good Dragon Ruler")
define gdl = Character("Dragon Librarian")

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
    "Your heart is still pounding from the sight of the giant beast."
    extend " You can continue travelling towards..."

    menu: 
        "The jungle where the dragon was headed":
            jump gooddragons
        "Continue traveling in the direction that you were headed":
            "After travelling, you find that you have reached a crossroads."
            jump crossroad

label gooddragons:
    #Insert good dragon jungle city
    "You find yourself faced with a majestic marble city in the Jungle... with dragons flying around it. The sight amazes and terrifies you at the same time. Do you..."
    menu:
        "Flee from the city":
            $time = time + 1 
            "After travelling, you find that you have reached a crossroads."
            jump crossroad
        "Approach the city":
            c1 "Are you crazy? You know that dragons EAT PEOPLE right? God you must be insane."
            c2 "Oh, maybe they’re friendly. After all, that one dragon back then saved our lives!"
            jump gooddragoncity

label goodcityfront:
    "Nevertheless, you decide to cautiously approach the city."
    "At the front you meet a gatekeeper who ROARS FEROCIOUSLY at you"
    #*Insert ROAR sound clip*
    menu:
        "FLEE":
            jump deadend
        "Present the Glowing Rock":
            "The dragon seems pleased, and escorts you into the city."
            jump goodcityinterior
        #"Leave behind c1, whose whining was not helpful anyway and FLEE"
        #    "After running away for your life, you and c2 find that you have arrived in front of a crossroads."
        #    jump crossroad
        
label goodcityinterior:
    "You are inside the gorgeous marble city. Magestic dragons fly all around you and you marvel at their horrible beauty."
    "You follow the gatekeeper towards what appears to be the center spire of the city."
    "You approach a regal looking dragon. Suddenly, a voice appears in your head"
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
    jump goodcitycenter

label goodcitycenter:
    menu:
        "Fountain":
            "You see many dragons gathered around a giant fountain."
            jump goodcitycenter
        "Library":
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
            $time = time - 1 
            jump templeoftime
        "Nursery":
            "You see a bunch of baby dragons. D'awww how cute."
            jump goodcitycenter
        "Leave the city":
            c1 "We had nothing to do in a city of DRAGONS anyway. Good riddance."
            "You walk away from the magestic city and wander until you reach a crossroads."
            jump crossroad

label indistortedspace:
    "You feel like you are floating, yet CRUSHED by the pressure at the same time."
    extend " You are burning and freezing."
    extend " You are in pain, but also numb."
    extend " The world is dark, but blindingly bright."
    "You are In Distorted Space,"
    extend " stuck In Broken Time."
    "You wander around blindly... Well as much as you could consider it 'wandering'"
<<<<<<< HEAD:game/stella script.rpy
    extend " It's more like swimming in some sort of jello. Your limbs feel heavy and given that you can't see anything, you can't actually tell if you're moving or not."
    "And you slug on..."
    extend " and on..."
    extend " and on..."
    extend " and on..."
=======
    extend " It's more like swimming in some sort of "
>>>>>>> origin/master:game/stella script.rpy

label deadend:
    "The dragon eats you and you exist in its stomach acid for all of eternity."
    return
