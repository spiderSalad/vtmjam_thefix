init 0 python:
    import math
    # from collections import OrderedDict
    # NOTE: (OrderedDicts don't work with rollback; had to switch back to native dictionaries)

define DEBUG        = True
define MUSIC_MUTED  = False

# Licensing info

define ccl_url1 = "{a=https://creativecommons.org/licenses/by-nc-sa/4.0/}"
define ccl_url2 = "{/a}"

# GUI constants (consider moving to gui.rpy)

define DEFAULT_DOT_COLOR        = "red"
define TRACKER_MAX_BOXES        = 13
define MERIT_MAX                = 3
define REP_GRID_ROWS            = 3
define REP_GRID_COLS            = 2
define BG_GRID_ROWS             = 3
define BG_GRID_COLS             = 2

define codexTabList             = ["scores", "powers", "status"]

# Backgrounds

image bg hotel room             = "gevora_hotel_room_1280x720.png"
image bg hotel exterior         = "hotel_exterior.jpg"
image bg driving road1          = "driving_at_night_1280x720.jpg"
image bg driving road2          = "driving_at_night_2.jpg"
image bg hunt1 consensualist    = "hunt_consensualist1.jpg"
image bg hunt1 roadsidekiller   = "hunt_roadsidekiller1.jpg"
image bg hunt1 scenequeen       = "hunt_scenequeen1.jpg"
image bg hunt1 siren_men        = "hunt_siren1_men.jpg"
image bg hunt1 siren_women      = "hunt_siren1_women.jpg"
image bg hunt siren_their_place = "hunt_siren_their_place.jpg"
image bg city nightscape1       = "citynight2.jpg"
image bg city officepark1       = "office_park_1.jpg"
image bg rooms boardroom1       = "boardroom1.jpg"
image bg huntX consensualist    = "generic_hunt_consensualist.jpg"
image bg huntX roadsidekiller   = "generic_hunt_roadsidekiller.jpg"
image bg huntX scenequeen       = "generic_hunt_scenequeen.jpg"
image bg huntX siren            = "generic_hunt_siren.jpg"
image bg danger alley1          = "bg_dark_alley.jpg"
image bg danger alleyRed        = "bg_red_alley.jpg"

# Overlays

image hungerlay three           = "gui/overlay/hunger_three.png"
image hungerlay four            = "gui/overlay/hunger_four.png"
image hungerlay five            = "gui/overlay/hunger_five.png"

# Character names

define _pc          = {"first":"Bethany", "last":"Salazar", "pet": "Beth"}
define _pcGhoul     = {"first":"Richard", "last":"Brown", "middle": "Bartholomew", "MI": "B.", "pet": "Richie"}
define _sensam      = {"first":"Sam", "last":"Torres", "subj":"they", "obj":"them", "pos":"their", "pospro":"theirs", "reflex":"themself"}
define _exmale      = {"first":"Michael", "last":"Garcia", "subj":"he", "obj":"him", "pos":"his", "pospro":"his", "reflex":"himself"}
define _exfemale    = {"first":"Michelle", "last":"Garcia", "subj":"she", "obj":"her", "pos":"her", "pospro":"hers", "reflex":"herself"}

# Music and sound aliases

