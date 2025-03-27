#! /usr/bin/env python3

# generally the target is to extend everything till 1950

import os

HERE = os.path.dirname(__file__)

FILE_LAND_DOCTORINE = os.path.join(HERE, 'gucci_land_doctorine.txt')
LAND_DOCTORINES = 6

FILE_INDUSTRY = os.path.join(HERE, 'gucci_industry.txt')
INDUSTRIES = 7

def extend_land_doctorine(file, extensions):

	content = ''
	content += 'technologies = {\n'

	for doctorine_idx in range(extensions):

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
		if doctorine_idx == extensions - 1:
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

	with open(file, 'w') as f:
		f.write(content)

def extend_industry(file, extensions):

	content = ''
	content += 'technologies = {\n'

	for idx in range(extensions):

		name_current = f'gucci_industry_{idx+1}'
		name_next = f'gucci_industry_{idx+2}'

		pos_y = 12 + idx * 2

		year = 1944 + idx * 1

		if idx == extensions - 1: # if last
			path = ''
		else:
			path = f'''
				path = {{
					leads_to_tech = {name_next}
				}}
			'''

		content += f'''

			{name_current} = {{
				folder = {{
					name = industry_folder
					position = {{ x = 5 y = {pos_y} }}
				}}

				research_cost = 2
				start_year = {year}

				categories = {{
					industry
				}}

				global_building_slots_factor = 0.20
				industrial_capacity_factory = 0.1
				industrial_capacity_dockyard = 0.1
				line_change_production_efficiency_factor = 0.01
				production_factory_start_efficiency_factor = 0.01
				industry_air_damage_factor = -0.01

				{path}
			}}
		'''

	content += '}\n'

	with open(file, 'w') as f:
		f.write(content)

extend_land_doctorine(FILE_LAND_DOCTORINE, LAND_DOCTORINES)
extend_industry(      FILE_INDUSTRY,       INDUSTRIES)
