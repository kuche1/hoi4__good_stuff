
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 500 -- default 24

NDefines.NDiplomacy.TENSION_DECAY = 0.25 -- reports as 0.5, bit works properly -- default 0.1
NDefines.NDiplomacy.TENSION_SIZE_FACTOR = 0.8 -- default 1.0
NDefines.NDiplomacy.TENSION_TIME_SCALE_MIN = 0 -- default 0.25

NDefines.NGame.GAME_SPEED_SECONDS = { 0.1, 0.75, 0.05, 0.04, 0.0 } -- default { 2.0, 0.5, 0.2, 0.1, 0.0 }
--
-- 0.75 is too slow for 1st gen i5
-- 0.05 is good eraly game, but too fast for 1st gen i5
--
-- 0.125 is too slow for r5 3600
-- 0.0625 is too fast for r5 3600
--
-- { 0.25, 0.09375, 0.0625, 0.03125, 0.0 }
-- { 0.25, 0.1875, 0.125, 0.0625, 0.0 }

NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 20 -- default 10
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 50 -- default 25

NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 4 -- default 20
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 1 -- default 5
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 2 -- default 10
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 0 -- default 24
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 512 -- setting this to 0 brakes the AI-- default 24
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 0 -- default 5
NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 6900 -- default 500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 6900 -- default 500
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 6906 -- default 500
