label nightloop:
    scene bg hotel room with fade
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
            else:
                if pc.getHunger() >= 4 or pc.getHumanity() < 6:
                    beast "FUCKING FINALLY!!! It's LONG past time we FED. And we're NOT gonna stop this time. Not if I can help it."

                    "..."
                else:
                    beast "Glad to see your priorities are in order. I like you much better when you're thinking straight."

                    "Don't make me change my mind."

                stop music fadeout 0.5
                scene bg driving road2 with trans_slowfade
                play sound audio.heels_on_pavement
                queue sound audio.carstart_pc

                "It's night [night]."

                "We don't have all the time in the world."

                "Need to get this done quickly."

                beast "We're here."

                play sound audio.carstopengine_pc
                play sound audio.carstopkeys_pc
                scene black with fade

                $ updateTime(0.5, pc)

                $ ptstring = str(pc.getPredatorType()).lower().strip().replace(" ", "")
                call expression "feeding.huntX_" + ptstring

        "Let me give some thought to the case.":
            # TODO: GEt next main quest info here, use it to inform menu below.

            menu:
                "Alright, let's consider our next move."

                "TESTBATTLE":
                    scene bg danger alley1
                    $ arena.setStage()
                    $ arena.startBattle()

        # "Attend Elysium":
        #     $ pass
        #
        # "Seek out the Anarchs" if story_anarchs_enabled:
        #     $ pass

        "I need to recuperate.":

            menu:
                "I can't go on like this. I need to recover, or I'll fall apart. Literally, figuratively, or both."

                "It'll take a lot of Blood, but I need to mend one of my worst, most aggravated wounds. Before it kills me." if hpbar[KEY_AGGD] > 0 and pc.canAggHPHeal():

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

                "I should probably mend some of my lesser injuries. You know, the stab wounds and bullet holes. Minor stuff." if hpbar[KEY_SPFD] > 0:
                    if pc.getHunger() >= HUNGER_MAX:
                        "Shit, I can't. I need to feed..."

                        play sound audio.beastgrowl1
                        beast "SO HELP ME GOD IF YOU DON'T GET OUT THERE AND HUNT I AM GOING TO DRAIN THE FIRST PERSON WE SEE"
                    else:
                        python:
                            pc.mend(KEY_HP, KEY_SPFD, pc.getBPMend())
                            pc.addHungerDebt(4)

                "The stress is building up. I'm this close to losing it. I need to just... relax." if willbar[KEY_SPFD] > 0: # TODO: implement this, add random battles

                    "..."

                    "No luck, huh?"


    # Menu reset
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

    label .Willpower:

        "..."

        "...I can't do this."

        "...Why did I think I could do this?"

        beast "{i}Because you're stupid. But don't worry. I'm here to guide you. In fact, I think I'll drive for a while.{/i}"

        "..."

        play sound audio.beastgrowl1

    return