define audio.title              = "audio/music/BenJamin Banger - Tom 2.0.mp3"
define audio.scene1_awakening   = "audio/music/2Kutup - Travelling Through Intergalactic Space.mp3"
define audio.club1              = "audio/music/BenJamin Banger - Freestyle 39.mp3"
define audio.car_meeting        = "<from 5>audio/music/AEED - Through The City.mp3"
define audio.car_hunting1       = "audio/music/BenJamin Banger - Not The Cypher.mp3"
define audio.car_hunting2       = "<from 2>audio/music/Metre - Don't Walk Home Alone.mp3"
define audio.elysium1           = "audio/music/Teddy and Marge - Dark Eyes.mp3"
define audio.talk_with_sire     = "audio/music/Ketsa - Sun Hope.mp3"
define audio.consensualist      = "audio/music/Tea K Pea - chromaticmetal.mp3"
define audio.roadside_killer    = "audio/music/ROZKOL - Careful now, Stalker.mp3"
define audio.scene_queen        = "audio/music/Andre Jetson - Andre Jetson - After The Storm (Original Mix).mp3"
define audio.scene_queen_x      = "audio/music/Andre Jetson - Andre Jetson - Bipolar (Original Mix).mp3"
define audio.siren_men1         = "audio/music/BenJamin Banger - Freestyle 39.mp3"
define audio.siren_women1       = "audio/music/Digi G'Alessio - Appuntamento Al Club.mp3"
define audio.siren_their_place  = "<from 68 to 125>audio/music/Makaih Beats - Guilty Pleasure (Majestic Drama Collab).mp3"
define audio.introMission       = "audio/music/Darkstar83 - Shadow Walker.mp3"
define audio.mission2           = "audio/music/InSpectr - Third eye.mp3"
define audio.seneschal          = "audio/music/DJ Spooky - Adagio in Blue.mp3"
define audio.seneschal2         = "<from 4>audio/music/DJ Spooky - Nocturne.mp3"
define audio.freakout           = "audio/music/InSpectr - Tension.mp3"
define audio.hotel_neutral      = "<from 5>audio/music/DJ Spooky - Check Your Math.mp3"
define audio.relaxation         = "audio/music/Ketsa - No-Light-Without-Darkness.mp3"
define audio.huntsuccess_cons   = "audio/music/Ketsa - Heart Science (no-beats).mp3"
define audio.huntsuccess        = "audio/music/Tea K Pea - commander.mp3"
define audio.huntfailure        = "audio/music/Darkstar83 - The Witches Dream.mp3"

define audio.phone_alarm        = "audio/sound/501881__greenworm__cellphone-alarm-clock-long.mp3"
define audio.heartbeat1         = "audio/sound/inspectorj__heartbeat-regular-single-01-01-loop.mp3"
define audio.heartbeat2         = "audio/sound/86886__timbre__74829-jobro-heartbeat-timbre-s-variant-1b-loop.mp3"
define audio.beastgrowl1        = "audio/sound/344903__aegersum__monster-deep-growl.mp3"
define audio.beastgag           = "audio/sound/347541__pfranzen__human-impression-of-cat-hacking-up-hairball.ogg"
define audio.shower_pc          = "audio/sound/189689__sangtao__women-in-the-shower.mp3"
define audio.heels_on_pavement  = "audio/sound/318900__robinhood76__05934-heels-walking-on-pavement-looping.mp3"
define audio.carstart_pc        = "audio/sound/185740__enric592__car-start.mp3"
define audio.carstopengine_pc   = "audio/sound/534921__spurioustransients__car-engine-stop-3.mp3"
define audio.carstopkeys_pc     = "audio/sound/58243__robinhood76__00238-stop-keys-and-manual-brake.mp3"
define audio.bite1              = "audio/sound/400174__jgriffie919__flesh-bite.mp3"
define audio.drinking1          = "audio/sound/608241__newlocknew__heart-beat-calm-rhythm-blood-flows-in-the-veins-6lrs.mp3"
define audio.tackle1            = "audio/sound/502553__kneeling__goblin-fall.mp3"
define audio.tablefist          = "audio/sound/570241__evanski__crunch.mp3"
define audio.punchgrunt1        = "audio/sound/497713__miksmusic__punch-grunt-1.mp3"
define audio.heels_running      = "<from 0 to 8>audio/sound/187291__soundadvices__parking-garage-footsteps-woman-heels-2.mp3"
define audio.car_screech        = "audio/sound/233558__waveplaysfx__sfx-car-screech-2.mp3"
define audio.kick1              = "audio/sound/450278__ethanchase7744__kick-2.mp3"
define audio.gunshot1           = "audio/sound/212607__pgi__machine-gun-002-single-shot.mp3"
define audio.womangrunt         = "audio/sound/536750__egomassive__gruntf.mp3"
define audio.swordclash         = "audio/sound/440069__ethanchase7744__sword-block-combo.mp3"
define audio.stab1              = "audio/sound/435238__aris621__nasty-knife-stab.mp3"
define audio.stab2              = "audio/sound/478145__aris621__nasty-knife-stab-2.mp3"
define audio.bulletimpacts      = "audio/sound/423301__u1769092__visceralbulletimpacts.mp3"

# Tran... sitions!

define trans_slowfade           = Fade(0.5, 2, 0.3)
transform basicfade:
    on show:
        alpha 0.0
        linear 3.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

# Gameplay constants

