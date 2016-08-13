"""Module containing methods used for computing water related
quantities in the idealized moist gray radiation model.
"""
from aospy.constants import L_v


def precip(condensation_rain, convection_rain):
    """Returns the total precipitation rate in the gray atmosphere idealized
    moist model.  This is just the sum of the condensation- and convection-
    induced rain.

    Parameters
    ----------
    condensation_rain : DataArray
        Condensation precipitation rate
    convection_rain : DataArray
        Convection precipitation rate

    Returns
    -------
    precip : DataArray
        Sum of condensation and convection precipitation rates
    """
    print condensation_rain
    return condensation_rain + convection_rain


def evap(flux_lhe):
    """Returns the evaporation rate of water in the gray atmosphere idealized
    moist model.  In this context it must be inferred from the latent heat flux
    at the surface.

    Parameters
    ----------
    flux_lhe : DataArray
        Latent heat flux of energy into the atmosphere

    Returns
    -------
    evap : DataArray
        Evaporation rate of water into the atmosphere
    """
    return flux_lhe / L_v.value


def p_minus_e(condensation_rain, convection_rain, flux_lhe):
    """Returns the precipitation minus evaporation in the gray atmosphere
    idealized moist model.

    Parameters
    ----------
    condensation_rain : DataArray
        Condensation precipitation rate
    convection_rain : DataArray
        Convection precipitation rate
    flux_lhe : DataArray
        Latent heat flux of energy into the atmosphere

    Returns
    -------
    p_minus_e : DataArray
        Precipitation rate minus evaporation rate
    """
    return precip(condensation_rain, convection_rain) - evap(flux_lhe)


def cond_minus_e(condensation_rain, flux_lhe):
    """Returns the condensation rain minus evaporation in the gray atmosphere
    idealized moist model.

    Parameters
    ----------
    condensation_rain : DataArray
        Condensation precipitation rate
    flux_lhe : DataArray
        Latent heat flux of energy into the atmosphere

    Returns
    -------
    cond_minus_e : DataArray
        Condensation rain rate minus evaporation rate
    """
    return condensation_rain - evap(flux_lhe)
