import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="F1 Telemetry Analysis",
    page_icon="🏎️",
    layout="wide"
)


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent

TABLES_DIR = PROJECT_ROOT / "outputs" / "tables"
FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

@st.cache_data
def load_table(filename):
    """
    Load a CSV file from outputs/tables.
    """

    path = TABLES_DIR / filename

    if not path.exists():
        return pd.DataFrame()

    return pd.read_csv(path)


def display_image(filename, caption=None):
    """
    Display an analysis figure if it exists.
    """

    path = FIGURES_DIR / filename

    if path.exists():
        st.image(
            str(path),
            caption=caption,
            use_container_width=True
        )
    else:
        st.warning(
            f"Figure not found: {filename}"
        )


# ============================================================
# LOAD TABLES
# ============================================================

driver_results = load_table(
    "driver_results.csv"
)

speed_comparison = load_table(
    "speed_comparison.csv"
)

speed_advantage = load_table(
    "speed_advantage.csv"
)

largest_speed = load_table(
    "largest_speed_differences.csv"
)

telemetry_summary = load_table(
    "telemetry_summary.csv"
)

throttle_statistics = load_table(
    "throttle_statistics.csv"
)

tire_stints = load_table(
    "tire_stints.csv"
)

longest_stints = load_table(
    "longest_tire_stints.csv"
)

compound_pace = load_table(
    "compound_pace.csv"
)

tire_degradation = load_table(
    "tire_degradation.csv"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏎️ F1 Telemetry")

st.sidebar.markdown(
    """
    ### Project
    **F1 Telemetry & Tire Strategy Analysis**

    **Grand Prix:**  
    2026 Australian Grand Prix

    **Qualifying:**  
    George Russell vs Charles Leclerc

    **Race:**  
    Tire strategy analysis
    """
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Overview",
        "🏎️ Driver Telemetry",
        "⚡ Speed Comparison",
        "🛞 Tire Strategy",
        "📊 Data Tables"
    ]
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "🏎️ F1 Telemetry & Tire Strategy Analysis"
)

st.markdown(
    """
    Analysis of the **2026 Australian Grand Prix** using
    the **FastF1 Python library**.

    The project compares **George Russell** and
    **Charles Leclerc** using telemetry data and analyzes
    tire strategy and degradation during the race.
    """
)

st.divider()


# ============================================================
# OVERVIEW
# ============================================================

if page == "🏠 Overview":

    st.header("Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Driver 1",
        "George Russell"
    )

    col2.metric(
        "Driver 2",
        "Charles Leclerc"
    )

    col3.metric(
        "Session",
        "Qualifying"
    )

    col4.metric(
        "Race Analysis",
        "Tire Strategy"
    )

    st.divider()

    st.subheader("📈 Key Findings")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Russell Avg Speed",
        "256.19 km/h"
    )

    col2.metric(
        "Leclerc Avg Speed",
        "252.42 km/h"
    )

    col3.metric(
        "Average Difference",
        "+3.76 km/h"
    )

    st.markdown(
        """
        ### Main Findings

        - Russell had the higher average speed across the
          compared telemetry data.
        - Russell was faster at approximately **78.40%**
          of comparison points.
        - Leclerc was faster at approximately **21.20%**
          of comparison points.
        - Russell's largest speed advantage was approximately
          **27.55 km/h**.
        - Leclerc's largest speed advantage was approximately
          **36.47 km/h**.
        - Both drivers used **Hard** and **Medium** compounds
          during the race.
        """
    )

    st.divider()

    st.subheader("🏁 Fastest Lap Comparison")

    display_image(
        "fastest_lap_comparison.png",
        "Fastest lap comparison"
    )

    st.subheader("📊 Lap Time Distribution")

    display_image(
        "lap_time_distribution.png",
        "Lap time distribution"
    )


# ============================================================
# DRIVER TELEMETRY
# ============================================================

