"""
Tire strategy and degradation analysis functions.
"""

import numpy as np
import pandas as pd


def prepare_lap_data(laps):
    """
    Prepare lap data for tire analysis.

    Converts LapTime into seconds and removes
    rows without valid lap or tire information.
    """

    data = laps.copy()

    # Remove missing lap times
    data = data[
        data["LapTime"].notna()
    ]

    # Remove missing compounds
    data = data[
        data["Compound"].notna()
    ]

    # Remove missing lap numbers
    data = data[
        data["LapNumber"].notna()
    ]

    # Convert lap time to seconds
    data["LapTimeSeconds"] = (
        data["LapTime"]
        .dt.total_seconds()
    )

    return data


def calculate_compound_pace(laps):
    """
    Calculate average lap time, best lap time,
    and lap count for each tire compound.
    """

    data = prepare_lap_data(laps)

    compound_pace = (
        data
        .groupby("Compound")
        .agg(
            AverageLapTime=(
                "LapTimeSeconds",
                "mean"
            ),
            BestLapTime=(
                "LapTimeSeconds",
                "min"
            ),
            LapCount=(
                "LapTimeSeconds",
                "count"
            )
        )
        .reset_index()
    )

    return compound_pace


def calculate_tire_stints(laps):
    """
    Calculate tire stint information.
    """

    data = prepare_lap_data(laps)

    stint_data = (
        data
        .groupby(
            [
                "Driver",
                "Stint",
                "Compound"
            ]
        )
        .agg(
            StartLap=(
                "LapNumber",
                "min"
            ),
            EndLap=(
                "LapNumber",
                "max"
            ),
            Laps=(
                "LapNumber",
                "count"
            ),
            MaxTyreLife=(
                "TyreLife",
                "max"
            )
        )
        .reset_index()
    )

    return stint_data


def calculate_longest_stint(laps):
    """
    Find the longest tire stint for each driver.
    """

    stint_data = calculate_tire_stints(
        laps
    )

    longest_stints = (
        stint_data
        .sort_values(
            "Laps",
            ascending=False
        )
        .groupby("Driver")
        .head(1)
        .reset_index(drop=True)
    )

    return longest_stints


def calculate_degradation(laps):
    """
    Estimate tire degradation using
    linear regression.

    Degradation is represented as:

    seconds per lap of tire life.

    Positive value:
    lap times increase as tire ages.

    Negative value:
    lap times decrease as tire ages.
    """

    data = prepare_lap_data(laps)

    results = []

    grouped = data.groupby(
        [
            "Driver",
            "Compound"
        ]
    )

    for (driver, compound), group in grouped:

        group = group.dropna(
            subset=[
                "TyreLife",
                "LapTimeSeconds"
            ]
        )

        # Need at least 3 points
        if len(group) < 3:
            continue

        x = group["TyreLife"].values
        y = group["LapTimeSeconds"].values

        # Linear regression
        slope, intercept = np.polyfit(
            x,
            y,
            1
        )

        # Correlation
        correlation = np.corrcoef(
            x,
            y
        )[0, 1]

        results.append(
            {
                "Driver": driver,
                "Compound": compound,
                "Degradation_sec_per_lap": slope,
                "Correlation": correlation,
                "DataPoints": len(group)
            }
        )

    return pd.DataFrame(results)