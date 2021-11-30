init 2 python:

    GOAL_MENTAL_ATTACK  = "Psychic assault"
    GOAL_SCARE          = "Fear attempt" # Mesmerize and Dread Gaze
    GOAL_DISARM         = "Disarm attempt" # Compel and Mesmerize

    GOAL_OPENFIRE       = "Enemy opening fire"
    GOAL_SHOOTOUT       = "Gunfight"
    GOAL_CLOSE          = "Close to melee"
    GOAL_BRAWL          = "Melee combat"
    GOAL_FEED_ATTACK    = "Drink the enemy"

    GOAL_FLEE           = "Flee attempt (PC)"
    GOAL_CHASE          = "Flee attempt (Enemy)"
    GOAL_GUNCHASE       = "Flee attempt (Enemy, PC Shooting)"
    GOAL_LETGO          = "Allowing enemy to flee"
    GOAL_BETHKILLS      = "PC killed Enemy"
    GOAL_KNOCKOUT       = "PC knocked out Enemy"

    class Combatant:
        def __init__(self, beth = None, name = "Unknown Assailant", vampire = True, fightsToDeath = False, knockable = False, escapable = True):
            self.name = name
            self.beth = beth
            self.dead = False
            self.awake = True
            self.vampire = vampire
            self.fightsToDeath = fightsToDeath
            self.knockable = knockable
            self.escapable = escapable
            self.chasePenalty = 0
            self.wantsToFlee = False
            self.lines = {}
            self.lines["intro"] = []
            self.lines["dead"] = []
            self.lines["outcold"] = []
            self.lines["fled"] = []
            self.lines["escape"] = []

        def embody(self, maxhp = 5, maxwill = 7, armor = 0):
            self.maxhp = maxhp
            self.hp = maxhp
            self.maxwill = maxwill
            self.will = maxwill
            self.armor = armor
            self.aggravated = False

        def equip(self, attack = 5, damage = 0, speed = 3, ranged = False, rangedAttack = 0, minAttack = 2):
            self.attack = attack
            self.damage = damage
            self.speed = speed
            self.ranged = ranged
            self.rangedAttack = rangedAttack
            self.minAttack = minAttack
            self.engaged = False
            self.shootout = False
            self.disarmed = False

        def getStoryText(self, which = "intro"):
            return self.lines[which]

        def peelOppLine(self, which):
            if len(self.lines[which]) > 0:
                line = self.lines[which][0]
                del self.lines[which][0]
                return line
            else:
                return None

        def setStoryText(self, intro = [], dead = [], outcold = [], fled = [], escape = []):
            if intro:
                self.lines["intro"] = intro
            if dead:
                self.lines["dead"] = dead
            if outcold:
                self.lines["outcold"] = outcold
            if fled:
                self.lines["fled"] = fled # when enemy escapes
            if escape:
                self.lines["escape"] = escape # when player escapes

        def debugGetHP(self):
            aggra = " (AGG)" if self.aggravated else ""
            return "{cur} / {max}{agg}".format(cur=self.hp, max=self.maxhp, agg=aggra)

        def isVampire(self):
            return self.vampire

        def canBeFled(self):
            return self.escapable

        def disarm(self):
            self.disarmed = True
            self.attack = min(self.minAttack, self.attack)
            self.rangedAttack = min(self.minAttack, self.rangedAttack)
            self.damage = 0

        def melee(self, engaged): # engaged and shootout can both be false, but they can't both be true
            self.engaged = engaged
            if self.engaged:
                self.shootout = False

        def gunfight(self, shootout):
            self.shootout = shootout
            if self.shootout:
                self.engaged = False

        def isFleeing(self):
            return self.wantsToFlee

        def isDisarmed(self):
            return self.disarmed

        def isDead(self):
            return self.dead

        def isAwake(self):
            return self.awake

        def _attack(self, bonus = 0, biting = False):
            results = []
            bethDamage = True
            mookDamage = True
            engageOnMookLoss = False
            engageOnMookWin = False

            bestMargin = -100
            bestResult = None

            beth = self.beth

            if self.wantsToFlee and not biting:
                return self._flee(bethAllows = False, bethShooting = self.shootout, bonus = bonus)
            elif self.wantsToFlee and biting:
                bestResult = beth.test(self.speed, _dex, _athl, bonus, bestialFailsOn = False, goal = GOAL_FEED_ATTACK)
                beth.slakeHunger(bestResult[0])
                return bestResult
            elif not self.awake:
                return (1, False, False, GOAL_KNOCKOUT)
            elif self.dead:
                return (1, False, False, GOAL_BETHKILLS)

            if self.ranged and not self.engaged and not self.shootout: # ranged enemy gets free attack
                bethDamage = False
                engageOnMookLoss = True
                results.append(beth.test(self.rangedAttack, _dex, _athl, bonus, messyCritsOn = False, bestialFailsOn = False, goal = GOAL_OPENFIRE))
            elif self.ranged and self.shootout: # ranged attack vs ranged beth
                results.append(beth.test(self.rangedAttack, _dex, _fire, bonus, messyCritsOn = True, goal = GOAL_SHOOTOUT))
                results.append(beth.test(self.rangedAttack, _com, _fire, bonus, messyCritsOn = True, goal = GOAL_SHOOTOUT))
            elif self.engaged: # melee combat forces regular attack vs melee beth
                brawlGoal = GOAL_BRAWL if not biting else GOAL_FEED_ATTACK
                results.append(beth.test(self.attack, _str, _comb, bonus, messyCritsOn = True, goal = brawlGoal))
                results.append(beth.test(self.attack, _dex, _comb, bonus, messyCritsOn = True, goal = brawlGoal))
            elif not self.ranged and not self.engaged: # chase vs ranged beth
                mookDamage = False
                engageOnMookWin = True
                if not beth.hasItemOfType(IT_FIREARM):
                    engageOnMookLoss = True
                results.append(beth.test(self.speed, _dex, _fire, bonus, messyCritsOn = True, goal = GOAL_CLOSE))
            else:
                raise ValueError("[Error]: This shouldn't have been reached! Combat bug!")

            for res in results:
                if res[0] > bestMargin:
                    bestMargin = res[0]
                    bestResult = res

            if bestMargin > 0: # beth wins this round
                if not biting:
                    self.takeDamage(bestMargin + beth.getDamageBonus(), bethDamage)
                else: # feeding drains power and slakes beth's hunger
                    juice = min(bestMargin, 3)
                    beth.slakeHunger(juice)
                    self.attack -= 1
                    self.speed -= 1
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

            return bestResult

        def takeDamage(self, amount, enabled = True):
            if not enabled:
                return

            damage = amount - self.armor
            self.hp -= amount
            if self.hp <= 0 and not self.aggravated:
                self.aggravated = True
                self.hp = self.maxhp
                if self.knockable:
                    self.awake = False
                elif not self.fightsToDeath:
                    self.wantsToFlee = True
            elif self.hp <= 0:
                self.dead = True
                self.wantsToFlee = False

        def dealDamage(self, amount, enabled = True):# TODO: ADD damage sound effects!
            if not enabled:
                return
            self.beth.damage(KEY_HP, KEY_SPFD, amount)

        def _mindWarp(self, goal, *args): # beth's mental attacks either disarm or drive off enemies
            result = self.beth.test(0, *args, goal = goal)
            if result[0] > 0 and result[1]:
                self.will -= (result[0] * 2)
            elif result[0] > 0:
                self.will -= result[0]
            else:
                log("Mental attack had no effect.")

            if self.will <= 0 and goal == GOAL_DISARM:
                self.disarm()
            elif self.will <= 0 and self.knockable:
                self.awake = False
            elif self.will <= 0:
                self.wantsToFlee = True
            else:
                return (result[0], result[1], result[2], GOAL_MENTAL_ATTACK) # if the combatant still has some willpower

            return result

        def _chase(self, bonus = 0):
            if self.wantsToFlee:
                return self._flee(bethAllows = True)

            result = self.beth.test(self.speed - self.chasePenalty, _dex, _athl, bonus, goal = GOAL_FLEE)
            if result[0] < 0:
                self.chasePenalty += 1

            return result

        def _flee(self, bethAllows = False, bethShooting = False, bonus = 0):
            self.wantsToFlee = True
            if bethAllows:
                return (-1, False, False, GOAL_LETGO)
            elif bethShooting:
                return self.beth.test(self.speed, _dex, _fire, bonus, goal = GOAL_GUNCHASE)
            return self.beth.test(self.speed, _dex, _athl, bonus, goal = GOAL_CHASE)


    class BattleArena:

        def __init__(self, battleBG = "bg danger alley1", returnBG = "bg hotel exterior", returnMusic = None):
            self.battleBG = battleBG
            self.returnBG = returnBG
            if returnMusic:
                self.returnMusic = returnMusic
            else:
                self.returnMusic = renpy.music.get_playing()

        def setStage(self, battleBG = None, returnBG = None, returnMusic = None):
            if battleBG:
                self.battleBG = battleBG
            if returnBG:
                self.returnBG = returnBG
            if returnMusic:
                self.returnMusic = returnMusic
            else:
                self.returnMusic = renpy.music.get_playing()

            self.setCombatParams()

        def setCombatParams(self, surged = False):
            self.rounds = 0
            self.surged = surged
            self.battlefeeds = 0
            self.pcHasCompel = pc.hasDisciplinePower(_dominate, DOM_COMPEL)
            self.pcHasMesmerize = pc.hasDisciplinePower(_dominate, DOM_MESMERIZE)
            self.pcHasDreadGaze = pc.hasDisciplinePower(_presence, PRES_SCARYFACE)
            self.pcHasToughness = pc.hasDisciplinePower(_fortitude, FORT_TOUGH)

        def generateRandomOpp(self):
            randomOpp = Combatant(beth = pc)
            randomOpp.embody(random.randint(4, 7), random.randint(3, 6), random.randint(0, 1))
            randomOpp.equip(random.randint(3, 6), random.randint(0, 2), random.randint(1, 4))
            randomOpp.setStoryText(intro = [
                "I get the bright idea of taking a shortcut suggested by Waze. I find myself driving through an alley just wide enough. All going according to plan, until...",

                "I'm boxed in by another car. I curse, thinking it's parked and empty and just blocking my shortcut.",

                "I was wrong. It roars to life, and its occupant steps out. Kindred. I can tell right away. And, I'm guessing Anarch. Is there anywhere for me to even flee?"
            ])

            randomOpp.setStoryText(dead = [
                "Great. Just great. A dead Anarch and his shitbox car. This isn't going to look good to anyone. I guess I should be grateful I'm alive."
            ])
            randomOpp.setStoryText(fled = [
                "The motherfucker ran! I can't believe this shit. Jumps me and has the nerve to fucking run!"
            ])
            randomOpp.setStoryText(escape = [
                "I turn a corner, sprint up to an alcove as fast as I can and pivot into it. I press myself into the crevasse, and my attacker runs past. I can't believe that worked.",

                (beast, "They're Anarchs. You were expecting Belisarius or something?",),

                "I creep back the way I came."
            ])

            return randomOpp

        def getNumRounds(self):
            return self.rounds

        def incRounds(self):
            self.rounds += 1

        def numBattleFeeds(self):
            return self.battlefeeds

        def incBattleFeeds(self):
            self.battlefeeds += 1

        def hasSurged(self):
            return self.surged

        def addSurge(self):
            self.surged = True

        def getBonus(self):
            if self.surged:
                self.surged = False
                return pc.getBPSurge()
            else:
                return 0

        def hasCompel(self):
            return self.pcHasCompel

        def hasMesmerize(self):
            return self.pcHasMesmerize

        def hasDreadGaze(self):
            return self.pcHasDreadGaze

        def hasToughness(self):
            return self.pcHasToughness

        def readOppStory(self, which, _opp = None):
            global opp

            if _opp:
                opp = _opp
            elif not opp:
                opp = Combatant(beth = pc)
                opp.embody()
                opp.equip()

            line = opp.peelOppLine(which)
            while line:
                if type(line) is tuple:
                    renpy.say(line[0], line[1])
                else:
                    renpy.say(None, line)
                line = opp.peelOppLine(which)

        def startBattle(self, _opp = None):
            global opp
            global pc

            if _opp:
                opp = _opp
            else:
                opp = Combatant(beth = pc, name = "Unidentified Assailant")
                opp.embody()
                opp.equip()

            renpy.sound.stop()
            renpy.music.stop(fadeout = 1.5)
            renpy.music.play(audio.mission2)
            renpy.scene()
            renpy.show(self.battleBG)

            self.readOppStory("intro")

            renpy.call("battles.battleLoop")

        def endBattle(self):
            global usingToughness
            usingToughness = False

            if opp.isDead():
                self.readOppStory("dead")
            elif not opp.isAwake():
                self.readOppStory("outcold")
            elif opp.isFleeing():
                self.readOppStory("fled")
            else:
                self.readOppStory("escape")

            renpy.scene()
            renpy.show(self.returnBG)
            renpy.music.play(self.returnMusic)
            renpy.jump("battles.leaveBattle")

        def processRound(self, evt):
            global opp
            global pc

            marg = evt[0]
            etype = evt[3]
            mcrit = evt[1]
            bfail = evt[2]
            mcstr = " It's a messy critical!"
            bfstr = " A bestial failure!"

            if DEBUG:
                renpy.say(None, "Type: {t}, result = {res}.{mc}{bf} Enemy HP: {hp}".format(t=evt[3], res=evt[0], mc=(mcstr if mcrit else ""), bf=(bfstr if bfail else ""), hp=opp.debugGetHP()))

            if etype == GOAL_FLEE and marg > -1:
                self.bethEscapes()
            elif etype == GOAL_FLEE:
                renpy.say(None, "Fuck! Can't shake this asshole.")
            elif etype == GOAL_BRAWL:
                self.bmsgBrawl(marg, pc, opp, mcrit, bfail)
            elif etype == GOAL_SHOOTOUT:
                self.bmsgShootout(marg, pc, opp, mcrit, bfail)
            elif etype == GOAL_OPENFIRE:
                self.bmsgOpenfire(marg)
            elif etype == GOAL_CLOSE:
                self.bmsgClose(marg, pc, opp, mcrit, bfail)
            elif etype == GOAL_FEED_ATTACK and marg > 0:
                self.incBattleFeeds()
                renpy.say(beast, "Yes... Wonderful work, dead girl.")
                renpy.say(None, "Can't believe that worked.")
            elif etype == GOAL_FEED_ATTACK:
                renpy.say(beast, "A failure. But I like where your head's at.")
            elif etype == GOAL_MENTAL_ATTACK or etype == GOAL_SCARE or etype == GOAL_DISARM:
                self.bmsgPsychicAttack(marg, etype, mcrit, bfail)
            elif etype == GOAL_CHASE and marg > 0:
                renpy.say(None, "Where do you think you're going?")
                opp.melee(True)
                opp.takeDamage(marg)
            elif etype == GOAL_GUNCHASE and marg > 0:
                renpy.say(None, "Don't run. What, you think I'm too noble to shoot you in the back?")
                opp.gunfight(True)
                opp.takeDamage(marg + pc.getDamageBonus())
            elif (etype == GOAL_CHASE or etype == GOAL_GUNCHASE) and marg < 1:
                renpy.say(beast, "They're getting away you imbecile. Catch them!")
                renpy.say(None, "...Ah, fuck.")
                self.bethWinsBattle(False)
            elif etype == GOAL_LETGO:
                renpy.say(beast, "No! You idiot, don't let them get away.")
                renpy.say(None, "Enough. It's over.")
                self.bethWinsBattle(False)
            elif etype == GOAL_BETHKILLS:
                renpy.say(beast, "Well done. Another notch on our belt, and maybe now the fools will learn to fear us.")
                renpy.say(None, "That's not what we're here for, asshole.")
                self.bethWinsBattle(True)
            elif etype == GOAL_KNOCKOUT:
                renpy.say(None, "Man. Out like a light.")
                self.bethWinsBattle(False)
            else:
                raise ValueError("[Error]: Unknown battle event!")

            self.incRounds()

        def bmsgBrawl(self, marg, pc, opp, mcrit = False, bfail = False):
            useweapon = pc.hasItemOfType(IT_WEAPON)
            oppweapon = opp.damage > 0

            if marg > 0 and useweapon and mcrit:
                renpy.say(beast, "Cut them to pieces! Paint the walls with their blood!")
            elif marg > 0 and mcrit:
                renpy.say(beast, "Crush. Them.")
            elif marg > 0 and useweapon:
                renpy.play(audio.stab1, u'sound')
                renpy.say(None, "I score a solid cut, and I'm rewarded with the sound of splitting meat. Not bad.")
            elif marg > 0:
                renpy.say(None, "I throw punches and kicks and elbows and my enemy reels. But I can't let my guard down.")
            elif marg == 0 and useweapon and oppweapon:
                renpy.play(audio.swordclash, u'sound')
                renpy.say(None, "Our weapons clash painfully. It's a draw.")
            elif marg == 0 and useweapon:
                renpy.say(None, "Well that was embarrassing. They don't even have a weapon.")
            elif marg == 0 and oppweapon:
                renpy.say(None, "Bringing fists to a knife fight would be pretty stupid if I weren't already dead.")
            elif marg == 0:
                renpy.say(None, "I didn't come here to wrestle, dammit.")
            elif marg < 0 and oppweapon:
                renpy.say(me, "Ahh!")
                renpy.say(None, "That fucking hurts!")
            elif marg < 0 and bfail:
                renpy.say(me, "Hurk...")
                renpy.say(beast, "What the fuck are you doing?! Fight back!")
            else:
                renpy.say(None, "This is shameful. I'm getting my ass handed to me on a platter.")

        def bmsgShootout(self, marg, pc, opp, mcrit = False, bfail = False):
            if marg > 0 and mcrit:
                renpy.say(beast, "Yes! Blow them apart!")
            elif marg > 0:
                renpy.say(beast, "Yes! Shoot! Maim! Kill!")
            elif marg == 0:
                renpy.say(None, "We both fire at each other almost blindly.")
            elif marg < 0 and bfail:
                renpy.play(audio.bulletimpacts, u'sound')
                renpy.say(me, "Ahh!")
                renpy.say(beast, "We're getting perforated, you idiot! Do something!")
            else:
                renpy.play(audio.bulletimpacts, u'sound')
                renpy.say(me, "Ughn...")
                renpy.say(None, "Apparently they're a better shot. That's not good.")

        def bmsgOpenfire(self, marg):
            if marg > -1:
                renpy.play(audio.gunshot1, u'sound')
                renpy.say(None, "My attacker opens up on me, but they're too slow and their aim sucks. Now I'm in a better position.")
            else:
                renpy.play(audio.bulletimpacts, u'sound')
                renpy.say(me, "Ughn...")
                renpy.say(None, "Fuck! I'm out of position and taking hits!")

        def bmsgClose(self, marg, pc, opp, mcrit = False, bfail = False):
            usegun = pc.hasItemOfType(IT_FIREARM)
            oppweapon = opp.damage > 0

            if marg > 0 and usegun and mcrit:
                renpy.say(beast, "Yes! Blow them apart!")
            elif marg > 0 and mcrit:
                renpy.say(beast, "Yes! Tear them apart! Beat them into the ground!")
            elif marg > 0 and usegun:
                renpy.say(None, "I land a solid shot, center mass. That should slow them down.")
            elif marg > 0:
                renpy.say(None, "I close with the enemy, surprising them with my speed.")
            elif marg == 0 and usegun:
                renpy.say(None, "I can't get a good shot. I wing them once, then it's too late. They're in my face.")
            elif marg == 0:
                renpy.say(None, "We clash and it's a draw.")
            elif marg < 0 and oppweapon:
                renpy.say(None, "They're on me in an instant. I barely avoid being run through!")
            elif marg < 0 and usegun and bfail:
                renpy.say(me, "Ahhh!")
                renpy.say(beast, "What the fuck are you doing?! I thought you knew how to shoot!")
            elif marg < 0 and bfail:
                renpy.say(me, "Hurk...")
                renpy.say(beast, "What are you doing?! Fight back!")
            else:
                renpy.say(None, "...Well that wasn't a great start.")

        def bmsgPsychicAttack(self, marg, goal, mcrit = False, bfail = False):
            if marg > 0 and mcrit:
                renpy.say(beast, "Yes... Break their will. Break their mind.")

            if marg > 0 and goal == GOAL_MENTAL_ATTACK:
                renpy.say(None, "They're out of it. I've almost got them.")
            elif marg > 0 and goal == GOAL_DISARM:
                renpy.say(None, "And there goes the weapon. That should make this easier.")
            elif marg > 0 and goal == GOAL_SCARE:
                renpy.say(None, "That's right, run you little bitch-ass...")
            else:
                renpy.say(None, "Hmm... no effect.")

        def bethWinsBattle(self, kill = False):
            if kill:
                renpy.say(me, "Shame it had to end up like this, but you asked for it.")
            else:
                renpy.say(me, "...I guess that means I win?")
            self.endBattle()

        def bethEscapes(self):
            renpy.say(me, "Christ that was close!")
            self.endBattle()


