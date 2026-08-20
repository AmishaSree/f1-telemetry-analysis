"""
Main analysis script for the F1 Telemetry Project.

This script:
- Loads F1 qualifying and race data
- Compares two drivers
- Analyzes telemetry
- Analyzes throttle usage
- Compares speed
- Analyzes tire strategy
- Calculates tire degradation
- Saves analysis results as CSV files
"""

import sys
from pathlib import Path

import pandas as pd


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Add project root to Python path
sys.path.append(
    str(PROJECT_ROOT)
)


# ============================================================
# OUTPUT DIRECTORIES
# ============================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

FIGURES_DIR = OUTPUT_DIR / "figures"

TABLES_DIR = OUTPUT_DIR / "tables"


# Create directories automatically
FIGURES_DIR.mkdir(
    parents=True,
    exist_ok=True
)

TABLES_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# IMPORT PROJECT MODULES
# ============================================================

from src.data_loader import (
    load_f1_session,
    get_driver_results
)

from src.telemetry_analysis import (
    get_driver_laps,
    get_fastest_lap,
    get_lap_telemetry,
    get_basic_telemetry_statistics,
    calculate_throttle_statistics,
    calculate_speed_comparison,
    calculate_speed_advantage,
    find_largest_speed_differences
)

from src.tire_analysis import (
    calculate_compound_pace,
    calculate_tire_stints,
    calculate_longest_stint,
    calculate_degradation
)


# ============================================================
# HELPER FUNCTION - SAVE DATAFRAME
# ============================================================

