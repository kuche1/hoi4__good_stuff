
-------- performance
NDefines.NCountry.EVENT_PROCESS_OFFSET = 30 -- default 20 -- Events are checked every X day per country or state (1 is ideal, but CPU heavy)
-- NDefines.NCountry.INTERPOLATED_FRONT_STEPS_SHORT = 1 -- default 2
-- NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 8 -- default 12 -- used to be 36, but that seems to lower the performance
NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10 -- default 20 -- how many mapicons get processed per frame for grouping. more = quicker response, fewer = better performance

-------- convenience
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = NDefines.NCountry.SPECIAL_FORCES_CAP_MIN * 10 -- disables special forces limit -- default 24
NDefines.NNavy.NAVAL_INVASION_PREPARE_HOURS = NDefines.NNavy.NAVAL_INVASION_PREPARE_HOURS / 5 -- makes naval invasions take less time -- default 168

-- template editing cost
NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 2 -- default 20
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 2 -- default 5
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 2 -- default 10

-- max armiy size
-- NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 26 -- default 24
-- NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 26 -- setting this to 0 brakes the AI -- default 24
-- NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 16 -- default 5

-- max experience and pp
NDefines.NCountry.POLITICAL_POWER_UPPER_CAP = NDefines.NCountry.POLITICAL_POWER_UPPER_CAP * 3 -- default 2000.0
NDefines.NMilitary.MAX_ARMY_EXPERIENCE = NDefines.NMilitary.MAX_ARMY_EXPERIENCE * 10 -- default 500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = NDefines.NMilitary.MAX_NAVY_EXPERIENCE * 10 -- default 500
NDefines.NMilitary.MAX_AIR_EXPERIENCE = NDefines.NMilitary.MAX_AIR_EXPERIENCE * 10 -- default 500

-- research saved and focus saved
NDefines.NTechnology.BASE_RESEARCH_POINTS_SAVED = NDefines.NTechnology.BASE_RESEARCH_POINTS_SAVED * 4 -- default 30.0
NDefines.NFocus.MAX_SAVED_FOCUS_PROGRESS = 35 -- default 10

-------- balance
-- NDefines.NDiplomacy.TENSION_DECAY = 0.16 -- reports as 0.5, but works properly -- default 0.1
-- NDefines.NDiplomacy.TENSION_SIZE_FACTOR = 0.8 -- default 1.0
-- NDefines.NDiplomacy.TENSION_TIME_SCALE_MIN = 0 -- default 0.25

NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR * 0.8 -- default 2
-- NDefines.NTechnology.MIN_RESEARCH_SPEED = 0.1 -- default 0.1

-------- can't remember
-- NDefines_Graphics.NGraphics.CAPITAL_ICON_CUTOFF = 1500 -- default 1100
-- NDefines_Graphics.NGraphics.CAMERA_ZOOM_SPEED_DISTANCE_MULT = 20.0 -- default 6.0
-- NDefines_Graphics.NGraphics.LAND_UNIT_MOVEMENT_SPEED = 9999 -- default 12
-- NDefines_Graphics.NGraphics.NAVAL_UNIT_MOVEMENT_SPEED = 9999 -- default 12

-------- puppets
NDefines.NDiplomacy.RESOURCE_SENT_AUTONOMY_DAILY_FACTOR = NDefines.NDiplomacy.RESOURCE_SENT_AUTONOMY_DAILY_FACTOR / 5 -- default 0.005 -- If puppet provides resources to its master they increasy their autonomy by the resources factored by this
-- TODO ideally this ^^^ we would not change, instead we would make it so that it is possible to trade for less than 80 with a puppet
