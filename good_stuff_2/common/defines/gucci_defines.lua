
NDefines.NCountry.EVENT_PROCESS_OFFSET = 40 -- increases performance -- default 20

NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 500 -- disables special forces limit -- default 24

NDefines.NDiplomacy.TENSION_DECAY = 0.3 -- reports as 0.5, but works properly -- default 0.1
NDefines.NDiplomacy.TENSION_SIZE_FACTOR = 0.75 -- default 1.0
NDefines.NDiplomacy.TENSION_TIME_SCALE_MIN = 0 -- default 0.25

NDefines.NGame.GAME_SPEED_SECONDS = { 0.3, 0.05, 0.04, 0.03, 0.0 } -- default { 2.0, 0.5, 0.2, 0.1, 0.0 }
-- r5 5600x
-- idkman its too fast
--
-- r5 3600
-- 0.125 is too high
-- 0.04 is too low
--
-- i5 750
-- 0.61 is too high
-- 0.3 - testing
-- 0.05 is good eraly game, but too low for mid to late game

NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 168 -- default 10
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 1440 -- default 25

NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 4 -- default 20
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 1 -- default 5
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 2 -- default 10
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 512 -- default 24
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 512 -- setting this to 0 brakes the AI-- default 24
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 512 -- default 5
NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 6900 -- default 500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 6900 -- default 500
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 6900 -- default 500

NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10 -- increases performance -- default 20

