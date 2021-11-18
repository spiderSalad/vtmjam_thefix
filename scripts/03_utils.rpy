init 1 python:
    class Artist:
        def __init__(self, name = "Unnamed Artist", infoText = "", *works):
            self.name = name
            self.infoText = infoText
            self.works = list(*works)

    class PlayerCharacter:
        def __init__(self, fname = _pc["first"], lname = _pc["last"]):
            self.fname = fname
            self.lname = lname
            self.hunger = HUNGER_MIN_LIVE
            self.hungerDebt = 0
            self.humanity = HUMANITY_START
            self.generation = 11
            self.bloodpotency = bloodpotency

            self.scores = {}
            self.scores[KEY_ATTR] = {
                _str: STR, _dex: DEX, _sta: STA, _cha: CHA,
                _man: MAN, _com: COM, _int: INT, _wit: WIT, _res: RES
            }
            self.scores[KEY_SKILL] = {
                _athl: Athl, _clan: Clan, _comb: Comb, _driv: Driv, _fire: Fire, # physical
                _inti: Inti, _intr: Intr, _perf: Perf, _pers: Pers, _stre: Stre, # social
                _acad: Acad, _awar: Awar, _inve: Inve, _occu: Occu, _tech: Tech  # mental
            }

            self.trackers = {}
            self.trackers[KEY_HP] = { KEY_TOTAL: self.scores[KEY_ATTR][_sta] + 3, KEY_SPFD: 0, KEY_AGGD: 0}
            self.trackers[KEY_WP] = { KEY_TOTAL: self.scores[KEY_ATTR][_com] + self.scores[KEY_ATTR][_res], KEY_SPFD: 0, KEY_AGGD: 0 }

            self.impaired = {}
            self.impaired[KEY_HP] = False
            self.impaired[KEY_WP] = False

            self.powers = {}
            self.powers[KEY_DISCIPLINE] = {
                _dominate: { KEY_LEVEL: dominate, KEY_DPOWERS: dominatePowers },
                _fortitude: { KEY_LEVEL: fortitude, KEY_DPOWERS: fortitudePowers },
                _presence: { KEY_LEVEL: presence, KEY_DPOWERS: presencePowers }
            }

            self.setResilienceLevel()
            self.merits = startMerits
            self.backgrounds = startBackgrounds
            self.inventory = inventory

        def _nudgeScores(self, neg, stype, names):
            for name in names:
                self.scores[stype][name] = increment(self.scores[stype][name])[0] if not neg else decrement(self.scores[stype][name])[0]
            if DEBUG : printPCScores(self.scores, stype)
            self.onScoresUpdated(stype)

        def incScores(self, stype, *scorenames): #incPCScores
            self._nudgeScores(False, stype, scorenames)

        def decScores(self, stype, *scorenames):
            self._nudgeScores(True, stype, scorenames)

        def onScoresUpdated(self, stype):
            if stype == KEY_ATTR:
                self.trackers[KEY_HP][KEY_TOTAL] = self.scores[KEY_ATTR][_sta] + 3
                self.trackers[KEY_WP][KEY_TOTAL] = self.scores[KEY_ATTR][_com] + self.scores[KEY_ATTR][_res]
            elif stype == KEY_SKILL:
                pass
            updateCharSheetValues(self.scores)
            if DEBUG : print("--[NOTE]: player scores have been updated.", self.scores)

        def setResilienceLevel(self):
            hasResilience = True if FORT_HP in self.powers[KEY_DISCIPLINE][_fortitude][KEY_DPOWERS] else False
            fortitudeLevel = self.powers[KEY_DISCIPLINE][_fortitude][KEY_LEVEL]
            self.trackers[KEY_HP][KEY_BONUS] = fortitudeLevel if hasResilience else 0

        def damage(self, which, dtype, amount):
            swkey = str(which)
            totalBoxes = self.trackers[swkey][KEY_TOTAL] + self.trackers[swkey][KEY_BONUS]

            for point in range(int(amount)):
                clearBoxes = totalBoxes - (self.trackers[swkey][KEY_SPFD] + self.trackers[swkey][KEY_AGGD])
                if clearBoxes > 0: # clear spaces get filled first
                    self.handleImpairment(False, swkey)
                    self.trackers[swkey][str(dtype)] += 1
                    print("====> damage " + str(point) + ": filling a clear space")
                elif self.trackers[swkey][KEY_SPFD] > 0: # if there are no clear boxes, tracker is filled with a mix of aggravated and superficial damage
                    self.handleImpairment(True, swkey)
                    self.trackers[swkey][KEY_SPFD] -= 1
                    self.trackers[swkey][KEY_AGGD] += 1 # if there's any superficial damage left, turn it into an aggravated
                    print("====> damage " + str(point) + ": removing a superficial and replacing with aggravated")
                else:
                    self.handleDemise(swkey) # a tracker completely filled with aggravated damage = game over: torpor, death, or a total loss of faculties, face and status
                    print("====> damage " + str(point) + ": oh shit you dead")

        def handleImpairment(self, fulltracker, whichtracker):
            keywrd1 = "physically" if whichtracker == KEY_HP else "mentally"
            keywrd2 = "physical" if whichtracker == KEY_HP else "mental and social"

            if self.impaired[whichtracker] and not fulltracker:
                self.impaired[whichtracker] = False
                print ("\n[STATUS]: You are no longer {w1} impaired.\n".format(w1=keywrd1))
            elif fulltracker and not self.impaired[whichtracker]:
                self.impaired[whichtracker] = True
                print ("\n[STATUS]: You are now {w1} impaired and suffer a penalty to {w2} tests.\n".format(w1=keywrd1, w2=keywrd2))
            # else:
            #     raise ValueError("[Error]: Must specify health or willpower tracker.")

        def handleDemise(self, which):
            if which == KEY_HP:
                print ("\n[STATUS]: You have either met the Final Death, or you've fallen into torpor and will probably die soon. Either way, you're done.")
            elif which == KEY_WP:
                print ("\n[STATUS]: Your spirit is broken, and you've lost so much face that your only option is to flee before you're destroyed. You've failed.")
            renpy.jump("gameover")

        def setStateOfUndeath(self, which, change, currentval, floor, ceiling, _sound = None, playSound = False, queueSound = False):
            cstr, cint, retval = str(change), int(change), None

            if "+" in cstr and "-" in cstr:
                raise ValueError("[Error]: Attempt to add and subtract at once?")
            elif "+" in cstr:
                retval = min(currentval + cint, ceiling)
                if playSound:
                    renpy.play(_sound, u'sound')
                elif queueSound:
                    renpy.sound.queue(_sound, u'sound')
            elif "-" in cstr:
                retval = max(currentval - cint, floor)
            else:
                if playSound and (which == "humanity" or (which == "hunger" and cint > currentval)):
                    renpy.play(_sound, u'sound')
                elif queueSound and (which == "humanity" or (which == "hunger" and cint > currentval)):
                    renpy.sound.queue(_sound, u'sound')
                retval = min(max(cint, floor), ceiling)

            return retval

        def setHumanity(self, change, reason, playSound = True, queueSound = True):
            if not hasInt(change):
                raise TypeError("[Error]: Can't set humanity to non-integer value.")

            currenthumanity = self.humanity
            self.humanity = self.setStateOfUndead("humanity", change, self.humanity, HUMANITY_MIN, HUMANITY_MAX)

            if self.humanity < HUMANITY_MIN:
                handleBeastEaten()
            elif self.humanity < currenthumanity:
                handleDegeneration()
            elif self.humanity >= HUMANITY_MAX and self.humanity > currenthumanity:
                handleSainthood()

        def handleBeastEaten():
            print("")

        def handleDegeneration():
            print("")

        def handleSainthood():
            print("")

        def setHunger(self, change, killed = False, innocent = False, playSound = True, queueSound = True):
            if not hasInt(change):
                raise TypeError("[Error]: Can't set hunger to non-integer value.")
            cstr, cint = str(change), int(change)
            hungerfloor = HUNGER_MIN_LIVE if not killed else HUNGER_MIN_DEAD

            self.hunger = self.setStateOfUndeath("hunger", change, self.hunger, hungerfloor, HUNGER_MAX, audio.beastgrowl1, playSound, queueSound)

            if self.hunger >= HUNGER_MAX_CALM:
                renpy.show_screen(_screen_name = "hungerlay", _layer = "master", _tag = "hungerlay", _transient = False)
            else:
                renpy.hide_screen("hungerlay", "master")

            if killed and innocent:
                handleMurder()

        def handleMurder(self, *args):
            print("\n[STATUS]: You murderer!\n") # TODO: More here, once humanity implemented

        def addHungerDebt(self, vitae):
            print("\nHUNGER DEBT [STATUS]: adding {vl} to current {hd}".format(vl = vitae, hd = self.hungerDebt))
            if self.hungerDebt + vitae < HUNGER_DEBT_MAX:
                self.hungerDebt = self.hungerDebt + vitae
            else:
                debtpaid = HUNGER_DEBT_MAX - self.hungerDebt # how much of added debt was paid? rest is rolled over
                self.hungerDebt = 0
                self.setHunger("+1", playSound = False)
                print("\nHUNGER DEBT [STATUS]: hunger INCREASED to {}!".format(self.hunger))
                self.addHungerDebt(vitae - debtpaid)

    def hasInt(val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    def _nudge(neg, ints):
        ups = []
        n = 1 if not neg else -1
        for i in ints:
            ups.append(i + n)
        return ups

    def increment(*ints):
        return _nudge(False, ints)

    def decrement(*ints):
        return _nudge(True, ints)

    def printPCScores(pcs, stype):
        attrs = ""
        for name in pcs[KEY_ATTR]:
            attrs += name + ": " + str(pcs[KEY_ATTR][name]) + ", "
        print(attrs)

    def getPCAttributes():
        global pcs
        if DEBUG:
            printPCScores(KEY_ATTR)
        return pcs[KEY_ATTR]

    def getPCSkills():
        global pcs
        if DEBUG:
            printPCScores(KEY_SKILL)
        return pcs[KEY_SKILL]

    def updateCharSheetValues(pcs):
        for name in pcs[KEY_ATTR]:
            print(name, pcs[KEY_ATTR][name])
        print("[NOTE]: Updated character sheet values.")

    def getCreditsText():
        global builtCredits
        global creditsText

        if not builtCredits:
            buildCreditsText()

        return creditsText

    def buildCreditsText():
        global creditsText, builtCredits

        if not bool(musicians):
            BJB = Artist("{a=https://www.benjaminbanger.com/}BenJamin Banger{/a}", "    Instagram: {a=https://www.instagram.com/benjaminbanger}@BenJaminBanger{/a}")
            BJB.works = ["Tom 2.0", "Freestyle 39"]
            musicians.append(BJB)

            KTP = Artist("{a=https://www.benjaminbanger.com/}2Kutup{/a}", "    Instagram: {a=https://www.instagram.com/benjaminbanger}@BenJaminBanger{/a}")
            KTP.works = ["Tom 2.0", "Freestyle 39"]
            musicians.append(KTP)

        ct = ""
        ct += "Artists\n\n"
        for a in artists:
            infoText = a.infoText if bool(a.infoText) else ""
            ct += a.name + "\n\n" + infoText
            for w in a.works:
                ct += "    \"" + w + "\" (" + ccl_url1 + "License" + ccl_url2 + ")\n\n"
        ct += "Musicians:\n\n";
        for m in musicians:
            infoText = m.infoText if bool(m.infoText) else ""
            ct += m.name + "\n\n" + infoText + "\n\n"
            for w in m.works:
                ct += "    \"" + w + "\" (" + ccl_url1 + "License" + ccl_url2 + ")\n\n"
        ct += "\n\n"

        creditsText = ct
        builtCredits = True
