from pathlib import Path


def extend_air_doctorine(file: Path, extensions: int) -> None:
    content = ""
    content += "technologies = {\n"

    for idx in range(extensions):
        is_first = idx == 0
        is_last = idx == extensions - 1

        pos_y = 20 + idx * 2

        # NOTE:
        # i'm taking advantage of `air_superiority` for the first doctorine so that I dont have to edit the stupid game files
        # TODO this actually causes a bug where you are able to research the additional doctorines if you have the original `air_superiority` tdoctorine
        if is_first:
            name_cur = "air_superiority"
        else:
            name_cur = f"gucci_air_doctorine_{idx + 1}"

        name_next = f"gucci_air_doctorine_{idx + 2}"

        if is_first:
            doctorine_name = 'doctrine_name = "TITLE_GUCCI_AIR_DOCTORINE"'
        else:
            doctorine_name = ""

        if is_first:
            cost = 250
        else:
            cost = 100

        if is_last:
            path = ""
        else:
            path = f"""
				path = {{
					leads_to_tech = {name_next}
				}}
			"""

        content += f"""
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
		"""

    content += "}\n"

    with open(file, "w") as f:
        f.write(content)