label battles:

    label .battleLoop:

        python:
            global opp
            global arena
            nextEvent = None
            hpbar = pc.getTrackerDamage(KEY_HP)
            totalhp = hpbar[KEY_TOTAL]
            clearhp = totalhp - (hpbar[KEY_AGGD] + hpbar[KEY_SPFD])

            roundCount = " Round: {}".format(str(arena.getNumRounds())) if DEBUG else ""

            if clearhp < 1 and hpbar[KEY_AGGD] > 2:
                status = "I don't feel so good... This might be it...{}".format(roundCount)
            elif clearhp < 2:
                status = "I'm taking a beating. If I can't mend, I may need to run for it.{}".format(roundCount)
            elif hpbar[KEY_SPFD] > float(totalhp) / 2:
                status = "...Ouch.{}".format(roundCount)
            else:
                status = "Doing alright so far. Gotta keep my wits about me.{}".format(roundCount)

            if opp.isDead():
                fleeMessage = "Uh... I think we got them."
            elif not opp.isAwake():
                fleeMessage = "They won't be up for a while."
            elif opp.isFleeing():
                fleeMessage = "Better just let them go..."
            elif not opp.canBeFled():
                fleeMessage = "...I can't run away from this one."
            else:
                fleeMessage = "This was a mistake... time to run!"

            if opp.isVampire():
                feedAttackMsg = "Feeding in combat is risky as fuck. But I'm hungry enough not to care. "
            else:
                feedAttackMsg = "If they're gonna run, that makes them acceptable prey... "
        menu:
            "[status]"

            # Brawl attack
            "And me, without a weapon. Guess I'll have to throw hands." if not pc.hasItemOfType(IT_WEAPON):
                python:
                    pc.setDamageBonus(0)
                    nextEvent = opp._attack(arena.getBonus())

                jump battles.processEvent

            # Melee weapon attack
            "I try to get in close and fuck them up!" if pc.hasItemOfType(IT_WEAPON):
                python:
                    damageBonus = 0
                    weapons = pc.getHeldItemsOfType(IT_WEAPON)
                    for weapon in weapons:
                        if weapon[DAMAGE_BONUS] > damageBonus:
                            damageBonus = weapon[DAMAGE_BONUS]

                    pc.setDamageBonus(damageBonus)
                    nextEvent = opp._attack(arena.getBonus())

                jump battles.processEvent

            # Firearms attack
            "I take aim and let off with my gun!" if pc.hasItemOfType(IT_FIREARM):
                python:
                    damageBonus = 0
                    if pc.hasItemOfType(IT_FIREARM):
                        weapons = pc.getHeldItemsOfType(IT_FIREARM)
                        for weapon in weapons:
                            if weapon[DAMAGE_BONUS] > damageBonus:
                                damageBonus = weapon[DAMAGE_BONUS]

                        pc.setDamageBonus(damageBonus)
                    opp.gunfight()
                    nextEvent = opp._attack(arena.getBonus())

                play sound audio.gunshot1
                jump battles.processEvent

            # Mental attack - disarm
            "I catch their gaze and command them to throw down their weapons!" if (arena.hasCompel() or arena.hasMesmerize()) and pc.getHunger() < HUNGER_MAX and not opp.isDisarmed() and opp.isAwake():
                python:
                    compel = pc.getAttr(_cha) + pc.getDisciplineLevel(_dominate)
                    mesmerize = pc.getAttr(_man) + pc.getDisciplineLevel(_dominate)
                    if arena.hasCompel() and (not arena.hasMesmerize() or compel > mesmerize or pc.getHunger() > 3): # try to prioritize compel
                        renpy.play(audio.dominate1, u'sound')
                        nextEvent = opp._mindWarp(GOAL_DISARM, _cha, _dominate, arena.getBonus())
                        pc.addHungerDebt(1)
                    else:
                        renpy.play(audio.dominate1, u'sound')
                        nextEvent = opp._mindWarp(GOAL_DISARM, _man, _dominate, arena.getBonus())
                        pc.addHungerDebt(4)

                jump battles.processEvent

            # Mental attack - drive off
            "I crush their will and compel them to flee!" if (arena.hasMesmerize() or arena.hasDreadGaze()) and pc.getHunger() < HUNGER_MAX and not opp.isFleeing() and opp.isAwake():
                python:
                    mesmerize = pc.getAttr(_man) + pc.getDisciplineLevel(_dominate)
                    dreadgaze = pc.getAttr(_cha) + pc.getDisciplineLevel(_presence)
                    if arena.hasDreadGaze() and dreadgaze > mesmerize:
                        renpy.play(audio.dreadgaze, u'sound')
                        nextEvent = opp._mindWarp(GOAL_SCARE, _cha, _presence, arena.getBonus())
                    else:
                        renpy.play(audio.dominate1, u'sound')
                        nextEvent = opp._mindWarp(GOAL_SCARE, _man, _dominate, arena.getBonus())
                    pc.addHungerDebt(4)

                jump battles.processEvent

            # Toughness (grants armor)
            "I flush Blood throughout my body and harden my flesh against blade and bullet alike." if arena.hasToughness() and pc.getHunger() < HUNGER_MAX and not usingToughness:
                python:
                    global usingToughness
                    usingToughness = True
                    pc.addHungerDebt(4)
                # play sound ???
                "There we go. I feel much safer."
                jump battles.battleLoop

            # Blood Surge (unavailable on first round)
            "I need more power. I send Blood surging throughout my body in preparation for my next move." if pc.getHunger() < HUNGER_MAX and not arena.hasSurged() and arena.getNumRounds() > 0:
                python:
                    arena.addSurge()
                    pc.addHungerDebt(4)
                play sound audio.heartbeat1
                "Much better. Now I'm ready..."
                jump battles.battleLoop

            # Feed attack (enemy vampire or fleeing enemy human)
            "[feedAttackMsg]I go in for a bite!" if pc.getHunger() > 2 and arena.numBattleFeeds() < MAX_BATTLE_FEEDS and (opp.isVampire() or opp.isFleeing()):
                python:
                    print("\n\nFEED ATTACK ISSUED")
                    pc.setDamageBonus(0)
                    nextEvent = opp._attack(arena.getBonus(), biting = True)

                jump battles.processEvent


            # Mend
            "I quickly mend my wounds!" if pc.getHunger() < HUNGER_MAX and hpbar[KEY_SPFD] > 0:
                python:
                    pc.mend(KEY_HP, KEY_SPFD, pc.getBPMend())
                    pc.addHungerDebt(4)

                play sound audio.mending
                "That's better... but I need to be careful. Can't get too hungry..."
                jump battles.battleLoop

            # Flee
            "[fleeMessage]":
                if not opp.canBeFled():
                    "No. I can't back out of this fight."
                    jump battles.battleLoop

                python:
                    nextEvent = opp._chase(arena.getBonus())

                jump battles.processEvent

        label .processEvent:

            $ arena.processRound(nextEvent)
            jump battles.battleLoop


        label .leaveBattle:

        return
