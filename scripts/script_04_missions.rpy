label missions:

    define securitycop = Character("Security Guy", color = "#66709a")
    define _shadyguy = Character("Shady Guy", color = "#2a2a44")
    define _dirtycop = Character("Dirty Cop", color = "#5551a1")
    define _anarch = Character("Anarch Enforcer", color = "#673030")
    define receptionist = Character("Receptionist", color = "#c54b8c")

    $ global arena
    $ global night
    $ global daysLeft
    $ daysLeft = 7 - int(night)

    label .mission1_start:

        play sound audio.shower_pc

        "I put on a dark blue tracksuit (it's better concealment at night than straight black), some shades, gloves, and running shoes. Then I take a pair of scissors and cut most of my hair off."

        "One of the first things I learned is that hair, nails, fingertips and other minor extremities can be grown back during daysleep, with little risk of growing Hunger."

        "So cutting my hair and growing it back the next night makes for an easy and effective disguise."

        $ pc.soundRoadTrip()

        scene bg driving road2 with trans_slowfade

        play music audio.car_hunting2 fadein 3.0 volume 0.6

        "In theory this isn't too different from, uh... let's call it past experience."

        "But breaking into a police precinct is probably well beyond my wheelhouse as a mortal. I'll probably need to rely on the Blood, at least to cover my ass."

        beast "Oh don't worry, I'm good at that. I've been doing it your whole life, after all."

        "..."

        "So anyway, I've reviewed all of the data that Kay Sanghera helpfully provided. I have a pretty standard toolset with me - backpack with a crowbar, boxcutter, zip ties, blood and tissue kit, bandages, duct tape, various odds and ends. Duffel bag with redundant sets of clothes."

        if pc.getSkill(_tech) > 2:
            "Laptop full of torrented software, USBs with all the latest script kiddie hacking tools and commercial malware, not my smartphone of course - I trust my sire's netsec people, but why risk it?"

            "I do have the burner that came with the GPS disabled. In case I need to take pictures of files."
        else:
            "Laptop and USBs to hit the precinct database and maybe shut down some cameras."

        "And just as an extra precaution..."

        play sound audio.stab1
        queue sound audio.womangrunt
        $ pc.damage(KEY_HP, KEY_SPFD, 1)

        "I take the boxcutter and slice up my face pretty good. Enough to make me unrecognizable if I'm seen or recorded, while still looking like I could be human. Everything can be mended later, and the pain is pretty easy to get used to when you've been dead for a few years."

        beast "Never a dull moment with you, eh?"

        if pc.getSkill(_tech) > 2:
            "I'm honestly surprised more licks don't use this trick. Though I wouldn't be surprised if in a decade or two facial recognition tech has advanced enough to make even this untenable."
        else:
            "I'm honestly surprised more licks don't use this trick. What, do the Nosferatu have a trademark on ugly or something? Am I gonna get sued?"

        "God, imagine what kind of injuries your average elder has seen. Though I've only met the one."

        beast "I'd like us to live long enough to find out. Well, realistically we're not making it to elderhood. But a bona fide ancilla? We could swing that, if we're clever and careful. How about it, [petname]? Think you can go a century or two without getting us killed?"

        "No promises."

        scene black with dissolve

        play sound audio.carstopengine_pc
        queue sound audio.carstopkeys_pc
        queue sound audio.heels_on_pavement

        "As usual, I park several blocks down from where I'm actually going, this time in a parking spot that's very much illegal. So I'd better be back in an hour or two, tops."

        "I keep my head down the whole way, wearing a cheap set of headphones connected to nothing so I can feign distraction."

        "...Which may have worked a bit too well. I cut through alleys in the dark, trying to map out some alternate routes for the job. Just a few minutes in I've picked up a tail."

        $ grade = None

        menu:
            "I could probably still run, and I could certainly take him. He's just some mortal. But I don't know how much trouble this guy's going to be either way."

            "I turn around and face him. I'm not about to run from some mortal lowlife. Even if I used to be one.":
                jump missions.mission1_thug_fight

            "I take off running. I don't have time to deal with this creep.":
                $ grade = pc.basictest(4, _dex, _athl)
                jump missions.mission1_thug_run

            "I don't have time for this; I'm on the job! I'm willing to burn some Blood to lose this worm.":
                $ grade = pc.basictest(4, _dex, _athl, pc.getBPSurge())
                $ pc.addHungerDebt(4)
                jump missions.mission1_thug_run

    label .mission1_thug_run:
        if grade > -1:
            $ arena.readOppStory("escape", shadyguy)
            jump missions.mission1_thug_escape
        else:
            "...Shit. This guy's faster than he looked, and he definitely knows the area. I'm not getting away. His loss."

            beast "Drain this puke."

            jump missions.mission1_thug_fight


    label .mission1_thug_fight:

        "He closes in on me like a wolf, a sick grin on his face and a switchblade in his hand. It's a Godfather, too. Chalk up \"good taste in knives\" as this creep's sole redeeming quality."

        _shadyguy "Now what's the hurry there, beautiful? I didn't even get your name."

        me "You can still walk away, asshole."

        "My voice is flat. His breath reeks of cheap booze."

        _shadyguy "And miss our chance to get to know each other? Perish the thought!"

        "Well that erases any doubt that this guy's here to do one of two things. Guess I'm gonna fuck him up."

        beast "Couldn't happen to a nicer guy. Let's make a nice quiet dinner out of him."

        # Battle with creep
        $ global shadyguy
        $ arena.setStage()
        $ arena.startBattle(shadyguy)

        "So that's that. Oh, but look. Our friend seems to have dropped something."

        $ pc.addToInventory("switchblade", customToolTip = None)

        beast "Well at least we got a weapon out of this sideshow. About time you started carrying one again. We're not Rabble or Sewer Rats; we can't tear our enemies limb from limb with our bare hands."

        "I should totally look into finding someone to teach me that art, though."

        beast "Yes, you should. Look at you, planning for our future as if you're not some aimless wastoid."

        "My sire says that any Kindred can learn the arts of any Clan, though some require more teaching than others. And you need to taste their Blood. Which is always a risk."

        jump missions.mission1_case_joint

    label .mission1_thug_escape:

        "I check for any other unwanted companions, then move on."

    label .mission1_case_joint:

        scene bg precinct exterior with fade

        "With that distraction out of the way, I make my way through the alleys and emerge a block north of the precinct complex at the waterfront."

        if night > 2:
            "I definitely want to case the joint first - but whatever I find, the job has to get done tonight."
        else:
            "I definitely want to case the joint first, but then I'll have to decide if I want to do the actual job tonight or make more preparations and come back tomorrow night."

        beast "Still putting off dealing with your problems, I see."

        menu:
            "Shut up and let me work."

            "I'll circle around a few times, take photos from a safe distance, and note entrances, cameras, any cops I can spot. Then I'll compare it to Kay's info and see what I can come up with. ([_wit] or [_int] + [_inve] or [_awar])":
                $ grade = evalt(pc.basictest(5, max(pc.getAttr(_int), pc.getAttr(_wit)), max(pc.getSkill(_inve), pc.getSkill(_awar))))

            "I don't want to mess this up, so before all of that I'm going to send Blood to my brain and eyes. I love being my own performance-enhancing drug.":
                $ grade = evalt(pc.basictest(5, max(pc.getAttr(_int), pc.getAttr(_wit)), max(pc.getSkill(_inve), pc.getSkill(_awar)), pc.getBPSurge()))

        scene black with fade

        "..."

        play sound audio.heels_on_pavement

        "..."

        scene bg precinct exterior with fade

        if grade == SUCCESS:
            label .mission1_try_again: # Start here if you're trying a second time after failing.
            scene bg precinct exterior with fade

            "Hmm... Well, I can see two ways of going about this. Both of them risky and difficult, just in different ways."

            "I can go around back and physically break in, which is no sure thing. I'll need to leap fences, dodge cameras, scale a wall, and break in without triggering any alarms. And then I'll need to be wary of security inside, though I do of course have Kay's schematics."

            "Alternatively, I can try talking my way in. According to Kay's info they're having network issues (can't imagine why) and are expecting someone in a few days. They're not happy about the delay, so maybe they'll be happy to see me - if I can bullshit well enough."

            # "Finally, there's that one off-duty cop hanging out in the front parking lot. He's got beer and a blunt; maybe he'd like some company to go with it. Might could wheedle a tour of the precinct out of him, if he thinks it'll get him laid."

            beast "I feel like you're forgetting something."

            "Naturally, for the latter I'll have to mend my scars and take the risk of showing my actual face. So much for my clever trick."

            if not story_mission1_start and not story_mission1_cased:
                call missions.mission1_proceed_choice from _call_missions_mission1_proceed_choice

            python:
                hottie = pc.hasPerk(M_LOOKS[KEY_NAME])
                hasAwe = pc.hasDisciplinePower(_presence, PRES_AWE)
                hasEntrance = pc.hasDisciplinePower(_presence, PRES_CHARM)
                hasMesmerize = pc.hasDisciplinePower(_dominate, DOM_MESMERIZE)

                if hottie:
                    tourMsg = "Luckily for me, I'm a total baddie and I look hot as fuck even in an unfashionable, ill-fitting tracksuit."
                    aweMsg = "between my looks and my aura he won't know up from down."
                else:
                    aweMsg = "sway him with my aura."
                    if hasAwe or hasEntrance:
                        tourMsg = "I'm not dressed in the most flattering wardrobe at the moment, but I'm sure can pull it off anyway. Even if I have to use my supernatural allure."
                    else:
                        tourMsg = "I'm not dressed in the most flattering wardrobe at the moment, but I'm sure I can charm or hoodwink a drunk, faded cop anyway."

            menu:
                beast "Alright, so hurry up and choose. Feel free to call on me, but only if you're prepared to pay the fee later. Or rather, make someone else pay it."

                "I think I want to try a manual break-in. I've got the tools and I've got the info, but I'll need strength, finesse, sharp senses and quick reflexes to pull it off. First step is avoiding the exterior cameras. ([_wit] + [_awar] or [_clan])" if not story_m1fail_burglary:
                    call missions.mission1_bloodsurge_choice from _call_missions_mission1_bloodsurge_choice
                    jump missions.mission1_breakin

                "They're expecting someone to fix their connectivity issues, so I can bluff my way in - if I can talk the talk. But before that, it'll help If I can take some of those exterior cameras offline. Don't want footage of my unscarred face. ([_int] or [_wit] + [_tech])" if not story_m1fail_tech:
                    call missions.mission1_bloodsurge_choice from _call_missions_mission1_bloodsurge_choice_1
                    jump missions.mission1_techbluff

                # "I'll think I'll head for the parking lot and pay Officer Blunted over there a social call. [tourMsg] ([_cha] + [_perf], or [_man] + [_intr])" if not story_m1fail_social:
                #     call missions.mission1_bloodsurge_choice
                #     jump missions.mission1_blunted_tour
                #
                # "I'll go see the zooted cop, and [aweMsg] ([_cha] + [_perf] + [_presence])" if hasAwe and not story_m1fail_social:
                #     $ global usingAwe
                #     $ usingAwe = True
                #     jump missions.mission1_blunted_tour
                #
                # "Why am I wasting time trying to make myself appealing to some drunk cop? I'll gladly risk Hunger if it means I can just march up and {i}make{/i} him take me inside." if (hasMesmerize or hasEntrance) and not story_m1fail_social:
                #     $ global usingMindControl
                #     $ usingMindControl = True
                #     jump missions.mission1_blunted_tour

        else:
            "Hmm... Well, I really only see one way in."

            beast "It's a police station. Did you expect it to be easy to break into?"

            "I'll have to go around back and physically break in, which won't be easy. It'll involve leaping fences, dodging cameras, scaling a wall, and breaking in through a window without triggering any alarms. And then I'll have to rely on Kay's info to deal with security inside."

            if not story_mission1_start and not story_mission1_cased:
                call missions.mission1_proceed_choice from _call_missions_mission1_proceed_choice_1

            call missions.mission1_bloodsurge_choice from _call_missions_mission1_bloodsurge_choice_2
            jump missions.mission1_breakin

    label .mission1_proceed_choice:
        if daysLeft < 2:
            "And I'll have to do this tonight. There's no time for more preparations. I'm already cutting it close to the deadline."
            return
        else:
            "This is all assuming I even do the job tonight. I've got time. I can hunt, prepare, or just relax."

            $ willdamage = (pc.getTrackerDamage(KEY_WP)[KEY_SPFD] > 2 or pc.getTrackerDamage(KEY_WP)[KEY_AGGD] > 0)
            $ hpdamage = (pc.getTrackerDamage(KEY_HP)[KEY_SPFD] > 2 or pc.getTrackerDamage(KEY_HP)[KEY_AGGD] > 0)

            menu:
                beast "Has putting things off ever led to anything good in your life?"

                "When you're right, you're right. Let's do this." if (not hpdamage and not willdamage) or story_mission1_cased:
                    $ story_mission1_cased = True
                    return

                "There's still time. I should come back better prepared.":
                    beast "..."

                    $ pc.soundRoadTrip()

                    stop music fadeout 1.5
                    scene black with fade

                    python:
                        if not story_mission1_cased:
                            pc.mend(KEY_WP, KEY_AGGD, 1)

                        story_mission1_cased = True
                        updateTime(0.5)

                    jump nightloop

    label .mission1_bloodsurge_choice:
        menu:
            "I can risk Hunger to send Blood wherever I need it for the upcoming task."

            "I could definitely use a little performance enhancement.":
                $ usingBloodSurge = True

            "Nah, not worth the risk. I can swing this on my own.":
                $ usingBloodSurge = False

        return

    # STAGE 1-A, SECRET AGENT BREAKIN
    label .mission1_breakin:
        play music audio.introMission fadeout 2.0 fadein 2.0 volume 0.7

        "So if I'm going with the Mission Impossible approach, I can leave my face cut up. Anyone I run into probably needs to get the old neuralyzer, but the most important thing is destroying the evidence."

        "The Seneschal won't like it if I'm spotted, but that's not in and of itself a breach of the Masquerade."

        if max(pc.getAttr(_str), pc.getAttr(_dex)) + pc.getSkill(_athl) > 4:
            "I circle around the back, walking casually but out of camera range. When I get in position, I can take a running start and easily parkour off an adjoining wall to jump the fence and land without too much noise. Even cleared the razorwire, no problem."

            "Now here comes the hard part. Well, the {i}first{/i} hard part."
        else:
            "I circle around the back, walking casually but out of camera range. I'm not going to be able to leap the fence, but after a few minutes I find a spot that's out of camera view. Or at least it better be, given what I have to do next."

            "I'm going to have to pull myself up and over the fence, razorwire and all. And I can't let my clothes or my gloves get shredded, so I have to strip and toss them over, then climb over a ten foot tall, spiked, razor-wired fence. Butt-ass naked. Wonderful."

            $ pc.damage(KEY_HP, KEY_SPFD, 1)

            "Well that was painful in more ways than one. Now that I've put my clothes back on, here comes the hard part. Well, the {i}first{/i} hard part."

        "I pull up Kay's schematics on the burner phone and double check them with my own notes from the casing, as well as what I can see from my current position."

        "After about ten minutes waiting and checking my notes, I think I have the pattern down, and a path through. Here goes..."

        python:
            chosenSkillScore = max(pc.getSkill(_awar), pc.getSkill(_clan))
            result = pc.test(5, _wit, chosenSkillScore, pc.maybeBloodSurge())
            print ("\n\nbreak-in result", result)
            grade = evalt(result)

        if grade == MESSYCRIT:
            beast "Oh for fuck's sake. Are we gonna stand here all night?"

            play sound audio.beastgrowl1

            "I find myself loping and bounding toward the spot below my chosen window, but I'm going way too fast. The timing is off; at this rate I'm going to end up within sight of a camera. That won't do."

            "Without breaking my stride, I scoop up a rock and hurl it at the camera whose field of view is - was - in my path. Now it's broken, haha."

            "...That means the cops will know there was a break-in later. Shit. That's not great, but it's better than being spotted. Phew, all this excitement has gotten my Blood up!"

            $ story_mission1_ghost = False
            $ freeBloodSurges += 1
        elif grade == SUCCESS:
            play sound audio.heels_running

            "I keep perfect timing, sprinting and pivoting and sidling across the asphalt, under and around the cameras. Staying entirely out of their fields of view and making it to the spot with time to spare. That couldn't have gone better."
        else: # FAIL or BEASTFAIL
            play sound audio.heels_running
            # queue sound alarm (or someting) TODO

            "I go for it. I sprint, pivot, slide, and scuttle over the asphalt under and around the- No!"

            "Shit. The camera above the loose brick. I fucking forgot! It spotted me. I know it did."

            beast "Great job, genius. Brilliant plan. Just run past a half dozen security cameras and hope they don't spot you."

            "..."

            $ story_mission1_spotted = True
            $ story_m1fail_burglary = True
            jump missions.mission1_failstate

        jump missions.mission1_breakin_climb

    label .mission1_breakin_climb:
        $ triedDex = triedStr = False

        "Alright, next I scale the wall. I've got rope, hooks, a harness, and high-friction gloves and kneepads... but the wall is too uniform for handholds, and there's no place in or around the window fixture for a hook to hold."

        "So I'm going to need to aim higher. At a crenellation above and to the left of the window I want. That's going to take skill and precision. Alternatively..."

        "There's a light fixture further up and to the right of the window. It'll be a lot easier to aim the hook there, but it'll take strength to manage it. Plus I won't be able to reach the wall with my feet to assist in the ascent."

        if freeBloodSurges > 0:
            "My Blood is percolating in my limbs and core. I feel great. Like I could do better than usual at either option. Like I'm a stone, skipping along the surface of the lake of human limitations, just for a few moments."

            beast "You're welcome."
        else:
            call missions.mission1_bloodsurge_choice from _call_missions_mission1_bloodsurge_choice_3

        label .mission1_climb_menu:

        menu:
            beast "You don't have very long to decide..."

            "I take careful aim try to get the hook up into a crenellation just {i}so{/i}. Then I can rappel my way down pretty easily and focus on the window itself. ([_dex] + [_athl])" if not triedDex:
                $ triedDex = True
                $ result = pc.basictest(6, _dex, _athl, pc.maybeBloodSurge())
                $ print ("\n\nhook throw dex result", result)
                $ grade = evalt(result)

                "Around and around and around and..."

                if grade == SUCCESS:
                    "Yes! The hook sails over and up, and catches in the narrow stone slit. From there I easily rappel up the wall (or whatever the proper word is) and climb onto the ledge."
                    jump missions.mission1_breakin_window
                else:
                    "Sigh..."
                    jump missions.mission1_climb_menu

            "I toss the hook as high as I can, up and over the light fixture. I'll need to summon the strength to pull myself up unaided, and swing toward the window fixture. ([_str] + [_athl])" if not triedStr:
                $ triedStr = True
                $ result = pc.basictest(6, _str, _athl, pc.maybeBloodSurge())
                $ print ("\n\nhook throw str result", result)
                $ grade = evalt(result)

                "Okay, need to get as much altitude as I can. Around and around and around and..."

                if grade == SUCCESS:
                    "Nice. The hook flies into the air and catches on the light fixture high above the window and the cameras. I pull myself up the rope with nothing but pure upper body strength, and swing back and forth until I'm crouched on the ledge."
                    jump missions.mission1_breakin_window
                else:
                    "Sigh..."
                    jump missions.mission1_climb_menu

            "...What am I doing? There's no way I can pull this off.":
                $ story_m1fail_burglary = True
                jump missions.mission1_failstate

    label .mission1_breakin_window:
        "And now there's the window. Fortunately this is just some shitty old police precinct, not a bank vault. Security isn't exactly state-of-the-art. According to Kay's info there's just a basic glass break sensor."

        "It'll trigger if I smash the window willy-nilly, but I should be able to carefully break or cut the top-right pane without breaking the circuit, and squeeze through. That said, if I fuck up it'll definitely set off the alarm. There won't be a second try."

        call missions.mission1_bloodsurge_choice from _call_missions_mission1_bloodsurge_choice_4

        menu:
            beast "..."

            "I take my crowbar and carefully break the top-right pane without tripping the sensor. ([_str] + [_clan], or [_com] + [_comb])":
                $ result1 = pc.basictest(5, _str, _clan, pc.maybeBloodSurge())
                $ result2 = pc.basictest(5, _com, _comb, pc.maybeBloodSurge())
                $ print ("\n\nwindow smash result", result1)
                $ grade = evalt(max(result1, result2))

                "I heft the crowbar in my hand. I aim the sharper end, draw back, and..."

                if grade == SUCCESS:
                    "There's a loud crash, of course. I wait for a few seconds that would have my heart racing and my skin dripping sweat, if I weren't dead."

                    "...Nothing. Thank God. I gingerly punch away enough of the remaining glass to wiggle through."

                    "Well, it was a long, tedious, and painful process. But I've breached precinct security and broken in."

                    jump missions.mission1_search
                else:
                    "There's a loud crash, followed immediately by a loud mechanical wailing."

                    "No, no, no, NO! I came so fucking far!"
                    $ story_m1fail_burglary = True
                    jump missions.mission1_failstate

            "I brought a glass cutter. I don't have a whole lot of experience using one, but I should be able to manage if I'm careful. ([_dex] + [_clan])":
                $ result = pc.basictest(6, _dex, _clan, pc.maybeBloodSurge())
                $ print ("\n\nglass cutter result", result)
                $ grade = evalt(result)

                if grade == SUCCESS:
                    "It's a lot slower and more arduous than the movies make it seem. But eventually I have a huge circle of glass carved out of the top-right pane. Large enough for me to wiggle through, carefully setting the circle down before me."

                    "I did it. I'm in."

                    jump missions.mission1_search
                else:
                    "It's a lot slower and more arduous than the movies make it seem. It's taking forever, so I press a bit harder and-"

                    "...I fucking dropped it. I... You've got to be..."

                    beast "Fuck that, we've come to far to slink away because you dropped your fucking toy!"

                    play sound audio.beastgrowl1

                    "I let loose a frustrated scream and smash the glass with my fist!"

                    "Predictably, the alarm goes off."

                    beast "OH COME ON"

                    "..."

                    $ story_m1fail_burglary = True
                    jump missions.mission1_failstate


    # STAGE 1-B, IT GIRL BLUFF
    label .mission1_techbluff:
        play music audio.introMission fadeout 2.0 fadein 2.0 volume 0.7

        "This precinct doesn't have its own in-house IT staff, so they have to contract it out to off-site private firms. The company that handles their cloud storage isn't the one sending people over to make physical backups, though."

        "Not their ISP, either. Even though the whole issue is supposed to be their internet outage, courtesy of the local Nosferatu. Strange."

        "It's some other firm I've never heard of, and their people will be here in [daysLeft] days, give or take. I'm guessing the desk jockeys aren't very happy about that. So maybe that's my way in."

        "First problem is that this plan requires me to mend my face and show it. The compound's external security cameras seem to be on their own intranet, separate from the security system inside."

        "So while it's not mission-critical, it'll be better for me and my reputation with the Camarilla if there aren't any recordings of my face on the way in. It'll take some knowhow and ingenuity, but I have to try to knock out at least some of the external cameras."

        $ chosenAttr = max(pc.getAttr(_int), pc.getAttr(_wit))
        $ result = pc.basictest(7, chosenAttr, _tech, pc.maybeBloodSurge())
        $ grade = evalt(result)

        if result > -1:
            "I open up the laptop I put together for this op. I boot up a tool that crawls nearby networks, looking for for unsecured nodes and entry points. It also provides a readout of the specs of all the hardware it comes across."

            "Nothing shows up at first. No obviously unsecured nodes, no routers still on factory settings. Newer routers are configured to run through an app or some other authenticated service, anyway."

            "But wait, here's something. I'm looking through the hardware specs, and one of these nodes is running older software whose devs stopped getting supporting it back in 2010. In fact, the company went out of business in 2014."

            "Both of those years are well before the Heartbleed patch went out. And the software is proprietary, so it's unlikely anyone patched it independently. I check, and sure enough the Heartbleed exploit works, and I'm reading out the device's memory."

            "Soon I have a password, and I'm in the network and doing what I want with the external cameras. Nice, we're off to a great start."

            $ freeBloodSurges += 1
        elif result > -4:
            "I open up the laptop I put together for this op. I boot up a tool that crawls nearby networks, looking for for unsecured nodes and entry points. It also provides a readout of the specs of all the hardware it comes across."

            "Unfortunately, I can't seem to find anything. Nothing easy like a router still on its factory settings, no obviously unsecured nodes. Maybe someone who knows a bit more about netsec could see something that I'm not, but I'm stumped."

            beast "They say second place is just being first among losers. That almost succeeding is just a more ostentatious form of failure."

            "You definitely made that last one up. Anyway, shut up. I can still talk my way in."

            $ story_mission1_ghost = False
            $ story_mission1_spotted = True
        else:
            "This was a terrible idea. Not sure why I thought I could do this. Hack security cameras? I don't even know where to start."

            beast "Doing great so far, keep at it."

            "Fuck off."

            $ pc.damage(KEY_WP, KEY_SPFD, 1)
            $ story_mission1_ghost = False
            $ story_mission1_spotted = True
            "...Okay. I think I can still manage to talk my way in, but my face is going to be on record. On to the next step, I guess."

        jump missions.mission1_techbluff_frontdesk

    label .mission1_techbluff_frontdesk:

        play sound audio.heels_on_pavement

        "I walk in, nonchalant but all business, and head for the front desk. The receptionist is a pretty older Black woman with mulberry lipstick and her hair done up in a gorgeous afro. She smiles when I approach, and I grin like a dope."

        beast "Focus."

        receptionist "May I help you?"

        me "Uh, yeah. Hi. I'm with Transurban Infosystems. I'm here to look into your connectivity issues, see what what the prognosis is and how soon we'll likely have it back up and running. I was also told to see about backing up your data in the meantime?"

        if daysLeft > 1:
            "She frowns. Uh oh."

            receptionist "You're from Transurban? But you weren't scheduled for another [daysLeft] days."
        elif daysLeft == 1:
            "She frowns. Uh oh."

            receptionist "You're from Transurban? But you weren't scheduled until tomorrow."
        else:
            "She nods, smiles again, and hands me a lanyard."

            $ pc.addToInventory("precinct_lanyard")

            receptionist "You're an hour early, but that's probably for the best. There are a lot of unprocessed reports and claims piling up. People are getting stressed out, and I'm hearing weird- Never mind. Sorry, it's just been a long week."

            me "Tell me about it. I'll see what I can do."

            receptionist "Thanks so much."

            jump missions.mission1_techbluff_authorized

        beast "Better make it good... Or use our Blood."

        call missions.mission1_bloodsurge_choice from _call_missions_mission1_bloodsurge_choice_5

        menu:
            "I..."

            "I feign ignorance and convince her there was some mistake. ([_man] + [_acad] or [_intr])":
                $ chosenSkill = max(pc.getSkill(_acad), pc.getSkill(_intr))
                $ result = pc.test(7, _man, chosenSkill, pc.maybeBloodSurge())
                $ grade = evalt(result)
                jump missions.mission1_snafu

            "I feign ignorance and convince her there was some mistake. I don't want to extend my aura so far I draw the cops' attention, but I should be able to easily entrance one mortal woman, no matter how beautiful. ([_man] + [_acad] or [_intr] + [_pres])" if pc.getHunger() < HUNGER_MAX and pc.hasDisciplinePower(_presence, PRES_CHARM):
                $ chosenSkill = max(pc.getSkill(_acad), pc.getSkill(_intr))
                $ result = pc.test(7, _man, chosenSkill, _presence, pc.maybeBloodSurge())
                $ grade = evalt(result)
                $ addHungerDebt(4)
                jump missions.mission1_snafu

            "I come up with some bullshit technical explanation for why I'm here early. ([_man] or [_int] + [_tech])":
                $ chosenAttr = max(pc.getAttr(_int), pc.getAttr(_man))
                $ result = pc.test(7, chosenAttr, _tech, pc.maybeBloodSurge())
                $ grade = evalt(result)
                # jump missions.mission1_technobabble
                jump missions.mission1_snafu

            "I come up with some bullshit technical explanation for why I'm here early. I don't want to extend my aura so far I draw the cops' attention, but I should be able to entrance one beautiful woman without a problem. ([_man] or [_int] + [_tech] + [_presence])" if pc.getHunger() < HUNGER_MAX and pc.hasDisciplinePower(_presence, PRES_CHARM):
                $ chosenAttr = max(pc.getAttr(_int), pc.getAttr(_man))
                $ result = pc.test(7, chosenAttr, _tech, _presence, pc.maybeBloodSurge())
                $ grade = evalt(result)
                $ addHungerDebt(4)
                # jump missions.mission1_technobabble
                jump missions.mission1_snafu

            "I'm not going to argue with the receptionist. I simply command her to give me the lanyard." if pc.getHunger() < HUNGER_MAX and pc.hasDisciplinePower(_dominate, DOM_COMPEL) and pc.getAttr(_int) < 3:
                beast "My thoughts exactly. Far too often you stoop to arguing and pleading and persuading with mortals. We're Ventrue. We tell {i}them{/i} what to do."

                me "Give me a lanyard."

                $ pc.addHungerDebt(1)

                "I catch her gaze. She fights for a second, not understanding what's happening to her. But she hands it over. I smile at her horrified face and start to walk further inward. I get about ten meters in before I hear her shouting."

                receptionist "Someone stop her! She's stolen a lanyard! She's not from Transurban."

                beast "Why didn't you wipe her mind, moron?!"

                "Shit. The command wore off too quickly, and I let her remember what happened. Fucking amateur mistake. Mortals may not understand what's happening to them when we mentally dominate them, but they usually understand that something's very wrong."

                "I turn and make a break for the exit. I can't believe I was so fucking careless."

                $ story_mission1_ghost = False
                $ story_mission1_spotted = True
                $ story_m1fail_tech = True

                jump missions.mission1_failstate

            "I'm not going to argue with the receptionist. I simply command her to give me the lanyard." if pc.getHunger() < HUNGER_MAX and (pc.hasDisciplinePower(_dominate, DOM_COMPEL) or pc.hasDisciplinePower(_dominate, DOM_MESMERIZE)) and pc.getAttr(_int) >= 3:
                beast "My thoughts exactly. Far too often you stoop to arguing and pleading and persuading with mortals. We're Ventrue. We tell {i}them{/i} what to do."

                me "Give me a lanyard."

                if pc.hasDisciplinePower(_dominate, DOM_COMPEL):
                    $ pc.addHungerDebt(1)
                else:
                    $ pc.addHungerDebt(4)

                "I catch her gaze. She fights for a second, not understanding what's happening to her. But she hands it over. The look on her face is a mix of indignation and horror and shame. Suddenly I feel guilty."

                me "I'm sorry. Just forget about this, okay?"

                $ pc.addHungerDebt(1)

                "Her eyes glaze over, and I briskly walk away before she comes to her senses."

                jump missions.mission1_techbluff_authorized

        # label .mission1_technobabble:
        #
        # if grade == MESSYCRIT:
        #     ""
        # elif grade == SUCCESS:
        #     ""
        # elif grade == FAIL:
        #     ""
        # else:
        #     ""

        label .mission1_snafu:

        if grade == MESSYCRIT:
            "Hmm... If I remember what I read from Kay's info correctly, Transurban Infosystems uses one of those project management software suites. They're supposed to automate management. I think that means the real TUIS employee was probably scheduled by an algorithm."

            me "Yeah... you didn't hear this from me, but the scheduling algorithm we use screws up all the time, especially when it has to communicate and coordinate with other instances of itself."

            receptionist "No kidding? They always seem to iron out the bugs eventually, though. It's crazy what AI can replace. I suppose {i}I'm{/i} lucky to have a job."

            me "As if some algorithm could ever replace someone like you. Doesn't seem likely."

            "She raises an eyebrow at that, then she chuckles."

            me "But if you ask me, the problem isn't what jobs AI can or can't replace, or whether or not jobs lost are offset by new jobs created. That's just a symptom."

            receptionist "Oh yeah? What's the real disease, then?"

            me "That we view this technology almost exclusively in terms of economic efficiency. How it can augment our productivity, or whether our productivity will be surpassed. As if the point of developing new technology is to more efficiently enrich its owners."

            receptionist "As opposed to what it can do to improve people's lives?"

            me "Exactly! I mean, I'm personally skeptical about a lot of the predictions that have been made about AI taking over the economy, but that's beside the point. If AI can do everyone's job, the question shouldn't be how people will work."

            beast "..."

            receptionist "But why they should need to? I've heard this reasoning before, and I don't necessarily disagree. I'd love for Star Trek to be our future, but what I find myself skeptical about is how that all shakes out in practice."

            receptionist "People tie their identities to what they do. Seems to be pretty universal across cultures. It's where they get their self-worth. Take it away from them and they get angry. Sometimes that means violence."

            receptionist "Sometimes it means electing demogogues who offer up scapegoats and promise simple solutions to complex problems. Either way, people tend to want their old ways back whether or not it's materially good for them, or even possible."

            me "You don't think people want their needs taken care of? You don't think that could ease conflict?"

            "My Blood is rushing around, percolating as it flows to and from my limbs."

            receptionist "I think it creates new conflict. I think a lot of people value psychological satisfaction and social status over practical, material interest. Better to reign in hell than serve in heaven and all that."

            "I could listen to her all night, but then I catch a glimpse of the clock behind her. Whoops."

            $ story_mission1_ghost = False

            me "Oh man, look at the time. I guess I got a bit sidetracked."

            receptionist "Just a bit. Don't let me hold you."

            me "Why wouldn't I let you do that?"

            receptionist "What?"

            me "Uh, what I'm trying to say is, I'd love to talk more. With you. Say, over coffee?"

            "She laughs, and it's like music. Her eyes shine as she looks at me with a thoughtful expression."

            receptionist "How about this? Here's my number. You can text me one of these nights, and we maybe we'll get to know each other better."

            me "I'd like that."

            receptionist "Now I think we both have work we need to get back to."

            "I catch myself grinning again. I'm probably a lot more pleased with myself than I should be, given how much time has passed. Not sure what I'm going to do when she finds out I'm not who I said I was."

            "Leaving people who are thinking about me is kinda the opposite of what we wanted. Oh well. I'll worry about it later. And I certainly got my in. Anyone close enough to have heard us is either snickering or giving me a knowing smile."

            jump missions.mission1_techbluff_authorized

        elif grade == SUCCESS:
            "Hmm... If I remember what I read from Kay's info correctly, Transurban Infosystems uses one of those project management software suites. They're supposed to automate management. I think that means the real TUIS employee was probably scheduled by an algorithm."

            me "Yeah... you didn't hear this from me, but the scheduling algorithm we use screws up all the time, especially when it has to communicate and coordinate with other instances of itself."

            receptionist "No kidding? They always seem to iron out the bugs eventually, though. It's crazy what AI can replace. I suppose {i}I'm{/i} lucky to have a job."

            me "No algorithm could ever replace someone like you."

            "She raises an eyebrow at that, then she chuckles."

            receptionist "Here's your lanyard. This should get you access to everywhere you need to go. Good luck out there."

            "She winks, and I'm grinning that dopey grin again before I can turn and walk further into the precinct."

            jump missions.mission1_techbluff_authorized

        elif grade == FAIL:
            me "Well, there has to have been some mistake."

            receptionist "I don't see why there would be."

            me "You know how these project managers can be. They're always trying to manage expectations. You know, \"underpromise and overdeliver\" and all that. They probably thought it'd make a good impression if I showed up early."

            receptionist "...Transurban uses project management software for all its scheduling. So does every precinct this side of 14th. The whole thing is organized by algorithm. A Transurban employee would know that."

            "Fuck. She caught me in a lie. Goddamnit."

            beast "Why are we wasting time arguing with this peon? Just make her sign us in!"

            me "L-Look, I'm just here to do a job. I don't pay attention to how the managers do things, okay? How about you just hand me that lanyard and we can both get on with our-"

            "I tried to catch her gaze as I said it, but she avoids my eyes. I can see her reach for something under her desk, probably one of those silent alarm buttons."

            receptionist "Ma'am, could you wait right there for a moment? Someone will be here to verify your identity shortly."

            "I'm not waiting for that. She won't look directly at me, as if she somehow instinctively knows I'm the kind of monster that you shouldn't look in the eye. I can't mindwipe her without eye contact. Shit. I can only turn and run."

            scene black with fade

            $ story_mission1_ghost = False
            $ story_mission1_spotted = True
            $ story_m1fail_tech = True

            if story_m1fail_burglary:
                "There's no way I'm getting back in there. Fuck!"
            else:
                "There's no way I'm getting back in there, unless I can break in with a disguise."

            jump missions.mission1_failstate
        else:
            me "Well, there has to have been some mistake."

            receptionist "I don't see why there would be."

            me "You know how these project managers can be. They're always trying to manage expectations. You know, \"underpromise and overdeliver\" and all that. They probably thought it'd make a good impression if I showed up early."

            receptionist "...Transurban uses project management software for all its scheduling. So does every precinct this side of 14th. The whole thing is organized by algorithm. A Transurban employee would know that."

            "Fuck. She caught me in a lie. Goddamnit."

            beast "Why are we wasting time arguing with this peon? Just make her sign us in!"

            me "L-Look, I'm just here to do a job. I don't pay attention to how the managers do things, okay? How about you just hand me that lanyard and we can both get on with our-"

            "I tried to catch her gaze as I said it, but she avoids my eyes. I can see her reach for something under her desk, probably one of those silent alarm buttons."

            receptionist "Ma'am, could you wait right there for a moment? Someone will be here to verify your identity shortly."

            beast "Fuck this."

            "I lunge for her, suddenly furious. She screams. A couple police officers are running toward me and drawing their guns. They shout for me to freeze. I roar in frustation and turn to run."

            play sound audio.gunshot1

            $ pc.damage(KEY_HP, KEY_SPFD, 6)

            "They get me right in the back. I cry out, stumble, and keep running out the door."

            scene black with fade

            beast "Fuck! That nosey bitch ruined everything. Why do these fucking peons even care? Like she's gonna get paid more for ratting us out or something."

            if story_mission1_spotted:
                "This is your fault! You made me fly off the handle again, and now the police have seen my face and they're looking for me. They have me on camera!"
            else:
                "This is your fault! You made me fly off the handle again, and now the police have seen my face and they're looking for me. At least I took the security cams offline, but they've seen my fucking face!"

            beast "Oh fuck off, dipshit. You're the one who got caught."

            $ story_mission1_ghost = False
            $ story_mission1_spotted = True
            $ story_m1fail_tech = True

            if story_m1fail_burglary:
                "There's no way I'm getting back in there. Fuck!"
            else:
                "There's no way I'm getting back in there, unless I can break in with a disguise."

            jump missions.mission1_failstate


    label .mission1_techbluff_authorized:

        "That wasn't too hard. With the lanyard I'm able to head upstairs without interference. Two floors up, to be precise. I don't have any valid cause to be in the security room, but there's only one bored-looking guy manning it."

        "I wait for a few minutes, and he gets up to go to the bathroom. I slip in."

        jump missions.mission1_security_room



    # ~~~~~~~~~~~~~~~~~~~~~~~
    # label .mission1_blunted_tour:
    #     play music audio.introMission fadeout 2.0 fadein 2.0 volume 0.7
    #
    #     ""


    # STAGE 2
    label .mission1_search:
        scene bg precinct interior1 with fade
        # play different music?

        play sound audio.heels_on_pavement # TODO: better sound

        "I tiptoe my way down the corridor until I reach an unlocked, empty office where I can get my bearings. The I mentally review my objectives. Now that I'm inside, there's not much time or space to pore over Kay's data."

        "There's supposed to be a police report that I need to steal. As in, a set of papers, probably in some manila folder in a filing cabinet somewhere. There's also physical evidence taken from {i}Bandita{/i}, which I also need to steal."

        "Then I need to find the security camera footage taken from the club and delete it. The Nosferatu - well, most likely just {i}a{/i} Nosferatu, who's probably just some neonate pawn like me - has made sure that no off-site cloud backups can be made."

        "By cutting off their internet access and making it look like a normal service outage. Something to be annoyed about rather than suspicious."

        "And I need to get in and out without being recorded and without my face being seen. That's not mission-critical, but if there's evidence of what I do here it makes headaches for the bosses and I end up looking incompetent."

        beast "..."

        if story_mission1_ghost:
            "So far I haven't left any evidence of my entry except for the window. That won't be found for a while, and I can make that look like vandalism pretty easily. So if I can avoid leaving any traces of what I'm actually doing here, so much the better."
        else:
            "Unfortunately I've already destroyed one of the exterior cameras in a way that can't be made to look like an accident or vandalism, so the cops are going to know that something went down. But it's not a huge deal so long as I'm not seen myself."

        "So the first thing I need to do is shut down internal security, or I won't get very far. And I know where the control room is, two floors up. I basically have two choices."

        "The first is to act like I belong here and casually make my way up, avoiding cameras where I can and casually walking past them where I can't. This will probably draw {i}some{/i} attention, but hopefully not too much."

        if pc.getDisciplineLevel(_dominate) > 1 or pc.getDisciplineLevel(_presence) > 1:
            "And if it does, I can use my mental arts to make sure any conversations go smoothly. Or at least favorably."

        "The second option is to try to combine speed and stealth and make my way up to security before I'm noticed by whoever's monitoring the camera feeds, or {i}very{/i} shortly after."

        "This is the riskier option; if any kind of alarm or commotion is raised, I'm fucked. But it's also a lot faster and more straightforward, with no chance of getting bogged down talking to curious or suspicious bystanders. And the less time I spend here, the better."

        if pc.getSkill(_tech) > 2:
            "Either way, I'm going to have to deal with whoever's in security quickly and quietly, and then I can put the cameras on a loop or introduce various failures or glitches as needed."
        else:
            "Either way, I'm going to have to deal with whoever's in security quickly and quietly, then shut off the cameras."

        "The only available paths will take me past offices that are still being used. It's late, but as expected there are still several cops and night staff on duty."

        call missions.mission1_bloodsurge_choice from _call_missions_mission1_bloodsurge_choice_6

        "Okay. Can't stay in this room much longer. Time to decide."

        menu:
            "I..."

            "I take the slow, safe route and casually make my way up to security. It'll be difficult to do so without drawing any attention, but if it goes sideways I'll still have options. ([_com] + [_clan] or [_perf])":
                $ chosenSkillScore = max(pc.getSkill(_clan), pc.getSkill(_perf))
                $ result = pc.test(7, _com, chosenSkillScore, pc.maybeBloodSurge(), bestialFailsOn = False)
                $ print ("\n\nact natural result", result)
                $ grade = evalt(result)

                if grade == MESSYCRIT:
                    "Just gotta stay cool. Walk casually. Try not to let anyone glimpse my face, but don't look like I'm trying to hide anything."

                    "I make sure to adopt an exasperated, longsuffering demeanor. Like being here is an imposition on me. But it's not working. I'm starting to get looks walking by..."

                    beast "If no one's supposed to notice us, then no one is going to fucking notice us."

                    play sound audio.beastgrowl1

                    "This is so frustrating. Why the fuck are all these people looking at me? I give one ogler a nasty look."

                    me "Forget, asshole."

                    $ pc.addHungerDebt(4)

                    "This just gets me more looks from others, so I have to tell each of them off, too."

                    $ pc.addHungerDebt(4)

                    play sound audio.dominate1

                    "...Hm. I may have gone a bit overboard."

                    "I'm surrounded by unconscious, catatonic, or otherwise unresponsive police officers and office workers. I head further up, walking briskly. I'm pretty sure they won't remember me."

                    "Security is open, and no one's inside. I turn toward the console."
                elif grade == SUCCESS:
                    "Just gotta stay cool. Walk casually. Try not to let anyone glimpse my face, but don't look like I'm trying to hide anything."

                    "I make sure to adopt an exasperated, longsuffering demeanor. Like being here is an imposition on me."

                    "...Well, I suppose it is. Just for very different reasons than the ones I'm trying to imply."

                    "It's working pretty well. Everyone seems engrossed in their work or otherwise occupied. I keep shuffling along, looking as if I know where I'm going because I've been there a dozen times, not because I skimmed over some building plans."

                    "It takes a while, but I get there. When I turn onto the corridor leading to security, I spot a portly, balding man in an officer's uniform. He's walking out of the room and heading toward where I'm pretty sure the restrooms are. He might be back before I'm done in there, but it definitely makes things either."

                    "I casually walk in and turn to the console."
                else:
                    $ story_mission1_ghost = False

                    "Just gotta stay cool. Walk casually. Try not to let anyone glimpse my face, but don't look like I'm trying to hide anything."

                    "I try to adopt an exasperated, longsuffering demeanor. Like being here is an imposition on me. Maybe I'm trying a bit too hard, because a few people are giving me weird looks. No one's challenged me yet, though."

                    "Then I get up the stairs, and there he is. Standing just outside security. Looking right at me with a frown on his face. Oh great."

                    if story_m1_cutface:
                        securitycop "Excuse me, ma'am. No one's supposed to- uh... No one's-"

                        me "No, go ahead. Please, stare as much as you like. I guess I should be used to it by now."

                        securitycop "Didn't mean to be rude, ma'am. But as I was saying, members of the public aren't allowed up here. I'm not sure how you got past security downstairs, but I'll be happy to escort you back down."
                    else:
                        securitycop "Excuse me, ma'am. No one's supposed to be up here without authorization. I'd be happy to escort you back downstairs."

                    me "Sigh... I knew it'd be like this. Look, sir, I was explicitly told by the front desk that I needed to come up here to give my statement."

                    securitycop "...Statement? Ma'am, th-"

                    me "Call me Audrey."

                    securitycop "Ms. Audrey, whatever mix-up there's been I'm absolutely sure that we can-"

                    "He's more annoyed than suspicious, which of course is what I was going for. Actually, he seems distracted. But by what? He doesn't have his comm on him; that's good. Must have left it by his desk."

                    "Then I look at his stance, and almost laugh out loud. Maybe if I can keep this guy talking long enough he'll give up and head off to relieve himself. So I start nitpicking over details, asking him to repeat or confirm things he's already said..."

                    "Just loop over the conversation over and over with different phrasing, generally pestering the guy while acting like I'm the one just trying to take care of business properly and {i}he's{/i} being unreasonable."

                    $ pc.damage(KEY_WP, KEY_SPFD, 2)

                    "It tries my patience as much as his, but I force myself to remain aloof and exasperated while we quibble back and forth. It only takes about five minutes for him to break."

                    securitycop "Look- I have some business to attend to. {i}Please{/i} return to the proper waiting area or I'll have to call in backup."

                    me "Crimony, this always happens with these insufferable bureaucracies. They're just going to send me right back up!"

                    securitycop "Look, ma'am, just... just wait here, alright?"

                    me "Sure, why not?"

                    "And he takes the opportunity to scamper off to the bathroom. I walk into security. It took a lot longer than it should have, but I'm here. I'll need to work quickly."

                jump missions.mission1_security_room

            "I just head there as quickly and stealthily as possible. Much simpler. But if I'm spotted, it's game over. It's a very \"all-or-nothing\" approach. ([_dex] + [_athl] + [_clan])":
                $ result = pc.test(7, _dex, _athl, _clan, pc.maybeBloodSurge())
                $ print ("\n\nsprint result", result)
                $ grade = evalt(result)

                "Alright, I'm making a (careful) break for it."

                if grade == MESSYCRIT:
                    "...Did I say \"careful\"? I did, right?"

                    play sound audio.beastgrowl1
                    beast "That's not what I remember."

                    "I'm bounding, sprinting, and leaping up the stairs. Fast. Probably faster than a normal human has ever moved. A few people notice as I pass them, but by the time they turn to look I'm gone - around a corner or into shadow."

                    "The cameras have definitely seen me, though. That's game over for me, unless..."

                    $ story_mission1_ghost = False

                    # sound here TODO

                    "I kick the door to security open. There's only one guy monitoring the screens, and he's reaching for the intercom as I burst in. He yelps in surprise and spins around in his chair to gape at me, shocked. Big mistake."

                    "What he {i}should{/i} have done is immediately punch the alarm. But he didn't, and as he turns toward it I'm already on him, biting down on the back of his neck. I pull him backwards, out of his chair and on top of me. I get one leg around his, and cover his mouth."

                    $ pc.soundFeed("I drink in his fear. It's so fucking good...")
                    $ pc.slakeHunger(3)

                    "Shit. I may have taken too much. Thank God he's still breathing. And he's out like a light. I lick his wound closed and heft him back into his chair. Hopefully he won't remember anything, since I can't flash him now."

                    "Hopefully anyone else will think he fell asleep."

                    jump missions.mission1_security_room

                elif grade == SUCCESS:
                    "I fly past the occupied offices quickly and quietly. I duck under most of the cameras and stop on a dime to walk casually past the ones I can't."

                    "When I have to, I duck behind walls or into offices, but I make keeping the pace up my top priority. And I do - I make excellent time, in fact."

                    "When I turn onto the corridor leading to security, I spot a balding desk jockey walking out of the room and heading toward where I'm pretty sure the restrooms are. He might be back before I'm done in there, but it definitely makes things either."

                    "I waltz on in, and turn to the console."

                    jump missions.mission1_security_room

                elif grade == FAIL:
                    "I fly past the occupied offices quickly and quietly. I duck under most of the cameras and stop on a dime to walk casually past the ones I can't."

                    "And right as I'm turning the corner I run smack into a fucking cop, armed and in uniform. He curses and shouts before I can stop him or flash his memory. He's reaching for his gun, but the real problem is that everyone on the whole floor definitely heard that."

                    me "FUCK!"

                    "And there goes all that time and effort. All for nothing. I sprint the other way, heading back down the stairs. There's no gunfire; this guy's not stupid enough to fire his gun inside his own precinct without a clear shot. Not that it matters."

                    if story_m1_cutface and daysLeft > 1:
                        "The only silver lining is that my face is still cut up, so I can't be identified. I'll need to hang back for a bit, but I can come back with my real face and try another way in. It'll probably be harder, though."

                        $ story_m1fail_burglary = True
                    else:
                        "They've seen my face. They'll reinforce security. There's no way I'm ever getting back in this place. Not anywhere close to the deadline."

                        "...That's it, then. I'm fucked."

                        $ story_m1fail_tech = True
                        $ story_m1fail_social = True

                    "I'm so furious and frustrated that I have to fight back bloody tears as I flee the way I came. But I do manage to get out and into the night, but I barely even care."

                    jump missions.mission1_failstate
                else:
                    "I fly past the occupied offices quickly and quietly. I duck under most of the cameras and stop on a dime to walk casually past the ones I can't."

                    "And right as I'm turning the corner I run smack into a fucking cop, armed and in uniform. He curses and shouts before I can stop him or flash his memory. He's reaching for his gun, but-"

                    play sound audio.beastgrowl1
                    queue sound audio.bite1

                    beast "..."

                    $ pc.slakeHunger(5, killed = True)
                    $ pc.setHumanity("-=1")

                    "..."

                    "...Oh. Oh, God. No..."

                    "No, no, no, no, nononononononononono..."

                    "He's dead. Skin white and shriveled. And I'm covered in his blood. His gun's in my hand. I feel so full, but someone's screaming."
                    $ pc.addToInventory("police_colt")

                    scene black with fade

                    "By the time I come to, I have no idea where I am. Not that it matters..."

                    beast "..."

                    $ story_mission1_ghost = False
                    $ story_mission1_spotted = True
                    $ story_mission1_failed = True

                    jump missions.mission1_failstate

    label .mission1_security_room:
        if pc.getSkill(_tech) > 2:
            "I don't waste any time. I have a whole baggie of USBs stuffed with malware, and I stick one in to the terminal. The dozens of screens go dark for a second. A few shell commands later, and the cameras are looping and flushing their cache every minute or so."

            "I have to use another hacking tool to get a few other cameras out of working order, but this lets me explore the evidence room more freely."

            $ story_m1_allcameras = True
        else:
            "I don't waste any time. I have a whole baggie of USBs stuffed with malware, and I stick one in to the terminal. The dozens of screens go dark for a second. Seems to have worked, but one of the cameras in the evidence room is still on."

        "I quickly slip out. Now I don't need to worry about cameras, just people. I make my way one floor down, into the room that Kay's info says will be full of file cabinets."

        play sound audio.heels_on_pavement

        "Fortunately, it is. It takes me a while to find the actual report, but this should be the only physical copy. After all, why would they need more than one? There are supposed to be secure, encrypted backups on the cloud."

        $ pc.addToInventory("police_report")

        jump missions.mission1_evidence_locker

    label .mission1_evidence_locker:

        play sound audio.heels_on_pavement

        "The evidence locker is down four floors, well underground. I have to take the elevator, which requires a passcode. Fortunately, I have it in my dossier."

        # sound here?

        "Great. There's someone down here. Looks like another desk jockey in uniform. He's looking for something in the lockers. He pulls out a shoebox, sifts through it, and takes a small baggie of what I'm assuming is cocaine, but who knows these days?"

        if story_m1_allcameras:
            "He pockets the baggie, and continues checking boxes. He's staying out of the range of that one camera that took extra work to disable. He of course doesn't know that it's looping."

            "No reason to hold back. We're alone down here."
        else:
            "He pockets the baggie, and continues checking boxes. He's staying out of the range of the camera I couldn't disable."

        "He turns with a start and looks at me. Shock turns to anger. He's got his service weapon holstered on his hip, and a vest over his shirt. His arms are thick, hairy, and corded."

        _dirtycop "Who the fuck are you? How the hell did you get down here? You better start talkin', real quick."

        "He's reaching for his gun."

        menu:
            beast "So how are we dealing with this dirty little piggy?"

            "Well I'm certainly not going to kill a cop, but there's no reason I can't knock his ass out. Cameras aren't an issue anymore." if story_m1_allcameras:
                beast "Oh? Well by all means."

                "I rush him, suddenly sprinting. He wasn't expecting that."

                $ arena.setStage(battleBG = "bg precinct interior")
                $ arena.startBattle(dirtycop)

                "Well, he's out cold. He's not gonna remember who hit "

            "I flash his memory, then order him away. Far away."  if pc.getHunger() < HUNGER_MAX and pc.hasDisciplinePower(_dominate, DOM_MESMERIZE):
                beast "Hah! I'm beginning to appreciate your style, [pcname]."

                me "Forget!"

                "He blinks, suddenly confused. I cover my face with one hand, leaving my eyes to bore into his."

                _dirtycop "...Wha? Where-"

                me "Shut up, leave the building, and walk out of the city without another word."

                $ pc.addHungerDebt(4)

                "For a moment he resists, his left eye twitching and his face twisting into a mask of fear and rage. But then the moment passes and he silently walks past me and into the elevator."

                "The command will wear off long before he can walk all the way out of the city, of course. But I'll be long gone by then."

            "No reason he can't be persuaded to see things my way. I have enough mastery of the subtler mental arts to sway an angry, crooked cop." if pc.getHunger() < HUNGER_MAX and pc.hasDisciplinePower(_presence, PRES_CHARM):
                "I shift my posture and make my voice low and husky as I walk nonchalantly toward him. I'm careful to keep my hands visible and open."

                me "I'm sorry, officer. I didn't get your name."

                if pc.hasPerk(M_LOOKS[KEY_NAME]):
                    _dirtycop "Yeah, that's a shame, ain't it? Maybe we can get to know each other a little better another time."

                    me "My thoughts exactly."
                else:
                    _dirtycop "I didn't give it. You must be real desperate or a special kind of stupid, breaking into a police station."

                    me "I just want to talk."

                "And that's all I need; I'm close enough. I stare into his eyes and weave my aura in and around him. The casual disdain on his face melts away, replaced with an almost bashful smile."

                $ pc.addHungerDebt(4)

                me "Let's be friends. Would you like that?"

                _dirtycop "Yeah, I think I would."

                me "I don't care what you were taking. That's your business, friend."

                _dirtycop "I appreciate that. Really, I do."

                me "I just need a few things. I won't be long. And hey - give me your phone number. Tomorrow night I'll give you a call and we can... get to know each other better."

                _dirtycop "That sounds wonderful. Here. I'll see you then."

                me "Looking forward to it. But don't mention this to your brothers-in-arms, okay?"

                _dirtycop "Of course not."

                "And he walks into the elevator. Without another word, but with several glances my way. If the Cam and the Anarchs get to have pet cops, why can't I? With all the chaos, I bet no one even notices."

                beast "I'm beginning to appreciate your style, [pcname]."

                "I'll need to track him down once the charm effect wears off in an hour or so, but he should be in my pocket by the end of tomorrow night."

            "Nothing to do but improvise. I mindwipe him, then fall back and lure him toward me.":
                me "Forget!"

                "While he's busy wondering what just happened and where he is, I move behind a row of lockers, then rap my knuckles on the metal."

                _dirtycop "Who's there?"

                "I can hear him draw his weapon and stalk toward my position. It's dark down here, probably because he prefers it that way while he's helping himself to some loot."

                if pc.getAttr(_dex) + pc.getSkill(_comb) > 4:
                    "When he turns the corner and points his gun, it's in the wrong direction. I pounce and bite into his neck from behind, grabbing the slide of his pistol as I do."
                else:
                    "When he turns the corner and points his gun, it's in the wrong direction. I pounce and bite. He yelps and his trigger finger twitches, but the trigger pull on those things is high enough that the gun doesn't go off."

                $ pc.soundFeed("This was a risk - but not much of one. He's a crooked cop; chances are pretty good that he's got something he's running from.")

                if pc.getHunger() > 3:
                    "Whoops. When I let him go, I realize I've taken a bit too much. He's out, and he won't be up for a while. So other cops are going to find him, and they'll have their suspicions I'm sure. And I don't have time to move this guy anywhere."

                    "But I haven't been spotted myself, so we're still on track for like a B+ here. I lick his bite marks away and set him down."

                    $ pc.slakeHunger(3)
                    $ story_mission1_ghost = False
                else:
                    "I drink until the pleasure and blood loss make him drowsy, and take my fangs out when he nods off. If anyone finds him he'll look like he fell asleep."

                    $ pc.slakeHunger(2)

            "I've always wanted a pet cop. And he's dirty, so I won't feel too bad messing with his head in a big way."  if pc.getHunger() < HUNGER_MAX and pc.hasDisciplinePower(_dominate, DOM_GASLIGHT):
                me "Forget about it, man."

                _dirtycop "...Wha-"

                "I walk up to him, and catch his gaze with mine. Something fairly simple to start with, and I can repeat the process later as needed."

                me "You work for me, remember? You've worked for me for a month now. It's been very profitable for you so far. You probably wouldn't want to upset me and jeopardize our relationship."

                beast "I like where this is going."

                me "You were to come to see me, tomorrow night, so that we can formalize our pact through a sacred ritual. You've seen it before, and you know that it has a great deal to offer a man such as yourself."

                me "You were also going to text me your number, so I can provide you with instructions to find the meeting place."

                _dirtycop "...Right. Right, of course boss. See you tomorrow night."

                "And he walks into the elevator, rubbing his temples with a perplexed look on his face. It doesn't matter how well the memories stuck. I can repaint that canvas as many times as needed. I just need him to show up so I can start the bonding process."

        beast "So here we are. The evidence locker."

        "I have the police report, and I can see the locker marked with the right date and address. It's not hard to finagle open. I pull out two sealed plastic bins and open them up."

        # sound here? TODO

        "There's some bloodstained clothing. There's an expensive-looking watch, also covered in blood. In the other bin there are sealed plastic bags containing several hard disk drives and some old Betamax tapes."

        if pc.getSkill(_tech) > 2:
            "This is a treasure trove of information for anyone interested in the holdings of Keerat Sanghera. Childe of the Ventrue Primogen, Philomena Al-Rashid. The hard drives are certainly encryped."

            "And I'm guessing the Betamax tapes are meant as analog backups that can't easily be read. Hard to find a Betamax player these days. But not impossible, and that's why I was told to get this out before the offsite IT guys show up."

        "This is it. This is what I came for. I'll confirm that Kay wants this stuff destroyed, and if so I'll find a burning barrel to toss it in."

        beast "Or we could say we destroyed it and keep it for ourselves. Who knows what the right Kindred would pay for it?"

        if pc.getAttr(_int) > 2:
            "Yeah, no. If she wants this stuff destroyed I'm sure she'll demand proof that it was done. And if she wants it back, I don't have any way of making copies of the drives or the tapes."
        else:
            "That seems like a bad idea."

        "I've gotten up to a lot of stuff that's frowned upon in the Tower, but what you're suggesting rises to the level outright betrayal. That kinda shit would get me staked on a roof. I thought you wanted to live a long time?"

        beast "Eh, just brainstorming. Nothing ventured, nothing gained."

        "Right. Now I just need to get this stuff out without being seen. Which shouldn't be too hard with the cameras down. I'll just mindwipe anyone I see."

        if story_m1_allcameras:
            "Oh, but what do we have here? In the corner of the room that was covered by that one pesky camera, a certain locker catches my eye."

            "I get it open, and ooh-"

            beast "Lucky us."

            "You're not kidding. A Smith & Wesson Model 500. Looks brand new, except for the serial number filed off. They're supposed to pack a real punch. Maybe even enough to make it useful against another vampire. There's some cash too."

            $ pc.addToInventory("swm500")
            $ pc.gainCash(1000)

            "I stash the gun, ammunition, and scratch, and make my way out."
        elif not story_mission1_spotted:
            "Something catches my eye on the way out. A locker underneath the purview of the camera I couldn't disable."

            "I can see well enough to tell that there's something valuable inside. Looks like some cash and what might be a gun. But if I go in to get it, I'll be spotted. No way around that."

            "I can hide my face, of course. But it'll be obvious what I was doing down here. The Cam won't like that, but I'll still have fulfilled the primary objective."

            menu:
                beast "Decisions, decisions..."

                "Fuck it. I need a piece anyway, and cash never hurts.":
                    "I keep my head down as I break into the locker. Hm, giving in to my impulses might just have been worth it this time. I hold what looks like a brand new Smith & Wesson Model 500."

                    "There's some cash too, but this gun packs enough of a punch to be useful against other vampires. I stash the heater, ammo and cash."

                "The favor of the Tower is worth more than money and a gun. Leave that shit where it is.":
                    beast "All the favor in the world won't do us much good if we get jumped without protection."

                    "..."

                    $ pc.addToInventory("swm500")
                    $ pc.gainCash(1000)
                    $ story_mission1_spotted = True

        else:
            "Hmm... What have we here? Something catches my eye on the way out. A locker underneath the purview of the camera I couldn't disable."

            "I can see well enough to tell that there's something valuable inside. Looks like some cash and what might be a gun. And I've kinda already been spotted, so who cares about the camera at this point?"

            "I still keep my head down as I break into the locker. This is quite a haul. I hold what looks like a brand new Smith & Wesson Model 500."

            "There's some cash too, but this gun packs enough of a punch to be useful against other vampires. I stash the heater, ammo and cash."

            $ pc.addToInventory("swm500")
            $ pc.gainCash(1000)

        jump missions.mission1_success


    label .mission1_success:

        if story_mission1_ghost:
            "I did it. Got in, got the evidence, got out, with absolutely no one the wiser. Shit, I'm good at this."

            $ pc.mend(KEY_WP, KEY_SPFD, 3)
            $ pc.mend(KEY_WP, KEY_AGGD, 1)
        elif not story_mission1_spotted:
            "I did it. They'll know something went down, and they might notice the evidence I took, if they can distinguish it from what their own crooked buddies take. But either way they'll have no proof and no idea who I was."

            $ pc.mend(KEY_WP, KEY_SPFD, 2)
        else:
            "Well... that could have gone better. But ultimately, it was a success."

            beast "By the skin of your ass."

        scene black with fade

        "I'm heading back to my car, cutting through the same alleyways I took on my way in. The place where I met that fucking creep."

        "When I see him, I realize that coming back this way was probably a stupid idea."

        scene bg danger alley1 with dissolve

        _anarch "Hey there. You must be that new Blue Blood lackey I've been hearing about."

        "His voice is deep and oozing with menace."

        me "You here for an autograph, champ?"

        _anarch "I think you know what I'm here for. Lotta useful data in there about Kay and the other Ventrue pukes that think they run this city. We been trying to get in there for days. Baron Marlowe doesn't want us just busting in and taking it, you see."

        me "Sounds like a smart guy."

        _anarch "That he is. I'll make you a deal. Hand over the goods now and I'll let you leave with your head attached."

        me "..."

        beast "The Rabble is threatening us. Let's drain him. Put his Blood to better use than embalming fluid for this worthless stiff."

        _anarch "Understand, this is a limited time offer. Better seize on it quick. The Ivory Tower doesn't give a shit about you, fledgling. You're not stupid enough to die for them, are you?"

        "...I can't. Not after everything. No way I'm just giving away my second shot at a decent life. One I'm not disgusted by."

        "The Tower is a nest of schemers and traitors, but so is every organized group of Kindred. At least the Tower can offer me security."

        "I'm not going to spend my unlife on the run, begging for suitable blood, scraping by from night to night. That's not living. That's just a slow death sentence."

        me "..."

        me "I..."

        _anarch "Time's up, kid."

        "And he's on me in a flash, almost faster than I can blink. I roll with his momentum and throw him over me as I hit the ground."

        $ arena.setStage()
        $ arena.startBattle(brujah) # Boss fight

        "..."

        "I can't believe I made it out of that alive. I limp the rest of the way to my car and drive off."

        # TODO diablerie?

        $ story_mission1_complete = True
        jump missions.mission1_end


    label .mission1_failstate:

        scene black with fade
        play music audio.freakout fadeout 2.0 fadein 2.0

        if daysLeft < 2:
            "...I failed. There's no time left to try again. My one shot..."

            "My second chance..."

            "What am I going to do now? I can't go to Elysium a failure. I can't stay in this city. I can't go back to my sire. I can't go home. I..."

            beast "..."

            beast "Well, we all knew this was coming, didn't we? The part where I clean up. Clean up the mess that you are. That you've always been."

            $ story_mission1_failed = True
            $ pc.damage(KEY_WP, KEY_AGGD, 10)
        elif (story_m1fail_burglary and story_m1fail_tech and story_m1fail_social):
            beast "How the FUCK did you manage to fail at absolutely everything?! At every single one of your stupid fucking gambits! You'd think one of your plans would succeed if only by chance!"

            "..."

            beast "This ain't fuckin' Fort Knox. This is some shit-ass local police precinct full of coffee-guzzling donut jockeys. How are you so fucking pathetic?"

            "I..."

            "I can't..."

            beast "Yes, that's abundantly clear now. You can't say I didn't give you a chance."

            $ story_mission1_failed = True
            $ pc.damage(KEY_WP, KEY_AGGD, 10)
        else:
            "...Goddamnit. FUCK! Why? WHY?! Why can't-"

            $ pc.damage(KEY_WP, KEY_AGGD, 1)

            "...I just..." # sound here?

            "Okay. Calm down, [petname]. Chill."

            "There's still time. This way won't work, but another will. Just need to retreat, regroup and try a different tack."

            beast "..."

            "There's still time..."

        $ story_mission1_cased = True
        jump missions.mission1_end


    label .mission1_end:

        $ updateTime(0.5, pc)

        jump nightloop
