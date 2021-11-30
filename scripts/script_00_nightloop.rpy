python:

    global shadyguy
    global dirtycop
    global brujah

    shadyguy = Combatant(beth = pc, vampire = False)
    shadyguy.embody(6, 4, 0)
    shadyguy.equip(5, 2, 4)
    shadyguy.setStoryText(dead = [
        "And there it is. I've killed someone again. Self-defense, upholding the Masquerade and all that, and he had it coming. But...",
        "I was hoping to leave all that behind. Or at least some of it.",
        (beast, "Then you're a fool. Everything we do is violent. At least this way he'll never hurt anyone else.",),
        "...Maybe you're right."
    ])
    shadyguy.setStoryText(fled = [
        "He backs away, and just before he turns to run I catch his gaze and shout.",
        (me, "Forget!",),
        (beast, "Are you really going to let this vermin live?",),
        "I wiped him. He won't be able to remember what he was even running from.",
        (beast, "So he's free to attack someone else? I thought you wanted to protect people.",),
        "Not by killing every mortal shitstain I come across. I'd never get done, and I'm not ready to let you take over quite yet."
    ])
    shadyguy.setStoryText(escape = [
        "I'm faster than him, and I quickly leave his shouts and slurs far behind. I'm behind schedule now, though.",
        (beast, "I can't believe we ran from some mortal rapist. We should have drained him and made the world a better place.",),
        "Am I supposed to kill every mortal scumbag I run into? I help enforce the Masquerade. I'm not supposed to be leaving a trail of bodies."
    ])

    dirtycop = Combatant(beth = pc, vampire = False, knockable = True, escapable = False)
    dirtycop.embody(5, 4, 1)
    dirtycop.equip(4, 2, 3, True, 5) # he's got a gun

    brujah = Combatant(beth = pc)
    brujah.embody(6, 6, 0)
    brujah.equip(6, 0, 6)

