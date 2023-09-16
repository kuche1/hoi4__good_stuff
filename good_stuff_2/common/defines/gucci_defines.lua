
-------- performance
NDefines.NCountry.EVENT_PROCESS_OFFSET = 30 -- default 20
-- NDefines.NCountry.INTERPOLATED_FRONT_STEPS_SHORT = 1 -- default 2
-- NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 8 -- default 12 -- used to be 36, but that seems to lower the performance
NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10 -- default 20

-------- convenience
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 400 -- disables special forces limit -- default 24
NDefines.NNavy.NAVAL_INVASION_PREPARE_HOURS = 33 -- makes naval invasions take less time -- default 168

-- template editing cost
NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 8 -- default 20
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 2 -- default 5
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 4 -- default 10

-- max armiy size
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 26 -- default 24
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 26 -- setting this to 0 brakes the AI -- default 24
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 11 -- default 5

-- max experience and pp
NDefines.NCountry.POLITICAL_POWER_UPPER_CAP = 6000.0 -- default 2000.0
NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 5000 -- default 500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 5000 -- default 500
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 5000 -- default 500

-- research saved and focus saved
NDefines.NTechnology.BASE_RESEARCH_POINTS_SAVED = 100.0 -- default 30.0
NDefines.NFocus.MAX_SAVED_FOCUS_PROGRESS = 35 -- default 10

-------- balance
-- NDefines.NDiplomacy.TENSION_DECAY = 0.16 -- reports as 0.5, but works properly -- default 0.1
-- NDefines.NDiplomacy.TENSION_SIZE_FACTOR = 0.8 -- default 1.0
-- NDefines.NDiplomacy.TENSION_TIME_SCALE_MIN = 0 -- default 0.25

NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = 1.5 -- used to be 0.7 at some point -- default 2
-- NDefines.NTechnology.MIN_RESEARCH_SPEED = 0.1 -- default 0.1

-------- can't remember
-- NDefines_Graphics.NGraphics.CAPITAL_ICON_CUTOFF = 1500 -- default 1100
-- NDefines_Graphics.NGraphics.CAMERA_ZOOM_SPEED_DISTANCE_MULT = 20.0 -- default 6.0
-- NDefines_Graphics.NGraphics.LAND_UNIT_MOVEMENT_SPEED = 9999 -- default 12
-- NDefines_Graphics.NGraphics.NAVAL_UNIT_MOVEMENT_SPEED = 9999 -- default 12

-------- compliance
-- NDefines.NResistance.COMPLIANCE_GROWTH_BASE = 0.075 -- base compliance grow
NDefines.NResistance.COMPLIANCE_GROWTH_IS_AT_PEACE = 160 -- `10` stands for `10%` -- default 10
NDefines.NResistance.COMPLIANCE_GROWTH_HAS_CLAIM = 80 -- default 5
--NDefines.NResistance.COMPLIANCE_FACTOR_ON_STATE_CONTROLLER_CHANGE = 0 -- TODO wtf does this even do? the following comment is not true -- `-0.5` stands for loose half your compliance on controller change (this does include changing ideology) -- default -0.5

-------- multiplayer
--NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 110 -- default 10
--NDefines.NGame.LAG_DAYS_FOR_PAUSE = 275 -- default 25

--NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 30 -- default 10
--NDefines.NGame.LAG_DAYS_FOR_PAUSE = 18 -- default 25

NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 300 -- default 10
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 750 -- default 25
