init 2 python:

    GOAL_MENTAL_ATTACK  = "Mindcrush"
    GOAL_SCARE          = "Scary" # Mesmerize and Dread Gaze
    GOAL_DISARM         = "Drop it" # Compel and Mesmerize

    GOAL_OPENFIRE       = "Open fire"
    GOAL_SHOOTOUT       = "Gunbattle"
    GOAL_CLOSE          = "Close gap"
    GOAL_BRAWL          = "Melee Fight"

    GOAL_FLEE           = "cheese it"
    GOAL_CHASE          = "get back here"
    GOAL_LETGO          = "and stay out"
    GOAL_BETHKILLS      = "murked"

    class Combatant:
        def __init__(self, beth = None, name = "Unknown Assailant", isVampire = True, fightsToDeath = False):
            self.name = name
            self.beth = beth
            self.dead = False
            self.isVampire = isVampire
            self.fightsToDeath = fightsToDeath
            self.chasePenalty = 0
            self.wantsToFlee = False

        def embody(self, maxhp = 5, maxwill = 7, armor = 0):
            self.maxhp = maxhp
            self.hp = maxhp
            self.maxwill = maxwill
            self.will = maxwill
            self.armor = armor
            self.aggravated = False

        def equip(self, attack = 5, damage = 0, chase = 3, ranged = False, rangedAttack = 0, minAttack = 2):
            self.attack = attack
            self.damage = damage
            self.chase = chase
            self.ranged = ranged
            self.rangedAttack = rangedAttack
            self.minAttack = minAttack
            self.engaged = False
            self.shootout = False

        def setMessages(self, intro = MSG_INTRO_DEFAULT, death = MSG_DIE_DEFAULT, flight = MSG_FLEE_DEFAULT): # TODO: What does the text bar say when shit happens?
            self.intro = intro
            self.death = death
            self.flight = flight

        def disarm(self):
            self.attack = min(self.minAttack, self.attack)
            self.rangedAttack = min(self.minAttack, self.rangedAttack)
            self.damage = 0 #min(self.minAttack, self.damage) if self.isVampire else 0

        def melee(self, engaged): # engaged and shootout can both be false, but they can't both be true
            self.engaged = engaged
            if self.engaged:
                self.shootout = False

        def gunfight(self, shootout):
            self.shootout = shootout
            if self.shootout:
                self.engaged = False

        def _attack(self):
            results = []
            bethDamage = True
            mookDamage = True
            engageOnMookLoss = False
            engageOnMookWin = False

            bestMargin = -100
            bestResult = None

            beth = self.beth

            if self.wantsToFlee:
                return self._flee()
            elif self.dead:
                return (1, False, False, GOAL_BETHKILLS)

            if self.ranged and not self.engaged and not self.shootout: # ranged enemy gets free attack
                bethDamage = False
                engageOnMookLoss = True
                results.append(beth.test(self.rangedAttack, _dex, _athl, messyCritsOn = False, bestialFailsOn = False, goal = GOAL_OPENFIRE))
            elif self.ranged and self.shootout: # ranged attack vs ranged beth
                results.append(beth.test(self.rangedAttack, _dex, _fire, messyCritsOn = True, goal = GOAL_SHOOTOUT))
                results.append(beth.test(self.rangedAttack, _com, _fire, messyCritsOn = True, goal = GOAL_SHOOTOUT))
            elif self.engaged: # melee combat forces regular attack vs melee beth
                results.append(beth.test(self.attack, _str, _comb, messyCritsOn = True, goal = GOAL_BRAWL))
                results.append(beth.test(self.attack, _dex, _comb, messyCritsOn = True, goal = GOAL_BRAWL))
            elif not self.ranged and not self.engaged: # chase vs ranged beth
                mookDamage = False
                engageOnMookWin = True
                if not beth.hasItemOfType(IT_FIREARM):
                    engageOnMookLoss = True
                results.append(beth.test(self.chase, _dex, _fire, messyCritsOn = True, goal = GOAL_CLOSE))
            else:
                raise ValueError("[Error]: This shouldn't have been reached! Combat bug!")

            for res in results:
                if res[0] > bestMargin:
                    bestMargin = res[0]
                    bestResult = res

            if bestMargin > 0: # beth wins this round
                self.takeDamage(bestMargin + beth.getDamageBonus(), bethDamage)
                if engageOnMookLoss:
                    self.melee(True)
            elif bestMargin == 0: # tie
                self.takeDamage(1, bethDamage)
                self.dealDamage(1, mookDamage)
            else: # oh no
                dmg = self.attack + self.damage if not self.ranged else self.rangedAttack + self.damage
                self.dealDamage(dmg, mookDamage)
                if engageOnMookWin:
                    self.melee(True)

            # bestResult
            return bestResult

        def takeDamage(self, amount, enabled = True):
            if not enabled:
                return

            damage = amount - self.armor
            self.hp -= amount
            if self.hp <= 0 and not self.aggravated:
                self.aggravated = True
                if self.fightsToDeath:
                    self.hp = self.maxhp
                else:
                    self.wantsToFlee = True
            elif self.hp <= 0:
                self.dead = True
            else:
                raise ValueError("[Error]: This shouldn't have been reached! Combat damage bug!")

        def dealDamage(self, amount, enabled = True):# TODO: ADD damage sound effects!
            if not enabled:
                return
            self.beth.damage(KEY_HP, KEY_SPFD, amount)

        def _mindWarp(self, goal, *args): # beth's mental attacks either disarm or drive off enemies
            result = self.beth.test(0, args, goal = goal)
            if result[0] > 0 and result[1]:
                self.will -= (result[0] * 2)
            elif result[0] > 0:
                self.will -= result[0]
            else:
                print("NADA")

            if self.will <= 0 and goal == GOAL_DISARM:
                self.disarm()
            elif self.will <= 0:
                self.wantsToFlee = True
            else
                return (result[0], result[1], result[2], GOAL_MENTAL_ATTACK) # if the combatant still has some willpower

            return result

        def _chase(self):
            if self.wantsToFlee:
                return self._flee(True)

            result = self.beth.test(self.chase - self.chasePenalty, _dex, _athl, goal = GOAL_FLEE)
            if result[0] < 0:
                self.chasePenalty += 1

            return result

        def _flee(self, bethAllows = False):
            self.wantsToFlee = True
            if bethAllows:
                return (-1, False, False, GOAL_LETGO)
            return self.beth.test(self.chase, _dex, _athl, goal = GOAL_CHASE)


    # ===========================
    def startBattle(_opp = None):
        global opp
        global pc

        if _opp:
            opp = _opp
        else:
            opp = Combatant(beth = pc, name = "Unidentified Assailant")
            opp.embody()
            opp.equip()

        renpy.call("battles.battleLoop")

    def processRound(evt):
        global opp
        global pc

        marg = evt[0]
        etype = evt[3]
        mcrit = evt[1]
        bfail = evt[2]
        mcstr = " It's a messy critical!"
        bfstr = " A bestial failure!"

        renpy.say(None, "Type: {t}, result = {res}.{mc}{bf}".format(t=evt[3], res=evt[0], mc=(mcstr if mcrit else ""), bf=(bfstr if bfail else "")))

        if etype == GOAL_FLEE and marg > -1:
            bethEscapes()
        elif etype == GOAL_FLEE:
            renpy.say("Fuck! Can't shake this asshole.")
        elif etype == GOAL_BRAWL:
            bmsgBrawl(marg, pc, opp, mcrit, bfail)
        elif etype == GOAL_SHOOTOUT:
            bmsgShootout(marg, pc, opp, mcrit, bfail)
        elif etype == GOAL_OPENFIRE:
            bmsgOpenfire(marg)
        elif etype == GOAL_CLOSE:
            bmsgClose(marg, pc, opp, mcrit, bfail)
        elif etype == GOAL_MENTAL_ATTACK or etype == GOAL_SCARE or etype == GOAL_DISARM:
            bmsgPsychicAttack(marg, pc, opp, mcrit, bfail)
        elif etype == GOAL_CHASE and marg > -1:
            renpy.say("Where do you think you're going?")
        elif etype == GOAL_CHASE:
            renpy.say(beast, "They're getting away you imbecile. Catch them!")
            renpy.say("...Ah, fuck.")
        elif etype == GOAL_LETGO:
            renpy.say(beast, "No! You idiot, don't let them get away.")
            renpy.say("Enough. It's over.")
        elif etype == GOAL_BETHKILLS:
            renpy.say(beast, "Well done. Another notch on our belt, and maybe now the fools will learn to fear us.")
            renpy.say("That's not what we're here for, asshole.")
        else:
            raise ValueError("[Error]: Unknown battle event!")

    def msgBrawl(marg, pc, opp, mcrit = False, bfail = False):
        useweapon = pc.hasItemOfType(IT_WEAPON)
        oppweapon = opp.damage > 0

        if marg > 0 and useweapon and mcrit:
            renpy.say(beast, "Cut them to pieces! Paint the walls with their blood!")
        elif marg > ) and mcrit
            renpy.say(beast, "Crush. Them.")
        elif marg > 0 and useweapon:
            renpy.say("I score a solid cut. There's a sound of splitting meat. Not bad.")
        elif marg > 0:
            renpy.say("I throw punches and kicks and elbows and my enemy reels. But I can't let my guard down.")
        elif marg == 0 and useweapon and oppweapon:
            renpy.say("Our weapons clash painfully. It's a draw.")
        elif marg == 0 and useweapon:
            renpy.say("Well that was embarrassing. They don't even have a weapon.")
        elif marg == 0 and oppweapon:
            renpy.say("Bringing fists to a knife fight would be pretty stupid if I weren't already dead.")
        elif marg < 0 and oppweapon:
            renpy.say(me, "Ahh!")
            renpy.say("That fucking hurts!")
        elif marg < 0 and bfail:
            renpy.say(me, "Hurk...")
            renpy.say(beast, "What the fuck are you doing?! Fight back!")
        else:
            renpy.say("This is shameful. I'm getting my ass handed to me on a platter.")

    def bmsgShootout(marg, pc, opp, mcrit = False, bfail = False):
        if marg > 0 and mcrit:
            renpy.say(beast, "Yes! Blow them apart!")
        elif marg > 0:
            renpy.say(beast, "Yes! Shoot! Maim! Kill!")
        elif marg == 0:
            renpy.say("We both fire at each other almost blindly.")
        elif marg < 0 and bfail:
            renpy.say(me, "Ahh!")
            renpy.say(beast, "We're getting perforated, you idiot! Do something!")
        else:
            renpy.say(me, "Ughn...")
            renpy.say("Apparently they're a better shot. That's not good.")

    def bmsgOpenfire(marg):
        if marg > -1:
            renpy.say("My attacker opens up on me, but they're too slow and their aim sucks. Now I'm in a better position.")
        else:
            renpy.say(me, "Ughn...")
            renpy.say("Fuck! I'm out of position and taking hits!")

    def bmsgClose(marg, pc, opp, mcrit = False, bfail = False):
        usegun = pc.hasItemOfType(IT_FIREARM)
        oppweapon = opp.damage > 0

        if marg > 0 and usegun and mcrit:
            renpy.say(beast, "Yes! Blow them apart!")
        elif marg > 0 and mcrit:
            renpy.say(beast, "Yes! Tear them apart! Beat them into the ground!")
        elif marg > 0 and usegun:
            renpy.say("I land a solid shot, center mass. That should slow them down.")
        elif marg > 0:
            renpy.say("I close with the enemy, surprising them with my speed.")
        elif marg == 0 and usegun:
            renpy.say("I can't get a good shot. I wing them once, then it's too late. They're in my face.")
        elif marg == 0:
            renpy.say("We clash and it's a draw.")
        elif marg < 0 and oppweapon:
            renpy.say(me, "Hurk...")
            renpy.say("They're on me in an instant, almost running me through. Ugh!")
        elif marg < 0 and usegun and bfail:
            renpy.say(me, "Ahhh!")
            renpy.say(beast, "What the fuck are you doing?! I thought you knew how to shoot!")
        elif marg < 0 and bfail:
            renpy.say(me, "Hurk...")
            renpy.say(beast, "What are you doing?! Fight back!")
        else:
            renpy.say("This is pretty sad. Also pretty painful.")

    def bmsgPsychicAttack(marg, goal, mcrit = False, bfail = False):
        if marg > 0 and mcrit:
            renpy.say(beast, "Yes... Break their will. Break their mind.")

        if marg > 0 and goal == GOAL_MENTAL_ATTACK:
            renpy.say("They're out of it. I've almost got them.")
        elif marg > 0 and goal == GOAL_DISARM:
            renpy.say("And there goes the weapon. That should make this easier.")
        elif marg > 0 and goal == GOAL_SCARE:
            renpy.say("That's right, run you little bitch-ass...")
        else:
            renpy.say("Hmm... no effect.")

    def bethWinsBattle(kill = False):
        global pc

        renpy.say(me, "I won!")
        renpy.jump("battles.leaveBattle")

    def bethEscapes():
        global pc

        renpy.say(me, "Christ that was close!")
        renpy.jump("battles.leaveBattle")

