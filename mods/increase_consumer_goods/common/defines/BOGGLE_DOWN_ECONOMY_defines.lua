
-- minimum consumer goods
-- should be default plus the additional amount
--NDefines.NProduction.MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_PERCENT = NDefines.NProduction.MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_PERCENT + 0.05 -- default 0.1

-- civ, mil and doc output
NDefines.NProduction.BASE_FACTORY_SPEED     = NDefines.NProduction.BASE_FACTORY_SPEED_MIL * 0.9 -- default 5   -- make civs produce less
NDefines.NProduction.BASE_FACTORY_SPEED_MIL = NDefines.NProduction.BASE_FACTORY_SPEED_MIL * 0.9 -- default 4.5 -- make mils produce less
NDefines.NProduction.BASE_FACTORY_SPEED_NAV = NDefines.NProduction.BASE_FACTORY_SPEED_NAV * 0.9 -- default 2.5 -- make docs produce less

NDefines.NCountry.POPULATION_YEARLY_GROWTH_BASE = NDefines.NCountry.POPULATION_YEARLY_GROWTH_BASE * 0.9 -- population growth
