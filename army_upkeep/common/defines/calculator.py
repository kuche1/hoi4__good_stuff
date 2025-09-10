#! /usr/bin/env python3

# last updated 2025.08.27

# https://hoi4.paradoxwikis.com/Attrition_and_accidents

RANDOM_0_to_1 = 0.5
NUMBER_OF_EQUIPMENT = 1_000
ATTRITION = 0.02 # 0.01 = 1% attrition
RELIABILITY = 0.8

def calc_equipment_lost_per_hour():
    equipment_lost_per_hour = 0.1 * ATTRITION * RANDOM_0_to_1 * max(1, NUMBER_OF_EQUIPMENT * 0.1 * (1-RELIABILITY))
    # print(f'{equipment_lost_per_hour=}')
    return equipment_lost_per_hour

def calc_equipment_lost_per_day():
    equipment_list_per_day = calc_equipment_lost_per_hour() * 24
    # actually this is not quite rigt wrong since it does not take into acccount]
    # that the total equipment is going to change, but it's going to be true as long
    # as the missing equipment is re-filled instantly after it was being lost

    # print(f'{equipment_list_per_day*67=}')

    return equipment_list_per_day

def calc_equipment_lost_per_year():
    loss = calc_equipment_lost_per_day() * 365.25
    ratio = loss / NUMBER_OF_EQUIPMENT
    print(f'Equipment Loss Per Year: {ratio * 100}')

calc_equipment_lost_per_year()
