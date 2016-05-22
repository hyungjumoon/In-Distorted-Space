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
define c1 = Character("Tomo-kun")
define c2 = Character("Tomo-chan")
define gd = Character("Good Dragon")
define pg = Character("Innkeeper")
define mg = Character("Mysterious Girl")

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
    extend " It was the best of times,"
    " it was the worst of times."
    extend " The churches faced revolt, collapse - their afterlife was lost to them forever." 
    "There were a few gruesome attempts at forcibly crossing that forbidden barrier between life and death, trying to claim their lives’ investment in holier things. But they were small bumps in the collective good feeling."
    "Still, perhaps it was then that we began to realize this immortality business wasn’t all roses..."

    jump otherend

label crossroad:
    "You arrive at a crossroads. You see different roads branching to differnt parts of the region."
    "One road, lined with trees, leads to a leafy jungle."
    extend " Another road cobbled with stones leads to some looming cliffs."
    extend " The final road follows a flowing river."

    "In which direction do you wish to go?"
    menu:      #add dialogue while travelling
        "The Jungle":
            "You decide to follow the leafy road."
            $time = time + 1
            jump gooddragons
        "The Cliffs":
            "You decide to follow thhe rocky road."
            jump baddragons
        "The Stream":
            "You decide to follow the road next to the river."
            jump refugeetown

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
    extend " With an innkeeper like you, this must be the safest place in town."
    pg "Haha, I used to be a pirate back in the day, until \"that event\" happened."
    pg "Well, actually I was kicked off for helping a stowaway."
    pg "Past aside, here are your keys, it's been a pleasure doing business with you."

    "You spend a pleasant night at the inn after a simple but hearty dinner."
    "You wake up in the morning and head to the fireplace in the lounge to warm up. You are joined by your companions"
    "You begin discussing what to do next in your mission to unkill death."
    
    mc "We need to find a lead about where Death went or disappeared to"
    c1 "There's no clues, we've been wandering aimlessly."
    c2 "Well, we've travelled far and wide. It's better than being stuck inside those walls."

    "Your innkeeper arrives with your breakfast of toast and marmalade."

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
    jump templeoftime

label baddragons:
    "bad drags"
    jump testend

label gooddragons2:
    "good drags"
    jump otherend

label templeoftime:
    "After a long and arduous travel, the party arrives at the location marked on the map."
    "Once there, the party is struck silent by the sight of an aging massive crater."
    c2 "What happened here?"
    c1 "Nothing good, I bet"
    mc "I can see a person over there, we should ask them for any leads."

    "The party approaches a mysterious girl staring morosely at the crater."

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

    jump otherend

label testend:
    d "You've reached the end of the game, congratulations"
    return

label otherend:
    gol "This is the other end"
    return