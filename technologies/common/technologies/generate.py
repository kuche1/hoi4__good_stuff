#! /usr/bin/env python3

# generally the target is to extend everything till 1950

import os

HERE = os.path.dirname(__file__)

def extend_land_doctorine(file, extensions):

	content = ''
	content += 'technologies = {\n'

	for doctorine_idx in range(extensions):

		doctorine_num = doctorine_idx + 1
		doctorine_num_next = doctorine_num + 1

		doctrine_name = 'doctrine_name = "GUCCI_WARFARE_DOCTRINE"' if doctorine_idx == 0 else ''
		doctorine_cost = 250 if doctorine_idx == 0 else 100

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

					soft_attack = 0.06
					hard_attack = 0.06
					breakthrough = 0.06

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

def extend_air_doctorine(file, extensions):

	content = ''
	content += 'technologies = {\n'

	for idx in range(extensions):
		is_first = (idx == 0)
		is_last = (idx == extensions - 1)

		pos_y = 20 + idx * 2

		# NOTE:
		# i'm taking advantage of `air_superiority` for the first doctorine so that I dont have to edin the stupid game files
		if is_first:
			name_cur = 'air_superiority'
		else:
			name_cur = f'gucci_air_doctorine_{idx+1}'

		name_next = f'gucci_air_doctorine_{idx+2}'

		if is_first:
			doctorine_name = 'doctrine_name = "TITLE_GUCCI_AIR_DOCTORINE"'
		else:
			doctorine_name = ''

		if is_first:
			cost = 250
		else:
			cost = 100

		if is_last:
			path = ''
		else:
			path = f'''
				path = {{
					leads_to_tech = {name_next}
				}}
			'''
		
		content += f'''
			{name_cur} = {{
				folder = {{
					name = air_doctrine_folder
					position = {{ x = 9 y = {pos_y} }}
				}}

				{doctorine_name}

				xp_research_type = air
				xp_unlock_cost = {cost}

				doctrine = yes	
				research_cost = 2.25 # I think this is worthless

				categories = {{
					air_doctrine
				}}

				category_fighter = {{
					air_agility = 0.04
				}}
				category_heavy_fighter = {{
					air_agility = 0.04
				}}
				category_cas = {{
					air_agility = 0.04
				}}
				tac_bomber = {{
					air_bombing = 0.04
				}}
				air_superiority_detect_factor = 0.04
				air_interception_detect_factor = 0.04
				air_cas_present_factor = 0.04
				air_strategic_bomber_bombing_factor = 0.04
				ground_attack_factor = 0.04
				air_strategic_bomber_defence_factor = 0.04

				{path}
			}}
		'''

	content += '}\n'

	with open(file, 'w') as f:
		f.write(content)