label nightloop:
    scene bg hotel room with fade

    if story_mission1_complete:
        jump nightloop.epilogue
    elif night >= 7:
        jump missions.mission1_failstate

    if herd_countdown > 0:
        $ herd_countdown -= 1

    play music audio.hotel_neutral fadeout 0.5 fadein 2.0 volume 0.5

    python:
        global pc
        global arena

        hpbar = pc.getTrackerDamage(KEY_HP)
        willbar = pc.getTrackerDamage(KEY_WP)

        if justWokeUp:
            wakeupcall = "Wake up, dead girl. Time to go to work."
            justWokeUp = False
        else:
            wakeupcall = "Hurry up and make a choice."

    menu:
        beast "[wakeupcall]"

        "Should I hunt?":
            $ herd = pc.hasPerk(M_HERD[KEY_NAME])

            if pc.getHunger() < 2 and pc.getHumanity() > 5:
                "Nah, no point hunting now. This is about as good as it gets. The only way to slake the Hunger completely is to kill someone. And even then, the peace doesn't last for long. It's not worth premeditated murder. I'm not that far gone yet."

                jump nightloop
            elif herd[0] > 0 and herd_countdown < 1:
                $ herdlevel = herd[0]

                "Instead of hunting tonight, why don't I just go visit some of my \"acquaintances\"?"

                beast "Fine by me."

                $ pc.slakeHunger(herdlevel)
                $ herd_countdown = 3
            else:
                if pc.getHunger() >= 4 or pc.getHumanity() < 6:
                    beast "FUCKING FINALLY!!! It's LONG past time we FED. And we're NOT gonna stop this time. Not if I can help it."

                    "..."
                else:
                    beast "Glad to see your priorities are in order. I like you much better when you're thinking straight."

                    "Don't make me change my mind."

                stop music fadeout 0.5
                scene bg driving road2 with trans_slowfade
                $ pc.soundRoadTrip()

                "It's night [night]."

                "We don't have all the time in the world."

                "Need to get this done quickly."

                if timesFed % 2 != 0: # odd number of feeding times
                    call nightloop.randomBattle from _call_nightloop_randomBattle

                    "Jesus Christ, the fuck is with this city?"

                    beast "The Court here is rotten. Corrupt, incompetent, or both. Anarchs running wild. Ugh."

                    "I get back into my car and continue on my way."

                beast "We're here."

                play sound audio.carstopengine_pc
                play sound audio.carstopkeys_pc
                scene black with fade

                $ ptstring = str(pc.getPredatorType()).lower().strip().replace(" ", "")
                call expression "feeding.huntX_" + ptstring from _call_expression

                $ timesFed += 1
                $ updateTime(0.5, pc) # this should always come at the end

        "Let me give some thought to the case.":
            menu:
                "Alright, let's consider our next move."

                "Test Battle 1 - vs default enemy" if DEBUG:
                    $ arena.setStage(battleBG = None)
                    $ arena.startBattle()

                "Test Battle 2 - vs brujah" if DEBUG:
                    $ arena.setStage()
                    $ arena.startBattle(brujah)

                "Let's head down to the police precinct, and at least case the joint." if not story_mission1_start and not story_mission1_cased:
                    stop music fadeout 2.5

                    "It's settled. After I get ready we'll try getting some actual work done."

                    if pc.getHunger() > 2:
                        beast "You don't think we maybe ought to hunt first, Einstein?"
                    else:
                        beast "Good luck. You'll probably need it."

                    jump missions.mission1_start

                "Alright, I think I still have a chance to get this done. Let's give our first case another shot." if (story_mission1_start and story_mission1_failed) or story_mission1_cased:
                    stop music fadeout 2.5

                    if pc.getHunger() > 2:
                        beast "You already failed once. Do you really want to go into your next and probably last attempt hungry? Are you that fucking dim?"
                    else:
                        beast "You're on thin ice. You know that, right? Don't fuck up again, [petname]."

                    jump missions.mission1_try_again

        # "Attend Elysium":
        #     $ pass
        #
        # "Seek out the Anarchs" if story_anarchs_enabled:
        #     $ pass

        "I need to recuperate.":
            label .resting:

            menu:
                "I can't go on like this. I need to recover, or I'll fall apart. Literally, figuratively, or both."

                "It'll take a lot of Blood, but I need to mend one of my worst, most aggravated wounds. Before it kills me." if pc.getTrackerDamage(KEY_HP)[KEY_AGGD] > 0 and pc.canAggHPHeal():

                    "..."

                    if pc.getHunger() >= HUNGER_MAX:
                        "Fuck. I can't! I need blood... I need..."

                        play sound audio.beastgrowl1
                        beast "SO HELP ME GOD IF YOU DON'T GET OUT THERE AND HUNT I AM GOING TO DRAIN THE FIRST PERSON WE SEE"

                        "...Oh God..."
                    else:
                        python:
                            pc.toggleAggHPHealing(False)
                            pc.mend(KEY_HP, KEY_AGGD, 1)
                            pc.addHungerDebt(12)

                        "...My body feels {i}much{/i} better. Physical agony is receding, and Final Death feels further away. But now a different sort of agony is growing. Diffusing throughout me like venom."

                        beast "I Think. You know. What time. It is. [pcname], old pal."

                    jump nightloop.resting

                "I should probably mend some of my lesser injuries. You know, the stab wounds and bullet holes. Minor stuff." if pc.getTrackerDamage(KEY_HP)[KEY_SPFD] > 0:
                    if pc.getHunger() >= HUNGER_MAX:
                        "Shit, I can't. I need to feed..."

                        play sound audio.beastgrowl1
                        beast "SO HELP ME GOD IF YOU DON'T GET OUT THERE AND HUNT I AM GOING TO DRAIN THE FIRST PERSON WE SEE"
                    else:
                        python:
                            pc.mend(KEY_HP, KEY_SPFD, pc.getBPMend())
                            pc.addHungerDebt(4)

                    jump nightloop.resting

                "The stress is building up. I'm this close to losing it. I need to just... relax." if willbar[KEY_SPFD] > 0: # TODO: implement this, add random battles

                    if pc.getTrackerDamage(KEY_WP)[KEY_SPFD] < 1:
                        "There's no point doing that now. I'm as relaxed as I can get, and I have work to do."

                        jump nightloop

                    "..."

                    jump rnr

                "I'm done.":
                    jump nightloop

            if pc.getHunger() > 2:
                "...I think I might be okay. Aside from the Hunger. So I guess not at all."
            else:
                "...I think I might be okay."

    # Menu reset
    jump nightloop


    # random battles
    label .randomBattle:

        $ _opp = arena.generateRandomOpp()
        $ arena.setStage()
        $ arena.startBattle(_opp)

        return


    # End of the game, sadly
    label .epilogue:

        # TODO music and sounds
        "I stumble into the shower and clean up as best I can. Then I dry off and throw myself onto the bed. I'll just... lie here for a bit."

        "There's a knock at the door. Go away, whoever you are."

        "But they don't. The knocking just gets more urgent. Fuck me. If that's another Anarch hitter, I'm done. I can't fight another fucking Brujah."

        ghoul "[pcname]? You in there? [petname]!"

        "Oh, that's my ghoul. Guess I better answer the door, then."

        beast "Let's eat him and use his blood to mend ourselves."

        "Fuck off."

        beast "It's survival. He'll understand."

        "I stagger over to the door, unlock the deadbolt and pull it open."

        ghoul "[petname]! Holy shit, what happened? I heard you got jumped, but... Jesus."

        me "Nice to see you too. You look great."

        "He does, actually. He's rocking a well-fitted crimson turtleneck and pressed slacks. His peacoat is on the floor in the hall."

        if pc.hasPerk(M_HERD[KEY_NAME]):
            ghoul "What do you need? You can heal all of that, right? If you have blood? I'll have one of your people sent up."

            me "That... actually sounds pretty good."

            scene black with fade
            scene bg hotel room with trans_slowfade
            python:
                pc.slakeHunger(2)
                while pc.getHunger() < 4 and pc.getTrackerDamage(KEY_HP)[KEY_SPFD] > 0:
                    pc.mend(KEY_HP, KEY_SPFD, 1)
                    pc.addHungerDebt(4)

            "That's much better. The young woman in a bathrobe who came to \"donate\" smiles and asks if I need anything else."

            me "Thank you, hon. But no. I'll see you later, okay?"

            "She nods and sees herself out."
        else:
            ghoul "What do you need? You can heal all of that, right? If you have blood? I'll find someone."

            me "...Later. First, business."

            ghoul "You sure? Okay."

        me "So the mission was a success, by some standards at least. I got the stuff."

        # endings
        if story_mission1_ghost:
            me "I got in and out with no one the wiser. There shouldn't be any clue as to what I was there to do, and no one should recognize me."

            ghoul "{i}Hell{/i} yeah. Good work, boss."

            call nightloop.burnstash from _call_nightloop_burnstash

            "Everyone's pretty pleased. In and out, with no complications. The Anarchs will notice their missing enforcer pretty quickly and their police contacts will realize something's wrong. But they won't have anything to go on, and Kay's secrets are out of their reach."

            "Kay Sanghera is already offering to introduce me to some of the other prominent Blue Bloods in the city. Apparently Clan Ventrue is pretty close-knit in this city."

            "Later at Elysium, the Seneschal {i}personally{/i} congratulates me on my \"valiant\" defeat of the \"Rabble savage\". The looks I get definitely change after that. People voluntarily associate with me now."

            beast "Yeah, it's been a while since you could say that. When you're done preening, we should consider our next move."

            me "You know [ghoulpet], we might just have a future here."

            "He smiles. So do I."

            ghoul "I'll make some calls."

            me "You do that. I've got some business to follow up on myself."
        elif not story_mission1_spotted:
            me "I got in and out without being identified. They'll know something went down, but I'm in the clear."

            ghoul "So basically it couldn't have gone much better."

            me "Hopefully the Seneschal sees it that way."

            call nightloop.burnstash from _call_nightloop_burnstash_1

            "All in all, everyone seems satisfied. My performance hasn't blown anyone away, but all the important metrics were met, and there's not much \"cleanup\" that needs doing."

            "Kay Sanghera sent me several cryptic texts. They express gratitude, and seem to suggest that she might be willing to introduce me to some of the other prominent Blue Bloods in the city. Apparently Clan Ventrue is pretty close-knit in this city."

            "Later at Elysium, the Seneschal {i}personally{/i} congratulates me on my \"valiant\" defeat of the \"Rabble savage\". The looks I get definitely change after that."

            me "You know [ghoulpet], we might just have a future here."

            "He smiles. So do I."

            ghoul "I'll make some calls."

            me "You do that. I've got some business to follow up on."
        elif not story_mission1_failed:
            me "I got the goods, on the first attempt no less."

            ghoul "Could there have been a second?"

            me "I don't know, honestly. But I have what I came for, and that'll have to be good enough."

            call nightloop.burnstash from _call_nightloop_burnstash_2

            "...So the Seneschal isn't exactly pleased with me. Kay is a bit more sympathetic. She sent me a cryptic text about how we were all young once. And congratulating me on my \"victory\", presumably referring to the Brujah."

            "I think she's just happy to have her dirty laundry disposed of."

            "It's not the best start, but I may have a future in this city. I've been wondering about that \"big\" job they were talking about before. I don't know if they still view me as qualified, but it seems like they've got their hands full."

            beast "Chaos is a ladder."

            "I'll have to think about it."

            me "[ghoulname], I think I'll be staying here at least a little longer. Look into some things, see if I can make any friends. See how it goes."

            "He smiles."

            ghoul "I'll make some calls."
        else:
            me "It took more than one try, admittedly. But there were no major Masquerade breaches, and I got the goods. That's good, right?"

            ghoul "Uh, I sure hope so. You'd know better than me, boss."

            call nightloop.burnstash from _call_nightloop_burnstash_3

            "...So the Seneschal isn't pleased. Neither is Kay Sanghera. They politely thank me for accomplishing the main objective and (mostly) upholding the Masquerade, but when I go to Elysium it's pretty clear what the Court thinks of my abilities."

            "...So much for my second shot."

            "But I'm not a complete failure, so maybe my sire will take me back. Worth a shot."

            beast "Yes, let's go crawling back to our sire. You've done so well, [pcname]. Maybe she'll coddle and mother us some more. You'd like that."

            "...I mean, yeah. I would. Was I supposed to take that bait?"

            beast "So you've just lost all sense of digni-"

            "We're vampires. We hide in shadows and suck blood. Ticks don't have dignity. Or pride. Fuck how you feel about it; I'm going home."

            beast "You've vowed to ignore me before. It never lasts. Because I'm the only part of you that isn't delusional."

            ghoul "...Boss?"

            me "Nothing, [ghoulpet]. I think I'll be checking out tomorrow. Heading back."

            ghoul "...Huh. Alright, I'll make some calls."

        scene black with fade

        jump endgame

        label .burnstash:
            "I contact the Seneschal with Kay Sanghera's burner phone. They confirm that the material is to be destroyed. I record a video of the drives and tapes being tossed in a bag, thrown into a dumpster, and set on fire."

            beast "Did it {i}have{/i} to be fire?"

            "From a safe distance, of course."

            scene bg hotel room

            return

