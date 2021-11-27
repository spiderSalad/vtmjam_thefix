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
            self.damageBonus = 0

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
            self.trackers[KEY_HP] = {KEY_TOTAL: self.scores[KEY_ATTR][_sta] + 3, KEY_SPFD: 0, KEY_AGGD: 0, KEY_ARMOR: 0}
            self.trackers[KEY_WP] = {KEY_TOTAL: self.scores[KEY_ATTR][_com] + self.scores[KEY_ATTR][_res], KEY_SPFD: 0, KEY_AGGD: 0, KEY_BONUS: 0, KEY_ARMOR: 0}
            self.canHealAggHPDamage = True

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
            self.setUnswayableMindLevel()
            self.setToughnessLevel()
            self.setBloodPotencyValues()

            self.merits = startMerits
            self.backgrounds = startBackgrounds
            self.inventory = inventory

        def getScore(self, stype, name):
            return self.scores[stype][name]

        def getScoreNoKey(self, name):
            n = str(name)
            if self.scores[KEY_ATTR].has_key(n):
                return self.getAttr(n)
            elif self.scores[KEY_SKILL].has_key(n):
                return self.getSkill(n)
            elif self.powers[KEY_DISCIPLINE].has_key(n):
                return self.getDisciplineLevel(n)
            elif bgTable.has_key(name):
                return self.hasPerk(n)
            else:
                raise ValueError("[Error]: Cannot find score for ", n)

        def getAttr(self, name):
            return self.getScore(KEY_ATTR, name)

        def getSkill(self, name):
            return self.getScore(KEY_SKILL, name)

        def _nudgeScores(self, neg, stype, names):
            for name in names:
                self.scores[stype][name] = increment(self.scores[stype][name])[0] if not neg else decrement(self.scores[stype][name])[0]
            self.onScoresUpdated(stype)

        def incScores(self, stype, *scorenames):
            self._nudgeScores(False, stype, scorenames)

        def decScores(self, stype, *scorenames):
            self._nudgeScores(True, stype, scorenames)

        def onScoresUpdated(self, stype):
            if stype == KEY_ATTR:
                self.trackers[KEY_HP][KEY_TOTAL] = self.scores[KEY_ATTR][_sta] + 3
                self.trackers[KEY_WP][KEY_TOTAL] = self.scores[KEY_ATTR][_com] + self.scores[KEY_ATTR][_res]
            elif stype == KEY_SKILL:
                pass
            if DEBUG : log("--[NOTE]: player scores have been updated.", self.scores)

        def getTrackerDamage(self, type):
            tracker = self.trackers[type]
            return {"type": type, KEY_TOTAL: tracker[KEY_TOTAL], KEY_SPFD: tracker[KEY_SPFD], KEY_AGGD: tracker[KEY_AGGD]}

        def setResilienceLevel(self):
            hasResilience = True if FORT_HP in self.powers[KEY_DISCIPLINE][_fortitude][KEY_DPOWERS] else False
            fortitudeLevel = self.getDisciplineLevel(_fortitude)
            self.trackers[KEY_HP][KEY_BONUS] = fortitudeLevel if hasResilience else 0

        def setUnswayableMindLevel(self):
            hasUM = True if FORT_STUBBORN in self.powers[KEY_DISCIPLINE][_fortitude][KEY_DPOWERS] else False
            fortitudeLevel = self.getDisciplineLevel(_fortitude)
            self.trackers[KEY_WP][KEY_ARMOR] = fortitudeLevel if hasUM else 0

        def setToughnessLevel(self):
            hasToughness = True if FORT_TOUGH in self.powers[KEY_DISCIPLINE][_fortitude][KEY_DPOWERS] else False
            fortitudeLevel = self.getDisciplineLevel(_fortitude)
            self.trackers[KEY_HP][KEY_ARMOR] = fortitudeLevel if hasToughness else 0

        def getBPDisciplineBonus(self):
            return self.powerBonus

        def getBPMend(self):
            return self.spfMending

        def getBPSurge(self):
            return self.surgeBonus

        def setBloodPotencyValues(self):
            global bpTable
            self.surgeBonus = bpTable[self.bloodpotency - 1]["surge"]
            self.powerBonus = bpTable[self.bloodpotency - 1]["discipline_bonus"]
            self.spfMending = bpTable[self.bloodpotency - 1]["superficial_mend"]

        def getDamageBonus(self):
            return self.damageBonus

        def setDamageBonus(self, val):
            self.damageBonus = val

        def getPredatorTypePower(self):
            return self.ptp

        def setPredatorTypePower(self, discipline, power, _label = None):
            self.ptp = {"discipline": discipline, "power": power, "label": _label}

        def getDisciplinePowerAtRank(self, discipline, level): # may be None
            rank = scoreWords[level]
            return self.powers[KEY_DISCIPLINE][discipline][KEY_DPOWERS][rank]

        def countPowersInDiscipline(self, discipline):
            numPowers = 0
            dpowers = self.powers[KEY_DISCIPLINE][discipline][KEY_DPOWERS]

            for i in range(5):
                if dpowers[scoreWords[i + 1]]:
                    numPowers += 1

            return numPowers

        def hasDisciplinePower(self, discipline, power):
            try:
                discPowers = self.powers[KEY_DISCIPLINE][discipline][KEY_DPOWERS]
            except:
                log("[Error]: Unknown error occured when attempting to check for a discipline power.")

            hasPower = False
            for i in range(5):
                scoreWord = scoreWords[i + 1]
                if discPowers[scoreWord] == power:
                    hasPower = True

            log("[Status]: Checking if we have the {disc} power of {pow}... {dowe}".format(disc=discipline, pow=power, dowe=("Yes!" if hasPower else "Nope.")))
            return hasPower

        def addDisciplinePower(self, discipline, power):
            disclevel = self.getDisciplineLevel(discipline)
            powerlevel = 0
            for count, levelset in enumerate(powerlist[discipline]):
                if power in levelset:
                    powerlevel = count + 1
                    break

            if powerlevel < 1:
                raise ValueError("[Error]: Power \"{pow}\" doesn't exist/belong in discipline \"{disc}\".".format(pow=power, disc=discipline))
            elif powerlevel > disclevel:
                raise ValueError("[Error]: Power \"{pow}\" requires \"{disc}\" level {dlevel}.".format(pow=power, disc=discipline, dlevel=powerlevel))
            elif self.countPowersInDiscipline(discipline) >= disclevel:
                raise ValueError("[Error]: You already have as many chosen powers as dots in discipline {}.".format(discipline))

            try:
                for i in range(powerlevel, disclevel + 1):
                    powerInThatSlot = self.powers[KEY_DISCIPLINE][discipline][KEY_DPOWERS][scoreWords[i]]
                    if not powerInThatSlot:
                        self.powers[KEY_DISCIPLINE][discipline][KEY_DPOWERS][scoreWords[i]] = power
                        return True
                return False
            except:
                log("[Error]: Unknown error occurred when attempting to add discipline power!")
            finally:
                return False

        def getDisciplineLevel(self, discipline):
            return self.powers[KEY_DISCIPLINE][discipline][KEY_LEVEL]

        def setDisciplineLevel(self, discipline, newlevel):
            self.powers[KEY_DISCIPLINE][discipline][KEY_LEVEL] = newlevel

        def addDisciplineDot(self, discipline, choosePower = False):
            disclevel = self.getDisciplineLevel(discipline)
            self.setDisciplineLevel(discipline, increment(disclevel)[0])

        def hasPerk(self, typeName): # should now return KEY_BGSCORE, 0 if not found
            if len(self.merits) < 1 and len(self.backgrounds) < 1:
                return (0, None, None, False)

            if len(self.backgrounds) > 0:
                for count, bg in enumerate(self.backgrounds):
                    if typeName.lower() == bg[KEY_BGTYPE]:
                        return (bg[KEY_BGSCORE], ISSA_BG, count, bg[ISSA_FLAW])

            if len(self.merits) > 0:
                for count, merit in enumerate(self.merits):
                    if typeName.lower() == merit[KEY_BGTYPE]:
                        return (merit[KEY_BGSCORE], ISSA_MERIT, count, merit[ISSA_FLAW])

            return (0, None, None, False)

        def removePerk(self, typeName):
            hasit = self.hasPerk(typeName) # TODO: Check if this still works, hasit[0] should still evaluate to False
            if hasit[0] and hasit[1] == ISSA_BG:
                del self.backgrounds[hasit[2]]
            elif hasit[0] and hasit[1] == ISSA_MERIT:
                del self.merits[hasit[2]]
            else:
                log("[Status]: Tried to remove a merit/background BUT we couldn't find it.")
                return False

            log("[Status]: Removed merit/background of type {}".format(typeName))
            return True

        def addPerk(self, typeName, level, merit = False, flaw = False, customToolTip = None):
            self.removePerk(typeName)
            found = False
            table = bgTable if not merit else meritTable

            for perk in table[typeName]:
                if perk[KEY_BGSCORE] == int(level) and (merit or perk[ISSA_FLAW] == flaw): # merits are never flaws
                    if customToolTip:
                        perk[KEY_TOOLTIP] = "{}".format(customToolTip)
                    if not merit:
                        self.backgrounds.append(perk)
                    else:
                        self.merits.append(perk)
                    found = True

            if not found:
                raise ValueError("[Error]: An attempt was made to add a background/flaw that couldn't be found in the table.")

        def getPredatorType(self):
            return self.predatorType

        def setPredatorType(self, pt):
            self.predatorType = pt

        def updateWallet(self, amount, deduct = False):
            if self.inventory[0][KEY_NAME] != "cash":
                raise ValueError("[Error]: Cash should always be at index 0 in inventory!")

            cash = self.inventory[0][KEY_VALUE]
            mult = 1 if not deduct else -1
            try:
                self.inventory[0][KEY_VALUE] = max(cash + (float(mult) * (amount or 0.0)), 0.0) # Can't go below broke
            except TypeError:
                log("[Error]: Someone tried to add something other than a number to the wallet!")

        def getHeldItemsOfType(self, itype):
            if not hasItemOfType():
                return []

            bag = []
            for item in inventory:
                iname = item[KEY_NAME]
                if itemTable[iname][KEY_ITEMTYPE] == itype:
                    bag.append(itemTable[iname])

            return bag

        def hasItemOfType(self, itype):
            for item in self.inventory:
                iname = item[KEY_NAME]
                if itemTable[iname][KEY_ITEMTYPE] == itype:
                    return True
            return False

        def removeFromInventory(self, itemName, payloadValue = None, checkAll = False):
            if str(itemName).lower() == "cash":
                self.updateWallet(payloadValue, deduct = True)
                return

            hasAlready = False
            for item in self.inventory:
                if item[KEY_NAME] == itemName:
                    hasAlready = True
                    self.inventory.remove(item)
                    if not checkAll:
                        break
            if not hasAlready:
                log("[Error]: Tried to remove item with name " + str(itemName) + ", but it wasn't found.")
                return
            renpy.sound.queue(audio.heartbeat2, u'sound')

        def loseCash(self, amount):
            self.updateWallet(amount, deduct = True)

        def gainCash(self, amount):
            self.updateWallet(amount, deduct = False)

        def addToInventory(self, itemName, payloadValue = None, customToolTip = None):
            if str(itemName).lower() == "cash":
                self.updateWallet(payloadValue)
                return

            hasAlready = False
            existingSet = None
            for item in self.inventory:
                if item[KEY_NAME] == itemName:
                    hasAlready = True
                    existingSet = item
                    break

            if not hasAlready: # Maybe later I'll add some logic to affect listed order NOTE: no i won't
                newItem = {KEY_NAME: itemName}
                if payloadValue:
                    newItem[KEY_VALUE] = payloadValue
                if customToolTip:
                    newItem[KEY_TOOLTIP] = customToolTip
                self.inventory.append(newItem)
            else:
                try:
                    existingSet[KEY_VALUE] += int(payloadValue)
                except TypeError:
                    log("[Error]: An invalid item adding operation was caught.")
                    return
            renpy.sound.queue(audio.heartbeat2, u'sound')

        def damage(self, which, dtype, amount):
            swkey = str(which)
            totalBoxes = self.trackers[swkey][KEY_TOTAL] + self.trackers[swkey][KEY_BONUS]
            armor = self.trackers[swkey][KEY_ARMOR]
            dented = False
            injured = False
            trueAmount = amount
            if dtype == KEY_SPFD: # NOTE: Superficial damage is halved before the loop
                trueAmount = math.ceil(float(amount) / 2)

            for point in range(int(amount)):
                if armor > 0:
                    dented = True
                    armor -= 1
                    continue

                clearBoxes = totalBoxes - (self.trackers[swkey][KEY_SPFD] + self.trackers[swkey][KEY_AGGD])
                if clearBoxes > 0: # clear spaces get filled first
                    self.handleImpairment(False, swkey)
                    self.trackers[swkey][str(dtype)] += 1
                    log("====> damage " + str(point) + ": filling a clear space")
                elif self.trackers[swkey][KEY_SPFD] > 0: # if there are no clear boxes, tracker is filled with a mix of aggravated and superficial damage
                    self.handleImpairment(True, swkey)
                    self.trackers[swkey][KEY_SPFD] -= 1
                    self.trackers[swkey][KEY_AGGD] += 1 # if there's any superficial damage left, turn it into an aggravated
                    log("====> damage " + str(point) + ": removing a superficial and replacing with aggravated")

                if self.trackers[swkey][KEY_AGGD] >= totalBoxes:
                    self.handleDemise(swkey) # a tracker completely filled with aggravated damage = game over: torpor, death, or a total loss of faculties, face and status
                    log("====> damage " + str(point) + ": oh shit you dead")

                injured = True
            if dented and not injured:
                #renpy.sound.queue(audio, u'sound')
                pass
            elif injured:
                renpy.sound.queue(audio.stab2, u'sound')

        def mend(self, which, dtype, amount):
            swkey = str(which)
            damage = self.trackers[swkey][dtype]
            self.trackers[swkey][dtype] = max(damage - amount, 0)

        def canAggHPHeal(self):
            return self.canHealAggHPDamage

        def toggleAggHPHealing(self, allow = False):
            self.canHealAggHPDamage = allow

        def handleImpairment(self, fulltracker, whichtracker):
            keywrd1 = "physically" if whichtracker == KEY_HP else "mentally"
            keywrd2 = "physical" if whichtracker == KEY_HP else "mental and social"

            if self.impaired[whichtracker] and not fulltracker:
                self.impaired[whichtracker] = False
                log("\n[STATUS]: You are no longer {w1} impaired.\n".format(w1=keywrd1))
            elif fulltracker and not self.impaired[whichtracker]:
                self.impaired[whichtracker] = True
                log("\n[STATUS]: You are now {w1} impaired and suffer a penalty to {w2} tests.\n".format(w1=keywrd1, w2=keywrd2))
            # else:
            #     raise ValueError("[Error]: Must specify health or willpower tracker.")

        def handleDemise(self, which):
            # if which == KEY_HP:
            # You have either met the Final Death, or you've fallen into torpor and will probably die soon. Either way, you're done.")
            # elif which == KEY_WP:
            # Your spirit is broken, and you've lost so much face that your only option is to flee before you're destroyed. You've failed.")
            renpy.jump("gameover." + which)

        def setStateOfUndeath(self, which, change, currentval, floor, ceiling, _sound = None, playSound = False, queueSound = False):
            cstr = str(change)
            cint = int(cstr.replace("=", ""))
            retval = None

            if "+" in cstr and "-" in cstr:
                raise ValueError("[Error]: Attempt to add and subtract at once?")
            elif "+=" in cstr:
                retval = min(currentval + cint, ceiling)
                if playSound:
                    renpy.play(_sound, u'sound')
                elif queueSound:
                    renpy.sound.queue(_sound, u'sound')
            elif "-=" in cstr:
                retval = max(currentval - abs(cint), floor)
            elif not hasInt(cstr):
                raise TypeError("[Error]: Can't set {} to non-integer value.".format(which))
            else:
                if playSound and (which == "humanity" or (which == "hunger" and cint > currentval)):
                    renpy.play(_sound, u'sound')
                elif queueSound and (which == "humanity" or (which == "hunger" and cint > currentval)):
                    renpy.sound.queue(_sound, u'sound')
                retval = min(max(cint, floor), ceiling)

            return retval

        def getHumanity(self):
            return self.humanity

        def setHumanity(self, change, reason, playSound = True, queueSound = True):
            currenthumanity = self.humanity
            self.humanity = self.setStateOfUndeath("humanity", change, self.humanity, HUMANITY_MIN, HUMANITY_MAX)

            if self.humanity < HUMANITY_MIN:
                handleBeastEaten()
            elif self.humanity < currenthumanity:
                handleDegeneration()
            elif self.humanity > HUMANITY_MAX and self.humanity > currenthumanity:
                handleSainthood() # This shouldn't ever fire.

        def handleBeastEaten():
            log("")

        def handleDegeneration():
            log("")

        def handleSainthood():
            log("")

        def getHunger(self):
            return self.hunger

        def setHunger(self, change, killed = False, innocent = False, playSound = True, queueSound = True):
            hungerfloor = HUNGER_MIN_LIVE if not killed else HUNGER_MIN_DEAD

            self.hunger = self.setStateOfUndeath("hunger", change, self.hunger, hungerfloor, HUNGER_MAX, audio.beastgrowl1, playSound, queueSound)

            if self.hunger >= HUNGER_MAX_CALM:
                renpy.show_screen(_screen_name = "hungerlay", _layer = "hunger_layer", _tag = "hungerlay", _transient = False)
            else:
                renpy.hide_screen("hungerlay", "master")

            if killed and innocent:
                handleMurder()

        def slakeHunger(self, change, killed = False, playSound = True, queueSound = True):
            self.setHunger("-=" + str(abs(change)), killed = killed, playSound = playSound, queueSound = queueSound)

        def raiseHunger(self, change, playSound = True, queueSound = True):
            self.setHunger("+=" + str(abs(change)), playSound = playSound, queueSound = queueSound)

        def handleMurder(self, *args):
            log("\n[STATUS]: You murderer!\n") # TODO: More here, once humanity implemented

        def addHungerDebt(self, vitae):
            log("\nHUNGER DEBT [STATUS]: adding {vl} to current {hd}".format(vl = vitae, hd = self.hungerDebt))
            if self.hungerDebt + vitae < HUNGER_DEBT_MAX:
                self.hungerDebt = self.hungerDebt + vitae
            else:
                debtpaid = HUNGER_DEBT_MAX - self.hungerDebt # how much of added debt was paid? rest is rolled over
                self.hungerDebt = 0
                self.raiseHunger(1, playSound = False)
                log("\nHUNGER DEBT [STATUS]: hunger INCREASED to {}!".format(self.hunger))
                self.addHungerDebt(vitae - debtpaid)

        def soundFeed(self, lineBetween = None):
            renpy.play(audio.bite1, u'sound')
            if lineBetween:
                renpy.say(None, str(lineBetween))
            renpy.sound.queue(audio.drinking1, u'sound')

        def soundFlee(self):
            renpy.play(audio.heels_running, u'sound')
            renpy.sound.queue(audio.carstart_pc, u'sound')

        def cloudMemory(self):
            self.addHungerDebt(1)

        def awe(self):
            self.addHungerDebt(1)

        def entrance(self):
            self.addHungerDebt(4)

        def awaken(self):
            global justWokeUp
            justWokeUp = True

            self.toggleAggHPHealing(True)
            self.addHungerDebt(4)
            herd = self.hasPerk(M_HERD[KEY_NAME])
            herdlevel = herd[0]

            if opinion_camarilla >= cam_rep_rank2 and herdlevel < 2:
                self.addPerk(M_HERD[KEY_NAME], 2,
                    customToolTip = "Looks like I've impressed the Camarilla enough that they're giving me additional hunting \"privileges\". How nice of them.")

            if opinion_camarilla >= cam_rep_rank1:
                self.gainCash(300)

        def getWillPenalty(self):
            return max(self.hunger - (self.humanity - 6), 0)

        def test(self, diff, *names, **kwargs): # messyCritsOn = False, bestialFailsOn = True, goal = None):
            pool = 0
            mcrit = False
            bfail = False

            for name in names:
                if not isNumber(name):
                    pool += self.getScoreNoKey(name)
                else:
                    pool += int(math.floor(name))

            marg = pool - diff
            mCritsOn = False
            bFailsOn = True
            goal = None

            for k, val in kwargs.iteritems():
                if k == "messyCritsOn":
                    mCritsOn = val
                elif k == "bestialFailsOn":
                    bFailsOn = val
                elif k == "goal":
                    goal = val

            if mCritsOn:
                mcrit = marg >= 0 and marg >= (5 - int(self.hunger))
            if bFailsOn:
                bfail = marg < 0 and abs(marg) >= (5 - int(self.hunger))

            return (marg, mcrit, bfail, goal)

        def basictest(self, diff, *scores):
            return self.test(diff, scores, messyCritsOn = False, bestialFailsOn = False)


    def hasInt(val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    def isNumber(val):
        try:
            float(val)
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

    def evalt(result, bestialFailsOn = True, messyCritsOn = True):
        if not hasInt(result[0]):
            raise TypeError("[Error]: Something wrong with this result tuple: ", result)

        if result[0] < 0:
            if result[2] and bestialFailsOn:
                return BEASTFAIL
            else:
                return FAIL
        elif result[0] >= 0:
            if result[1]:
                return MESSYCRIT
            else:
                return SUCCESS
        else:
            raise ValueError("[Error]: This shouldn't have happened during an test result evaluation.")

    def getItemProperty(item, ikey):
        if not item or not item[KEY_NAME]:
            raise TypeError("[Error]: Invalid inventory item or item name?")

        name = item[KEY_NAME]
        itemDetails = itemTable[name]

        if item.has_key(ikey):
            return item[ikey]
        elif itemDetails.has_key(ikey):
            return itemDetails[ikey]

        return None

    def getOpinion(factionKey):
        global opinions
        return opinions[factionKey]

    def setOpinion(factionKey, newval, operation = "set"):
        global opinions
        prevOpinion = getOpinion(factionKey)
        if operation == "set":
            newOpinion = newval
        elif operation == "add" or operation == "+":
            newOpinion = min(max(prevOpinion + newval, REP_MIN), REP_MAX)
        elif operation == "subtract" or operation == "-":
            newOpinion = min(max(prevOpinion - newval, REP_MIN), REP_MAX)
        else:
            raise ValueError("[Error]: That's an invalid setOpinion operation.")

        opinions[factionKey] = newOpinion

    def advanceCalendar(cpc = None):
        global night, timetonight
        night += 1
        timetonight = 1.0
        if cpc:
            cpc.awaken()
        renpy.jump("nightloop")

    def updateTime(elapsed, cpc = None):
        global timetonight
        timetonight -= float(elapsed)
        if timetonight <= 0:
            advanceCalendar(cpc)

    def getCreditsJSON():
        global creditsFile
        global creditsJSON
        creditsFile = renpy.file(creditsFileName)
        creditsJSON = json.load(creditsFile)

    def sortCredits(credits_json):
        sortedCredits = {}

        for credit in credits_json:
            ctype = credit["type"]
            if ctype and not sortedCredits.has_key(ctype):
                sortedCredits[ctype] = []
            elif ctype:
                sortedCredits[ctype].append(credit)

        return sortedCredits


    def log(*args):
        print(args)

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