def save_dataframe(dataframe, filename):
    """
    Save a pandas DataFrame to outputs/tables/.
    """

    output_path = TABLES_DIR / filename

    dataframe.to_csv(
        output_path,
        index=False
    )

    print(
        f"Saved: {output_path}"
    )


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():

    print("\n")
    print("=" * 70)
    print("        F1 TELEMETRY & TIRE STRATEGY ANALYSIS")
    print("=" * 70)


    # ========================================================
    # STEP 1 - LOAD QUALIFYING SESSION
    # ========================================================

    session = load_f1_session(
        year=2026,
        event="Australia",
        session_type="Q",
        cache_dir=str(
            PROJECT_ROOT / "cache"
        )
    )


    # ========================================================
    # STEP 2 - DRIVER RESULTS
    # ========================================================

    print("\n")
    print("=" * 70)
    print("DRIVERS")
    print("=" * 70)

    driver_results = get_driver_results(
        session
    )

    print(
        driver_results
    )

    # Save driver results
    save_dataframe(
        driver_results,
        "driver_results.csv"
    )


    # ========================================================
    # STEP 3 - SELECT DRIVERS
    # ========================================================

    driver1 = "RUS"
    driver2 = "LEC"

    print("\nSelected drivers:")
    print("George Russell - RUS")
    print("Charles Leclerc - LEC")


    # ========================================================
    # STEP 4 - GET LAPS
    # ========================================================

    russell_laps = get_driver_laps(
        session,
        driver1
    )

    leclerc_laps = get_driver_laps(
        session,
        driver2
    )

    print("\n")
    print("=" * 70)
    print("LAP COUNTS")
    print("=" * 70)

    print(
        f"George Russell: {len(russell_laps)} laps"
    )

    print(
        f"Charles Leclerc: {len(leclerc_laps)} laps"
    )


    # ========================================================
    # STEP 5 - FASTEST LAPS
    # ========================================================

    fastest_russell = get_fastest_lap(
        session,
        driver1
    )

    fastest_leclerc = get_fastest_lap(
        session,
        driver2
    )

    print("\n")
    print("=" * 70)
    print("FASTEST LAP COMPARISON")
    print("=" * 70)

    print(
        "George Russell:",
        fastest_russell["LapTime"]
    )

    print(
        "Charles Leclerc:",
        fastest_leclerc["LapTime"]
    )


    # ========================================================
    # STEP 6 - TELEMETRY
    # ========================================================

    telemetry_russell = get_lap_telemetry(
        fastest_russell
    )

    telemetry_leclerc = get_lap_telemetry(
        fastest_leclerc
    )

    print("\n")
    print("=" * 70)
    print("TELEMETRY STATISTICS")
    print("=" * 70)


    # Get basic telemetry statistics
    russell_telemetry_stats = (
        get_basic_telemetry_statistics(
            telemetry_russell
        )
    )

    leclerc_telemetry_stats = (
        get_basic_telemetry_statistics(
            telemetry_leclerc
        )
    )


    print("\nGeorge Russell:")
    print(
        russell_telemetry_stats
    )

    print("\nCharles Leclerc:")
    print(
        leclerc_telemetry_stats
    )


    # ========================================================
    # SAVE TELEMETRY SUMMARY
    # ========================================================

    telemetry_summary = pd.DataFrame(
        [
            {
                "Driver": "George Russell",
                **russell_telemetry_stats
            },
            {
                "Driver": "Charles Leclerc",
                **leclerc_telemetry_stats
            }
        ]
    )

    save_dataframe(
        telemetry_summary,
        "telemetry_summary.csv"
    )


    # ========================================================
    # STEP 7 - THROTTLE
    # ========================================================

    print("\n")
    print("=" * 70)
    print("THROTTLE STATISTICS")
    print("=" * 70)


    russell_throttle = (
        calculate_throttle_statistics(
            telemetry_russell
        )
    )

    leclerc_throttle = (
        calculate_throttle_statistics(
            telemetry_leclerc
        )
    )


    print("\nGeorge Russell:")
    print(
        russell_throttle
    )

    print("\nCharles Leclerc:")
    print(
        leclerc_throttle
    )


    # ========================================================
    # SAVE THROTTLE STATISTICS
    # ========================================================

    throttle_statistics = pd.DataFrame(
        [
            {
                "Driver": "George Russell",
                **russell_throttle
            },
            {
                "Driver": "Charles Leclerc",
                **leclerc_throttle
            }
        ]
    )

    save_dataframe(
        throttle_statistics,
        "throttle_statistics.csv"
    )


    # ========================================================
    # STEP 8 - SPEED COMPARISON
    # ========================================================

    speed_comparison = (
        calculate_speed_comparison(
            telemetry_russell,
            telemetry_leclerc,
            driver1_name="Russell",
            driver2_name="Leclerc"
        )
    )


    print("\n")
    print("=" * 70)
    print("SPEED ADVANTAGE")
    print("=" * 70)


    advantage = calculate_speed_advantage(
        speed_comparison,
        driver1_name="Russell",
        driver2_name="Leclerc"
    )

    print(
        advantage
    )


    # ========================================================
    # SAVE SPEED COMPARISON
    # ========================================================

    save_dataframe(
        speed_comparison,
        "speed_comparison.csv"
    )


    # ========================================================
    # SAVE SPEED ADVANTAGE
    # ========================================================

    speed_advantage = pd.DataFrame(
        [
            advantage
        ]
    )

    save_dataframe(
        speed_advantage,
        "speed_advantage.csv"
    )


    # ========================================================
    # STEP 9 - LARGEST SPEED DIFFERENCES
    # ========================================================

    largest_russell, largest_leclerc = (
        find_largest_speed_differences(
            speed_comparison,
            driver1_name="Russell",
            driver2_name="Leclerc"
        )
    )


    print("\n")
    print("=" * 70)
    print("LARGEST SPEED DIFFERENCES")
    print("=" * 70)


    print("\nRussell's largest advantage:")
    print(
        largest_russell
    )


    print("\nLeclerc's largest advantage:")
    print(
        largest_leclerc
    )


    # ========================================================
    # SAVE LARGEST SPEED DIFFERENCES
    # ========================================================

    largest_speed_differences = pd.DataFrame(
        [
            {
                "Driver": "Russell",
                **largest_russell.to_dict()
            },
            {
                "Driver": "Leclerc",
                **largest_leclerc.to_dict()
            }
        ]
    )

    save_dataframe(
        largest_speed_differences,
        "largest_speed_differences.csv"
    )


    # ========================================================
    # STEP 10 - LOAD RACE DATA
    # ========================================================

    print("\n")
    print("=" * 70)
    print("LOADING RACE DATA FOR TIRE ANALYSIS")
    print("=" * 70)


    race_session = load_f1_session(
        year=2026,
        event="Australia",
        session_type="R",
        cache_dir=str(
            PROJECT_ROOT / "cache"
        )
    )


    race_laps = race_session.laps


    # ========================================================
    # STEP 11 - TIRE STINTS
    # ========================================================

    stints = calculate_tire_stints(
        race_laps
    )


    print("\n")
    print("=" * 70)
    print("TIRE STINTS")
    print("=" * 70)


    selected_stints = stints[
        stints["Driver"].isin(
            [
                driver1,
                driver2
            ]
        )
    ]


    print(
        selected_stints
    )


    # Save tire stints
    save_dataframe(
        selected_stints,
        "tire_stints.csv"
    )


    # ========================================================
    # STEP 12 - LONGEST STINT
    # ========================================================

    longest_stints = calculate_longest_stint(
        race_laps
    )


    print("\n")
    print("=" * 70)
    print("LONGEST TIRE STINT")
    print("=" * 70)


    selected_longest_stints = (
        longest_stints[
            longest_stints["Driver"].isin(
                [
                    driver1,
                    driver2
                ]
            )
        ]
    )


    print(
        selected_longest_stints
    )


    # Save longest stints
    save_dataframe(
        selected_longest_stints,
        "longest_tire_stints.csv"
    )


    # ========================================================
    # STEP 13 - COMPOUND PACE
    # ========================================================

    russell_race_laps = get_driver_laps(
        race_session,
        driver1
    )


    leclerc_race_laps = get_driver_laps(
        race_session,
        driver2
    )


    russell_pace = calculate_compound_pace(
        russell_race_laps
    )


    leclerc_pace = calculate_compound_pace(
        leclerc_race_laps
    )


    print("\n")
    print("=" * 70)
    print("RUSSELL COMPOUND PACE")
    print("=" * 70)


    print(
        russell_pace
    )


    print("\n")
    print("=" * 70)
    print("LECLERC COMPOUND PACE")
    print("=" * 70)


    print(
        leclerc_pace
    )


    # ========================================================
    # SAVE COMPOUND PACE
    # ========================================================

    russell_pace_saved = (
        russell_pace.copy()
    )

    russell_pace_saved.insert(
        0,
        "Driver",
        "George Russell"
    )


    leclerc_pace_saved = (
        leclerc_pace.copy()
    )

    leclerc_pace_saved.insert(
        0,
        "Driver",
        "Charles Leclerc"
    )


    compound_pace = pd.concat(
        [
            russell_pace_saved,
            leclerc_pace_saved
        ],
        ignore_index=True
    )


    save_dataframe(
        compound_pace,
        "compound_pace.csv"
    )


    # ========================================================
    # STEP 14 - TIRE DEGRADATION
    # ========================================================

    degradation = calculate_degradation(
        race_laps
    )


    print("\n")
    print("=" * 70)
    print("TIRE DEGRADATION")
    print("=" * 70)


    selected_degradation = (
        degradation[
            degradation["Driver"].isin(
                [
                    driver1,
                    driver2
                ]
            )
        ]
    )


    print(
        selected_degradation
    )


    # Save degradation
    save_dataframe(
        selected_degradation,
        "tire_degradation.csv"
    )


    # ========================================================
    # COMPLETE
    # ========================================================

    print("\n")
    print("=" * 70)
    print("              ANALYSIS COMPLETE")
    print("=" * 70)

    print("\nAll analysis tables have been saved to:")

    print(
        TABLES_DIR
    )

    print("\nGenerated files:")

    for file in sorted(
        TABLES_DIR.glob("*.csv")
    ):
        print(
            f"  - {file.name}"
        )


# ============================================================
# RUN MAIN
# ============================================================

if __name__ == "__main__":
    main()