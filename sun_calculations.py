import numpy as np
from constants import SOLAR_CONSTANTS

def calculate_sun_position(latitude, day_of_year):
    # Convert inputs to radians
    lat = np.radians(latitude)
    
    # Calculate solar declination
    declination = np.radians(23.45 * np.sin(np.radians((360/365) * (day_of_year - 81))))
    
    # Generate hour angles for the day (-π to π)
    hour_angles = np.linspace(-np.pi, np.pi, 100)
    
    # Calculate solar altitude
    altitude = np.arcsin(
        np.sin(lat) * np.sin(declination) +
        np.cos(lat) * np.cos(declination) * np.cos(hour_angles)
    )
    
    # Calculate solar azimuth with better numerical stability
    sin_azimuth = -np.cos(declination) * np.sin(hour_angles)
    cos_azimuth = np.cos(lat) * np.sin(declination) - np.sin(lat) * np.cos(declination) * np.cos(hour_angles)
    
    # Add small epsilon to prevent division by very small numbers
    epsilon = 1e-10
    sin_azimuth = np.where(np.abs(sin_azimuth) < epsilon, np.sign(sin_azimuth) * epsilon, sin_azimuth)
    cos_azimuth = np.where(np.abs(cos_azimuth) < epsilon, np.sign(cos_azimuth) * epsilon, cos_azimuth)
    
    azimuth = np.arctan2(sin_azimuth, cos_azimuth)
    # Adjust azimuth to be in 0-360 range instead of -180 to 180
    azimuth = np.where(azimuth < 0, azimuth + 2*np.pi, azimuth)
    
    # Convert to degrees
    altitude_deg = np.degrees(altitude)
    azimuth_deg = np.degrees(azimuth)
    hour_angles_deg = np.degrees(hour_angles)
    
    return hour_angles_deg, altitude_deg, azimuth_deg, np.degrees(declination)

def day_to_declination(day):
    return 23.45 * np.sin(np.radians((360/365) * (day - 81)))

def declination_to_day(declination):
    # Convert declination to day of year
    # We need to handle the fact that there are two days with the same declination
    # We'll return the day closest to the current day
    day = 81 + (365/(2*np.pi)) * np.arcsin(declination/23.45)
    # Ensure the day is in the range [1, 365]
    day = day % 365
    if day < 1:
        day += 365
    return day 