define KEY_ATTR             = "Attributes"
define KEY_SKILL            = "Skills"
define KEY_DISCIPLINE       = "Disciplines"
define KEY_MERIT_BACKGROUND = "Merits_Backgrounds"
define KEY_PRED_TYPE        = "predatorType"

define KEY_HP               = "Health"
define KEY_HP_FORT          = "HealthFort"
define KEY_WP               = "Willpower"
define KEY_TOTAL            = "total"
define KEY_BONUS            = "bonus"
define KEY_ARMOR            = "armor"
define KEY_SPFD             = "Superficial Damage"
define KEY_AGGD             = "Aggravated Damage"
define KEY_LEVEL            = "level"
define KEY_DPOWERS          = "disc_powers"

define HUMANITY_MAX         = 8
define HUMANITY_MIN         = 5
define HUMANITY_START       = 7

define HUNGER_MAX           = 5
define HUNGER_MIN_LIVE      = 1
define HUNGER_MIN_DEAD      = 0
define HUNGER_MAX_CALM      = 2
define HUNGER_DEBT_MAX      = 8

define ATTRIBUTE_MAX        = 5
define ATTRIBUTE_MIN        = 1
define SKILL_MAX            = 5
define SKILL_MIN            = 0
define REP_MIN              = 0 # -100
define REP_MAX              = 200 # 100
define REP_VALUE_ADJUST     = 100

define BEASTFAIL            = "Bestial Failure"
define FAIL                 = "Failure"
define SUCCESS              = "Success"
define MESSYCRIT            = "Messy Critical"
define DRAW                 = "Draw" # combat only

# Attribute names

define _str     = "Strength"
define _dex     = "Dexterity"
define _sta     = "Stamina"
define _cha     = "Charisma"
define _man     = "Manipulation"
define _com     = "Composure"
define _int     = "Intelligence"
define _wit     = "Wits"
define _res     = "Resolve"

# Skill names

define _athl    = "Athletics"
define _clan    = "Clandestine"
define _comb    = "Combat"
define _driv    = "Drive"
define _fire    = "Firearms"

define _inti    = "Intimidation"
define _intr    = "Intrigue"
define _perf    = "Performance"
define _pers    = "Persuasion"
define _stre    = "Streetwise"

define _acad    = "Academics"
define _awar    = "Awareness"
define _inve    = "Investigation"
define _occu    = "Occult"
define _tech    = "Technology"

# Discipline names

define _dominate    = "Dominate"
define _fortitude   = "Fortitude"
define _presence    = "Presence"

# Attribute tooltips

define tooltipTable = {
    _str: "Lifting, pulling, pushing, punching, kicking, etc.",
    _dex: "Coordination and acuity of all kinds, from sprinting to aiming a gun.",
    _sta: "How much punishment I can take if I have to. Or want to.",
    _cha: "Getting people to like me, fear me, want me. Making them feel.",
    _man: "Getting people to listen whether they like me or not..",
    _com: "Staying cool in the moment so I don't lose my shit again.",
    _int: "Learning, reasoning, problem-solving, memory. The stuff they're always trying to test people for.",
    _wit: "Reaction, intuition, thinking on your feet!",
    _res: "Focus and determination not to let things go like before.",

    _athl: "",
    _clan: "",
    _comb: "",
    _driv: "",
    _fire: "",
    _inti: "",
    _intr: "",
    _perf: "",
    _pers: "",
    _stre: "",
    _acad: "",
    _awar: "",
    _inve: "",
    _occu: "",
    _tech: ""
}

# Discipline power keys

define DOM_FORGET           = "Cloud Memory"
define DOM_COMPEL           = "Compel"
define DOM_MESMERIZE        = "Mesmerize"
define DOM_GASLIGHT         = "The Forgetful Mind"
define DOM_MANCHURIA        = "Submerged Directive"

define FORT_STUBBORN        = "Unswayable Mind"
define FORT_HP              = "Resilience"
define FORT_TOUGH           = "Toughness"
define FORT_FIREWALKER      = "Defy Bane"
define FORT_POKERFACE       = "Fortify the Inner Facade"

define PRES_AWE             = "Awe"
define PRES_DAUNT           = "Daunt"
define PRES_ADDICTED2U      = "Lingering Kiss"
define PRES_CHARM           = "Entrancement"
define PRES_SCARYFACE       = "Dread Gaze"
define PRES_DOMVOICE        = "Irresistible Voice"
define PRES_WELLDOITLIVE    = "Star Magnetism"

# Predator types