elif page == "🏎️ Driver Telemetry":

    st.header("🏎️ Driver Telemetry Analysis")

    st.markdown(
        """
        Telemetry analysis compares the fastest laps of
        George Russell and Charles Leclerc.
        """
    )

    st.subheader("Throttle Analysis")

    display_image(
        "throttle_vs_distance.png",
        "Throttle percentage along the track"
    )

    st.subheader("Brake Analysis")

    display_image(
        "brake_vs_distance.png",
        "Brake input along the track"
    )

    st.subheader("Speed Along Track")

    display_image(
        "speed_vs_distance.png",
        "Speed comparison along the track"
    )

    st.subheader("Telemetry Summary")

    if not telemetry_summary.empty:
        st.dataframe(
            telemetry_summary,
            use_container_width=True
        )
    else:
        st.info(
            "Telemetry summary data is not available."
        )

    st.subheader("Throttle Statistics")

    if not throttle_statistics.empty:
        st.dataframe(
            throttle_statistics,
            use_container_width=True
        )


# ============================================================
# SPEED COMPARISON
# ============================================================

elif page == "⚡ Speed Comparison":

    st.header("⚡ Speed Comparison")

    st.markdown(
        """
        This section compares Russell and Leclerc's speed
        at common distance points around the circuit.
        """
    )

    st.subheader("Speed Difference")

    display_image(
        "speed_difference.png",
        "Russell speed minus Leclerc speed"
    )

    st.subheader("Speed Advantage Distribution")

    if not speed_advantage.empty:
        st.dataframe(
            speed_advantage,
            use_container_width=True
        )

    st.divider()

    st.subheader("Largest Speed Differences")

    if not largest_speed.empty:
        st.dataframe(
            largest_speed,
            use_container_width=True
        )

    st.divider()

    st.subheader("Speed Comparison Data")

    if not speed_comparison.empty:
        st.dataframe(
            speed_comparison.head(100),
            use_container_width=True
        )

        st.caption(
            "Showing the first 100 comparison points."
        )


# ============================================================
# TIRE STRATEGY
# ============================================================

elif page == "🛞 Tire Strategy":

    st.header("🛞 Tire Strategy Analysis")

    st.markdown(
        """
        Race data is used to compare tire compounds,
        stint lengths, pace and degradation.
        """
    )

    st.subheader("Tire Strategy Timeline")

    display_image(
        "tire_strategy_timeline.png",
        "Tire strategy used during the race"
    )

    st.divider()

    st.subheader("Longest Tire Stints")

    if not longest_stints.empty:
        st.dataframe(
            longest_stints,
            use_container_width=True
        )

    st.divider()

    st.subheader("Compound Pace")

    if not compound_pace.empty:
        st.dataframe(
            compound_pace,
            use_container_width=True
        )

    st.divider()

    st.subheader("Tire Degradation")

    if not tire_degradation.empty:
        st.dataframe(
            tire_degradation,
            use_container_width=True
        )

    st.subheader("Russell Tire Degradation")

    display_image(
        "russell_tire_degradation.png",
        "George Russell tire degradation"
    )

    st.subheader("Leclerc Tire Degradation")

    display_image(
        "leclerc_tire_degradation.png",
        "Charles Leclerc tire degradation"
    )


# ============================================================
# DATA TABLES
# ============================================================

elif page == "📊 Data Tables":

    st.header("📊 Analysis Data")

    table_name = st.selectbox(
        "Select a dataset",
        [
            "Driver Results",
            "Telemetry Summary",
            "Throttle Statistics",
            "Speed Advantage",
            "Speed Comparison",
            "Largest Speed Differences",
            "Tire Stints",
            "Longest Tire Stints",
            "Compound Pace",
            "Tire Degradation"
        ]
    )

    datasets = {
        "Driver Results": driver_results,
        "Telemetry Summary": telemetry_summary,
        "Throttle Statistics": throttle_statistics,
        "Speed Advantage": speed_advantage,
        "Speed Comparison": speed_comparison,
        "Largest Speed Differences": largest_speed,
        "Tire Stints": tire_stints,
        "Longest Tire Stints": longest_stints,
        "Compound Pace": compound_pace,
        "Tire Degradation": tire_degradation
    }

    selected_data = datasets[table_name]

    if not selected_data.empty:

        st.dataframe(
            selected_data,
            use_container_width=True
        )

        csv_data = selected_data.to_csv(
            index=False
        )

        st.download_button(
            label="⬇️ Download CSV",
            data=csv_data,
            file_name=(
                table_name.lower()
                .replace(" ", "_")
                + ".csv"
            ),
            mime="text/csv"
        )

    else:

        st.warning(
            "No data available for this selection."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "F1 Telemetry Analysis | FastF1 + Python + Pandas + Streamlit"
)