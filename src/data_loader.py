import fastf1


def enable_cache(cache_dir="cache"):
    """
    Enable FastF1 cache.
    """
    fastf1.Cache.enable_cache(cache_dir)


def load_f1_session(
    year,
    event,
    session_type,
    cache_dir="cache"
):
    """
    Load an F1 session using FastF1.

    Parameters
    ----------
    year : int
        F1 season year.

    event : str
        Grand Prix/event name.

    session_type : str
        Session type such as Q, R, FP1, FP2, FP3.

    cache_dir : str
        Directory used by FastF1 for caching.

    Returns
    -------
    fastf1.core.Session
        Loaded FastF1 session.
    """

    # Enable FastF1 cache
    fastf1.Cache.enable_cache(cache_dir)

    print(
        f"\nLoading {year} {event} {session_type} session..."
    )

    session = fastf1.get_session(
        year,
        event,
        session_type
    )

    session.load(
        telemetry=True,
        laps=True,
        weather=False,
        messages=False
    )

    print("Session loaded successfully!")

    return session


def load_session(year, event, session_type):
    """
    Alias for load_f1_session().
    """

    return load_f1_session(
        year,
        event,
        session_type
    )


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


def get_driver_telemetry(session, driver):
    """
    Get telemetry from the driver's fastest lap.
    """

    fastest_lap = get_fastest_lap(
        session,
        driver
    )

    telemetry = (
        fastest_lap
        .get_car_data()
        .add_distance()
    )

    return telemetry

def get_driver_results(session, driver=None):
    """
    Get driver results from a FastF1 session.

    If a driver is provided, return only that driver's result.
    If no driver is provided, return the complete results table.
    """

    results = session.results

    # Return complete results if no driver is specified
    if driver is None:
        return results

    # Return only the selected driver's result
    driver_result = results[
        results["Abbreviation"] == driver
    ]

    return driver_result