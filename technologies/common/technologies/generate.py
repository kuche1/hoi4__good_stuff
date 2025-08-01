#! /usr/bin/env python3

# generally the target is to extend everything till 1950

import os

HERE = os.path.dirname(__file__)

SUPPOSEDLY_AAVERAGE_DOCTORINE_STATS = r'''
infantry = {
	combat_width = -0.0175        # -0.7 / 40
	default_morale = 0.0075       # 0.30 / 40
}

category_all_infantry = {
	max_organisation = 3.25       # 130 / 40
	default_morale = 0.01125
	defense = 0.01
	soft_attack = 0.0025
	hard_attack = 0.00125
	breakthrough = 0.0025
}

category_cavalry = {
	breakthrough = 0.0125
	maximum_speed = 0.015
	default_morale = 0.005
	supply_consumption = -0.001
	#max_organisation = 0 # what the fuck is this ????
}

category_vehicle_infantry = {
	max_organisation = 0.875
	default_morale = 0.0025
}

category_all_armor = {
	breakthrough = 0.015
	maximum_speed = 0.005
	default_morale = 0.01625
	hard_attack = 0.0025
	soft_attack = 0.0025
}

category_tanks = {
	max_organisation = 0.75
	breakthrough = 0.0125
}

category_mobile_and_mobile_combat_sup = {
	maximum_speed = 0.0025
	default_morale = 0.005
}

recon = {
	maximum_speed = 0.01125
	battalion_mult = {
		category = category_light_infantry
		soft_attack = 0.00125
	}
	battalion_mult = {
		category = category_cavalry
		soft_attack = 0.00125
	}
	recon = 0.025
}

mot_recon = {
	maximum_speed = 0.0025
	battalion_mult = {
		category = category_anti_air
		air_attack = 0.0025
	}
}

armored_car = {
	max_organisation = 1
	default_morale = 0.01375
	breakthrough = 0.0075
}

armored_car_recon = {
	maximum_speed = 0.0025
	battalion_mult = {
		category = category_all_armor
		breakthrough = 0.0025
	}
	battalion_mult = {
		category = category_light_infantry
		max_organisation = 0.025
		add = yes
	}
}

category_light_infantry = {
	max_organisation = 0.875
	breakthrough = 0.0025
}

category_line_artillery = {
	soft_attack = 0.0025
	default_morale = 0.005
}

category_front_line = {
	max_organisation = 0.125
	soft_attack = 0.00625
}

category_support_battalions = {
	max_organisation = 0.5
	soft_attack = 0.0125
}

signal_company = {
	battalion_mult = {
		category = category_artillery
		defense = 0.0025
	}
}

category_army = {
	hard_attack = 0.0025
	breakthrough = 0.0075
	soft_attack = 0.0025
	default_morale = 0.005
}

category_artillery = {
	soft_attack = 0.0025
	hard_attack = 0.00125
}

category_recon = {
	recon = 0.025
}

logistics_company = {
	battalion_mult = {
		category = category_all_infantry
		defense = 0.00125
	}
}

#additional_brigade_column_size = 0.2
army_speed_factor = 0.005
army_bonus_air_superiority_factor = 0.00375
coordination_bonus = 0.00375
conscription = 0.0025
land_reinforce_rate = 0.0115
org_loss_when_moving = -0.01125
planning_speed = 0.035
resistance_damage_to_garrison_on_our_occupied_states = 0.005
resistance_growth_on_our_occupied_states = 0.00625
command_power_gain = 0.0125
command_power_gain_mult = 0.00375
dig_in_speed_factor = 0.0125
max_command_power = 0.75
max_dig_in = 0.75
max_planning = 0.0125
land_night_attack = 0.00625
supply_consumption_factor = -0.0075
minimum_training_level = -0.005
no_supply_grace = 2.4
out_of_supply_factor = -0.0125
weekly_casualties_war_support = 0.00005
attrition = -0.0025
'''

def extend_land_doctorine(file, extensions):

	content = ''
	content += 'technologies = {\n'

	for doctorine_idx in range(extensions):

		doctorine_num = doctorine_idx + 1
		doctorine_num_next = doctorine_num + 1

		doctrine_name = 'doctrine_name = "GUCCI_WARFARE_DOCTRINE"' if doctorine_idx == 0 else ''
		doctorine_cost = 250 if doctorine_idx == 0 else 195

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

				#### those are the original stats that I made up
				## we have `category_front_line`, `category_army`, and also we could just ignore putting a categoty
				#category_army = {{
                #
				#	soft_attack = 0.06
				#	hard_attack = 0.06
				#	breakthrough = 0.06
                #
				#	default_morale = 0.01 # recovery rate
				#	defense = 0.01
                #
				#	# supply_consumption = -0.02
				#	max_organisation = 1
				#}}
				#supply_consumption_factor = -0.01
				#army_speed_factor = 0.01
				#planning_speed = 0.05

				##### those are the "summed up" stats
				{SUPPOSEDLY_AAVERAGE_DOCTORINE_STATS}

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
		# i'm taking advantage of `air_superiority` for the first doctorine so that I dont have to edit the stupid game files
		# TODO this actually causes a bug where you are able to research the additional doctorines if you have the original `air_superiority` tdoctorine
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
				#air_strategic_bomber_bombing_factor = 0.04
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

extend_land_doctorine(os.path.join(HERE, 'gucci_land_doctorine.txt'), 18)
extend_industry      (os.path.join(HERE, 'gucci_industry.txt')      ,  7)
extend_air_doctorine (os.path.join(HERE, 'gucci_air_doctorine.txt') , 12)
extend_artillery     (os.path.join(HERE, 'gucci_artillery.txt')     ,  7)