define PT_CONSENSUALIST     = "Consensualist"
define PT_ROADSIDE_KILLER   = "Roadside Killer"
define PT_SCENE_QUEEN       = "Scene Queen"
define PT_SIREN             = "Siren"

define SIREN_BOTH           = "either"
define SIREN_MEN            = "men"
define SIREN_WOMEN          = "women"
define SIREN_ENBIES         = "nonbinary"

define PT_QUIP_TABLE        = {
    DOM_COMPEL: "I can give an order that {i}must{/i} be obeyed. It can't be too complicated, though. Like, \"stop\" or \"give me that\".",
    DOM_MESMERIZE: "I can give someone orders that they {i}must{/i} obey. Those orders can be long and complex if need be.",
    FORT_STUBBORN: "I've learned to use the Blood to actually toughen, like, my mind. Shit just doesn't faze me. Not easily.",
    FORT_HP: "I'm tough. Like, supernaturally tough. Well, all vampires are. But I mean on top of even that.",
    PRES_AWE: "I can project an aura of allure, that draws attention and interest. Makes people more amenable to what I have to say.",
    PRES_DAUNT: "I can project an aura of \"don't fuck with me\". Makes people uneasy around me and terrified to get close or interact with me."
}

# Merit, loresheet, background keys

define KEY_NAME             = "name"
define KEY_NAME_ALT         = "altname"
define KEY_VALUE            = "itemvalue"
define KEY_TOOLTIP          = "tooltip"
define KEY_ITEMTYPE         = "typeName"
define KEY_BGTYPE           = "typeName"
define KEY_BGSCORE          = "score"
define KEY_MERITS           = "merits"
define KEY_FLAWS            = "flaws"
define KEY_BGTYPE           = "merit_type"
define ISSA_MERIT           = "ismerit"
define ISSA_LORESHEET       = "islore"
define ISSA_BG              = "isbg"
define ISSA_FLAW            = "isflaw"

define M_ALLIES             = {KEY_NAME: "Allies", KEY_NAME_ALT: "Enemy", KEY_BGTYPE: ISSA_BG, KEY_FLAWS: ["Gifted Mortal Enemy"], KEY_MERITS: ["Weak Mortal Ally", "Average Mortal Ally"]}
define M_CONTACTS           = {KEY_NAME: "Contacts", KEY_BGTYPE: ISSA_BG, KEY_MERITS: ["\"Jack\"", "\"Jack\" and his \"crew\"", "The Dragon's Claws"]}
define M_HERD               = {KEY_NAME: "Herd", KEY_BGTYPE: ISSA_BG, KEY_FLAWS: ["Obvious Predator"], KEY_MERITS: ["Small Herd", "Medium Herd", "Large Herd"]}
define M_INFLUENCE          = {KEY_NAME: "Influence", KEY_BGTYPE: ISSA_BG, KEY_FLAWS: ["Disliked"], KEY_MERITS: ["Well-connected", "Influential", "Entrenched"]}
define M_LOOKS              = {KEY_NAME: "Looks", KEY_BGTYPE: ISSA_MERIT, KEY_FLAWS: ["Ugly", "Repulsive"], KEY_MERITS: ["Beautiful", "Stunning"]}
define M_LINE_HARDESTADT    = {KEY_NAME: "Descendant of Hardestadt", KEY_BGTYPE: ISSA_LORESHEET, KEY_MERITS: [
                                    "Voice of Hardestadt", "Supreme Leader", "Ventrue Pillar", "Line to the Founders", "Hardestadt's Heir"
                            ]}
define M_RESOURCES          = {KEY_NAME: "Resources", KEY_BGTYPE: ISSA_BG, KEY_FLAWS: ["Destitute"], KEY_MERITS: ["", "", "", "", ""]}

define IT_MONEY             = "Money"
define IT_JUNK              = "Junk"
define IT_CLUE              = "Clue"
define IT_QUEST             = "Quest Item"
define IT_WEAPON            = "Weapon"
define IT_FIREARM           = "Firearm"
define IT_EQUIPMENT         = "Equipment"
define IT_MISC              = "Misc."

define DAMAGE_BONUS         = "Lethality"
define ITEM_CONCEALED       = "concealedCarry"

define IT_COLOR_KEYS        = {
    IT_MONEY: "#399642", IT_JUNK: "#707070", IT_CLUE: "#ffffff", IT_WEAPON: "#8f8f8f",
    IT_EQUIPMENT: "#cbcbdc", IT_QUEST: "#763cb7", IT_MISC: "#cbcbdc"
}

