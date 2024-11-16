
-- base compliance growth
NDefines.NResistance.COMPLIANCE_GROWTH_BASE = NDefines.NResistance.COMPLIANCE_GROWTH_BASE * 1.7

-- compliance growth when at piece
-- `10` stands for `10%`
-- default 10
NDefines.NResistance.COMPLIANCE_GROWTH_IS_AT_PEACE = NDefines.NResistance.COMPLIANCE_GROWTH_IS_AT_PEACE * 1.7

-- compliance growth if claim
-- default 5
NDefines.NResistance.COMPLIANCE_GROWTH_HAS_CLAIM = NDefines.NResistance.COMPLIANCE_GROWTH_HAS_CLAIM * 1.7

-- wtf does this even do? the following comment is not true:
-- `-0.5` stands for loose half your compliance on controller change (this does include changing ideology)
-- default -0.5
--NDefines.NResistance.COMPLIANCE_FACTOR_ON_STATE_CONTROLLER_CHANGE = 0 