# ========================
label battles:

    label .battleLoop:

        python:
            nextEvent = None
            hptracker = pc.getTracker(KEY_HP)
            status = "..."

        menu:
            "[status]"

            "And me, without a weapon. Guess I'll have to throw hands." if not pc.hasItemOfType(IT_WEAPON):
                python:
                    pc.setDamageBonus(0)
                    nextEvent = opp._attack()

                jump battles.processEvent

            "I try to get in close and fuck them up!" if pc.hasItemOfType(IT_WEAPON):
                python:
                    damageBonus = 0
                    weapons = pc.getHeldItemsOfType(IT_WEAPON)
                    for weapon in weapons:
                        if weapon[DAMAGE_BONUS] > damageBonus:
                            damageBonus = weapon[DAMAGE_BONUS]

                    pc.setDamageBonus(damageBonus)
                    nextEvent = opp._attack()

                jump battles.processEvent

            "I take aim and pop off with my gun!" if pc.hasItemOfType(IT_FIREARM):
                python:
                    damageBonus = 0
                    if pc.hasItemOfType(IT_FIREARM):
                        weapons = pc.getHeldItemsOfType(IT_FIREARM)
                        for weapon in weapons:
                            if weapon[DAMAGE_BONUS] > damageBonus:
                                damageBonus = weapon[DAMAGE_BONUS]

                        pc.setDamageBonus(damageBonus)
                    opp.gunfight()
                    nextEvent = opp._attack()

                jump battles.processEvent

            "I catch their gaze and command them to throw down their weapons!" if pc.hasDisciplinePower(_dominate, DOM_COMPEL) or pc.hasDisciplinePower(_dominate, DOM_MESMERIZE):
                python:
                    compel = pc.getAttr(_cha) + pc.getDisciplineLevel(_dominate)
                    mesmerize = pc.getAttr(_man) + pc.getDisciplineLevel(_dominate)
                    if compel > mesmerize:
                        nextEvent = opp._mindWarp(GOAL_DISARM, _cha, _dominate)
                    else:
                        nextEvent = opp._mindWarp(GOAL_DISARM, _man, _dominate)

                jump battles.processEvent

            "I crush their will and rout them!" if pc.hasDisciplinePower(_dominate, DOM_MESMERIZE) or pc.hasDisciplinePower(_presence, PRES_SCARYFACE):
                python:
                    mesmerize = pc.getAttr(_man) + pc.getDisciplineLevel(_dominate)
                    dreadgaze = pc.getAttr(_cha) + pc.getDisciplineLevel(_presence)
                    if dreadgaze > mesmerize:
                        nextEvent = opp._mindWarp(GOAL_SCARE, _cha, _presence)
                    else:
                        nextEvent = opp._mindWarp(GOAL_SCARE, _man, _dominate)

                jump battles.processEvent

            "I quickly mend my wounds!" if pc.getHunger() < HUNGER_MAX and hptracker[KEY_SPFD] > 0:
                python:
                    pc.mend(KEY_HP, KEY_SPFD, pc.getBPMend())
                    pc.addHungerDebt(4)

                "That's better... but I need to be careful. Can't get too hungry..."
                jump battles.battleLoop

            "This may have been a mistake... time to run!":
                python:
                    nextEvent = opp._chase()

                jump battles.processEvent

        label .processEvent:

            $ print("[processEvent]: nextEvent = ", nextEvent)
            $ processRound(nextEvent)

            jump battles.battleLoop


        label .leaveBattle

        return
