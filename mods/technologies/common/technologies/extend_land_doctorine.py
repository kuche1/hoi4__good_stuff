from pathlib import Path

SUPPOSEDLY_AVERAGE_DOCTORINE_STATS = r"""
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
"""


def extend_land_doctorine(file: Path, extensions: int) -> None:
    content = ""
    content += "technologies = {\n"

    for doctorine_idx in range(extensions):
        doctorine_num = doctorine_idx + 1
        doctorine_num_next = doctorine_num + 1

        doctrine_name = (
            'doctrine_name = "GUCCI_WARFARE_DOCTRINE"' if doctorine_idx == 0 else ""
        )
        doctorine_cost = 250 if doctorine_idx == 0 else 195

        doctorine_pos_y = 22 + (2 * doctorine_idx)

        doctorine_path = f"""
			path = {{
				leads_to_tech = gucci_warfare_{doctorine_num_next}
			}}
		"""
        if doctorine_idx == extensions - 1:
            doctorine_path = ""

        content += f"""
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
				{SUPPOSEDLY_AVERAGE_DOCTORINE_STATS}

				{doctorine_path}
			}}
		"""

    content += "}\n"

    with open(file, "w") as f:
        f.write(content)


# def extend_land_doctorine(file: Path, extentions: int) -> None:
#     file.unlink()
