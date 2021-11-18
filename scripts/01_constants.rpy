init 0 python:
    import math
    # from collections import OrderedDict
    # NOTE: (OrderedDicts don't work with rollback; had to switch back to native dictionaries)

define DEBUG        = True
define MUSIC_MUTED  = True

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

# Overlays

image hungerlay three           = "gui/overlay/hunger_three.png"
image hungerlay four            = "gui/overlay/hunger_four.png"
image hungerlay five            = "gui/overlay/hunger_five.png"

# Character names

define _pc          = {"first":"Bethany", "last":"Salazar", "pet": "Beth"}
define _pcGhoul     = {"first":"Leonard", "last":"Jackson", "middle": "Bartholomew", "MI": "B."}

# Music and sound aliases

define audio.title              = "audio/music/BenJamin Banger - Tom 2.0.mp3"
define audio.scene1_awakening   = "audio/music/2Kutup - Travelling Through Intergalactic Space.mp3"
define audio.club1              = "audio/music/BenJamin Banger - Freestyle 39.mp3"

define audio.phone_alarm        = "audio/sound/501881__greenworm__cellphone-alarm-clock-long.mp3"
define audio.heartbeat1         = "audio/sound/inspectorj__heartbeat-regular-single-01-01-loop.mp3"
define audio.heartbeat2         = "audio/sound/86886__timbre__74829-jobro-heartbeat-timbre-s-variant-1b-loop.mp3"
define audio.beastgrowl1        = "audio/sound/344903__aegersum__monster-deep-growl.mp3"
define audio.beastgag           = "audio/sound/347541__pfranzen__human-impression-of-cat-hacking-up-hairball.ogg"

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

# Merit, loresheet, background keys

define KEY_NAME             = "name"
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

define M_CONTACTS           = {KEY_NAME: "Contacts", KEY_BGTYPE: ISSA_BG, KEY_MERITS: ["??? (Add this)", "", "", "", ""]}
define M_HERD               = {KEY_NAME: "Herd", KEY_BGTYPE: ISSA_BG, KEY_FLAWS: ["Obvious Predator"], KEY_MERITS: ["Small Herd", "Medium Herd"]}
define M_LOOKS              = {KEY_NAME: "Looks", KEY_BGTYPE: ISSA_MERIT, KEY_FLAWS: ["Ugly", "Repulsive"], KEY_MERITS: ["Beautiful", "Stunning"]}
define M_LINE_HARDESTADT    = {KEY_NAME: "Descendant of Hardestadt", KEY_BGTYPE: ISSA_LORESHEET, KEY_MERITS: [
                                    "Voice of Hardestadt", "Supreme Leader", "Ventrue Pillar", "Line to the Founders", "Hardestadt's Heir"
                            ]}
define M_RESOURCES          = {KEY_NAME: "Resources", KEY_BGTYPE: ISSA_BG, KEY_FLAWS: ["Destitute"], KEY_MERITS: ["", "", "", "", ""]}

define IT_MONEY             = "Money"
define IT_JUNK              = "Junk"
define IT_CLUE              = "Clue"
define IT_QUEST             = "Quest Item"
define IT_MISC              = "Misc."

define IT_COLOR_KEYS        = {IT_MONEY: "#399642", IT_JUNK: "#707070", IT_CLUE: "#ffffff", IT_QUEST: "#763cb7", IT_MISC: "#cbcbdc"}

define ITEM_CASH            = "Cash"
define ITEM_PHONE1          = "Smartphone"

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

# Starting player attributes

define STR      = 1
define DEX      = 1
define STA      = 2
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
define Tech     = 1

# List of powers

define dominate_powers      = [[DOM_FORGET, DOM_COMPEL], [DOM_MESMERIZE], [DOM_GASLIGHT, DOM_MANCHURIA]]
define fortitude_powers     = [[FORT_HP, FORT_STUBBORN], [FORT_TOUGH], [FORT_FIREWALKER, FORT_POKERFACE]]
define presence_powers      = [[PRES_AWE, PRES_DAUNT], [PRES_ADDICTED2U], [PRES_CHARM, PRES_SCARYFACE], [PRES_DOMVOICE], [PRES_WELLDOITLIVE]]

# List of merits (max 3)

define beautiful            = {KEY_BGTYPE: M_LOOKS[KEY_NAME], KEY_NAME: "Beautiful", KEY_BGSCORE: 1, "flaw": False}
define voice_of_hardestadt  = {KEY_BGTYPE: M_LINE_HARDESTADT[KEY_NAME], KEY_NAME: "Voice of Hardestadt", KEY_BGSCORE: 1, "flaw": False}
# TODO: third merit here?

# List of backgrounds

define money0               = {KEY_BGTYPE: M_RESOURCES[KEY_NAME], KEY_NAME: "Destitute", KEY_BGSCORE: 1, "flaw": True}
define money1               = {KEY_BGTYPE: M_RESOURCES[KEY_NAME], KEY_NAME: "Stipend", KEY_BGSCORE: 1, "flaw": False}
define money2               = {KEY_BGTYPE: M_RESOURCES[KEY_NAME], KEY_NAME: "Actual Budget", KEY_BGSCORE: 2, "flaw": False}

define herd1                = {KEY_BGTYPE: M_HERD[KEY_NAME], KEY_NAME: "Small Herd", KEY_BGSCORE: 1, "flaw": False}
define herd2                = {KEY_BGTYPE: M_HERD[KEY_NAME], KEY_NAME: "Medium Herd", KEY_BGSCORE: 2, "flaw": False}

define contacts1            = {KEY_BGTYPE: M_CONTACTS[KEY_NAME], KEY_NAME: "???", KEY_BGSCORE: 1, "flaw": False}

# Starting discipline powers

define dominate         = 3
define dominatePowers   = [DOM_FORGET, DOM_MESMERIZE, DOM_GASLIGHT]
define fortitude        = 4
define fortitudePowers  = [FORT_HP, FORT_STUBBORN, FORT_TOUGH, FORT_POKERFACE]
define presence         = 5
define presencePowers   = [PRES_AWE, PRES_DAUNT, PRES_CHARM, PRES_DOMVOICE, PRES_WELLDOITLIVE]

# Starting merits

define startMerits      = [beautiful, voice_of_hardestadt, money0]

# Starting backgrounds

define startBackgrounds = [contacts1, herd1, money0, money1, herd2, money2]

# Default opinions

default opinion_anarchs     = -10
default opinion_camarilla   = 35
default opinion_ventrue     = 45
default opinion_nosferatu   = 0
default opinion_ghoul       = 55

# Starting inventory

default cash            = 1500 # wtf?
default inventory       = [
    {KEY_NAME: ITEM_CASH, KEY_VALUE: 1500, KEY_ITEMTYPE: IT_MONEY, KEY_TOOLTIP: "Money in hand, for expenses best left off the books."},
    {KEY_NAME: ITEM_PHONE1, KEY_VALUE: "Smartphone", KEY_ITEMTYPE: IT_QUEST,
        KEY_TOOLTIP: "The third-latest iPhone model, rooted and jailbroken and whatnot by my sire's people. Secure, in theory."},
    {KEY_NAME: "Chewing Gum", KEY_VALUE: "Chewing Gum", KEY_ITEMTYPE: IT_JUNK, KEY_TOOLTIP: "I was hoping it would help with blood-breath. It doesn't."}
]
