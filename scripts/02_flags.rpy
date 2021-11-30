default currentCodexTab         = codexTabList[0]

default pc                      = None
default arena                   = None
default opp                     = None

# Faction/character opinions

default opinions                = {}

# Story flags

default night                   = 1
default daysLeft                = 7
default justWokeUp              = True
default timetonight             = 1.0
default prologue                = True
default timesFed                = 0

default predator_type           = None
default predator_type_power     = None
default feeding_consent         = False
default feeding_transients      = False
default feeding_scene           = False # EDM/rave scene
default hunting_difficulty      = 5 # later 6, 7, but only if training is implemented
default herd_countdown          = 0

default story_hunted_early      = False
default story_background        = None
default story_orientation       = None
default story_orientation_set   = False
default story_this_time         = None

default story_met_ex            = False
default story_attacked_ex       = False
default story_times_dodged_ex   = 0
default story_ghouled_ex        = False
default story_brainwashed_ex    = False
default story_ex_resolved       = False

default story_con_generic1      = False
default story_con_generic2      = False
default story_rsk_generic1      = False
default story_rsk_generic2      = False
default story_sqn_generic1      = False
default story_sqn_generic2      = False
default story_srn_generic       = False

default anarchs_enabled         = False
default anarchs_found           = False

default usingBloodSurge         = False
default freeBloodSurges         = 0
default usingAwe                = False
default usingMindControl        = False # Entrance or Mesmerize
default usingToughness          = False # Used in combat, unlike most of these flags

default story_mission1_cased    = False
default story_mission1_start    = False
default story_mission1_ghost    = True
default story_mission1_spotted  = False
default story_mission1_failed   = False
default story_mission1_complete = False

default story_m1_cutface        = True
default story_m1_allcameras     = False

default story_m1fail_burglary   = False
default story_m1fail_tech       = False
default story_m1fail_social     = False

default relaxclub               = False
default relaxbeach              = False
default relaxbar                = False

# Variable characters
define pcex                 = {"first":"", "last":"", "subj":"", "obj":"", "pos":"", "pospro":"", "reflex":""}
define shadyguy             = None
define dirtycop             = None
define brujah               = None

# Credits and licensing

default creditsFile         = None
default creditsJSON         = None
default sortedCredits       = None