# No items, fox only, final destination
default itemTable       = {
    # racks
    "cash": {KEY_ITEMTYPE: IT_MONEY, KEY_TOOLTIP: "Money in hand, for expenses best left off the books."},

    # equipment
    "smartphone1": {KEY_VALUE: "Smartphone", KEY_ITEMTYPE: IT_EQUIPMENT},
    "smartphone2b": {KEY_VALUE: "Cam Burner Phone", KEY_ITEMTYPE: IT_EQUIPMENT},

    # weapons
    "gun_ruger_1": {KEY_VALUE: "Stolen Ruger LCP", KEY_ITEMTYPE: IT_FIREARM, DAMAGE_BONUS: 2, ITEM_CONCEALED: True, KEY_TOOLTIP: "Confiscated and then re-confiscated."},
    "switchblade": {KEY_VALUE: "Switchblade", KEY_ITEMTYPE: IT_WEAPON, DAMAGE_BONUS: 2, ITEM_CONCEALED: True,
        KEY_TOOLTIP: "You know what they say about knife fights. Good thing I'm already dead."},

    # junk
    "chewing_gum": {KEY_VALUE: "Chewing Gum", KEY_ITEMTYPE: IT_JUNK, KEY_TOOLTIP: "I was hoping this would help with blood-breath. It doesn't."}
}

# Story factions
define F_ANARCHS            = "Local Anarchs"
define F_CAMARILLA          = "Local Camarilla"
define F_VENTRUE            = "Local Ventrue"
define F_NOSFERATU          = "Local Nosferatu"
default F_GHOUL             = "" # Depends on Ghoul's name.

# list orders, since we can't use orderedDicts

define scoreWords           = ["zero", "one", "two", "three", "four", "five"]
define humanityScores       = ["Callously disdainful", "Jaded and cynical", "Concerned and contrite", "Doggedly principled", "Serenely absolved"]
define hungerScores         = ["Blissfully sated", "Mostly satisfied", "Peckish", "Hungry", "Famished", "Ravenous!"]
define attributeOrder       = [_str, _dex, _sta, _cha, _man, _com, _int, _wit, _res]
define skillOrder           = [_athl, _clan, _comb, _driv, _fire, _inti, _intr, _perf, _pers, _stre, _acad, _awar, _inve, _occu, _tech]
define disciplineOrder      = [_dominate, _fortitude, _presence]

define humanityQuotes   = [
    ""
]
define hungerQuotes     = [ # hunger 0-5, humanity 5-8 (you lose at 4; 9 is unreachable)
    ["{i}Goddamn{/i} that feels good.", "I feel... whole.", "The emptiness is gone, just for a bit.", "Oh God, what have I done?"],
    ["Eh... I could eat.", "I'm fine...", "I'm good.", "I'm good."],
    ["Time to hunt...", "Time to hunt...", "Eh, I could eat.", "Eh, I could eat."],
    ["Ayyy where my juicebags at?", "Should feed soon...", "Getting pretty hungry...", "It can wait."],
    ["FEED. NOW.", "'Bout to grab me a fuckin' drink!", "Come on, Beth. Mind over matter.", "The Beast doesn't rule me. {i}I{/i} rule me."],
    ["Can't think. Blood...", "FUCKFUCKFUCKFUCKFUCK", "I need to feed before I lose control...", "I need to feed before I lose control..."]
]

# Starting PC vampire dossier

define clan         = "Ventrue"
define sire         = "Ms. Walker"
define generation   = "11th"
define bloodpotency = 1
define bpTable      = [{"surge": 2, "discipline_bonus": 0, "superficial_mend": 1}, {"surge": 2, "discipline_bonus": 1, "superficial_mend": 2}]

# Starting player attributes

define STR      = 1
define DEX      = 1
define STA      = 1
define CHA      = 1
define MAN      = 1
define COM      = 2
define INT      = 2
define WIT      = 1
define RES      = 1

# Starting player skills

define Athl     = 1
define Clan     = 1
define Comb     = 0
define Driv     = 1
define Fire     = 0

define Inti     = 1
define Intr     = 1
define Perf     = 1
define Pers     = 0
define Stre     = 1

define Acad     = 2
define Awar     = 1
define Inve     = 0
define Occu     = 0
define Tech     = 0

