# The script of the game goes in this file.

label start:

# The game starts here.

label chapter0:

    # In-game variable initializations, to make sure they get tracked by Ren'py

    $ pc = PlayerCharacter()
    $ F_GHOUL = _pcGhoul["first"]
    $ opinions = {F_ANARCHS: opinion_anarchs, F_CAMARILLA: opinion_camarilla, F_GHOUL: opinion_ghoul, F_VENTRUE: opinion_ventrue, F_NOSFERATU: opinion_nosferatu}

    # Characters used by this game. The color argument colorizes the name of the character.

    define me           = Character(_pc["first"], color = "#fefefe")
    define beast        = Character("The Beast", color = "#ee1212")
    define sire         = Character("Ms. Walker", color = "#002366")
    define pcghoul      = Character(_pcGhoul["first"], color = "#803CA2")

    # Show a background. This uses a placeholder by default, but you can add a file (named either "bg room.png" or "bg room.jpg") to the images directory to show it.

    scene bg hotel room
    with fade

    if not MUSIC_MUTED:
        play music audio.scene1_awakening fadeout 1.0 fadein 1.0 volume 0.7

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

    "But the obnoxious jingle is comforting, somehow. Makes me feel a bit more like the human being I used to be. Normal."

    "...But not too much like her. Not too normal."

    "Alright, enough navel-gazing. I've got work tonight, and the bosses don't like to be kept waiting. Except..."

    "I might {i}have{/i} to keep them waiting, because I have a problem."

    $ pc.setHunger(3) # plays tiger growl
    beast "..."

    "It hits like a punch to the gut. Can't focus, can't think of anything else through the ache spreading everywhere. My arms, my legs, my chest, my throat, my guts, behind my eyes. The Beast is hungry. I have to feed."

    beast "You're goddamned right you do. The fuck were you thinking, letting us go hungry like that?"

    "Kindred are sustained by blood - our own and, in turn, others'. With blood, I can do and feel miraculous things. Without it... well, this happens. I'll starve, go mad, and die. Blood demands blood, and the Beast is its voice."

    # $ if DEBUG: pc.setHunger(4, playSound = False)

    beast "Aptly put. And how fortunate for us that this cesspit of a city has blood to spare."

    "The only problem is getting to it. Without getting caught. Without killing someone, or hurting them more than I have to."

    "Well, those are the problems for most Kindred. For Blue Bloods, our heritage makes things even more complicated."

    "Not my human heritage - that's a whole other thing. My Kindred bloodline, passed down to me from my sire the night she drank my blood and I died in ecstacy. The night she fed my corpse some Blood of her own. The night I {i}rose{/i}."

    beast "I thought you said you were done navel-gazing."

    "Shut up and let me think."

    "I actually have some bagged blood in the mini fridge. For emergencies, and in case I need to host another Kindred in the (actually pretty nice for once) hotel room the Seneschal put me up in. I {i}could{/i}, in theory, drink that."

    # $ if DEBUG: pc.setHunger(5, playSound = False)

    beast "We could also, in theory, drink the contents of the nearest S-bend."

    "For most Kindred, preserved blood is like thin gruel - flavorless and passably nourishing at best. For a Blue Blood, it's almost a complete non-starter. My Beast is like some Tamil king's pampered pet panther, a picky predator that won't abide the bagged stuff."

    beast "One of us has to have standards."

    "Every member of Clan Ventrue has what some of us like to call a \"refined palate\". Only certain kinds of blood will do, and every Blue Blood is different. Natural blondes. College graduates. Tourists. Cancer patients. Anything, potentially."

    "Drink the wrong kind of blood, and your Beast will barf it right back up all over your nice new blouse. But my sire taught me that Ventrue {i}can{/i} feed outide of their palates. It just takes a tremendous exertion of will to fight the Beast and keep the blood down."

    beast "Do you really want to exhaust your limited mental faculties fighting me for the right to drink medical waste? No one's going to coddle you this time if you fall apart again."

    "..."

    "So anyway, I could brace myself and try to hork down what's in the fridge, like when I used to make myself throw up the mornings after the best ragers. Or I could take a big risk, and try to hunt in an unfamiliar city."

    "I know my type. I know what I need. And I {i}do{/i} have permission. But hunting is risky even under the best of circumstances, and if anything goes wrong I'll have added to the problem I was flown out here to fix."

    "That would be an {i}extremely{/i} bad look, and I {i}really{/i} can't afford that now. Especially not if it comes back on my sire."

    $ pcname = _pc["first"]
    $ ghoulname = _pcGhoul["first"]

    # $ if DEBUG: pc.setHunger(3)

    "Or I could just suck it up and deal. By the end of the briefing [ghoulname] should be in town, and he can pick up someone I'll like. He's good at that sort of thing. It'll be excruciating, but if I can keep it professional the bosses might trust me more."

    menu:
        beast "You know what the smart choice is. You know what best suits our strengths. Do it. Do {i}something{/i}, before we lose our cool."

        "I'll chance it and hunt, even if it'll make me late. I know people and I know how to get what I want. Nothing ventured, nothing gained.":
            # +DEX, +CHA, +WIT, +Clandestine, +Intrigue, +Awareness | Reduce Hunger to 1 | Spend cash, -Cam opinion | +Presence
            jump chapter0.hunt_before_work

        "I'm not going to be late, and I'm not going to stoop to choking down filth. I'm tough and I can keep it cool, no problem. Later I'll meet up with [ghoulname] for dinner.":
            # +STR, +COM, +RES, +Combat, +Intimidation, +Technology | +Cam opinion | Hunger remains at 3 | +Fortitude
            jump chapter0.wait_until_after

        "Hunting and showing up hungry are both bad ideas. Smarter to take the edge off. I drink the bagged stuff and force my Beast to deal with it.":
            # +STA, +MAN, +INT, +Athletics, +Persuasion, +Occult | Reduce Hunger to 2, +Cam opinion | Spend 2 willpower | +Dominate
            jump chapter0.drink_bagged_blood

    label .hunt_before_work:

        beast "Yes... Wise choice, [pcname]. The bare necessities should always come first."

        "I'll just have to make this quick, which shouldn't be an issue."

        beast "Because of your magnetic personality."

        "I was going to say radiant beauty and immaculate drip, but sure."

        python:
            pc.incScores(KEY_ATTR, _dex, _cha, _wit)
            pc.incScores(KEY_SKILL, _clan, _intr, _awar)
            story_hunted_early = True
            addDisciplineDot(_presence)

        call chapter0.choose_predator_type from im_hungry_dammit

        jump chapter0.hunt_early

    label .wait_until_after:

        beast "...Seriously? You'll regret this, you idiot. You think you can hold me back for that long?"

        "Yeah, I do."

        beast "Maybe I should take over again. Wouldn't that be fun? For me, at least."

        "Fuck you. That will {i}never{/i} happen again. I didn't understand what you were before."

        beast "Think so? Try it. Keep denying me. See what happens."

        "...It's true. I can't hold out forever. But I don't need to. I just need to get through the briefing. Then with [ghoulname]'s help I can do this the right way. I'm strong enough for that."

        python:
            pc.incScores(KEY_ATTR, _str, _com, _res)
            pc.incScores(KEY_SKILL, _comb, _inti, _tech)
            addDisciplineDot(_fortitude)

        "I'm strong enough for this..."

        call chapter0.choose_predator_type from delayed_gratification

        jump chapter0.head_to_meeting

    label .drink_bagged_blood:

        beast "No. No no no no no no no no NO we are NOT drinking that f-"

        "I pop open the fridge, grab a bag and suck that shit down like a Capri Sun."

        play sound audio.beastgag

        beast "..."

        "{i}Oh God{/i}. It's revolting. I'm drinking liquid shit. Steady, steady, got to keep it down no matter how much..."

        $ pc.damage(KEY_WP, KEY_SPFD, 2)

        beast "..."

        play sound audio.beastgag

        "...and finally, whatever the hell is in blood that actually sustains us - because I'm pretty sure it ain't the calories - settles into my veins. Nourishment. Relief. Shit was fucking nasty, and I'm still hungry. But it does take the edge off, and now we know whose will is stronger."

        python:
            $ pc.setHunger(2)
            $ pc.incScores(KEY_ATTR, _sta, _man, _int)
            $ pc.incScores(KEY_SKILL, _athl, _pers, _occu)
            $ addDisciplineDot(_dominate)

        beast "...You disgust me, as you eventually do everyone."

        "Glad to hear it. Hope you enjoyed it as much as I did, asshole. ...But I really {i}do{/i} need to feed for real when I get the chance. I don't know if I can make myself do that again."

        call chapter0.choose_predator_type from who_says_ventrue_cant_be_baggers

        jump chapter0.head_to_meeting

    label .choose_predator_type:

        "Back in the early nights of my unlife, my sire would take me hunting near the strip. She made it clear that she wasn't going to let me anywhere near her blood dolls until I was certain of my \"palate\"."

        "I told her that \"blood doll\" was a really fucked-up thing to call a human being. She shrugged and said-"

        $ pclastname = _pc["last"]
        $ pcpetname = _pc["pet"]

        sire "Nicer language won't change what we do to them, Ms. [pclastname]. Or how they feel about it. But you might, one day."

        me "Right. Sure."

        sire "If anything about us {i}can{/i} truly be changed. You're in way too deep to get cynical now, Ms. [pclastname]. You chose this, remember? Unlike most of us."

        me "I know. I know. I'm not giving up, it's just-"

        sire "I know, [pcpetname]. One night at a time. One night at a time."

        "I still haven't gotten completely used to it. Hunting. Preying on human beings. Hopefully I never do. But I do have a way of going about it that I can stomach. {i}And{/i} that I'm pretty good at. And eventually..."

        "My Blood got with the program. Adapted, somehow. To what I was trying to do, as long as I was working toward the next meal. My sire says it's normal, that most vampires {i}change{/i} according to their hunting tactics and feeding habits."

        python:
            if story_hunted_early == True:
                beastbabble = "You know I'm always in your corner. Always happy to help. Come on, {petname}. Let's do it just the way you like it.".format(petname=pcpetname)
            else:
                beastbabble = "We could be hunting together right now if you weren't so goddamn stubborn."

        menu:
            beast "[beastbabble]"

            "I only feed with consent. It's never easy and it can conflict with my chosen line of work, but I promised myself I'd do better and I meant it.":
                # +Persuasion, +Fortitude, +Humanity, -moderate Cam opinion
                python:
                    pc.setPredatorType(PT_CONSENSUALIST)
                    pc.incScores(KEY_SKILL, _pers)
                    pc.setHumanity("+1", PT_CONSENSUALIST)
                    setOpinion(F_CAMARILLA, 20, "subtract")
                    addDisciplineDot(_fortitude)
                    feeding_consent = True

            "I hit the road when I'm hungry. Truckers, tourists, drifters, commuters. Aways plenty of transients in and around cities, even if that means shady people in rough areas.":
                # +Investigation, +Fortitude, +Herd, +minor Anarch opinion
                python:
                    pc.setPredatorType(PT_ROADSIDE_KILLER)
                    pc.incScores(KEY_SKILL, _inve)
                    ctt = "In every city there are places you can go to find people just passing through. The only problem is they're usually claimed, but that's not a problem for me here."
                    pc.addPerk(M_HERD[KEY_NAME], 1, customToolTip = ctt)
                    setOpinion(F_ANARCHS, 10, "add")
                    addDisciplineDot(_fortitude)
                    feeding_transient = True

            "I was big into EDM festivals and the rave scene back in my college days. You can usually find some nice spots with blinding strobe lights, fog machines and a crowd that's just the right combination of amped-up and faded.":
                # +Performance, +Dominate, +Contacts
                python:
                    pc.setPredatorType(PT_SCENE_QUEEN)
                    pc.incScores(KEY_SKILL, _perf)
                    ctt = "He goes by \"Jack\". I met him at a festival where he was providing security on the books and party favors on the low. He can get things done."
                    pc.addPerk(M_CONTACTS[KEY_NAME], 1)
                    addDisciplineDot(_dominate)
                    feeding_scene = True

            "Why beat around the bush? I feed during sex. I've got the looks, I've got the charm, and this way everyone gets a little of what they want. Or maybe more than a little, if I'm in the mood.":
                # +Intrigue, +Presence, +Looks (Beautiful), +Flaw (Enemy)
                python:
                    pc.setPredatorType(PT_SIREN)
                    pc.incScores(KEY_SKILL, _intr)
                    pc.addPerk(M_LOOKS[KEY_NAME], 1, merit = True, customToolTip = "They say if you've got it, flaunt it. And I've got it.")
                    pc.addPerk(M_ALLIES[KEY_NAME], 1, flaw = True)
                    addDisciplineDot(_presence)

        return

    label .head_to_meeting:

        stop music fadeout 2.5

        "Alright, time to go."

        play sound audio.shower_pc

        "A quick shower, some eyeshadow and lipstick, and my favorite purple number. Okay, let's hit the road."

        queue sound audio.heels_on_pavement

        "Shit, where did I park again?"

        queue sound audio.carstart_pc

        scene bg driving road1 with trans_slowfade

        if not MUSIC_MUTED:
            play music ("<from 5>" + audio.car_meeting) fadeout 1.0 fadein 1.0

        "Something's off about this town. Other than the fact that there are dead things lurking in the shadows and preying on the innocent, I mean. Not the awful shit going on in the news, either. Something I can't put my finger on..."

        "Something Lola would have called a power, or a principality. I used to scoff at all that Bible-thumping mumbo-jumbo, but now? For all I know she'd be right. Maybe she was right about everything. No skin off my ass, though. I was going to hell anyway."

        "Becoming Kindred has changed a lot of things for me, but my relationships with God and family aren't among them. Everything else, though..."

        call chapter0.choose_background from en_route_to_meeting

        "sdfdsdfdsfd"

        beast "sdfdddfdfd"

        jump chapter0.first_meeting_ends

    label .hunt_early:

        stop music fadeout 2.5

        "The Seneschal will be pissed, but she won't like me any more if I show up twitching with Hunger. Let's get ourselves a bite to eat."

        beast "It's a date."

        play sound audio.shower_pc

        if pc.getPredatorType() == PT_SIREN:
            "A quick shower, some eyeshadow and lipstick, and my favorite purple minidress. Shows exactly the right amount of skin, and I can move pretty well in it. How do I look?"

            beast "Like a snack. Now let's go get one, shall we?"
        else:
            "A quick shower, some eyeshadow and lipstick, and my favorite purple number. Ready to go."

        queue sound audio.heels_on_pavement

        "Shit, where did I park again?"

        beast "Sixteen, level E. Don't forget your ticket this time."

        "Right."

        queue sound audio.carstart_pc

        scene bg driving road1 with trans_slowfade

        if not MUSIC_MUTED:
            play music ("<from 2>" + audio.car_hunting2) fadeout 1.0 fadein 1.0 volume 0.9

        "This city is strange. It feels like its own little island in the cosmic sea, lost in its own time and space. Nothing here feels real or connected to anything in the outside world."

        "Or maybe that's just the Hunger messing with my head."

        call chapter0.choose_background from en_route_to_first_hunt

        "Alright, let's do this quick."

        "My type is... hard to explain. I had a hell of a time figuring it out myself. Basically I feed on people who are, well, in flight. People running from something. Trying to put something behind them."

        "What exactly it is doesn't matter per se. It can be a place, a person, an event, a state of mind. But they have to have physically moved somewhere in order to get away from it, and - this is the killer - they have to let me know about it."

        "They don't have to do it intentionally, or even verbally. Sometimes just a furtive or pained look on their face is enough. But there has to be a tell. I have to {i}know.{/i}"

        beast "You are what you eat, or rather you eat what you are. Cowards running from their problems. You're a spiritual cannibal, feeding on those like yourself."

        stop music fadeout 2.0

        play sound audio.carstopengine_pc

        "...You finished? Because here we are."

        queue sound audio.carstopkeys_pc

        queue sound audio.heels_on_pavement

        scene black with fade

        "Naturally I don't park where I plan to hunt. (Not that I could, even if I wanted to.) I park a few blocks out and hoof it the rest of the way."

        $ ptstring = str(pc.getPredatorType()).lower().strip()

        call expression ("index.hunts.hunt1_" + ptstring) from early_bird_gets_worm

        python:
            if story_hunted_early == True:
                setOpinion(F_CAMARILLA, 15, "subtract")
                pc.removeFromInventory("cash", 253.56)

        beast "ayo that was some wild shit huh"

        "yea"

        jump chapter0.head_to_meeting

    label .choose_background:

        "I don't think either of us saw it turning out this way. I was just happy to have a job after everything, and my sire... well, I don't think she was all that impressed with me at first. Which made two of us."

        menu:
            "Until that one night when everything changed..."

            "Our car was ambushed by hitmen with molotovs. I wrenched a burning door open, freeing her from the car as she thrashed around in frenzy. Then I grabbed a gun and kept shooting just long enough for her to come to her senses.":
                # +STR, +STA, +COM | +Awareness, +Clandestine, +Firearms
                $ story_background = "defender"
                $ pc.incScores(KEY_ATTR, _str, _sta, _com)
                $ pc.incScores(KEY_SKILL, _awar, _clan, _fire)

                "I still have no idea how we made it through those first few minutes. It felt like an eternity at the time, but now it's all a blur. We were caught completely off guard, and in seconds half of her security were dead."

                "But I got her out of the car and let off at them. They weren't expecting that, and it bought her just enough time. And when she came out of her frenzy... she was like some goddess of war. Like motherfucking Kali in the flesh."

                "They shot her a dozen times and even burned her a bit, but she wouldn't go down. She kept shouting demands at them that I could somehow hear over all the noise, and... they fucking listened. They obeyed. I was dumbstruck."

                "The people who came to kill her turned their guns on each other at her command, some defecting to her side. I've never seen anything like it, before or since. When it was over we had to scatter, torching the cars and anything else we could."

                "I went along with it, because what the fuck else was I going to do? But she remembered what I did in those first few moments and she was grateful... and impressed. Not half bad, considering I was a glorified secretary at the time."

            "I mediated and defused a brewing conflict between two mortal gangs that would have interfered with the Prince's financial interests, saving him a massive headache and giving her the credit for it.":
                # +STA, +MAN, +RES | +Intimidation, +Investigation, +Persuasion
                $ story_background = "negotiator"
                $ pc.incScores(KEY_ATTR, _sta, _man, _res)
                $ pc.incScores(KEY_SKILL, _inti, _inve, _pers)

                "The Camarilla is just like any other racket. Even its reach has limits. If large groups of mortals decide they want to do something the Cam doesn't want them to, well then the Cam might just be shit out of luck."

                "It was two sets where I grew up, and a war would have had bodies piling up, all kinds of attention from law enforcement and media, and plummeting property values. All of which would have been bad for the Prince's checkbook."

                "I didn't know that at the time, of course. I just knew a lot of people in the area, and didn't want them getting hurt. So over the next few days I got some folks to sit down, and we had ourselves a chat."

                "I played it cool, and struck the right balance between sympathetic, fair, and tough (backed up by some hitters on loan from my sire). In the end we had a truce that let both sides save face."

                "It only worked because there were influential people on both sides that already wanted peace, probably because they would have had family in the crossfire too."

                "But there was a whole other business angle I wasn't even aware of, and honestly wouldn't have given a shit about if I had been. That's not what I told the Prince, though. When he called me up, all I knew was that he was my boss's boss."

                "So I played up her role and made the whole thing seem like her idea. I had no idea that I was actually talking to a fucking undead monarch that probably could have, I don't know, made my head explode with a thought or some shit."

            "I chased down what I later learned was a thinblood Anarch on foot, fought and subdued him, and recovered some important documents he'd stolen.":
                # +DEX, +STA, +WIT | +Athletics, +Combat, +Streetwise
                $ story_background = "agent_j"
                $ pc.incScores(KEY_ATTR, _dex, _sta, _wit)
                $ pc.incScores(KEY_SKILL, _athl, _comb, +stre)

                "He was {i}fast{/i}, and when I caught up to him he hit like a Mack truck. Especially for such a small, skinny guy. I probably chased him for a mile through down streets and through alleys, but I knew the area better."

                "I cornered him off Sixth and Brenshaw. He telegraphed his punches, but they came way harder and faster than I was expecting. And nothing I did seemed to hurt him for more than a second. Until I sank my rusty old Pro-Tech into his belly, that is."

                "I didn't want to, but he had me on the ground and was kicking the shit out of my ribs. So I had to wet him up a bit."

                "I don't even know why I chased him down. I'm definitely not the type to risk my life for some faceless corporation that could give a fuck about me. I just knew it would be my ass if I lost whatever was in that suitcase."

                "And I didn't want to lose the first gainful employment I'd had in a minute. It was my foothold, you know? But apparently the whole mess caught a different kind of attention, and a few days later I was in her office."

            "I surprised her by putting together an elaborate biographical performance piece about her mortal life. I thought I was researching her ancestry, but she assumed I'd figured out it was actually her! I just went along with it.":
                # +STA, +CHA, +INT | +Academics, +Performance, +Technology
                $ story_background = "bluff"
                $ pc.incScores(KEY_ATTR, _sta, _cha, _int)
                $ pc.incScores(KEY_SKILL, _acad, _perf, _tech)

                "It's amazing how far a little luck and a bit of aplomb can take you. That, and a willingness to just go with the flow now matter how weird things get. I didn't really have much else going on at the time."

                "I thought I had myself a brilliant idea, thought I'd figured out who she was. A descendant of {i}the{/i} Madam C. J. Walker, the famous entrepreneur, activist, and philanthropist. No fucking kidding."

                "She was the first kid in her family who wasn't born enslaved, and she became one of the country's first woman millionaires making and selling hair care products. How could I not respect that kind of hustle?"

                "I figured I'd ingratiate myself with the boss, indulge my artsy side, {i}and{/i} get through one of those excruciating corporate team-building exercises, all in one stroke. My group's presentation came second-to-last."

                "Well, my presentation really. I wrote the script, did most of the costume design, and {i}all{/i} the editing. Fucking group projects. Thought I was done with that shit after undergrad."

                "At the end of it her eyes were wide and her jaw was on the floor. I was {i}visibly{/i} feeling myself, thinking my little multimedia project was just that good."

                "Later in her office, she asked how I'd known. I dodged the question and told her she should be proud, and that I was the one who should be impressed."

        if not MUSIC_MUTED:
            play music audio.talk_with_sire fadeout 1.0 fadein 0.5

        "We had a long conversation in her office that night. About what I wanted out of life, where I saw myself headed. About what I wanted to do with my time on this Earth. I was a lot more honest than I'd planned to be."

        if story_background == "bluff":
            sire "So you had it pretty rough, huh? I had you pegged for the starving young artist type, but not all that..."

            me "People usually {i}like{/i} starving artists. They're supposed to have beautiful souls, or something like that."

            sire "Well, what does a [pcname] that people like look like to you?"
        else:
            sire "You're tough for such a pretty young thing, huh? Makes sense. Girls have to be tough to make it through that kind of environment. The more things change..."

            me "Yeah, well I didn't exactly make things any better on that front. Or any front, really."

            sire "But you want to now, is that it?"

        "My Embrace didn't come until years later, after I'd seen and done a whole lot more. But that night, she offered me a drink."

        "Generally speaking, it's probably a red flag when your employer offers calls you into their office and offers you lean. And after I tried the shit once I swore I'd never touch it again. It was exactly how I never want to feel again."

        "But this stuff was different. It was deep crimson, and it smelled... amazing."

        sire "This is your choice. Entirely optional. I mean that. The promotion and raise we talked about, for all your hard work? They're yours, whether you choose to take the next step or not."

        sire "Nothing is going to be held against you. In fact, if you do it because you feel pressured or coerced that defeats the whole purpose. But what I'm offering you is a place in... let's call it my inner circle."

        sire "If you were looking for a chance to do more, {i}be{/i} more... I can promise you this is it."

        "It was like sipping fine bourbon from a glass made of starlight. Like kissing my way down the back of an angel made of honey. So, not at all like lean."

        "Those first few months as retainer to Ms. Walker (she went by a different name around regular mortals) were some of the best in my life."

        if not story_hunted_early:
            beast "What an enchanted world you live in. You really do just want someone to tell you what to do, don't you?"

            beast "You really were happier as a ghoul, weren't you? It let you shed the unbearable burden of being responsible for your own shitty choices so you could go back to being a good little girl that everybody likes. Fucking. Pathetic."

            "Karin once mentioned that every Kindred experiences their Beast differently. For some it's just a set of alien, predatory urges. Fear, rage, hunger. For others it's the voice of someone they respect... or fear."

            "Me? I get saddled with this noxious, sulking thing that won't shut the fuck up no matter what I do."

            if pc.getHunger() > 2:
                beast "You know {i}exactly{/i} what to do to get me to shut the fuck up, and you refused to do it."
            else:
                beast "I have the sense not to drink distilled ass, at least. If you're going wear yourself out on something that stupid, you really may as well just let me take over for good."

                "I already told you it was a stopgap measure. To keep you from freaking out. Blame yourself."

                beast "You {i}are{/i} my self. And I do blame you."

            beast "Anyway, back in the real world... we're here. We've arrived."
        else:
            beast "If you're done strolling down memory lane, we do have important business to attend to. We've arrived."

        return

    label .first_meeting_ends:

        "and so the meeting ends blah blah placeholder"

        "mo text"

# These labels end the game.
label endgame:

    $ print "\n[STATUS]: Game ended.\n"

    return

label gameover:

    $ print "\n[STATUS]: Failure. Game over.\n"

    return
