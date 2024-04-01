#! /usr/bin/env python3

FACTORIES = 1_000

UNFAIR_PENALTY_AT = 600 # factories
# the moment where building more factories actually reduces your output
# it's really not that bad since you'll get factory output from reasearch
# and you'll get this at much higher factory count

# PENALTY = - (0.5/UNFAIR_PENALTY_AT)
PENALTY = -0.001

ADDITIONAL_PRODUCTION = 0.35

for num_factories in range(FACTORIES):
    num_factories += 1

    modifier = num_factories * PENALTY
    # if modifier < -0.7:
    #     modifier = -0.7

    # modifier
    # facs = num_factories
    # if facs >= 50:

    factory_production = num_factories * (1+modifier+ADDITIONAL_PRODUCTION)
    factory_production_without_modifier = num_factories * (1+ADDITIONAL_PRODUCTION)
    print(f'{PENALTY=} {num_factories=:4} {factory_production_without_modifier:=15.10f} {factory_production:=15.10f} {100*modifier=}')
