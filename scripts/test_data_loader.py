from src.data_loader import (
    enable_cache,
    load_session,
    get_driver_laps,
    get_fastest_lap,
    get_driver_telemetry
)


# Enable cache
enable_cache("cache")


# Load Australian GP Qualifying
session = load_session(
    2026,
    "Australia",
    "Q"
)


# Get George Russell laps
russell_laps = get_driver_laps(
    session,
    "RUS"
)

print("\n========== RUSSELL ==========")
print("Number of laps:", len(russell_laps))


# Get Charles Leclerc laps
leclerc_laps = get_driver_laps(
    session,
    "LEC"
)

print("\n========== LECLERC ==========")
print("Number of laps:", len(leclerc_laps))


# Fastest laps
russell_fastest = get_fastest_lap(
    session,
    "RUS"
)

leclerc_fastest = get_fastest_lap(
    session,
    "LEC"
)


print("\n========== FASTEST LAPS ==========")

print(
    "Russell:",
    russell_fastest["LapTime"]
)

print(
    "Leclerc:",
    leclerc_fastest["LapTime"]
)


# Telemetry
russell_telemetry = get_driver_telemetry(
    session,
    "RUS"
)

leclerc_telemetry = get_driver_telemetry(
    session,
    "LEC"
)


print("\n========== TELEMETRY ==========")

print(
    "Russell telemetry points:",
    len(russell_telemetry)
)

print(
    "Leclerc telemetry points:",
    len(leclerc_telemetry)
)

print("\nRussell telemetry columns:")
print(russell_telemetry.columns.tolist())

print("\nLeclerc telemetry columns:")
print(leclerc_telemetry.columns.tolist())


print("\n========== STEP 57 COMPLETE ==========")