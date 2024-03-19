"""
File: aero.py
Description: DSAL-PY aerospace math formula functions

Date: February 21st, 2024
Copyright: Copyright (c) 2023 Lukas R. Jackson, Vanguard Precision, Gothric Solitions. 

Author: Lukas R. Jackson (LukasJacksonEG@gmail.com)

License: BSD-3-Clause License
         Copyright (c) 2023 Lukas R. Jackson, Vanguard Precision
         All rights reserved.

         Redistribution and use in source and binary forms, with or without
         modification, are permitted provided that the following conditions are met:

         1. Redistributions of source code must retain the above copyright notice,
            this list of conditions and the following disclaimer.
         2. Redistributions in binary form must reproduce the above copyright notice,
            this list of conditions and the following disclaimer in the documentation
            and/or other materials provided with the distribution.
         3. Neither the name of the copyright holder nor the names of its contributors
            may be used to endorse or promote products derived from this software
            without specific prior written permission.

         THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
         ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
         WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
         DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
         FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
         DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
         SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
         CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
         OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
         OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


def knots_to_mps(knots):
    """Converts speed from knots to meters per second."""
    return knots * 0.514444

def mps_to_knots(mps):
    """Converts speed from meters per second to knots."""
    return mps / 0.514444

def true_airspeed(ias, pressure_altitude, static_air_temp):
    """Calculates true airspeed (TAS) using indicated airspeed (IAS), pressure altitude, and static air temperature."""
    pressure_altitude_ft = pressure_altitude * 3.28084  # Convert pressure altitude to feet
    temp_celsius = (static_air_temp - 32) * 5/9  # Convert static air temperature to Celsius
    pressure_ratio = (1 - 0.0000068756 * pressure_altitude_ft) ** 5.25588  # Pressure ratio
    return ias * pressure_ratio / ((273.15 + temp_celsius) / 273.15) ** 0.5

def mach_number(tas, speed_of_sound):
    """Calculates Mach number using true airspeed (TAS) and speed of sound."""
    return tas / speed_of_sound

def density_altitude(pressure_altitude, oat):
    """Calculates density altitude using pressure altitude and outside air temperature (OAT)."""
    pressure_altitude_ft = pressure_altitude * 3.28084  # Convert pressure altitude to feet
    return pressure_altitude_ft + ((15 - oat) * 120)

def stall_speed(weight, wing_area, cl_max, air_density):
    """Calculates stall speed using weight, wing area, maximum lift coefficient, and air density."""
    return ((2 * weight) / (wing_area * cl_max * air_density)) ** 0.5
