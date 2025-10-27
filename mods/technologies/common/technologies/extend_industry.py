def extend_industry(file, extensions):
    content = ""
    content += "technologies = {\n"

    for idx in range(extensions):
        is_first = idx == 0
        is_last = idx == extensions - 1
        is_regular = (not is_first) and (not is_last)

        pos_y = 14 + idx * 2

        year = 1944 + idx * 1

        ind_name_current = f"gucci_industry_{idx + 1}"
        ind_name_next = f"gucci_industry_{idx + 2}"

        prod_name_current = f"guci_production_{idx + 1}"
        prod_name_next = f"guci_production_{idx + 2}"

        cons_name_current = f"gucci_construction_{idx + 1}"
        cons_name_next = f"gucci_construction_{idx + 2}"

        if is_first:
            ind_pos_y = pos_y - 2
        else:
            ind_pos_y = pos_y

        # path: industry

        if is_first:
            ind_path = f"""
				path = {{
					leads_to_tech = {ind_name_next}
				}}
				path = {{
					leads_to_tech = {prod_name_current}
				}}
				path = {{
					leads_to_tech = {cons_name_current}
				}}
			"""
        elif is_regular:
            ind_path = f"""
				path = {{
					leads_to_tech = {ind_name_next}
				}}
			"""
        else:
            ind_path = ""

        # path: production

        if is_first or is_regular:
            prod_path = f"""
				path = {{
					leads_to_tech = {prod_name_next}
				}}
			"""
        else:
            prod_path = ""

        # path: construction

        if is_first or is_regular:
            cons_path = f"""
				path = {{
					leads_to_tech = {cons_name_next}
				}}
			"""
        else:
            cons_path = ""

        # save

        content += f"""

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
		"""

    content += "}\n"

    with open(file, "w") as f:
        f.write(content)
