#! /usr/bin/env python3

import os

HERE = os.path.dirname(__file__)

FILE_LAND_DOCTORINE = os.path.join(HERE, 'gucci_land_doctorine.txt')

DOCTORINES = 6

content = ''
content += 'technologies = {\n'

for doctorine_idx in range(DOCTORINES):

    doctorine_num = doctorine_idx + 1
    doctorine_num_next = doctorine_num + 1

    doctrine_name = 'doctrine_name = "GUCCI_WARFARE_DOCTRINE"' if doctorine_idx == 0 else ''
    doctorine_cost = 300 if doctorine_idx == 0 else 100

    doctorine_pos_y = 22 + (2 * doctorine_idx)

    doctorine_path = f'''
		path = {{
			leads_to_tech = gucci_warfare_{doctorine_num_next}
		}}
'''
    if doctorine_idx == DOCTORINES - 1:
        doctorine_path = ''

    content += f'''
	gucci_warfare_{doctorine_num} = {{
		folder = {{
			name = land_doctrine_folder
			position = {{ x = 12 y = {doctorine_pos_y} }}
		}}

		{doctrine_name}

		xp_research_type = army
		xp_unlock_cost = {doctorine_cost}

		doctrine = yes
		research_cost = 4.5 # what the fuck ??? does this even do anything ??? this must be ancient code from the time where you used to need to research doctorines

		categories = {{
			land_doctrine
		}}

		# we have `category_front_line`, `category_army`, and also we could just ignore putting a categoty
		category_army = {{

			soft_attack = 0.06 # 0.1
			hard_attack = 0.06
			breakthrough = 0.06 # 0.20

			default_morale = 0.01 # recovery rate
			defense = 0.01

			# supply_consumption = -0.02
			max_organisation = 1
	    }}
		supply_consumption_factor = -0.01
		army_speed_factor = 0.01
		planning_speed = 0.05

		{doctorine_path}
	}}
'''

content += '}\n'

with open(FILE_LAND_DOCTORINE, 'w') as f:
    f.write(content)
