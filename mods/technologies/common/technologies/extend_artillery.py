def extend_artillery(file, extensions):
    content = ""
    content += "technologies = {\n"

    for idx in range(extensions):
        is_first = idx == 0
        is_last = idx == extensions - 1
        is_regular = (not is_first) and (not is_last)

        pos_y = 16 + idx * 2

        year = 1944 + idx

        num_cur = idx + 1
        num_next = idx + 2

        art_name = "gucci_artillery_"
        rockart_name = "gucci_rocket_artillery_"
        antiair_name = "gucci_antiair_"
        antitank_name = "gucci_antitank_"

        # artillery

        art_pos_y = pos_y
        if is_first:
            art_pos_y -= 2

        if is_first:
            art_path = f"""
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
			"""
        elif is_regular:
            art_path = f"""
				path = {{
					leads_to_tech = {art_name}{num_next}
				}}
			"""
        else:
            art_path = ""

        # rocket artillery

        if is_last:
            rockart_path = ""
        else:
            rockart_path = f"""
				path = {{
					leads_to_tech = {rockart_name}{num_next}
				}}
			"""

        # antiair

        if is_last:
            antiair_path = ""
        else:
            antiair_path = f"""
				path = {{
					leads_to_tech = {antiair_name}{num_next}
				}}
			"""

        # antitant

        if is_last:
            antitank_path = ""
        else:
            antitank_path = f"""
				path = {{
					leads_to_tech = {antitank_name}{num_next}
				}}
			"""

        # actual file content

        content += f"""
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
		"""

        content += f"""
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
		"""

        content += f"""
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
		"""

        content += f"""
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
		"""

    content += "}\n"

    with open(file, "w") as f:
        f.write(content)
