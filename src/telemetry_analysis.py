"""
Driver telemetry analysis functions.

This module contains functions for:
- Selecting drivers
- Finding fastest laps
- Extracting telemetry
- Calculating speed statistics
- Calculating throttle statistics
- Calculating braking statistics
"""

import numpy as np
import pandas as pd


def get_driver_laps(session, driver):
    """
    Get all laps for a specific driver.
    """

    return session.laps.pick_drivers(driver)


def get_fastest_lap(session, driver):
    """
    Get the fastest lap for a specific driver.
    """

    driver_laps = get_driver_laps(
        session,
        driver
    )

    return driver_laps.pick_fastest()


def get_lap_telemetry(fastest_lap):
    """
    Extract car telemetry from a lap
    and add distance along the track.
    """

    telemetry = (
        fastest_lap
        .get_car_data()
        .add_distance()
    )

    return telemetry


def get_basic_telemetry_statistics(telemetry):
    """
    Calculate basic telemetry statistics.
    """

    statistics = {
        "Telemetry Data Points": len(telemetry),
        "Maximum Speed (km/h)": telemetry["Speed"].max(),
        "Average Speed (km/h)": telemetry["Speed"].mean(),
        "Maximum Throttle (%)": telemetry["Throttle"].max(),
        "Maximum RPM": telemetry["RPM"].max()
    }

    return statistics


def calculate_throttle_statistics(telemetry):
    """
    Calculate the percentage of telemetry points
    spent at high and low throttle.

    High throttle:
    >= 95%

    Low throttle:
    <= 5%
    """

    total_points = len(telemetry)

    high_throttle_points = (
        telemetry["Throttle"] >= 95
    ).sum()

    low_throttle_points = (
        telemetry["Throttle"] <= 5
    ).sum()

    high_throttle_percentage = (
        high_throttle_points /
        total_points *
        100
    )

    low_throttle_percentage = (
        low_throttle_points /
        total_points *
        100
    )

    return {
        "High Throttle (%)": high_throttle_percentage,
        "Low Throttle (%)": low_throttle_percentage
    }


def calculate_speed_comparison(
    telemetry_driver1,
    telemetry_driver2,
    driver1_name="Driver 1",
    driver2_name="Driver 2"
):
    """
    Compare the speed of two drivers
    using distance along the track.

    Returns a dataframe containing:
    - Distance
    - Driver 1 speed
    - Driver 2 speed
    - Speed difference
    """

    # Create copies
    data1 = telemetry_driver1.copy()
    data2 = telemetry_driver2.copy()

    # Determine common distance
    max_distance = min(
        data1["Distance"].max(),
        data2["Distance"].max()
    )

    # Create common distance points
    comparison_distance = np.linspace(
        0,
        max_distance,
        1000
    )

    # Interpolate speeds
    speed1 = np.interp(
        comparison_distance,
        data1["Distance"],
        data1["Speed"]
    )

    speed2 = np.interp(
        comparison_distance,
        data2["Distance"],
        data2["Speed"]
    )

    comparison = pd.DataFrame(
        {
            "Distance": comparison_distance,
            f"{driver1_name}Speed": speed1,
            f"{driver2_name}Speed": speed2
        }
    )

    comparison["SpeedDifference"] = (
        comparison[f"{driver1_name}Speed"]
        -
        comparison[f"{driver2_name}Speed"]
    )

    return comparison


def calculate_speed_advantage(
    comparison,
    driver1_name="Driver 1",
    driver2_name="Driver 2"
):
    """
    Calculate how often each driver is faster.
    """

    difference = comparison["SpeedDifference"]

    driver1_faster = (
        difference > 0
    ).mean() * 100

    driver2_faster = (
        difference < 0
    ).mean() * 100

    within_one = (
        difference.abs() <= 1
    ).mean() * 100

    return {
        f"{driver1_name} Faster (%)": driver1_faster,
        f"{driver2_name} Faster (%)": driver2_faster,
        "Within ±1 km/h (%)": within_one
    }


def find_largest_speed_differences(
    comparison,
    driver1_name="Driver 1",
    driver2_name="Driver 2"
):
    """
    Find the largest speed advantage
    for each driver.
    """

    driver1_row = comparison.loc[
        comparison["SpeedDifference"].idxmax()
    ]

    driver2_row = comparison.loc[
        comparison["SpeedDifference"].idxmin()
    ]

    return driver1_row, driver2_row