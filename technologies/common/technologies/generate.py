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
		is_first = (idx == 0)
		is_last = (idx == extensions - 1)
		is_regular = (not is_first) and (not is_last)

		pos_y = 14 + idx * 2

		year = 1944 + idx * 1

		ind_name_current = f'gucci_industry_{idx+1}'
		ind_name_next = f'gucci_industry_{idx+2}'

		prod_name_current = f'guci_production_{idx+1}'
		prod_name_next = f'guci_production_{idx+2}'

		cons_name_current = f'gucci_construction_{idx+1}'
		cons_name_next = f'gucci_construction_{idx+2}'

		if is_first:
			ind_pos_y = pos_y - 2
		else:
			ind_pos_y = pos_y

		# path: industry

		if is_first:
			ind_path = f'''
				path = {{
					leads_to_tech = {ind_name_next}
				}}
				path = {{
					leads_to_tech = {prod_name_current}
				}}
				path = {{
					leads_to_tech = {cons_name_current}
				}}
			'''
		elif is_regular:
			ind_path = f'''
				path = {{
					leads_to_tech = {ind_name_next}
				}}
			'''
		else:
			ind_path = ''

		# path: production

		if is_first or is_regular:
			prod_path = f'''
				path = {{
					leads_to_tech = {prod_name_next}
				}}
			'''
		else:
			prod_path = ''

		# path: construction

		if is_first or is_regular:
			cons_path = f'''
				path = {{
					leads_to_tech = {cons_name_next}
				}}
			'''
		else:
			cons_path = ''

		# save

		content += f'''

			{ind_name_current} = {{
				folder = {{
					name = industry_folder
					position = {{ x = 5 y = {ind_pos_y} }}
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

				{ind_path}
			}}

			{prod_name_current} = {{
				folder = {{
					name = industry_folder
					position = {{ x = 0 y = {pos_y} }}
				}}

				research_cost = 2
				start_year = {year}

				categories = {{
					industry
					cat_production
				}}

				production_factory_max_efficiency_factor = 0.1

				{prod_path}
			}}

			{cons_name_current} = {{
				folder = {{
					name = industry_folder
					position = {{ x = 8 y = {pos_y} }}
				}}

				research_cost = 2
				start_year = {year}

				categories = {{
					industry
					construction_tech
				}}

				production_speed_buildings_factor = 0.10
				industry_repair_factor = 0.10
				
				{cons_path}
			}}
		'''

	content += '}\n'

	with open(file, 'w') as f:
		f.write(content)

extend_land_doctorine(FILE_LAND_DOCTORINE, LAND_DOCTORINES)
extend_industry(      FILE_INDUSTRY,       INDUSTRIES)