# List of powers

define powerlist        = {
    _dominate: [[DOM_FORGET, DOM_COMPEL], [DOM_MESMERIZE], [DOM_GASLIGHT, DOM_MANCHURIA]],
    _fortitude: [[FORT_HP, FORT_STUBBORN], [FORT_TOUGH], [FORT_FIREWALKER, FORT_POKERFACE]],
    _presence: [[PRES_AWE, PRES_DAUNT], [PRES_ADDICTED2U], [PRES_CHARM, PRES_SCARYFACE], [PRES_DOMVOICE], [PRES_WELLDOITLIVE]]
}

# List of merits (max 3) and backgrounds/flaws

define meritTable       = {
    M_LOOKS[KEY_NAME]: [{KEY_BGTYPE: M_LOOKS[KEY_NAME], KEY_NAME: "Beautiful", KEY_BGSCORE: 1, ISSA_FLAW: False}],
    M_LINE_HARDESTADT[KEY_NAME]: [{KEY_BGTYPE: M_LINE_HARDESTADT[KEY_NAME], KEY_NAME: "Voice of Hardestadt", KEY_BGSCORE: 1, ISSA_FLAW: False}]
}

define bgTable          = {
    M_ALLIES[KEY_NAME]: [{KEY_BGTYPE: M_ALLIES[KEY_NAME], KEY_NAME: "Enemy: My Ex", KEY_BGSCORE: 1, ISSA_FLAW: True}],
    M_CONTACTS[KEY_NAME]: [
        {KEY_BGTYPE: M_CONTACTS[KEY_NAME], KEY_NAME: "\"Jack\"", KEY_BGSCORE: 1, ISSA_FLAW: False},
        {KEY_BGTYPE: M_CONTACTS[KEY_NAME], KEY_NAME: "\"Jack\" and his \"crew\"", KEY_BGSCORE: 2, ISSA_FLAW: False}
    ],
    M_INFLUENCE[KEY_NAME]: [{KEY_BGTYPE: M_INFLUENCE[KEY_NAME], KEY_NAME: "Disliked", KEY_BGSCORE: 1, ISSA_FLAW: True}],
    M_HERD[KEY_NAME]: [
        {KEY_BGTYPE: M_HERD[KEY_NAME], KEY_NAME: "Small Herd", KEY_BGSCORE: 1, ISSA_FLAW: False},
        {KEY_BGTYPE: M_HERD[KEY_NAME], KEY_NAME: "Medium Herd", KEY_BGSCORE: 2, ISSA_FLAW: False}
    ],
    M_RESOURCES[KEY_NAME]: [
        {KEY_BGTYPE: M_RESOURCES[KEY_NAME], KEY_NAME: "Destitute", KEY_BGSCORE: 1, ISSA_FLAW: True},
        {KEY_BGTYPE: M_RESOURCES[KEY_NAME], KEY_NAME: "Stipend", KEY_BGSCORE: 1, ISSA_FLAW: False},
        {KEY_BGTYPE: M_RESOURCES[KEY_NAME], KEY_NAME: "Actual Budget", KEY_BGSCORE: 2, ISSA_FLAW: False}
    ]
}

# Starting discipline powers

define dominate         = 1
define dominatePowers   = {"one": DOM_FORGET, "two": None, "three": None, "four": None, "five": None}
define fortitude        = 0
define fortitudePowers  = {"one": None, "two": None, "three": None, "four": None, "five": None}
define presence         = 0
define presencePowers   = {"one": None, "two": None, "three": None, "four": None, "five": None}

# Starting merits and backgrounds

define startMerits      = []
define startBackgrounds = []

# Default opinions

default opinion_anarchs     = -10
default opinion_camarilla   = 35
default opinion_ventrue     = 45
default opinion_nosferatu   = 0
default opinion_ghoul       = 55

default cam_rep_rank1       = 35
default cam_rep_rank2       = 55

# Starting inventory

default inventory       = [ # Items in the player's inventory should only have a name/item table reference, and possibly
    {KEY_NAME: "cash", KEY_VALUE: 300.0}, # an instance-specific value or tooltip
    {KEY_NAME: "smartphone1", KEY_TOOLTIP: "The third-latest iPhone model, rooted and jailbroken and whatnot by my sire's people. Secure, in theory."},
    {KEY_NAME: "chewing_gum"}
]
