
-------- performance
-- NDefines.NCountry.EVENT_PROCESS_OFFSET = 40 -- increases performance -- default 20
-- NDefines.NCountry.INTERPOLATED_FRONT_STEPS_SHORT = 1 -- default 2
-- NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 8 -- default 12 -- used to be 36, but that seems to lower the performance

-------- convenience
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 400 -- disables special forces limit -- default 24
NDefines.NNavy.NAVAL_INVASION_PREPARE_HOURS = 33 -- makes naval invasions take less time -- default 168
NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 336 -- default 10
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 2880 -- default 25

-- template editing cost
NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 8 -- default 20
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 2 -- default 5
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 4 -- default 10

-- max armiy size
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 32 -- default 24
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 32 -- setting this to 0 brakes the AI -- default 24
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 8 -- default 5

-- max experience and pp
NDefines.NCountry.POLITICAL_POWER_UPPER_CAP = 4000.0 -- default 2000.0
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

-- NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = -- 0.7 -- default 2
-- NDefines.NTechnology.MIN_RESEARCH_SPEED = 0.1 -- default 0.1

-------- can't remember
-- NDefines_Graphics.NGraphics.CAPITAL_ICON_CUTOFF = 1500 -- default 1100
-- NDefines_Graphics.NGraphics.CAMERA_ZOOM_SPEED_DISTANCE_MULT = 20.0 -- default 6.0
-- NDefines_Graphics.NGraphics.LAND_UNIT_MOVEMENT_SPEED = 9999 -- default 12
-- NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 5 -- increases performance -- default 20
-- NDefines_Graphics.NGraphics.NAVAL_UNIT_MOVEMENT_SPEED = 9999 -- default 12

-------- speed buttons
NDefines.NGame.GAME_SPEED_SECONDS = {0.13, 0.10333333333333333, 0.07666666666666667, 0.05, 0.0} -- default { 2.0, 0.5, 0.2, 0.1, 0.0 }
-- shitty laptop:
--     game runs too fast (in >=mid game)         0.05
--     game runs fine but can probably be tweaked 0.09166666666666667
--     game runs too low                          0.13333333333333333

-- NDefines.NGame.GAME_SPEED_SECONDS = { 0.175, 0.13333333333333333, 0.09166666666666667, 0.05, 0.0 } -- default { 2.0, 0.5, 0.2, 0.1, 0.0 }
--
-- these need to be re-tested with certain parts of the world disabled
--
-- r5 5600x
--     south america disabled
--         0.0625 too slow
--
-- r5 3600
-- 0.125 is too high
-- 0.04 is too low
--
-- i5 750
-- game runs fine on 0.05 in 1936 with only europe and russia on the map
-- 0.025 game runs too quickly, cannot catch up even in early game: europe + russia + USA
