# The script of the game goes in this file.

label start:

# The game starts here.

label chapter0:

    # In-game variable initializations, to make sure they get tracked by Ren'py

    python:
        pc = PlayerCharacter()
        F_GHOUL = _pcGhoul["first"]
        opinions = {F_ANARCHS: opinion_anarchs, F_CAMARILLA: opinion_camarilla, F_GHOUL: opinion_ghoul, F_VENTRUE: opinion_ventrue, F_NOSFERATU: opinion_nosferatu}
        arena = BattleArena()

    # Characters used by this game. The color argument colorizes the name of the character.

    define me           = Character(_pc["first"], color = "#fefefe")
    define beast        = Character("The Beast", color = "#ee1212")
    define sire         = Character("Ms. Walker", color = "#002366")
    define ghoul      = Character(_pcGhoul["first"], color = "#803CA2")
    define keeratghoul  = Character("Gabriel", color = "#a2883c")
    define samghoulf    = Character("Agnes", color = "#dbdb76")
    define samghoulm    = Character("Barak", color = "#dbdb76")
    define keerat       = Character("Keerat \"Kay\" Sanghera", color = "#ffa100")
    define sam          = Character("Seneschal " + _sensam["last"], color = "#FFD700")
    define exlover      = Character(pcex["first"], color = "#d75b9a")

    # Show a background. This uses a placeholder by default, but you can add a file (named either "bg room.png" or "bg room.jpg") to the images directory to show it.

    scene bg hotel room with fade

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

    $ pc.raiseHunger(3)

    "I don't actually need an alarm - none of my kind do. I couldn't stay asleep past sundown if I wanted to. I've tried."

    $ pc.slakeHunger(2)

    "But the obnoxious jingle is comforting, somehow. Makes me feel a bit more like the human being I used to be. Normal."

    "...But not too much like her. Not too normal."

    "Alright, enough navel-gazing. I've got work tonight, and the bosses don't like to be kept waiting. Except..."

    "I might {i}have{/i} to keep them waiting, because I have a problem."

    python:
        intro = [
            "Yo what up this line 1",
            "Yo this is line 2",
            ("Some Guy", "This is Some Guy comin at you with line 3",),
            "and thats it"
        ]

        dead = ["Yo wtf we all dead man","RIP"]
        fled = ["Oh shit she gon get us", "cheese it"]

        testopp = Combatant(beth = pc)
        testopp.embody()
        testopp.equip(attack = 1, rangedAttack = 0)
        testopp.setStoryText(intro = intro, dead = dead, fled = fled)
        arena.setStage(returnBG = "bg hotel room")
        arena.startBattle(testopp)

    $ pc.setHunger(3) # plays tiger growl
    beast "..."

    "It hits like a punch to the gut. Can't focus, can't think of anything else through the ache spreading everywhere. My arms, my legs, my chest, my throat, my guts, behind my eyes. The Beast is hungry. I have to feed."

    beast "You're goddamned right you do. The fuck were you thinking, letting us go hungry like that?"

    "Kindred are sustained by blood - our own and, in turn, others'. With blood, I can do and feel miraculous things. Without it... well, this happens. I'll starve, go mad, and die. Blood demands blood, and the Beast is its voice."

    beast "Aptly put. And how fortunate for us that this cesspit of a city has blood to spare."

    "The only problem is getting to it. Without getting caught. Without killing someone, or hurting them more than I have to."

    "Well, those are the problems for most Kindred. For Blue Bloods, our heritage makes things even more complicated."

    "Not my human heritage - that's a whole other thing. My Kindred bloodline, passed down to me from my sire the night she drank my blood and I died in ecstacy. The night she fed my corpse some Blood of her own. The night I {i}rose{/i}."

    beast "I thought you said you were done navel-gazing."

    "Shut up and let me think."

    "I actually have some bagged blood in the mini fridge. For emergencies, and in case I need to host another Kindred in the (actually pretty nice for once) hotel room the Seneschal put me up in. I {i}could{/i}, in theory, drink that."

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
            pc.addDisciplineDot(_presence)

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
            pc.addDisciplineDot(_fortitude)

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
            pc.setHunger(2)
            pc.incScores(KEY_ATTR, _sta, _man, _int)
            pc.incScores(KEY_SKILL, _athl, _pers, _occu)
            pc.addDisciplineDot(_dominate)

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
                    pc.setHumanity("+=1", PT_CONSENSUALIST)
                    setOpinion(F_CAMARILLA, 25, "subtract")
                    pc.addDisciplineDot(_fortitude)
                    feeding_consent = True

            "I hit the road when I'm hungry. Truckers, tourists, drifters, commuters. Aways plenty of transients in and around cities, even if that means shady people in rough areas.":
                # +Investigation, +Fortitude, +Herd, +minor Anarch opinion
                python:
                    pc.setPredatorType(PT_ROADSIDE_KILLER)
                    pc.incScores(KEY_SKILL, _inve)
                    ctt = "In every city there are places you can go to find people just passing through. The only problem is they're usually claimed, but that's not a problem for me here."
                    pc.addPerk(M_HERD[KEY_NAME], 1, customToolTip = ctt)
                    setOpinion(F_ANARCHS, 10, "add")
                    pc.addDisciplineDot(_fortitude)
                    feeding_transient = True

            "I was big into EDM festivals and the rave scene back in my college days. You can usually find some nice spots with blinding strobe lights, fog machines and a crowd that's just the right combination of amped-up and faded.":
                # +Performance, +Dominate, +Contacts
                python:
                    pc.setPredatorType(PT_SCENE_QUEEN)
                    pc.incScores(KEY_SKILL, _perf)
                    ctt = "He goes by \"Jack\". I met him at a festival where he was providing security on the books and party favors on the low. He can get things done."
                    pc.addPerk(M_CONTACTS[KEY_NAME], 1)
                    pc.addDisciplineDot(_dominate)
                    feeding_scene = True

            "Why beat around the bush? I feed during sex. I've got the looks, I've got the charm, and this way everyone gets a little of what they want. Or maybe more than a little, if I'm in the mood.":
                # +Intrigue, +Presence, +Looks (Beautiful), +Flaw (Enemy)
                python:
                    pc.setPredatorType(PT_SIREN)
                    pc.incScores(KEY_SKILL, _intr)
                    pc.addPerk(M_LOOKS[KEY_NAME], 1, merit = True, customToolTip = "They say if you've got it, flaunt it. And I've {i}definitely{/i} got it.")
                    pc.addPerk(M_ALLIES[KEY_NAME], 1, flaw = True)
                    pc.addDisciplineDot(_presence)

        return

    label .head_to_meeting:

        stop music fadeout 2.5

        "Alright, time to go."

        play sound audio.shower_pc

        "A quick shower, some eyeshadow and lipstick, and my favorite purple number. Okay, let's hit the road."

        queue sound audio.heels_on_pavement

        "Shit, where did I park again?"

        queue sound audio.carstart_pc

        scene bg driving road2 with trans_slowfade

        if not MUSIC_MUTED:
            play music audio.car_meeting fadeout 1.0 fadein 2.0 volume 0.7

        "Something's off about this town. Other than the fact that there are dead things lurking in the shadows and preying on the innocent, I mean. Not the awful shit going on in the news, either. Something I can't put my finger on..."

        "Something Lola would have called a power, or a principality. I used to scoff at all that Bible-thumping mumbo-jumbo, but now? For all I know she'd be right. Maybe she was right about everything. No skin off my ass, though. I was going to hell anyway."

        "Becoming Kindred has changed a lot of things for me, but my relationships with God and family aren't among them. Everything else, though..."

        call chapter0.choose_background from en_route_to_meeting

        "I make my way to a gated office park. The drive from the hotel is basically crossing most of the city, so it takes about an hour. The guard at the booth seems to have been given my description, and immediately buzzes me in. I'm still a half hour early."

        beast "What a shithole."

        jump chapter0.meeting_start

    label .hunt_early:

        stop music fadeout 2.5

        "The Seneschal will be pissed, but she won't like me any more if I show up twitching with Hunger. Let's get ourselves a bite to eat."

        beast "Sounds like a plan."

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

        scene bg driving road2 with trans_slowfade

        if not MUSIC_MUTED:
            play music audio.car_hunting2 fadeout 1.0 fadein 2.0 volume 0.9

        "This city is strange. It feels like its own little island in the cosmic sea, lost in its own time and space. Nothing here feels real or connected to anything in the outside world."

        "Or maybe that's just the Hunger messing with my head."

        call chapter0.choose_background from en_route_to_first_hunt

        "Alright, let's do this quick."

        call feeding.hunt1_preamble from early_bird_gets_worm_1

        $ ptstring = str(pc.getPredatorType()).lower().strip().replace(" ", "")

        call expression ("feeding.hunt1_" + ptstring) from early_bird_gets_worm_2

        stop music fadeout 0.5

        python:
            if story_hunted_early == True:
                setOpinion(F_CAMARILLA, 30, "subtract")
                setOpinion(F_VENTRUE, 15, "subtract")

        play sound audio.heels_on_pavement

        scene bg city nightscape1 with trans_slowfade

        queue sound audio.carstart_pc

        beast "Well, I don't know about you but I feel {i}much{/i} better."

        "...Yeah. I'm about to get my ass chewed, though."

        beast "Those other ticks know as well as you and I that sustenance always comes first. So we're a bit late. Who cares? Fuck how they feel about it."

        if pc.getPredatorType() != PT_CONSENSUALIST:
            "My dress is stained with someone else's sweat, but at this point heading back to the hotel for a shower and change of clothes would probably do more harm than good. Plus, we're not meeting at Elysium."

        "I drive as quickly as I can without attracting attention, and make my way to a gated office park downtown. It takes about twenty minutes. Fortunately, the place is much closer to where I came from than the hotel."

        "The guard at the booth seems to have been given my description, and immediately buzzes me in."

        jump chapter0.meeting_start

    label .choose_background:

        "I don't think either of us saw it turning out this way. I was just happy to have a job after everything, and my sire... well, I don't think she was all that impressed with me at first. Which made two of us."

        menu:
            "Until that one night when everything changed..."

            "Our car was ambushed by hitmen with molotovs. I wrenched a burning door open, freeing her from the car as she thrashed around in frenzy. Then I grabbed a gun and kept shooting just long enough for her to come to her senses.":
                # +STR, +STA, +COM | +Awareness, +Clandestine, +Firearms
                # +Fortitude (if < 2) or +Dominate (if < 3) TODO: Change this if I get far enough for Defy Bane/FtIF to be useful
                python:
                    story_background = "defender"
                    pc.incScores(KEY_ATTR, _str, _sta, _com)
                    pc.incScores(KEY_SKILL, _awar, _clan, _fire)
                    if pc.getDisciplineLevel(_fortitude) < 2:
                        pc.addDisciplineDot(_fortitude)
                    else:
                        pc.addDisciplineDot(_dominate)

                "I still have no idea how we made it through those first few minutes. It felt like an eternity at the time, but now it's all a blur. We were caught completely off guard, and in seconds half of her security were dead."

                "But I got her out of the car and let off at them. They weren't expecting that, and it bought her just enough time. And when she came out of her frenzy... she was like some goddess of war. Like motherfucking Kali in the flesh."

                "They shot her a dozen times and even burned her a bit, but she wouldn't go down. She kept shouting demands at them that I could somehow hear over all the noise, and... they fucking listened. They obeyed. I was dumbstruck."

                "The people who came to kill her turned their guns on each other at her command, some defecting to her side. I've never seen anything like it, before or since. When it was over we had to scatter, torching the cars and anything else we could."

                "I went along with it, because what the fuck else was I going to do? But she remembered what I did in those first few moments and she was grateful... and impressed. Not half bad, considering I was a glorified secretary at the time."

            "I mediated and defused a brewing conflict between two mortal gangs that would have interfered with the Prince's financial interests, saving him a massive headache and giving her the credit for it.":
                # +STA, +MAN, +RES | +Intimidation, +Investigation, +Persuasion | +Dominate (if < 3) or +Presence
                python:
                    story_background = "negotiator"
                    pc.incScores(KEY_ATTR, _sta, _man, _res)
                    pc.incScores(KEY_SKILL, _inti, _inve, _pers)
                    if pc.getDisciplineLevel(_dominate) < 3:
                        pc.addDisciplineDot(_dominate)
                    else:
                        pc.addDisciplineDot(_presence)

                "The Camarilla is just like any other racket. Even its reach has limits. If large groups of mortals decide they want to do something the Cam doesn't want them to, well then the Cam might just be shit out of luck."

                "It was two sets where I grew up, and a war would have had bodies piling up, all kinds of attention from law enforcement and media, and plummeting property values. All of which would have been bad for the Prince's checkbook."

                "I didn't know that at the time, of course. I just knew a lot of people in the area, and didn't want them getting hurt. So over the next few days I got some folks to sit down, and we had ourselves a chat."

                "I played it cool, and struck the right balance between sympathetic, fair, and tough (backed up by some hitters on loan from my sire). In the end we had a truce that let both sides save face."

                "It only worked because there were influential people on both sides that already wanted peace, probably because they would have had family in the crossfire too."

                "But there was a whole other business angle I wasn't even aware of, and honestly wouldn't have given a shit about if I had been. That's not what I told the Prince, though. When he called me up, all I knew was that he was my boss's boss."

                "So I played up her role and made the whole thing seem like her idea. I had no idea that I was actually talking to a fucking undead monarch that probably could have, I don't know, made my head explode with a thought or some shit."

            "I chased down what I later learned was a thinblood Anarch on foot, fought and subdued him, and recovered some important documents he'd stolen.":
                # +DEX, +STA, +WIT | +Athletics, +Combat, +Streetwise | +Fortitude (if < 2) or +Presence TODO: see above
                python:
                    story_background = "agent_j"
                    pc.incScores(KEY_ATTR, _dex, _sta, _wit)
                    pc.incScores(KEY_SKILL, _athl, _comb, _stre)
                    if pc.getDisciplineLevel(_fortitude) < 2:
                        pc.addDisciplineDot(_fortitude)
                    else:
                        pc.addDisciplineDot(_presence)

                "He was {i}fast{/i}, and when I caught up to him he hit like a Mack truck. Especially for such a small, skinny guy. I probably chased him for a mile through down streets and through alleys, but I knew the area better."

                "I cornered him off Sixth and Brenshaw. He telegraphed his punches, but they came way harder and faster than I was expecting. And nothing I did seemed to hurt him for more than a second. Until I sank my rusty old Pro-Tech into his belly, that is."

                "I didn't want to, but he had me on the ground and was kicking the shit out of my ribs. So I had to wet him up a bit."

                "I don't even know why I chased him down. I'm definitely not the type to risk my life for some faceless corporation that could give a fuck about me. I just knew it would be my ass if I lost whatever was in that suitcase."

                "And I didn't want to lose the first gainful employment I'd had in a minute. It was my foothold, you know? But apparently the whole mess caught a different kind of attention, and a few days later I was in her office."

            "I surprised her by putting together an elaborate biographical performance piece about her mortal life. I thought I was researching her ancestry, but she assumed I'd figured out it was actually her! I just went along with it.":
                # +STA, +CHA, +INT | +Academics, +Performance, +Technology | +Presence
                python:
                    story_background = "bluff"
                    pc.incScores(KEY_ATTR, _sta, _cha, _int)
                    pc.incScores(KEY_SKILL, _acad, _perf, _tech)
                    pc.addDisciplineDot(_presence)

                "It's amazing how far a little luck and a bit of aplomb can take you. That, and a willingness to just go with the flow now matter how weird things get. I didn't really have much else going on at the time."

                "I thought I had myself a brilliant idea, thought I'd figured out who she was. A descendant of {i}the{/i} Madam C. J. Walker, the famous entrepreneur, activist, and philanthropist. No fucking kidding."

                "She was the first kid in her family who wasn't born enslaved, and she became one of the country's first woman millionaires making and selling hair care products. How could I not respect that kind of hustle?"

                "I figured I'd ingratiate myself with the boss, indulge my artsy side, {i}and{/i} get through one of those excruciating corporate team-building exercises, all in one stroke. My group's presentation came second-to-last."

                "Well, my presentation really. I wrote the script, did most of the costume design, and {i}all{/i} the editing. Fucking group projects. Thought I was done with that shit after I dropped out of college."

                "At the end of it her eyes were wide and her jaw was on the floor. I was {i}visibly{/i} feeling myself, thinking my little multimedia project was just that good."

                "Later in her office, she asked how I'd known. I dodged the question and told her she should be proud, and that I was the one who should be impressed."

        if not MUSIC_MUTED:
            play music audio.talk_with_sire fadeout 3.0 fadein 3.0 volume 0.5

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

        "Generally speaking, it's probably a red flag when your employer calls you into their office and offers you lean. And after I tried the shit once I swore I'd never touch it again. It was exactly how I never want to feel."

        "But this stuff was different. It was deep crimson, and it smelled... amazing."

        sire "This is your choice. Entirely optional. I mean that. The promotion and raise we talked about, for all your hard work? They're yours, whether you choose to take the next step or not."

        sire "Nothing is going to be held against you. In fact, if you do it because you feel pressured or coerced that defeats the whole purpose. But what I'm offering you is a place in... let's call it my inner circle."

        sire "If you were looking for a chance to do more, {i}be{/i} more... I can promise you this is it."

        "It was like sipping fine bourbon from a glass made of starlight. Like kissing my way down the back of an angel made of honey. So, not at all like lean."

        "Those first few months as retainer to Ms. Walker (she went by a different name around regular mortals) were some of the best in my life."

        if not story_hunted_early:
            beast "What an enchanted world you live in. You really do just want someone to tell you what to do."

            beast "You were actually happier as a ghoul, weren't you? I bet I know why, too. It let you shed the unbearable burden of being responsible for your own shitty choices, so you could go back to being a good little girl that everybody likes. Truly pathetic."

            "Theresa (my first Kindred friend) once mentioned that every Kindred experiences their Beast differently. For some it's just a set of alien, predatory urges. Fear, rage, hunger. For others it's the voice of someone they respect... or fear."

            beast "Theresa's not your friend, you lackwit. Kindred don't have friends. Which means your Embrace changed little."

            "Me? I get saddled with this noxious, sulking thing that won't shut the fuck up no matter what I do."

            if pc.getHunger() > 2:
                beast "You know {i}exactly{/i} what to do to get me to shut the fuck up, and you refused to do it."
            else:
                beast "I have the sense not to drink distilled ass, at least. If you're going wear yourself out on something that stupid, you really might as well just let me take over for good."

                "I already told you it was a stopgap measure. To keep you from freaking out. Blame yourself."

                beast "You {i}are{/i} my self. And I do blame you."

            beast "Anyway, back in the real world... we're here. We've arrived."
        else:
            beast "If you're done strolling down memory lane, we do have important business to attend to. We've arrived."

        stop music fadeout 1.0

        return

    label .meeting_start:

        play sound audio.carstopengine_pc

        scene bg city officepark1

        "Here we are. Building six. Third floor."

        queue sound audio.carstopkeys_pc

        queue sound audio.heels_on_pavement

        python:
            senfirst = _sensam["first"]
            senlast = _sensam["last"]
            sen_subj = _sensam["subj"]
            sen_obj = _sensam["obj"]
            sen_pos = _sensam["pos"]

        if story_hunted_early:
            play music audio.scene1_awakening

            "Aside from a few white vans and other utility vehicles, there's only one other car - a deep blue 2015 BMW X6. Snazzy. That must be the Seneschal's car."

            "I enter the lobby through automated doors. There's just one guy sitting at the front desk with his feet up. He's a tall, gangly man with five o' clock shadow and a vague expression of disdain on his face as he looks at me."

            keeratghoul "Ms. Sanghera will see you upstairs. Third floor, room 306."

            me "Sanghera? I thought I Was meeting the Seneschal, [senfirst] [senlast]. I was to receive my briefing and orders from [sen_obj]."

            "His lips curl into a sneer and he shakes his head."

            keeratghoul "You {i}were{/i} meeting the Seneschal. Then you didn't show for like, an hour. So [sen_subj] left Ms. Sanghera to brief you. Everyone's {i}real{/i} happy with you, hotshot. For your own sake I hope you're worth the hassle."

            me "I am."

            beast "Are we really going to let a fucking ghoul talk down to us?"

            "There's nothing wrong with being a ghoul. They deserve respect. It's not like Kindred could survive without them."

            beast "And for most of history mortals couldn't survive without their livestock, either. Do you see humans taking any lip from cows?"

            "Will you shut the fuck up, for once?"

            keeratghoul "...What are you muttering about?"

            me "Nothing. If Ms. Sanghera is ready to see me I'll head in."

            keeratghoul "By all means..."

            me "Thank you."

            keeratghoul "...Sure."
        else:
            stop music fadeout 0.5

            "Aside from utility vehicles, there are three other cars parked here. A deep blue 2015 BMW X6, a black Chevrolet Suburban, and a black 2018 Lincoln MKZ. That last one has got to be the Seneschal's car."

            "The automated doors slide open. There are three people standing around. The first is a tall, gangly man with a stubbly face. The second is a shorter (but still pretty tall) blonde woman with a short pixie cut and a scar across her cheek. She stands straight-backed and alert."

            "The third is an olive-skinned man with a handsome face and slicked back hair. He's of average height. All three are dressed in immaculate dark suits. All three are armed with heavy pistols. The handsome man speaks, in a lightly-accented voice."

            samghoulm "Hello there. You must be Miss [pcname] [pclastname]. I'm Barak. This is Agnes. We're retainers to the Seneschal. And over here is Gabriel, retainer to Kay Sanghera."

            samghoulf "She is of your Clan, I believe."

            keeratghoul "You're early. But the Seneschal will probably like that. No reason you shouldn't go on up and see [sen_obj] now."

            samghoulf "Third floor. Room 306."

        play sound audio.heels_on_pavement

        "I take the stairs up. Most of the building is dark. I haven't even seen any custodial staff around, and it's still pretty early in the night."

        "So here I am. This is what I was flown out here to do. There's been some kind of major Masquerade breach, and containment efforts are ongoing. Ms. Walker recommended me for this job, so my performance here is going to reflect on her."

        "This is it. My second shot at life. Well, \"life\". If I succeed, I'll have an actual career. Doing something that helps people, kind of. Sort of. Definitely, when compared to the Camarilla's alternatives. If I fail..."

        beast "We're probably screwed, so try not to fuck everything up this time around. I don't think we'd do well on the run."

        "Probably not as an Anarch, either. With my feeding requirements and hunting style, I'm kinda reliant on political stability and clear-cut rules about access and domain."

        "It's actually kind of ironic. I could survive on my own just fine as a mortal human being. But as an immortal undead monster, I'm dependent on the system in a way I never was before."

        beast "Please. You were {i}not{/i} surviving just fine on your own. You were well on your way to being found dead on some trap house sofa."

        "Shut the fuck up. You weren't even there for any of that. That was long before I got saddled with you."

        beast "Oh, [pcname]. Haven't you realized? I've {i}always{/i} been here. The Curse of Caine merely gave me a louder voice. {i}Everyone{/i} has a Beast inside them."

        beast "Vampires have simply built a culture around externalizing the Beast. Blaming it for their depraved thoughts, their vile actions. As if it hadn't always been a part of them since the day of their mortal birth."

        "That's nothing but conjecture. You don't actually know any of that. You don't know anything. You're just an ugly voice in my head, spouting bullshit, as usual."

        beast "If it's bullshit, it's as much yours as mine. We're one and the same. There's a reason I'm not just a nameless, voiceless urge in your gut. You experience me this way because you {i}want{/i} to. Maybe because you {i}need{/i} to."

        "You're so full of it."

        beast "Anyway, good luck with the meeting. Our future is on the line. No pressure."

        scene bg rooms boardroom1 with dissolve

        if not story_hunted_early:
            play music audio.seneschal2 fadein 1.5 volume 0.5

            "Right. Room 306. I open the door. It's a small, tastefully-furnished boardroom. Well-lit, unlike most of the building. Two people are inside, both obviously Kindred."

            if pc.getHunger() < 3 and pc.getPredatorType == PT_SIREN:
                "One of them is a gorgeous South Asian woman with lustrous black hair in one long braid. She looks like she's modeling that pinstripe suit. It's a fucking look. Even {i}I'm{/i} jealous."

                beast "{i}Focus.{/i}"
            else:
                "One of them is a dark-skinned woman with a jet-black braid, holding a tablet. She wears her pinstripe suit like she's modeling it for an ad."

            "She must be Kay Sanghera, because the other Kindred fits the description of the Seneschal that I was given. Somehow, it doesn't do [sen_obj] justice."

            "The Seneschal is like a Renaissance painting come to life. Slender, nearly as tall as Gabriel outside, with olive skin, prominent cheekbones, in a deep blue robe over leggings and a blouse that I'm pretty sure is designer."

            $ sen_Subj = str(sen_subj).capitalize()
            "[sen_Subj] turn to look at me with [sen_pos] deep green eyes, and nod in approval."

            sam "[pcname] [pclastname] of Clan Ventrue. Childe of Madam Walker. You're early, good. Punctuality is important in our line of work. This is Keerat Sanghera, a prominent member of our Court, also of the Clan of Kings."

            sam "And I'm [senfirst] [senlast]. Clan Toreador. Seneschal to Prince Nevarra."

            me "Pleased to meet you both."

            keerat "Likewise, I'm sure. I go by \"Kay\"."

            sam "Let's not waste any more time. Ms. Sanghera is here mainly because this matter concerns her own holdings in this city."

            if pc.getHunger() < 3:
                me "I was told I'd be assisting with a large-scale Masquerade cleanup operation."

                sam "Yes, we'll be getting to that in a few nights. There's still more work to be done on that front, as well as a matter I need to consult the Prince on. But there's a simpler, more immediate issue we'd like you to handle in the meantime."

                me "Understood. Whatever you need, I'm here to help. I'm listening."

                sam "Kay, would you like to handle the briefing? I want to make sure your concerns are addressed."

                keerat "Certainly, Seneschal."
            else:
                "Hunger bubbles its way back up to the front of my mind, like an erupting geyser scalding my brain. It's so hard to focus through the ache..."

                sam "Ms. [pclastname]. Ms. [pclastname]!"

                "The Seneschal's eyes bore into me. Kay looks unimpressed."

                me "I'm sorry, please continue."

                keerat "...Right."

                $ setOpinion(F_CAMARILLA, 15, "subtract")
                $ setOpinion(F_VENTRUE, 10, "subtract")

                beast "This is what happens when we don't feed, genius. You space out like some sleep-deprived mortal at an office job."
        else:
            "Yeah, and whose fault is it that we've already made a bad impression?"

            beast "Yours, of course. For letting us go hungry in the first place. I merely ensured that the bare necessities were taken care of. As I always do."

            "Oh fuck off, Baloo. We're here. Room 306. I open the door."

            "It's a small, tastefully-furnished boardroom. Well-lit, unlike most of the building. Standing off to one side is a dark-skinned woman in a pinstripe suit. She looks like she could be modeling it for a magazine. Her jet-black hair is tied back in one long braid."

            keerat "Ah, you must be [pcname] [pclastname]. I'm Kay Sanghera. How wonderful that you've deigned to join us."

            beast "..."

            "Her voice carries only the faintest hint of an accent. Her face is flat and expressionless, but her anger shines out through her eyes. We're off to a great start."

            me "Uh, yeah. Sorry I'm late. I, uh... I had something to take care of."

            keerat "You had something to take care of."

            me "..."

            keerat "Well, hopefully you've now concluded whatever business was important enough to keep the Seneschal waiting. More important, presumably, than the security of an entire city's worth of Kindred. Certainly more important than anyone else's time."

            keerat "Perhaps you were rooting out a nest of Sabbat, heroically slaying their pack leader in single combat? Or securing the sarcophagus of some ancient Cainite, to prevent it from rising and devouring us all?"

            play music audio.freakout fadein 1.5 volume 0.6

            beast "The concrete walls outside seem pretty sturdy. I wonder which would break first - them, or her head?"

            me "Okay, okay."

            keerat "Or perhaps the worst has already happened! Perhaps an ancient has already awoken, and you come to us from the front lines, battling bravely to destroy-"

            if pc.getAttr(_com) > 2:
                me "Enough. You made your point. I held up the show. I'm sorry. I was hunting. You know that sustenance always comes first for our kind, and my Clan has unique requirements."

                keerat "Our Clan, and of course I do. It's your job to account for that."

                me "And I did. In a strange city. So it took a bit longer. Why was the meeting scheduled this early, anyway? Any Kindred could have woken up hungry and needed to feed. I wasn't given any accommodations of that sort."

                python:
                    if not pc.hasPerk(M_LINE_HARDESTADT[KEY_NAME]):
                        pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

                "My voice is resonant and booming with authority, and Kay's expression softens."

                keerat "You do have a point. The meeting was scheduled unusually early. But while you're here, you're on the Seneschal's time. They don't do anything without reason. So get used to odd hours."
            else:
                play sound audio.tablefist

                me "I WAS FUCKING HUNGRY, OKAY?! Jesus FUCKING Christ. Why the FUCK was this meeting scheduled so early in the night anyway?! What the fuck was I {i}supposed{/i} to do if I woke up hungry? Just show up here shaking like a fucking tweaker?"

                python:
                    pc.damage(KEY_HP, KEY_SPFD, 1)
                    if not pc.hasPerk(M_LINE_HARDESTADT[KEY_NAME]):
                        pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

                "Oh shit. I said all that out loud didn't I? And oops, looks like I broke a piece off the table. With my fist. Fuck. That happens sometimes when I get really, really stressed."

                "And I shouted, did the voice thing again. Fuck. Pull yourself together, [pcpetname]. I can't lose my shit. Not here. Not now."

                beast "Can't we, though? I mean, who's gonna know? We could eat this bitch, eat her ghoul, and skip town."

                "...Didn't you just fucking point out that we wouldn't do well on the run?"

                beast "Just throwing out suggestions. Brainstorming."

                stop music fadeout 1.0

                keerat "..."

                me "I'm sorry. That outburst was uncalled for."

                if pc.getSkill(_intr) + pc.getAttr(_wit) > 4:
                    "She hasn't moved an inch. She isn't the slightest bit afraid of me. But the anger has gone out of her eyes and her expression has softened a bit. Her look is... not exactly sympathetic, but less contemptuous and more curious."
                else:
                    "She hasn't moved an inch. Guess she doesn't scare easy."

                keerat "Indeed it was. But you do have a point. The meeting was scheduled unusually early. But there is a reason for everything the Seneschal does. And while you're here, you're on {i}their{/i} time. So get used to odd hours."

            "I give her a quick bow. I'm not sure if that's a thing, but I figure a gesture of respect might help move things along."

            me "Please, Ms. Sanghera. Let's proceed."

            play music audio.scene1_awakening volume 0.5

        keerat "Very well. We'll keep it short. There is a larger issue, the one we brought you here to help deal with. A series of high-profile Masquerade breaches have occurred in recent weeks. But that's not what this particular briefing concerns."

        keerat "This is an issue that came up two nights ago, and unlike the larger case, its cause is known. Anarchs. An unauthorized Embrace. Police involvement. You'll be helping deal with that."

        "I really, really hope she's not about to ask me what I think she is."

        me "...You want me to hunt Anarchs?"

        "She smirks."

        keerat "Ah, no. The Sheriff is taking care of that. We want you to handle the police involvement."

        keerat "The illegal embrace took place at {i}Bandita{/i}, a club that I own. My people have already handled the witnesses. Non-lethally, of course. And we expect the same of you."

        "Okay, good. I didn't sign up for wetwork."

        keerat "Unfortunately, the police arrived more quickly than we expected and we weren't able to prevent them from seizing our security footage and a few other items. Not without causing more problems, anyway."

        keerat "You are to infiltrate the police precinct at 3rd and Goliath. Your objectives are as follows: Retrieve a physical copy of the police report. Use it to find and delete the security footage."

        keerat "Next, you are to locate their evidence storage and seize or destroy any physical evidence that is visible or mentioned in the report. Access their database and destroy all relevant records, including any digital copies of the report."

        keerat "Finally, destroy {i}their{/i} security footage, and get out without being seen. Do you have any questions or comments?"

        me "Well, first off, what about offsite backups? Cloud storage and all that?"

        keerat "We have another asset handling that. There will be no backups for these particular data. Not that the police here put much effort into security or data protection anyway."

        me "Okay, cool. Second, what do you even need me for? I thought it was standard practice for the Tower in any city to control that city's police department."

        keerat "That's a valid point, albeit based on an oversimplified, exaggerated idea of our species' control over mortal affairs. Yes, we do have our agents among the police. The problem is that the Anarchs have a few of their own."

        keerat "And until we can identify and either remove or co-opt whichever law enforcement officials are on \"Baron\" Marlowe's payroll, so to speak, we don't want to reveal any of our own agents."

        keerat "The Anarchs are paying close attention to these events, and there's no element of plausible deniability here. Any interference we engage in through our agents will be obvious and easily traceable. We'd rather not lose assets over this."

        me "So I'm the expendable pawn."

        if story_hunted_early:
            keerat "Until you prove yourself to be more, yes. If you fail we'll simply move on to our next contingency."

            beast "Eh, can't fault her honesty. I still want to smash her face in, though."

            keerat "Naturally, you'll be paid a salary while you're here as our \"consultant\". Above-board, as I understand you're very young and still using your mortal identity. Here's a small advance. It would have been bigger if you hadn't annoyed the Seneschal."

            $ pc.gainCash(300)

            keerat "And I've provided you with an email address, at which you'll receive some useful documentation."

            me "Thanks. What's our time frame here?"

            keerat "You have three nights. If you're worth the recommendation you come with you should be able to do it in one night, but - as you brought up earlier - we want you to have time to prepare. So you can do the job right."

            keerat "Here's a burner phone you can use to contact the Seneschal in an emergency. {i}Only{/i} in an emergency. Good luck to you. You're dismissed. Get out."

            $ pc.addToInventory("smartphone2b")

            me "Right. Thanks again. Sorry about the table."

            "I get out. Kay's retainer gives me a strange look as I pass. I get into the car and drive off."
        else:
            sam "You're in the wrong line of work if you're afraid of a few cops. Especially as a Blue Blood."

            me "I'll manage."

            sam "I'm sure you will. While you're here as our \"consultant\", you'll be paid a salary. A normal, legal, taxable one that shouldn't be problematic for your mortal identity. Here's a small advance."

            if pc.getHunger() < 3:
                $ pc.gainCash(1000)

                "Huh. A thousand bucks. That should make things a little easier. I'm going to need clothes and equipment."
            else:
                $ pc.gainCash(700)

                "$700. That should help with operating expenses."

            sam "There's more in it for you, potentially. Depending on how satisfied the Court is with your performance. And here's a burner phone. Use it to contact me, but only in an emergency. Otherwise, you can call on me at Elysium."

            $ pc.addToInventory("smartphone2b")

            keerat "And I've provided you with an email address, at which you'll receive some useful documentation."

            sam "I believe that concludes our business here, unless you have anything to add, Ms. Sanghera?"

            keerat "No, Seneschal."

            sam "Then you're dismissed, neonate. Good luck."

            me "Thank you, Seneschal. I'll be in touch."

            "I walk back out to my car. Agnes, Barak and Gabriel nod to me as I pass them."

        queue sound audio.heels_on_pavement

        queue sound audio.carstart_pc

        scene bg driving road2 with trans_slowfade

        play music audio.car_meeting fadein 2.0 volume 0.6

        if story_hunted_early:
            "Well that could have gone a lot better. But I have my orders, and this first assignment doesn't seem hard. I text [ghoulname], tell him to wait for me at the hotel."
        elif pc.getHunger() > 2:
            "That could have gone a bit better. But I have my orders. This thing with the cops doesn't sound too difficult. I text [ghoulname] and tell him to meet me at the hotel. And to bring me someone to eat."

            beast "He'd better."
        else:
            "Well that went pretty well. I had to choke down some nasty shit to make it happen, but I have my orders now. I text [ghoulname] and tell him to meet me at the hotel. I can feed for real, and then we can talk strategy."

        "Kay said that the Sheriff was taking care of the \"unauthorized Embrace\". Meaning some poor bastard had their first life stolen from them and now they have to run or fight for their second. Assuming they aren't already dead."

        beast "Don't start down that path. There's nothing you can do about it. And even if you could, who says you should? Maybe that new fledgling was going to murder a bus full of kids or some shit. Maybe they're better off destroyed."

        "Maybe. It's true that vampires who can't handle what they are always end up doing something horrible. It's just... that could have easily been me, you know?"

        beast "Not really. You think Embraces are common, legal or not? There are like 7.5 billion people on this planet. And there's, what? A couple hundred thousand of us? If even that?"

        beast "Nah, the average cases for someone like you are prison, an early grave, or - if you were lucky - a lifetime of pointless toil in the mortal rat race. Instead, you got {i}super{/i} fucking lucky and stumbled your way into Kindred society, unscathed."

        "You're right. I suppose I should be grateful. Most people don't get second chances. Not with the things that matter. So, what, I should be loyal to the Ivory Tower out of gratitude?"

        "Because they rescued me from my shitty choices, and also capitalism?"

        beast "I didn't say all that. Vampires aren't capable of loyalty, and they don't appreciate gratitude. Vampires appreciate {i}results{/i}. Get the job done, and we'll stay as \"loyal\" as we need to in order to get what we want."

        "A chance to help people. To make something of myself. To give back. To establish a proof-of-concept that we can get what we need without inflicting quite so much death and suffering on innocent muggles."

        beast "Food, security, resources, power. Then all of that stuff, sure. Heirarchy of needs. We carve out our own little corner of eternity and do whatever we want until the law of averages kicks in and it all inevitably comes crashing down."

        beast "I mean, let's be real. Even if we're technically capable of living forever, we're not going to. Something's gonna get us eventually. But if we play our cards right we can definitely spend a few centuries living high on the hog."

        beast "And if you want to play nice with our human herd once we get it, fine. I won't stop you. But whatever you want to do, you're going to need power. Status. And right now that means focusing on the task at hand."

        "Right. One night at a time."

        jump chapter0.ghoul_hookup

    label .ghoul_hookup:

        # TODO: ghoul meeting should be here, and two more discipline power selections (after feeding)

        scene bg hotel exterior with fade

        "I pull up alongside the hotel I'm staying at, and [ghoulname]  is waiting for me. I step out and hand my keys and a generous tip to the valet."

        python:
            pc.loseCash(100)
            ghoulmiddle = _pcGhoul["middle"]
            ghoullast = _pcGhoul["last"]
            ghoulpet = _pcGhoul["pet"]

        ghoul "Do these eyes deceive me? Or am I in the presence of [pcpetname] motherfuckin' [pclastname]?"

        "I can't help but grin and hug him."

        me "This fucking guy! Hey [ghoulname]. You look good."

        ghoul "I know it, I know it. But not as good as you, baby girl. That purple minidress, with the necklace."

        "He makes the chef's kiss gesture. He's dressed like if Cirque du Soleil had a pimp on retainer. But he knows better than most how to dress for an occasion. I've seen his bag of tricks."

        "[ghoulname] [ghoulmiddle] [ghoullast]. I've known this guy since college. He was my dealer. I pulled some people together to help him out with his housing situation. It may or may not have involved some colorful threats to the landlord and a pair of rusty pliers."

        "We weren't going to hurt him (much), but he didn't know that. And [ghoulname] showed his gratitude by selling us Adderall and weed at a discount. Eventually I got into the harder stuff, though. After a while he stopped selling to me."

        beast "{alt}Laughing: {/alt}I remember that. Your fucking drug dealer had to cut you off."

        "Anyway, we've been friends since and when I got Embraced he was my first choice for a ghoul. Sly, elusive, persistent, and a lot tougher than he looks. He's pretty much the whole package."

        ghoul "You want to head up to your room and talk business?"

        if story_hunted_early or pc.getHunger() < 3:
            me "Yeah, let's."
        else:
            me "First order of business is lunch. I'm fucking starving. You brought food, right?"

            ghoul "About that... let's head upstairs and talk."

            beast "Whatever he's got to say better be good. Or we're eating him."

            if pc.getHumanity() > 7:
                "No, you idiot. We're not eating [ghoulpet]."
            else:
                "No, you idiot. We're not eating [ghoulname]. Although, he {i}is{/i} our type. We could feed from him as a last resort. With his permission, of course."

        play sound audio.heels_on_pavement

        scene bg hotel room with dissolve

        play music audio.hotel_neutral fadein 2.0 fadeout 1.5 volume 0.5

        ghoul "Damn. They got you set the fuck up, huh? That Egyptian cotton? What's on the room service menu?"

        me "Best hotel room I've had in a long time, for sure."

        ghoul "That just means you {i}really{/i} gotta deliver. So let's talk about that."

        if story_hunted_early:
            me "Sounds good."

            jump chapter0.strats_huddle
        else:
            if pc.getHunger() < 3:
                me "Hmm, I think I should feed first. Do you have anyone for me?"
            else:
                me "Food first. Don't you have someone for me?"

            ghoul "Uh, no. What, did you expect me to just snatch a motherfucker off the street? If you want me to set up that kind of operation, I'm going to need time and money."

            "I thought he was kidding, but the expression on his dark face has suddenly grown deadly serious. His brown eyes are cold and hard."

            ghoul "And what about the other Kindred in the city?"

            me "No, I meant just invite someone up. Or, no. Not up here. To some third location. With cash. Or whatever."

            ghoul "Similar issues apply, but yeah I can work on that. I still need to know the situation with the other Kindred, though. I don't know much about y'all, but I know what happens when you get caught doing some shit in the wrong neighborhood."

            me "Yeah, similar rules definitely apply. But I've got permission to hunt downtown. So you can start there."

            if pc.getHumanity() > 7:
                me "Wait, would you really start kidnapping people if I asked you to?"

                ghoul "I wouldn't exactly be celebratin' or nothin', but yeah. You gotta eat, right?"

                me "Yeah, but not like that."

                ghoul "Okay. Good."

                $ setOpinion(F_GHOUL, 10, "add")

            me "So..."

            ghoul "Well what I {i}have{/i} done is a bit of research. Marked out several spots where there's, uh, good huntin' or whatever."

            if pc.getPredatorType() == PT_SCENE_QUEEN:
                ghoul "Places that play that beep boop {b}BWAAAH{/b} music you like, where everybody's high as fuck. Speaking of which, you hit up \"Jack\" yet?"

                me "No, I'll do that tomorrow night. But good work."

                ghoul "No problem."
            elif pc.getPredatorType() == PT_SIREN:
                "He knows what I like."

                call feeding.establish_orientation from early_ghoul_meet_siren

                python:
                    exname = pcex["first"]
                    exsubj = pcex["subj"]
                    exobj = pcex["obj"]
                    exSubj = str(exsubj).capitalize()

                if story_orientation == SIREN_MEN:
                    ghoul "Places with those pretty boys you like. Lean muscle, tight shirts. Grade-A American beef."
                elif story_orientation == SIREN_WOMEN:
                    ghoul "Places with those pretty girls in tight dresses you like. Some real baddies, too."
                else:
                    ghoul "Places with beautiful boys, girls, and everything in between! Mmm-hm."

                me "Hell yeah. Mama's thirsty tonight."

                ghoul "Just, uh, let me know if you bringin' somebody back here. So I can leave."

                me "I don't plan on it, but sure."

                ghoul "And, uh... one last thing. Your ex is in town."

                stop music fadeout 0.3

                me "What."

                ghoul "Yeah. [exname]. [exSubj] caught me at a Royal Farms just outside of town. Wanted to know if I'd seen you lately. I told [exobj] no, obviously. And I made sure [exsubj] didn't follow me here."

                me "You {i}cannot{/i} be serious."

                ghoul "But [exsubj] definitely followed me into the city. Somehow [exsubj] got word you'd be here, in this city, now."

                me "No. No. I cannot deal with [exobj]. Not now."

                beast "Don't sweat it, [pcpetname]. We can just eat [exobj]."

                ghoul "I don't really have any connections in this town. Not yet. But I'll see what I can do."

                me "...It's fine. [exSubj] doesn't know where I'm staying, and the car's a rental. What are the odds I run into [exobj]?"

                ghoul "Well now you went and jinxed it."

                me "Shut up."

                play music audio.hotel_neutral fadein 2.0 fadeout 1.5 volume 0.5
            elif pc.getPredatorType() == PT_ROADSIDE_KILLER:
                ghoul "So I went and looked up traffic data for this city on... the fuck's it called? TomTom. And I found some nearby establishments that are close to major congestion spots. This city's got some big, fat, clogged arteries for you to suck on."

                ghoul "Commuters, homeless, truckers, everything! Should be real easy huntin'."

                me "Nice. Good work."
            else:
                ghoul "I ain't exactly sure how to look for people that'll just... {i}let{/i} you suck their blood. Like, out of the blue. Not without drawin' the wrong kind of attention, anyway."

                me "I guess I don't make it easy for you."

                ghoul "You really don't. But I did find a couple sex clubs, and a few groups on Fetlife that are in this city and open to, uh, \"blood play\"."

                me "Hmm... keep working that angle, but I'll hunt on my own tonight."

                ghoul "Whatever you say, boss."

            me "Alright, I'm headed out to hunt. Should be back in an hour, two tops."

            ghoul "Good luck."

            play sound audio.heels_on_pavement

            queue sound audio.carstart_pc

            "I think I can work with what [ghoulname] came up with. I take some time to freshen up, then head out."

            beast "Fucking {i}finally{/i}."

            scene bg driving road2

            "Okay, so with the address [ghoulpet] gave me, we have... Okay. Cool."

            "I punch the address into the GPS. Now I just need to be on the lookout for my \"type\". Something my Beast will accept."

            "..."

            "..."

            call feeding.hunt1_preamble from better_late_than_never_1

            $ ptstring = str(pc.getPredatorType()).lower().strip().replace(" ", "")

            call expression ("feeding.hunt1_" + ptstring) from better_late_than_never_2

            stop music fadeout 0.5

            jump chapter0.strats_huddle

    label .strats_huddle:

        scene bg hotel room

        play music audio.mission2

        ghoul "Alright, so what are the bosses makin' you do, exactly?"

        me "Well there's supposed to be a whole other issue that they won't tell me anything about for some bullshit bureaucratic reasons. But there was also an illegal Embrace, with an Anarch sire."

        me "While the Cam's off hunting those poor bastards down, I'm supposed to break into the police precinct on 3rd and Goliath. Once I'm in, they basically want me to steal all the physical evidence and wipe all the digital records."

        ghoul "Ah. Well, can't help you with Five Oh, but did they give you any, like, building schematics or some shit?"

        me "No... wait, maybe."

        "I log into the email address Kay gave me, using the burner phone."

        me "There's information about shift schedules, patrol routes, comm frequencies, passwords, and building schematics."

        ghoul "Oh. Damn. Sounds like they hooked up you up. But you still gotta physically get in and out, right? How are we pullin' that off?"

        me "Presumably some combination drawn from my abundance of natural talent and effortless mastery of the Ventrue arts."

        beast "Hah! Yeah, right."

        ghoul "Remind me what you can do, again? I mean the specifics. I know you can do some kind of Jedi mind trick woo-woo bullshit."

        call chapter0.power_select from pick_dot_3_power

        ghoul "So is that everything?"

        me "Not yet."

        call chapter0.power_select from pick_dot_4_power # Choose two more powers depending on your established four dots.

        ghoul "Damn. Alright, anything else?"

        me "Got one more."

        python:
            ptlabel = pc.getPredatorTypePower()["label"]
            ptquip = PT_QUIP_TABLE[pc.getPredatorTypePower()["power"]]
            if ptlabel:
                ptquip = ptlabel

        me "[ptquip]"

        ghoul "And that's it."

        me "Yep."

        ghoul "Well, all in all that was terrifying. Hearing the crazy disturbing shit y'all can do."

        me "Oh you don't know the half of it. There are other Clans with superhuman strength, Clans that can move so fast you can't even see, that can change their shape or do literal fucking magic, that can-"

        ghoul "Okay, okay! Enough for now. We'll speak on that later."

        jump chapter0.epilogue

    label .power_select:

        python:
            domrank = pc.getDisciplineLevel(_dominate)
            dompowers = pc.countPowersInDiscipline(_dominate)

            fortrank = pc.getDisciplineLevel(_fortitude)
            fortpowers = pc.countPowersInDiscipline(_fortitude)

            presrank = pc.getDisciplineLevel(_presence)
            prespowers = pc.countPowersInDiscipline(_presence)

        menu:
            me "Well, in addition to that..."

            # Dominate 3 - The Forgetful Mind
            "I can rewrite people's memories, if I can get their full attention for long enough to narrate it to them verbally." if domrank >= 3 and dompowers >= 2 and dompowers < domrank and not pc.hasDisciplinePower(_dominate, DOM_GASLIGHT):
                $ pc.addDisciplinePower(_dominate, DOM_GASLIGHT)

                ghoul "...Really?"

                me "Yeah, it's some straight-up Inception-type shit. Or Blade Runner. I never saw the 2049 movie, was it any good?"

                ghoul "..."

                me "...[ghoulpet]?"

                me "Oh come on, man! I didn't do it to {i}you{/i}. I wouldn't. We've been friends since before I dropped out of college. You know, when I was walking around in daylight?"

                ghoul "How the fuck do I know if that's true?"

                if pc.getHumanity > 7 or pc.getAttr(_cha) + pc.getSkill(_pers) >= 5 or pc.getAttr(_man) + pc.getSkill(_pers) >= 6:
                    me "Jesus Christ, dude. You're, like, the only actual friend I have left. That legit hurts."

                    beast "He really is, isn't he? Everyone else kind of hates you now. Or they're afraid of you."

                    me "That's why I chose you. If I were going to brainwash someone into it I could have done that to anyone."

                    ghoul "...You mean that?"

                    me "Of fucking course I do. And the whole point of this gig is so I can protect people from my fellow monsters. I use it to make people forget stuff that'll get them killed. I'd never use it on you."

                    ghoul "Okay. Alright. I believe you."

                    me "I'm glad. I don't want to lose you over this shit, man. Plus, I'm pretty sure repeated exposure to these powers is bad for people. I don't wanna give my ghoul brain cancer."

                    ghoul "You a laugh and a fuckin' half, ain't you?"

                    beast "You know he's Blood-bonded to you, right? Even if you were friends before?"
                else:
                    me "If I were going to brainwash someone into being my ghoul I could have picked anyone. Why would I have picked you?"

                    ghoul "Oh, thanks. That makes me feel a whole lot better about this arrangement! Fuck you, [pcpetname]."

                    me "For fuck's sake man, you know I didn't mean it like that. I meant that I chose you because we were already friends, and I already trusted you."

                    ghoul "Uh huh."

                    me "Seriously. And that's worth more to me than any mind-control powers. I use that shit on witnesses that would otherwise have gotten knocked off. To make them forget, and replace the gap with something plausible."

                    if pc.getSkill(_tech) >= 3:
                        me "Shit's not reliable, anyway. I don't have any way of knowing if it worked. It's like, I've got write permissions but not read. Like I'm just guessing at a range of memory addresses, and blinding overwriting whatever was there."
                    else:
                        me "The shit's actually kinda spotty and unreliable. I don't have any way of knowing for sure whether or not it worked. I can't {i}read{/i} minds."

                    ghoul "...Alright. Whatever. If you did brainwash me it's probably pointless to try and unravel it or whatever. The shit I had going on before isn't really worth crossing you to get back to, anyway."

                    me "...I didn't brainwash you, man."

                    ghoul "Let's just move on."

                    $ setOpinion(F_GHOUL, 20, "subtract")

                    beast "Well you sure did a shit job smoothing that over. But at least we know [ghoulname] is afraid of you too. That's good, right?"

                me "Okay, moving on..."

            # Dominate 2 - Mesmerize
            "I can give someone orders that they {i}must{/i} obey. Those orders can be long and complex if need be." if domrank >= 2 and dompowers >= 1 and dompowers < domrank and not pc.hasDisciplinePower(_dominate, DOM_MESMERIZE):
                $ pc.addDisciplinePower(_dominate, DOM_MESMERIZE)

                ghoul "So like in the Dark Tower? Damn."

                me "Not quite. I can't make people do things that they couldn't choose to do on their own. Or that go against, like, the core of who they are. Like I can't order a parent to shoot their kid, not that I ever would."

                me "I also can't give any orders that require them to, like, think. Because I don't have access to the contents of their mind; I'm just kinda hijacking their will. So I can't use it to get information."

                ghoul "So you're like Plankton in that one episode of Spongebob?"

                me "More or less."

            # Dominate 1 - Compel
            "I can give an order that {i}must{/i} be obeyed. It can't be too complicated, though. Like, \"stop\" or \"give me that\"." if domrank >= 1 and dompowers < domrank and not pc.hasDisciplinePower(_dominate, DOM_COMPEL):
                $ pc.addDisciplinePower(_dominate, DOM_COMPEL)

                ghoul "That sounds useful if you can get the words out in time."

                me "Yeah, and it's efficient too. Doesn't take much juice."

            # Fortitude 2 - Toughness
            "I can make my body hard, like granite. But still supple, like a normal person's body. Like a non-Newtonian fluid or something." if fortrank >= 2 and fortpowers >= 1 and fortpowers < fortrank and not pc.hasDisciplinePower(_fortitude, FORT_TOUGH):
                $ pc.addDisciplinePower(_fortitude, FORT_TOUGH)

                me "I'm not bulletproof, to be clear. But they're a lot less of a threat than they would be, even to other vampires."

                ghoul "Simple enough. But wait, hold up. I know they didn't give you permission to kill any fuckin' cops. Ain't no way your Illuminati bosses got that much pull."

                me "No, you're right. This is supposed to be non-lethal. Which is what I was expecting, or I wouldn't have signed up. But if a cop sees me and gets trigger-happy, better to have it than not. Plus, Anarchs."

                ghoul "Makes sense."

            # Fortitude 1 - Resilience
            "I'm tough. Like, supernaturally tough. Well, all vampires are. But I mean on top of even that." if fortrank >= 1 and fortpowers < fortrank and not pc.hasDisciplinePower(_fortitude, FORT_HP):
                $ pc.addDisciplinePower(_fortitude, FORT_HP)

                ghoul "Simple enough."

            # Fortitude 1 - Unswayable Mind
            "I've learned to use the Blood to actually toughen, like, my mind. Shit just doesn't faze me. Not easily." if fortrank >= 1 and fortpowers < fortrank and not pc.hasDisciplinePower(_fortitude, FORT_STUBBORN):
                $ pc.addDisciplinePower(_fortitude, FORT_STUBBORN)

                ghoul "So? You were always like that. Even when you really {i}should{/i} have been fazed."

                beast "Some might call that recklessness. Or stupidity. But I'm sure for you it felt like a superpower."

                me "Yeah, but moreso now. Plus, this protection actually works against supernatural mind control stuff like... the things my Clan does."

                ghoul "Well, that's way out of my wheelhouse."

            # Presence 3 - Entrancement
            "When I look into someone's eyes, I can make them fall in love with me. No, seriously." if presrank >= 3 and prespowers >= 2 and prespowers < presrank and not pc.hasDisciplinePower(_presence, PRES_CHARM):
                $ pc.addDisciplinePower(_presence, PRES_CHARM)

                ghoul "What if they're not attracted to you?"

                me "Doesn't matter. It's not necessarily romantic or sexual love, although I'm sure it could be. It's also, like, love for a family member or close friend."

                ghoul "So you can just get anything you want from anybody, huh?"

                me "Well, there are limits. Like if the person you love most told you to, I don't know, throw a toddler down a manhole, or hand them all your cash and product... would you?"

                ghoul "Probably not. I see what you mean."

                me "All these arts have a bunch of different names. This one's sometimes called, uh, \"Sublimitas\". Or, \"Enthrallment\". It can't {i}make{/i} anyone do anything, unlike Mesmerism."

                me "It just makes people {i}want{/i} to do what you want. Doesn't mean they will. But in exchange, it's way more subtle and doesn't leave people with that sense of violation, of losing control."

                me "They think that's just what they felt at the time."

                ghoul "...Good Lord."

                me "Yeah it's really fucked up. I'm trying to be judicious with this stuff. Trying to keep perspective, remember what the alternatives are."

                ghoul "The Cam knocks off witnesses."

                me "Not if I can help it."

            # Presence 3 - Dread Gaze
            "I can project my Beast out towards a single person and scare them shitless." if presrank >= 3 and prespowers >= 2 and prespowers < presrank and not pc.hasDisciplinePower(_presence, PRES_SCARYFACE):
                $ pc.addDisciplinePower(_presence, PRES_SCARYFACE)

                ghoul "That sounds fuckin' hilarious, actually. Useful too."

                me "It is pretty funny. They usually either run screaming or fall into the fetal position. Works on other vampires, too."

                beast "Heh."

            # Presence 2 - Lingering Kiss
            "When Kindred bite and feed on someone, it feels good. Great, actually. I know that from experience. But I can make it even better. I can make them want more." if presrank >= 2 and prespowers >= 1 and prespowers < presrank and not pc.hasDisciplinePower(_presence, PRES_ADDICTED2U):
                $ pc.addDisciplinePower(_presence, PRES_ADDICTED2U)

                ghoul "Wow. So you're the dealer {i}and{/i} the drug. Ain't you supposed to be using these powers for good?"

                me "Well, generally. This one is for keeping me fed so I don't flip out and exsanguinate somebody's grandmother. But I take your point. It's for emergencies."

                ghoul "Well, far be it from me to impugn your sterling character on grounds so similar to my own illustrious career."

                me "Magnanimous as ever."

            # Presence 1 - Awe
            "I can project an aura of allure, that draws attention and interest. Makes people more amenable to what I have to say." if presrank >= 1 and prespowers < presrank and not pc.hasDisciplinePower(_presence, PRES_AWE):
                $ pc.addDisciplinePower(_presence, PRES_AWE)

                if pc.hasPerk(M_LOOKS[KEY_NAME]):
                    "So basically I'm even more irresistible than usual."
                else:
                    "I'm always the life of the party, if I want to be. Unless there's a more powerful vampire around."

                ghoul "Well, shit. That sounds like it would be useful... pretty much everywhere."

                me "Not when shit's already popping off. But otherwise, kinda."

            # Presence 1 - Daunt
            "I can project an aura of \"don't fuck with me\". Makes people uneasy around me and terrified to get close or interact with me." if presrank >= 1 and prespowers < presrank and not pc.hasDisciplinePower(_presence, PRES_DAUNT):
                $ pc.addDisciplinePower(_presence, PRES_DAUNT)

                beast "So basically your normal personality, dialed up to 11."

                ghoul "I can see how that would come in handy in a Mexican stand-off type of situation. Best self-defense technique is to avoid the fight in the first place."

                me "Exactly."

        return

    label .epilogue:

        "Dawn's almost here. This wasn't terrible for my first night on the job. Real work starts tomorrow."

        # TODO: More here.

        scene black with fade
        jump nightloop
