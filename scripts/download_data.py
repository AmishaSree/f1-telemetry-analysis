import fastf1

# ============================================================
# 1. ENABLE FASTF1 CACHE
# ============================================================

fastf1.Cache.enable_cache("cache")


# ============================================================
# 2. LOAD 2026 AUSTRALIAN GRAND PRIX - QUALIFYING
# ============================================================

print("Loading 2026 Australian Grand Prix Qualifying...")

session = fastf1.get_session(
    2026,
    "Australia",
    "Q"
)

# Load session data
session.load(
    telemetry=True,
    laps=True,
    weather=False,
    messages=False
)

print("\nSession loaded successfully!")


# ============================================================
# 3. DISPLAY EVENT INFORMATION
# ============================================================

print("\n========== EVENT INFORMATION ==========")

print("Event:")
print(session.event)

print("\nSession:")
print(session.name)


# ============================================================
# 4. DISPLAY ALL DRIVERS
# ============================================================

print("\n========== DRIVERS ==========")

drivers = session.results[
    ["Abbreviation", "FullName", "TeamName"]
]

print(drivers)


# ============================================================
# 5. SELECT TWO DRIVERS
# ============================================================

driver1 = "RUS"   # George Russell
driver2 = "LEC"   # Charles Leclerc


# ============================================================
# 6. GET ALL LAPS FOR BOTH DRIVERS
# ============================================================

driver1_laps = session.laps.pick_drivers(driver1)
driver2_laps = session.laps.pick_drivers(driver2)

print("\n========== DRIVER LAP COUNTS ==========")

print(f"George Russell laps: {len(driver1_laps)}")
print(f"Charles Leclerc laps: {len(driver2_laps)}")


# ============================================================
# 7. DISPLAY LAP INFORMATION
# ============================================================

print("\n========== GEORGE RUSSELL LAPS ==========")

print(
    driver1_laps[
        ["LapNumber", "LapTime"]
    ]
)


print("\n========== CHARLES LECLERC LAPS ==========")

print(
    driver2_laps[
        ["LapNumber", "LapTime"]
    ]
)


# ============================================================
# 8. FIND FASTEST LAP FOR EACH DRIVER
# ============================================================

fastest_lap_1 = driver1_laps.pick_fastest()
fastest_lap_2 = driver2_laps.pick_fastest()


# ============================================================
# 9. DISPLAY FASTEST LAP INFORMATION
# ============================================================

print("\n========== FASTEST LAP COMPARISON ==========")

print("\nGeorge Russell:")
print(fastest_lap_1)

print("\nCharles Leclerc:")
print(fastest_lap_2)


# ============================================================
# 10. DISPLAY ONLY LAP TIMES
# ============================================================

print("\n========== FASTEST LAP TIMES ==========")

print(
    "George Russell:",
    fastest_lap_1["LapTime"]
)

print(
    "Charles Leclerc:",
    fastest_lap_2["LapTime"]
)


# ============================================================
# 11. DISPLAY LAP NUMBERS
# ============================================================

print("\n========== FASTEST LAP NUMBERS ==========")

print(
    "George Russell fastest lap number:",
    fastest_lap_1["LapNumber"]
)

print(
    "Charles Leclerc fastest lap number:",
    fastest_lap_2["LapNumber"]
)


print("\n========== STEP 4 COMPLETE ==========")
print("Driver selection and fastest-lap analysis completed.")

# ============================================================
# 12. EXTRACT TELEMETRY FROM FASTEST LAPS
# ============================================================

print("\n========== EXTRACTING TELEMETRY ==========")

# Get telemetry for George Russell's fastest lap
telemetry_rus = fastest_lap_1.get_telemetry()
telemetry_lec = fastest_lap_2.get_telemetry()

# ============================================================
# 13. DISPLAY TELEMETRY COLUMNS
# ============================================================

print("\nGeorge Russell telemetry columns:")
print(telemetry_rus.columns.tolist())

print("\nCharles Leclerc telemetry columns:")
print(telemetry_lec.columns.tolist())


# ============================================================
# 14. DISPLAY FIRST 10 TELEMETRY ROWS
# ============================================================

print("\n========== GEORGE RUSSELL TELEMETRY ==========")

print(telemetry_rus.head(10))


print("\n========== CHARLES LECLERC TELEMETRY ==========")

print(telemetry_lec.head(10))


print("\n========== TELEMETRY SUMMARY ==========")

print("\nGeorge Russell:")
print(f"Telemetry data points: {len(telemetry_rus)}")
print(f"Maximum speed: {telemetry_rus['Speed'].max():.2f} km/h")
print(f"Average speed: {telemetry_rus['Speed'].mean():.2f} km/h")
print(f"Maximum throttle: {telemetry_rus['Throttle'].max():.2f}%")

if "RPM" in telemetry_rus.columns:
    print(f"Maximum RPM: {telemetry_rus['RPM'].max():.0f}")


print("\nCharles Leclerc:")
print(f"Telemetry data points: {len(telemetry_lec)}")
print(f"Maximum speed: {telemetry_lec['Speed'].max():.2f} km/h")
print(f"Average speed: {telemetry_lec['Speed'].mean():.2f} km/h")
print(f"Maximum throttle: {telemetry_lec['Throttle'].max():.2f}%")

if "RPM" in telemetry_lec.columns:
    print(f"Maximum RPM: {telemetry_lec['RPM'].max():.0f}")