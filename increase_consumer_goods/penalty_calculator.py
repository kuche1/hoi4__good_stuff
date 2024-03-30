#! /usr/bin/env python3

FACTORIES = 550

raw_factory_production = 0

for num_factories in range(FACTORIES):
    num_factories += 1

    modifier = num_factories * -0.001
    if modifier < -0.5:
        modifier = -0.5

    raw_factory_production += 1

    factory_production = raw_factory_production * (1+modifier)
    print(f'{num_factories=} {modifier=} {factory_production=}')