def extend_artillery(file, extensions):

	content = ''
	content += 'technologies = {\n'

	for idx in range(extensions):
		is_first = (idx == 0)
		is_last = (idx == extensions - 1)
		is_regular = (not is_first) and (not is_last)

		pos_y = 16 + idx * 2

		year = 1944 + idx

		num_cur = idx+1
		num_next = idx+2

		art_name = 'gucci_artillery_'
		rockart_name = 'gucci_rocket_artillery_'
		antiair_name = 'gucci_antiair_'
		antitank_name = 'gucci_antitank_'

		# artillery

		art_pos_y = pos_y
		if is_first:
			art_pos_y -= 2

		if is_first:
			art_path = f'''
				path = {{
					leads_to_tech = {art_name}{num_next}
				}}
				path = {{
					leads_to_tech = {rockart_name}{num_cur}
				}}
				path = {{
					leads_to_tech = {antiair_name}{num_cur}
				}}
				path = {{
					leads_to_tech = {antitank_name}{num_cur}
				}}
			'''
		elif is_regular:
			art_path = f'''
				path = {{
					leads_to_tech = {art_name}{num_next}
				}}
			'''
		else:
			art_path = ''
		
		# rocket artillery

		if is_last:
			rockart_path = ''
		else:
			rockart_path = f'''
				path = {{
					leads_to_tech = {rockart_name}{num_next}
				}}
			'''

		# antiair

		if is_last:
			antiair_path = ''
		else:
			antiair_path = f'''
				path = {{
					leads_to_tech = {antiair_name}{num_next}
				}}
			'''

		# antitant

		if is_last:
			antitank_path = ''
		else:
			antitank_path = f'''
				path = {{
					leads_to_tech = {antitank_name}{num_next}
				}}
			'''

		# actual file content

		content += f'''
			{art_name}{num_cur} = {{
				folder = {{
					name = artillery_folder
					position = {{ x = 0 y = {art_pos_y} }}
				}}

				research_cost = 1.0
				start_year = {year}

				categories = {{
					artillery
					mio_cat_all_artillery_equipment
					mio_cat_artillery #Only Artillery
				}}
				special_project_specialization = {{ specialization_land }}

				artillery = {{
					soft_attack = 0.1
				}}
				artillery_brigade = {{
					soft_attack = 0.1
				}}
				mot_artillery_brigade = {{
					soft_attack = 0.1
				}}
				category_self_propelled_artillery = {{
					soft_attack = 0.05
				}}

				{art_path}
			}}
		'''

		content += f'''
			{rockart_name}{num_cur} = {{
				folder = {{
					name = artillery_folder
					position = {{ x = 3 y = {pos_y} }}
				}}

				research_cost = 1.0
				start_year = {year}

				categories = {{
					rocketry
					mio_cat_all_artillery_equipment
				}}
				special_project_specialization = {{ specialization_air }}

				rocket_artillery = {{
					soft_attack = 0.15
				}}
				rocket_artillery_brigade = {{
					soft_attack = 0.15
				}}
				mot_rocket_artillery_brigade = {{
					soft_attack = 0.15
				}}
				motorized_rocket_brigade = {{
					soft_attack = 0.15
				}}

				{rockart_path}
			}}
		'''

		content += f'''
			{antiair_name}{num_cur} = {{
				folder = {{
					name = artillery_folder
					position = {{ x = -7 y = {pos_y} }}
				}}

				research_cost = 1.0
				start_year = {year}

				categories = {{
					artillery
					cat_anti_air
					mio_cat_all_artillery_equipment
				}}
				special_project_specialization = {{ specialization_land specialization_air }}

				anti_air = {{
					air_attack = 0.1
				}}
				anti_air_brigade = {{
					air_attack = 0.1
				}}
				mot_anti_air_brigade = {{
					air_attack = 0.1
				}}
				category_self_propelled_anti_air = {{
					air_attack = 0.05
				}}
				tech_air_damage_factor = -0.02

				{antiair_path}
			}}
		'''

		content += f'''
			{antitank_name}{num_cur} = {{
				folder = {{
					name = artillery_folder
					position = {{ x = 7 y = {pos_y} }}
				}}

				research_cost = 1.0
				start_year = {year}

				categories = {{
					artillery
					cat_anti_tank
					mio_cat_all_artillery_equipment
				}}
				special_project_specialization = {{ specialization_land }}

				anti_tank = {{
					hard_attack = 0.1
					ap_attack = 0.1
				}}
				anti_tank_brigade = {{
					hard_attack = 0.1
					ap_attack = 0.1
				}}
				mot_anti_tank_brigade = {{
					hard_attack = 0.05
					ap_attack = 0.1
				}}
				category_tank_destroyers = {{
					hard_attack = 0.05
					ap_attack = 0.05
				}}

				{antitank_path}
			}}
		'''

	content += '}\n'

	with open(file, 'w') as f:
		f.write(content)

extend_land_doctorine(os.path.join(HERE, 'gucci_land_doctorine.txt'), 12)
extend_industry      (os.path.join(HERE, 'gucci_industry.txt')      ,  7)
extend_air_doctorine (os.path.join(HERE, 'gucci_air_doctorine.txt') , 12)
extend_artillery     (os.path.join(HERE, 'gucci_artillery.txt')     ,  7)
