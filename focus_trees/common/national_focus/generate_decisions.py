#! /usr/bin/env python3

ITERATIONS = 20

# [[[ITER]]]
# [[[ITER_PREV]]]
TEXT = '''

	#####
	##### iteration: [[[ITER]]]
	#####

	focus = {
		id = decision_[[[ITER]]]_civ
		icon = GFX_goal_generic_construct_civ_factory
		prerequisite = { focus=decision_[[[ITER_PREV]]]_civ focus=decision_[[[ITER_PREV]]]_balance focus=decision_[[[ITER_PREV]]]_mil focus=decision_[[[ITER_PREV]]]_army focus=decision_[[[ITER_PREV]]]_war }
		relative_position_id = decision_[[[ITER_PREV]]]_mil
		mutually_exclusive = { focus = decision_[[[ITER]]]_balance focus = decision_[[[ITER]]]_mil focus = decision_[[[ITER]]]_army focus = decision_[[[ITER]]]_war }

		x = -4
		y = 1
		cost = 10

		completion_reward = {
			random_owned_controlled_state = {
				limit = {
					free_building_slots = {
						building = industrial_complex
						size > 0
						include_locked = yes
					}
					OR = {
						is_in_home_area = yes
						NOT = {
							owner = {
								any_owned_state = {
									free_building_slots = {
										building = industrial_complex
										size > 0
										include_locked = yes
									}
									is_in_home_area = yes
								}
							}
						}
					}
				}
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 2
					instant_build = yes
				}
			}
		}
	}

	focus = {
		id = decision_[[[ITER]]]_balance
		icon = GFX_goal_generic_neutrality_focus
		prerequisite = { focus=decision_[[[ITER_PREV]]]_civ focus=decision_[[[ITER_PREV]]]_balance focus=decision_[[[ITER_PREV]]]_mil focus=decision_[[[ITER_PREV]]]_army focus=decision_[[[ITER_PREV]]]_war }
		mutually_exclusive = { focus = decision_[[[ITER]]]_civ focus = decision_[[[ITER]]]_mil focus = decision_[[[ITER]]]_army focus = decision_[[[ITER]]]_war }
		relative_position_id = decision_[[[ITER]]]_civ

		x = 2
		y = 0
		cost = 10

		completion_reward = {
			random_owned_controlled_state = {
				limit = {
					free_building_slots = {
						building = industrial_complex
						size > 0
						include_locked = yes
					}
					OR = {
						is_in_home_area = yes
						NOT = {
							owner = {
								any_owned_state = {
									free_building_slots = {
										building = industrial_complex
										size > 0
										include_locked = yes
									}
									is_in_home_area = yes
								}
							}
						}
					}
				}
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
		}
	}

	focus = {
		id = decision_[[[ITER]]]_mil
		icon = GFX_goal_generic_construct_mil_factory
		prerequisite = { focus=decision_[[[ITER_PREV]]]_civ focus=decision_[[[ITER_PREV]]]_balance focus=decision_[[[ITER_PREV]]]_mil focus=decision_[[[ITER_PREV]]]_army focus=decision_[[[ITER_PREV]]]_war }
		mutually_exclusive = { focus = decision_[[[ITER]]]_balance focus = decision_[[[ITER]]]_civ focus = decision_[[[ITER]]]_army focus = decision_[[[ITER]]]_war }
		relative_position_id = decision_[[[ITER]]]_civ

		x = 4
		y = 0
		cost = 10

		completion_reward = {
			random_owned_controlled_state = {
				limit = {
					free_building_slots = {
						building = industrial_complex
						size > 0
						include_locked = yes
					}
					OR = {
						is_in_home_area = yes
						NOT = {
							owner = {
								any_owned_state = {
									free_building_slots = {
										building = industrial_complex
										size > 0
										include_locked = yes
									}
									is_in_home_area = yes
								}
							}
						}
					}
				}
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = arms_factory
					level = 2
					instant_build = yes
				}
			}
		}
	}

	focus = {
		id = decision_[[[ITER]]]_army
		icon = GFX_goal_generic_allies_build_infantry
		prerequisite = { focus=decision_[[[ITER_PREV]]]_civ focus=decision_[[[ITER_PREV]]]_balance focus=decision_[[[ITER_PREV]]]_mil focus=decision_[[[ITER_PREV]]]_army focus=decision_[[[ITER_PREV]]]_war }
		mutually_exclusive = { focus = decision_[[[ITER]]]_civ focus = decision_[[[ITER]]]_balance focus = decision_[[[ITER]]]_mil focus = decision_[[[ITER]]]_war }
		relative_position_id = decision_[[[ITER]]]_civ

		x = 6
		y = 0
		cost = 10

		completion_reward = {

			army_experience = 25

			add_doctrine_cost_reduction = {
				cost_reduction = 0.5
				uses = 1
				category = land_doctrine
			}

			add_doctrine_cost_reduction = {
				cost_reduction = 0.5
				uses = 1
				category = air_doctrine
			}

			add_doctrine_cost_reduction = {
				cost_reduction = 0.5
				uses = 1
				category = naval_doctrine
			}

			random_owned_controlled_state = {
				limit = {
					free_building_slots = {
						building = industrial_complex
						size > 0
						include_locked = yes
					}
					OR = {
						is_in_home_area = yes
						NOT = {
							owner = {
								any_owned_state = {
									free_building_slots = {
										building = industrial_complex
										size > 0
										include_locked = yes
									}
									is_in_home_area = yes
								}
							}
						}
					}
				}
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
		}
	}

	focus = {
		id = decision_[[[ITER]]]_war
		icon = GFX_goal_generic_wolf_pack
		prerequisite = { focus=decision_[[[ITER_PREV]]]_civ focus=decision_[[[ITER_PREV]]]_balance focus=decision_[[[ITER_PREV]]]_mil focus=decision_[[[ITER_PREV]]]_army focus=decision_[[[ITER_PREV]]]_war }
		mutually_exclusive = { focus = decision_[[[ITER]]]_civ focus = decision_[[[ITER]]]_balance focus = decision_[[[ITER]]]_mil focus = decision_[[[ITER]]]_army }
		relative_position_id = decision_[[[ITER]]]_civ

		x = 8
		y = 0
		cost = 10

		available = {
			has_idea = ideological_fanaticism_focus
		}

		completion_reward = {

			army_experience = 50

			add_doctrine_cost_reduction = {
				cost_reduction = 0.75
				uses = 1
				category = land_doctrine
			}

			add_doctrine_cost_reduction = {
				cost_reduction = 0.75
				uses = 1
				category = air_doctrine
			}

			add_doctrine_cost_reduction = {
				cost_reduction = 0.75
				uses = 1
				category = naval_doctrine
			}

			random_owned_controlled_state = {
				limit = {
					free_building_slots = {
						building = industrial_complex
						size > 0
						include_locked = yes
					}
					OR = {
						is_in_home_area = yes
						NOT = {
							owner = {
								any_owned_state = {
									free_building_slots = {
										building = industrial_complex
										size > 0
										include_locked = yes
									}
									is_in_home_area = yes
								}
							}
						}
					}
				}
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = arms_factory
					level = 2
					instant_build = yes
				}
			}

			# gain war goal fora random neighbour
			random_neighbor_country = {
				ROOT = { # war will be declared by
					create_wargoal = {
						type = annex_everything
						target = PREV # war will be delared on
					}
				}
			}

		}
	}
'''

for iter in range(2, ITERATIONS+1):
    text = TEXT
    text = text.replace('[[[ITER]]]', str(iter))
    text = text.replace('[[[ITER_PREV]]]', str(iter-1))

    # print(text.count('[[[ITER]]]'))
    print(text)
