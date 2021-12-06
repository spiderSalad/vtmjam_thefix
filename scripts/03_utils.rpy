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
            self.predatorType = "???"

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
            # self.setToughnessLevel()
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
                return self.hasPerk(n)[0]
            else:
                print ("n = ", n)
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
            hasResilience = self.hasDisciplinePower(_fortitude, FORT_HP)
            fortitudeLevel = self.getDisciplineLevel(_fortitude)
            self.trackers[KEY_HP][KEY_BONUS] = fortitudeLevel if hasResilience else 0

        def setUnswayableMindLevel(self):
            hasUM = self.hasDisciplinePower(_fortitude, FORT_STUBBORN)
            fortitudeLevel = self.getDisciplineLevel(_fortitude)
            self.trackers[KEY_WP][KEY_ARMOR] = fortitudeLevel if hasUM else 0

        def setToughnessLevel(self):
            hasToughness = self.hasDisciplinePower(_fortitude, FORT_TOUGH)
            fortitudeLevel = self.getDisciplineLevel(_fortitude)
            self.trackers[KEY_HP][KEY_ARMOR] = fortitudeLevel if hasToughness else 0

        def setHerdLevel(self):
            herdlevel = 0
            ctt = ""

            if opinion_camarilla >= cam_rep_rank2:
                herdlevel += 1
                ctt = "Looks like I've impressed the Camarilla enough that they're giving me additional hunting \"privileges\". How nice of them."

            if self.getPredatorType() == PT_ROADSIDE_KILLER:
                herdlevel += 1
                ctt = "In every city there are places you can go to find people just passing through. The only problem is they're usually claimed, but that's not a problem for me here."

            if PRES_ADDICTED2U in self.powers[KEY_DISCIPLINE][_presence][KEY_DPOWERS]:
                herdlevel += 1
                ctt = "My milkshake brings all the boys to the yard. Girls too. People of any gender, really."

            if ctt:
                pc.addPerk(M_HERD[KEY_NAME], herdlevel, customToolTip = ctt)

        def getBPDisciplineBonus(self):
            return self.powerBonus

        def getBPMend(self):
            return self.spfMending

        def getBPSurge(self):
            return self.surgeBonus

        def useBloodSurge(self, freeSurges = 0): # NOTE: will ALWAYS attempt to surge, only fails if at hunger 5
            global freeBloodSurges
            if freeSurges > 0:
                renpy.play(audio.heartbeat1, u'sound')
                freeBloodSurges -= 1
                print ("useBloodSurge() --> FREE returning ", self.getBPSurge())
                return self.getBPSurge()
            elif self.hunger < HUNGER_MAX:
                renpy.play(audio.heartbeat1, u'sound')
                self.addHungerDebt(4)
                print ("useBloodSurge() --> paid returning ", self.getBPSurge())
                return self.getBPSurge()
            else:
                return 0

        def maybeBloodSurge(self):
            if usingBloodSurge or freeBloodSurges > 0:
                print ("maybeBloodSurge() --> returning useBloodSurge()")
                return self.useBloodSurge(freeBloodSurges)
            else:
                print ("maybeBloodSurge() --> returning zero")
                return 0

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

        def checkPowers(self):
            self.setResilienceLevel()
            self.setUnswayableMindLevel()
            self.setHerdLevel()

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
                    # print("\n\npowerInThatSlot", powerInThatSlot, scoreWords, i)
                    if not powerInThatSlot:
                        self.powers[KEY_DISCIPLINE][discipline][KEY_DPOWERS][scoreWords[i]] = power
                        print("\n\npowers:: ", scoreWords[i], self.powers[KEY_DISCIPLINE][discipline][KEY_DPOWERS])
                        self.checkPowers()
                        return True
                self.checkPowers()
                return False
            except:
                log("[Error]: Unknown error occurred when attempting to add discipline power!")
                return False

        def getDisciplineLevel(self, discipline):
            return self.powers[KEY_DISCIPLINE][discipline][KEY_LEVEL]

        def setDisciplineLevel(self, discipline, newlevel):
            self.powers[KEY_DISCIPLINE][discipline][KEY_LEVEL] = newlevel

        def addDisciplineDot(self, discipline, choosePower = False):
            disclevel = self.getDisciplineLevel(discipline)
            self.setDisciplineLevel(discipline, increment(disclevel)[0])
            self.setResilienceLevel()
            self.setUnswayableMindLevel()
            self.setHerdLevel()

        def hasPerk(self, typeName): # should now return KEY_BGSCORE, 0 if not found
            if len(self.merits) < 1 and len(self.backgrounds) < 1:
                return (0, None, None, False)

            if len(self.backgrounds) > 0:
                for count, bg in enumerate(self.backgrounds):
                    if typeName.lower() == bg[KEY_BGTYPE].lower():
                        print("returnm", (bg[KEY_BGSCORE], ISSA_BG, count, bg[ISSA_FLAW]))
                        return (bg[KEY_BGSCORE], ISSA_BG, count, bg[ISSA_FLAW])

            if len(self.merits) > 0:
                for count, merit in enumerate(self.merits):
                    if typeName.lower() == merit[KEY_BGTYPE].lower():
                        print("return", (merit[KEY_BGSCORE], ISSA_MERIT, count, merit[ISSA_FLAW]))
                        return (merit[KEY_BGSCORE], ISSA_MERIT, count, merit[ISSA_FLAW])

            print("return baseline")
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
            if not self.hasItemOfType(itype):
                return []

            bag = []
            for item in inventory:
                iname = item[KEY_NAME]
                if itemTable[iname][KEY_ITEMTYPE] == itype:
                    bag.append(itemTable[iname])

            return bag

        def hasItem(self, itemName):
            for item in self.inventory:
                if item[KEY_NAME] == itemName:
                    return item
            return None

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

            existingCopy = self.hasItem(itemName)
            while existingCopy:
                self.inventory.remove(existingCopy)
                existingCopy = self.hasItem(itemName)

            renpy.sound.queue(audio.heartbeat2, u'sound')

        def loseCash(self, amount):
            self.updateWallet(amount, deduct = True)

        def gainCash(self, amount):
            self.updateWallet(amount, deduct = False)

        def addToInventory(self, itemName, payloadValue = None, customToolTip = None):
            if str(itemName).lower() == "cash":
                self.updateWallet(payloadValue)
                return

            existingSet = self.hasItem(itemName)

            if not existingSet: # Maybe later I'll add some logic to affect listed order NOTE: no i won't
                newItem = {KEY_NAME: itemName}
                if payloadValue:
                    newItem[KEY_VALUE] = payloadValue
                if customToolTip:
                    newItem[KEY_TOOLTIP] = customToolTip
                self.inventory.append(newItem)
            else:
                try:
                    print("dfdfdf", KEY_VALUE, existingSet, payloadValue)
                    if payloadValue:
                        existingSet[KEY_VALUE] += int(payloadValue)
                    else:
                        existingSet[KEY_VALUE] += 1
                except TypeError:
                    log("[Error]: An invalid item adding operation was caught.")
                    return
                except KeyError:
                    return
            renpy.sound.queue(audio.heartbeat2, u'sound')

        def damage(self, which, dtype, amount):
            swkey = str(which)
            totalBoxes = self.trackers[swkey][KEY_TOTAL] + self.trackers[swkey][KEY_BONUS]

            if usingToughness and swkey == KEY_HP:
                armor = self.getDisciplineLevel(_fortitude)
            else:
                armor = self.trackers[swkey][KEY_ARMOR]

            dented = False
            injured = False
            trueAmount = amount
            if swkey == KEY_HP and dtype == KEY_SPFD: # NOTE: Superficial damage is halved before the loop
                trueAmount = math.ceil(float(amount) / 2)

            for point in range(int(trueAmount)):
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
                renpy.sound.queue(audio.pc_hit_fort_melee, u'sound')
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
            if lineBetween and type(lineBetween) is tuple:
                renpy.say(lineBetween[0], lineBetween[1])
            elif lineBetween:
                renpy.say(None, str(lineBetween))
            renpy.sound.queue(audio.drinking1, u'sound')

        def soundRoadTrip(self, lineBetween = None):
            renpy.play(audio.heels_on_pavement, u'sound')
            if lineBetween and type(lineBetween) is tuple:
                renpy.say(lineBetween[0], lineBetween[1])
            elif lineBetween:
                renpy.say(None, str(lineBetween))
            renpy.sound.queue(audio.carstart_pc, u'sound')

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

            if opinion_camarilla >= cam_rep_rank2:
                self.setHerdLevel()

            if opinion_camarilla >= cam_rep_rank1:
                self.gainCash(300)

        def getWillPenalty(self):
            return max(self.hunger - (self.humanity - 6), 0)

        def test(self, diff, *names, **kwargs): # messyCritsOn = False, bestialFailsOn = True, goal = None):
            pool = 0
            mcrit = False
            bfail = False

            print("\n\n", names)
            for name in names:
                print(name)
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
            return self.test(diff, *scores, messyCritsOn = False, bestialFailsOn = False)


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
        except TypeError:
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
        global night, timetonight, daysLeft
        night += 1
        timetonight = 1.0
        daysLeft = 7 - night
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
