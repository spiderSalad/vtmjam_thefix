default currentCodexTab         = codexTabList[0]

default pc                      = None
default arena                   = None
default opp                     = None

# Faction/character opinions

default opinions                = {}

# Story flags

default night                   = 1
default justWokeUp              = True
default timetonight             = 1.0
default prologue                = True

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

# Variable characters
define pcex                 = {"first":"", "last":"", "subj":"", "obj":"", "pos":"", "pospro":"", "reflex":""}

# Credits and licensing

default artists             = []
default musicians           = []

default creditsText         = ""
default creditsFile         = None
default creditsJSON         = None
default sortedCredits       = None
default builtCredits        = False
