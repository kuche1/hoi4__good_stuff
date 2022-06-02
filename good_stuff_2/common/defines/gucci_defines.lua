
NDefines.NCountry.EVENT_PROCESS_OFFSET = 40 -- increases performance -- default 20
NDefines.NCountry.INTERPOLATED_FRONT_STEPS_SHORT = 1 -- default 2
NDefines.NCountry.POLITICAL_POWER_UPPER_CAP = 4000.0 -- default 2000.0
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 500 -- disables special forces limit -- default 24

NDefines.NDiplomacy.TENSION_DECAY = 0.18 -- reports as 0.5, but works properly -- default 0.1
NDefines.NDiplomacy.TENSION_SIZE_FACTOR = 0.75 -- default 1.0
NDefines.NDiplomacy.TENSION_TIME_SCALE_MIN = 0 -- default 0.25

NDefines.NFocus.MAX_SAVED_FOCUS_PROGRESS = 30 -- default 10

NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 4 -- default 12 -- used to be 36, but that seems to lower the performance

NDefines.NGame.GAME_SPEED_SECONDS = { 0.175, 0.1375, 0.1, 0.0625, 0.0 } -- default { 2.0, 0.5, 0.2, 0.1, 0.0 }
--NDefines.NGame.GAME_SPEED_SECONDS = { 0.1375, 0.102083333, 0.066666666, 0.03125, 0.0 } -- default { 2.0, 0.5, 0.2, 0.1, 0.0 }
--
-- these need to be re-tested with certain parts of the world disabled
--
-- r5 5600x
-- idkman its too fast
--
-- r5 3600
-- 0.125 is too high
-- 0.04 is too low
--
-- i5 750
-- game runs fine on 0.05 in 1936 with only europe and russia on the map
-- 0.025 game runs too quickly, cannot catch up even in early game: europe + russia + USA

NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 336 -- default 10
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 2880 -- default 25

NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 4 -- default 20
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 1 -- default 5
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 2 -- default 10
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 512 -- default 24
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 512 -- setting this to 0 brakes the AI -- default 24
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 512 -- default 5
NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 5000 -- default 500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 5000 -- default 500
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 5000 -- default 500

NDefines.NNavy.NAVAL_INVASION_PREPARE_HOURS = 33 -- default 168

NDefines.NTechnology.BASE_RESEARCH_POINTS_SAVED = 90.0 -- default 30.0
NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = 0.7 -- default 2
--NDefines.NTechnology.MIN_RESEARCH_SPEED = 0.1 -- default 0.1

NDefines_Graphics.NGraphics.CAPITAL_ICON_CUTOFF = 1500 -- default 1100
NDefines_Graphics.NGraphics.CAMERA_ZOOM_SPEED_DISTANCE_MULT = 20.0 -- default 6.0
NDefines_Graphics.NGraphics.LAND_UNIT_MOVEMENT_SPEED = 9999 -- default 12
NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 5 -- increases performance -- default 20
NDefines_Graphics.NGraphics.NAVAL_UNIT_MOVEMENT_SPEED = 9999 -- default 12

