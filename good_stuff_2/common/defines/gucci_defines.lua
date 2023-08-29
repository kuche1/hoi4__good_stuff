
-------- performance
-- NDefines.NCountry.EVENT_PROCESS_OFFSET = 40 -- increases performance -- default 20
-- NDefines.NCountry.INTERPOLATED_FRONT_STEPS_SHORT = 1 -- default 2
-- NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 8 -- default 12 -- used to be 36, but that seems to lower the performance

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

NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = 1.8 -- used to be 0.7 at some point -- default 2
-- NDefines.NTechnology.MIN_RESEARCH_SPEED = 0.1 -- default 0.1

-------- can't remember
-- NDefines_Graphics.NGraphics.CAPITAL_ICON_CUTOFF = 1500 -- default 1100
-- NDefines_Graphics.NGraphics.CAMERA_ZOOM_SPEED_DISTANCE_MULT = 20.0 -- default 6.0
-- NDefines_Graphics.NGraphics.LAND_UNIT_MOVEMENT_SPEED = 9999 -- default 12
-- NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 5 -- increases performance -- default 20
-- NDefines_Graphics.NGraphics.NAVAL_UNIT_MOVEMENT_SPEED = 9999 -- default 12

-------- compliance
-- NDefines.NResistance.COMPLIANCE_GROWTH_BASE = 0.075 -- base compliance grow
NDefines.NResistance.COMPLIANCE_GROWTH_IS_AT_PEACE = 40 -- default 10
NDefines.NResistance.COMPLIANCE_GROWTH_HAS_CLAIM = 20 -- default 5
NDefines.NResistance.COMPLIANCE_FACTOR_ON_STATE_CONTROLLER_CHANGE = 0 -- `-0.5` stands for loose half your compliance on controller change (this does include changing ideology) -- default -0.5

-------- multiplayer
NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 110 -- default 10
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 275 -- default 25

NDefines.NGame.GAME_SPEED_SECONDS = {0.16799999999999998, 0.07, 0.05, 0.03, 0.0} -- default { 2.0, 0.5, 0.2, 0.1, 0.0 }
--  generate new indexes with:
--      start = 0.022
--      end = 0.22
--      gen_idx = lambda start, end, idx: start + idx * (end-start)/3
--      f'{{{gen_idx(start, end, 3)}, {gen_idx(start, end, 2)}, {gen_idx(start, end, 1)}, {gen_idx(start, 0.18, 0)}, 0.0}}'
--
--  2023.08.29: debug_smooth + optimizations:
--      amd ryzen 5600G (using windows):
--          0.024 - 1936 - can't keep up with 5600X
--          NOTE: 0.072 should be overkill
--
--  2023.08.25: debug_smooth + optimizations:
--      amd ryzen 5600G (using windows):
--          0.022 - 1936 - can't keep up with 5600X
--
--  2023.08.23: debug_smooth + optimizations:
--      amd ryzen 5600G (using windows):
--          0.18 - late game (sov & chi vs ger) - can't keep up with 5600X
--          0.018 - early game (before war with japan) - can't keep up with 5600X
--
--  with new mod optimizations + debug_smooth
--      amd ryzen 5 1600
--          0.02 - minor slowdown at 1936 jul while using rustdesk
--          0.03 - no slowdown until at least 1936 mar
--          0.04 - no slowdown until at least 1938 may
--          0.06 - no slowdown until at least 1937 jul
--      amd ryzen 5 5600
--          0.02 - no slowdown until at least 1940
--
-- shitty laptop:
--     with optimized map v2:
--         MP lag during war   on 0.13
--         MP lag during piece on 0.05
