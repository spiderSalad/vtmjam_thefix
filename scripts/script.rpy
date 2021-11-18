# The script of the game goes in this file.

# The game starts here.

label start:

    # In-game variable initializations, to make sure they get tracked by Ren'py

    $ pc = PlayerCharacter()
    $ opinions = {"Anarchs": opinion_anarchs, "Camarilla": opinion_camarilla, "Your Ghoul": opinion_ghoul, "Local Ventrue": opinion_ventrue, "Local Nosferatu": opinion_nosferatu}

    # Characters used by this game. The color argument colorizes the name of the character.

    define me           = Character(_pc["first"], color = "#fefefe")
    define beast        = Character("The Beast", color = "#ee1212")
    define sire         = Character("Ms. Walker", color = "#002366")
    define pcghoul      = Character(_pcGhoul["first"], color = "#803CA2")

    # Show a background. This uses a placeholder by default, but you can add a file (named either "bg room.png" or "bg room.jpg") to the images directory to show it.

    scene bg hotel room
    with fade

    if not MUSIC_MUTED:
        play music audio.scene1_awakening fadeout 1.0 fadein 1.0

    $ pc.damage(KEY_HP, KEY_SPFD, 5)
    $ pc.damage(KEY_HP, KEY_AGGD, 2)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "..."

    "There's nothing. No light, no sound. No feeling, no warmth. No life."

    "..."

    "Until suddenly, there is. Oblivion recedes from around me and I float up into consciousness, like a bloated corpse bobbing at the surface of a lake. Rigor mortis fades as stolen life flows into my limbs. I {i}rise{/i}."

    "The experience is viscerally unpleasant. Comfortably numb nothingness instantly replaced with agonizing sensation everywhere, all at once. {i}Ugh.{/i} Fortunately, it's over as quickly as it started."

    play sound audio.phone_alarm

    "And there's the alarm. After a few seconds I reach for my phone and shut it off."

    "I don't actually need an alarm - none of my kind do. I couldn't stay asleep past sundown if I wanted to. I've tried."

    "But the obnoxious jingle is calming, somehow. Makes me feel a bit more like the human being I used to be. Normal. ...But not too much like her. Not too normal."

    "Alright, enough navel-gazing. I've got work tonight, and the bosses don't like to be kept waiting. Except..."

    "I might {i}have{/i} to keep them waiting, because I have a problem."

    $ pc.setHunger(3) # plays tiger growl
    beast "..."

    "It hits like a punch to the gut. Can't focus, can't think of anything else through the ache spreading everywhere. My arms, my legs, my chest, my throat, my guts, behind my eyes. The Beast is hungry. I have to feed."

    beast "You're goddamned right you do. The fuck were you thinking, letting us go hungry like that?"

    "Kindred are sustained by blood - our own and, in turn, others'. With blood, I can do and feel miraculous things. Without it... well, this happens. I'll starve, go mad, and die. Blood demands blood, and the Beast is its voice."

    $ if DEBUG: pc.setHunger(4, playSound = False)

    beast "Aptly put. And how fortunate for us that this cesspit of a city has blood to spare."

    "The only problem is getting to it. Without getting caught. Without killing someone, or hurting them more than I have to."

    "Well, those are the problems for most Kindred. For Blue Bloods, our heritage makes things even more complicated."

    "Not my human heritage - that's a whole other thing. My Kindred bloodline, passed down to me from my sire the night she drank my blood and I died in ecstacy. The night she fed my corpse some Blood of her own. The night I {i}rose{/i}."

    beast "I thought you said you were done navel-gazing."

    "Shut up and let me think."

    "I actually have some bagged blood in the mini fridge. For emergencies, and in case I need to host another Kindred in the (actually pretty nice for once) hotel room the Seneschal put me up in. I {i}could{/i}, in theory, drink that."

    $ if DEBUG: pc.setHunger(5, playSound = False)

    beast "We could also, in theory, drink the contents of the nearest S-bend."

    "For most Kindred, preserved blood is like thin gruel - flavorless and passably nourishing at best. For a Blue Blood, it's almost a complete non-starter. My Beast is like some Tamil king's pampered pet panther, a picky predator that won't abide the bagged stuff."

    beast "One of us has to have standards."

    "Every member of Clan Ventrue has what some of us like to call a \"refined palate\". Only certain kinds of blood will do, and every Blue Blood is different. Natural blondes. College graduates. Tourists. Cancer patients. Anything, potentially."

    "Drink the wrong kind of blood, and your body will barf it right back up all over your nice new blouse. But my sire taught me that Ventrue {i}can{/i} feed outide of their palates. It just takes a tremendous exertion of will to fight the Beast and keep the blood down."

    beast "Do you really want to exhaust your limited mental faculties fighting me for the right to drink medical waste? No one's going to coddle you this time if you fall apart again."

    "... So anyway, I could brace myself and try to hork down what's in the fridge, like when I used to make myself throw up the mornings after the best ragers. Or I could take a big risk, and try to hunt in an unfamiliar city."

    "I know my type. I know what I need. And I {i}do{/i} have permission. But hunting is risky even under the best of circumstances, and if anything goes wrong I'll have added to the problem I was flown out here to fix."

    "That would be an {i}extremely{/i} bad look, and I {i}really{/i} can't afford that now. Especially not if it comes back on my sire."

    $ pcname = _pc["first"]
    $ ghoulname = _pcGhoul["first"]

    $ if DEBUG: pc.setHunger(3)

    "Or I could just suck it up and deal. By the end of the briefing [ghoulname] should be in town, and he can pick up someone I'll like. He's good at that sort of thing. It'll be excruciating, but if I can keep it professional the bosses might trust me more."

    menu:
        beast "You know what the smart choice is. You know what best suits our strengths. Do it. Do {i}something{/i}, before we lose our cool."

        "I'll chance it and hunt, even if it'll make me late. I know people and I know how to get what I want. Nothing ventured, nothing gained.":
            # +DEX, +CHA, +WIT, +Clandestine, +Intrigue, +Awareness | Reduce Hunger to 1 | Spend cash, -Cam opinion
            jump hunt_before_work

        "I'm strong, but I'm not going to waste effort keeping down that nasty swill. I'm cool enough to hold it together, and then I'll meet up with [ghoulname] for dinner.":
            # +STR, +COM, +RES, +Combat, +Intimidation, +Technology | +Cam opinion | Hunger remains at 3
            jump wait_until_after

        "Hunting and showing up hungry are both bad ideas. I choke down the bagged stuff, just to take the edge off. It's the safest choice with the best odds.":
            # +STA, +MAN, +INT, +Athletics, +Persuasion, +Occult | Reduce Hunger to 2, +Cam opinion | Spend 2 willpower
            jump drink_bagged_blood

    label hunt_before_work:

        beast "Yes... Wise choice, [pcname]. The bare necessities should always come first."

        "I'll just have to make this quick."

        $ pc.incScores(KEY_ATTR, _dex, _cha, _wit)
        $ pc.incScores(KEY_SKILL, _clan, _intr, _awar)
        $ story_hunted_early = True

        call choose_predator_type

        jump hunt_early

    label wait_until_after:

        beast "...Seriously? You'll regret this, you idiot. You think you can hold me back for that long?"

        "Yeah, I do."

        beast "Maybe I should take over again. Wouldn't that be fun? For me, at least."

        "Fuck you. That will {i}never{/i} happen again. I didn't understand what you were before."

        beast "Think so? Try it. Keep denying me. See what happens."

        "...It's true. I can't hold out forever. But I don't need to. I just need to get through the briefing. Then with [ghoulname]'s help I can do this the right way. I'm strong enough for that."

        $ pc.incScores(KEY_ATTR, _str, _com, _res)
        $ pc.incScores(KEY_SKILL, _comb, _inti, _tech)

        "I'm strong enough for this..."

        call choose_predator_type

        jump head_to_meeting

    label drink_bagged_blood:

        beast "No. No no no no no no no no NO we are NOT drinking that f-"

        "I pop open the fridge, grab a bag and suck that shit down like a Capri Sun."

        play sound audio.beastgag

        beast "..."

        "{i}Oh God{/i}. It's revolting. The worst fucking thing I've ever tasted, living or dead. Steady, steady, got to keep it down no matter how much..."

        $ pc.damage(KEY_WP, KEY_SPFD, 2)

        beast "..."

        play sound audio.beastgag

        "...and finally, whatever the hell is in blood that actually sustains us - because I'm pretty sure it ain't the calories - settles into my veins. Nourishment. Relief. Nasty stuff, and I'm still hungry. But it does take the edge off."

        $ pc.setHunger(2)

        beast "...You disgust me, as you eventually do everyone."

        $ pc.incScores(KEY_ATTR, _sta, _man, _int)
        $ pc.incScores(KEY_SKILL, _athl, _pers, _occu)

        "Glad to hear it. Hope you enjoyed it as much as I did, asshole. ...But I really {i}do{/i} need to feed for real when I get the chance. I don't know if I can make myself do that again."

        call choose_predator_type

        jump head_to_meeting

    label choose_predator_type:

        "Back in the early nights of my unlife, my sire would take me hunting near the strip. She made it clear that she wasn't going to let me anywhere near her blood dolls until I was certain of my \"palate\"."

        "I told her that \"blood doll\" was a really fucked-up thing to call a human being. She shrugged and said-"

        $ pclastname = _pc["last"]
        $ pcpetname = _pc["pet"]

        sire "Nicer language won't change what we do to them, Ms. [pclastname]. Or how they feel about it. But you might, one day."

        me "Right. Sure."

        sire "If anything about us {i}can{/i} truly be changed. You're in way too deep to get cynical now, Ms. [pclastname]. You chose this, remember? Unlike most of us."

        me "I know. I know. I'm not giving up, it's just-"

        sire "I know, [pcpetname]. One night at a time. One night at a time."

        "I still haven't gotten completely used to it. Hunting. Preying on human beings. Hopefully I never do. But I did develop a way of going about it that I could stomach. {i}And{/i} that I was pretty good at. And eventually..."

        "The Blood is a strange thing. My sire says it has a will of its own, and that it adapts to the needs of its host."

        "If a vampire sticks to a certain method of hunting for long enough, the Blood mutates. Carves out new pathways. And the vampire often finds themselves developing new powers or strengthening old ones."

        "Sounded like a buncha hocus pocus at the time, but between then and now I've lived it. The more I hunted, the more my Blood and I worked in sync."

        python:
            if story_hunted_early == True:
                beastbabble = "You know I'm always in your corner. Always happy to help. Come on, [pcpetname]. Let's do it just the way you like it."
            else:
                beastbabble = "We could be working in sync right now if you weren't so goddamned stubborn."

    menu:
        beast "[beastbabble]"

        "I only feed with consent. It's never easy, and it conflicts with my chosen line of work, but I promised myself I'd do better and I meant it.":
            # ???
            $ pc.predatorType = PT_CONSENSUALIST
            $ feeding_consent = True

        "I mingle with mortals that share my itinerant lifestyle. Truckers, tourists, drifters, commuters. Always plenty of transients to be found if you know where to hang.":
            # ???
            $ pc.predatorType = PT_ROADSIDE_KILLER
            $ feeding_transient = True

        "I was big into EDM festivals and the rave scene back in my college days. You can usually find some hot spots with blinding lights and a crowd that's just the right combination of amped-up and faded.":
            # ???
            $ pc.predatorType = PT_SCENE_QUEEN
            $ feeding_scene = True

        "Why beat around the bush? I feed during sex. I've got the looks, I've got the charm, and this way everyone gets a little of what they want. Or maybe more than a little, if I'm in the mood.":
            # ???
            $ pc.predatorType = PT_SIREN
            $ pass # gain flaw: enemy

    label head_to_meeting:

        beast "bruh"

    label hunt_early:

        beast "yea boi"


    # These labels end the game.
    label endgame:

    $ print "\n[STATUS]: Game ended.\n"

    return

    label gameover:

    $ print "\n[STATUS]: Failure. Game over.\n"

    return