label rnr: # TODO random battles here?

    "I think I'll just take the night off. Can't keep burning the candle at both ends, or whatever version of that saying makes sense for Kindred."

    scene bg hotel exterior with fade

    $ pc.soundRoadTrip("I mean, what's the point of living forever if it's all just stress and work and hunting and looking over your shoulder?")

    beast "Not dying. That's the fucking point. Avoiding the pathetic end that mortals are doomed to. At least for a while. We can swing at least three or four human lifetimes, right?"

    scene bg driving road2

    if random.randint(0, 1) > 0:
        "{i}Goddamnit.{/i} Another one of these."

        beast "Hey, if we're on vacation I should get to have fun too, right?"

        call nightloop.randomBattle from _call_nightloop_randomBattle_1

    play music audio.relaxation fadeout 2.0 fadein 2.0

    menu: # TODO Better music?
        "Where am I even going?"

        "To the beach!":
            if not relaxbeach:
                beast "What for?"

                "Because it's beautiful and atmospheric. I'm trying to establish a mood. Melancholy, wistful, contemptlative. You know."

                beast "I don't see how saltwater and sand help with that."

                "Just relax, Anakin. And let me do the same."

                beast "...Whatever. As long as we get back to what's important afterward."

            scene bg relax beach with trans_slowfade
            play music audio.relaxation

            "It's peaceful out here. Calm. Beautiful. Exactly the mood I was looking for."

            "I get why the Outlanders are into this sort of thing, now. Traveling the world, independent. Free."

            "Of course, that's not an option for most Blue Bloods. Probably not any, unless you have a type that lets you stick to, like, popular hiking trails or something."

            "From here the city looks beautiful. Obsidian spires lined with sparkling jewels of a dozen colors."

            "I could get used to this..."

        "Let's go dancing.":
            if not relaxclub:
                beast "...Who's \"us\"? You're alone."

                "It's just an expression."

                beast "Fine, but if we run into another handsy creep I reserve the right to eat him. Or her, that one time."

                "...We'll see. I'm not saying no, but don't get your hopes up."

            scene bg relax club with trans_slowfade
            play music audio.siren_women1 fadeout 2.0 fadein 2.0

            "..."

            "It's a good night. I hit an intimate little spot with great music and a great crowd. I dance my heart out and then spend a few hours hanging out with some cool chicks I've seen around."

            "They're cool people, and I barely have any trouble resisting the temptation to eat them. It's good to just spend time with mortals. Just chill and vibe, with no ulterior motives."

            beast "{i}Everyone{/i} has ulterior motives. All the time, no exceptions. You understood that when you were mortal. Don't start viewing the kine with rose-colored glasses now that we prey on them."

            "I'm feeling way too good to listen to you tonight."

        "I want to hit a bar and get fucking zooted.":
            if not relaxbar:

                beast "Remember when our sire explained to you that we can't get drunk or high because we're dead? I remember you nodding like you understood the words coming out of her mouth."

                "I also remember when the Malkavian Primogen's third childe showed us exactly how to get around that particular hurdle. I miss Zachariah. Dude's a riot and a half."

                beast "...That's just hunting with extra steps. Not that I'm complaining."

                "No, because feeding isn't the point; it's just the delivery mechanism. Fangs instead of hypodermic needles."

                "The purpose is to get, as I explained earlier, {i}fucking zooted{/i}. Zonked. Zoinkied. Wasted. Basted. Tanked. Tipsy, even."

                beast "Yes, yes, yes. This sounds very normal and very healthy."

                "That's rich, coming from you."

                beast "Everything I tell you to do is natural and normal for our kind. Lions rip apart gazelle and eat their flesh raw, because that's their nature. But you wouldn't let a lion drink a gallon of whiskey, would you?"

                "I wouldn't try to stop it, either. Seems like that's the lion's business and not ours."

                beast "..."

            scene bg relax smokebar with trans_slowfade
            play music audio.relaxation

            "I get a table near the back and order a glass of Jim Beam, neat. I'm not about to spring for expensive booze if I'm not the one who's going to be drinking it, but that doesn't mean I should subject my vessel to cheap rotgut. I want them to enjoy themselves."

            "I'm not there long before some dude in a leather jacket comes by to hit on me. He's not going to get what he wants, but he's definitely in for an interesting time."

            "In a couple hours I'm in a booth even further back with him and his boys. We're laughing and joking. They're plastered. Almost falling-over drunk. I know because I've been tasting them. The two who are my type, anyway."

            "I don't know what they'll think happened tomorrow morning, but these dudes aren't so bad. They've got a sort of goofy charm, and they've even been nice enough to pay for the drinks and cigars. I'm about to get {i}real{/i} sloshy. This is going to be a good night."

            beast "..."

    $ pc.mend(KEY_WP, KEY_SPFD, 5)

    scene black with fade

    $ updateTime(1)

    jump nightloop


# ==========================
# These labels end the game.

label endgame:

    $ log("\n[STATUS]: Game ended.\n")

    return

label gameover:

    $ log("\n[STATUS]: Failure. Game over.\n")

    label .Health:

        "..."

        "...This isn't how it was supposed to go."

        "But..."

        "Maybe it's for the best. Everyone else... is..."

        "...probably better off."

        "I'm sorry."

        jump gameover.end

    label .Willpower:

        "..."

        "...I can't do this."

        "...Why did I think I could do this?"

        beast "{i}Because you're stupid. But don't worry. As ever, I'm here to guide you. In fact, I think I'll take over for a while.{/i}"

        "..."

        play sound audio.beastgrowl1

        jump gameover.end

    label .end:

    "..."

    return

    return
