# 🏎️ F1 Telemetry & Tire Strategy Analysis

An end-to-end Formula 1 data analytics project using **FastF1, Python, Pandas, NumPy, Matplotlib, and Streamlit** to analyze driver telemetry, speed, throttle, braking behavior, and tire strategy.

The project focuses on the **2026 Australian Grand Prix**, comparing **George Russell (RUS)** and **Charles Leclerc (LEC)** during qualifying and analyzing their tire strategies during the race.

## 🚀 Live Demo

👉 **[Open the F1 Telemetry Analysis Dashboard](https://amishasree-f1-telemetry-analysis-app-vleqe2.streamlit.app/)**

## 📂 GitHub Repository

👉 **[View the source code on GitHub](https://github.com/AmishaSree/f1-telemetry-analysis)**

---

# 📌 Project Overview

Formula 1 generates large amounts of telemetry and race data that can be used to understand driver performance and race strategy.

This project uses the **FastF1 Python library** to retrieve Formula 1 session data and build a complete data analysis workflow.

The project analyzes:

- Driver telemetry
- Speed differences
- Throttle usage
- Braking zones
- Fastest laps
- Tire compounds
- Tire stints
- Compound pace
- Tire degradation
- Driver performance differences

The analysis results are processed into reusable Python modules, CSV tables, visualizations, Jupyter notebooks, and an interactive Streamlit dashboard.

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Retrieve Formula 1 session data using FastF1.
2. Compare the telemetry of two drivers.
3. Analyze driver speed throughout a lap.
4. Compare throttle application between drivers.
5. Identify braking zones and braking distances.
6. Analyze tire compounds and stint strategies.
7. Estimate tire degradation using regression.
8. Generate visualizations and analysis tables.
9. Build a reusable Python analysis pipeline.
10. Deploy the final analysis as an interactive Streamlit application.

---

# 🏁 Grand Prix & Drivers

## Event

**2026 Australian Grand Prix**

### Qualifying Analysis

The telemetry comparison focuses on:

- **George Russell — RUS**
- **Charles Leclerc — LEC**

### Sessions Used

- Qualifying (`Q`) — driver telemetry analysis
- Race (`R`) — tire strategy and degradation analysis

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastF1 | Formula 1 session and telemetry data |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical calculations and interpolation |
| Matplotlib | Data visualization |
| SciPy | Scientific and statistical analysis |
| Streamlit | Interactive web dashboard |
| Jupyter Notebook | Exploratory data analysis |
| Git | Version control |
| GitHub | Source code hosting |
| Streamlit Community Cloud | Application deployment |

---

# 📊 Analysis Performed

## 1. Driver Telemetry Analysis

Telemetry data from the fastest laps of both drivers is extracted using FastF1.

The analysis includes:

- Speed
- Throttle
- Brake
- RPM
- Distance
- Telemetry data points

### Basic Telemetry Results

| Metric | George Russell | Charles Leclerc |
|---|---:|---:|
| Average Speed | 238.62 km/h | 239.63 km/h |
| Maximum Speed | 327 km/h | 318 km/h |
| Maximum Throttle | 100% | 100% |
| Maximum RPM | 12,166 | 12,300 |

---

# ⚡ Speed Comparison

The fastest laps of both drivers are aligned using **distance along the track**.

A common distance grid is created and the speed values are interpolated so that both drivers can be compared at equivalent track positions.

### Overall Speed Analysis

| Metric | Result |
|---|---:|
| Russell Average Speed | 256.19 km/h |
| Leclerc Average Speed | 252.42 km/h |
| Average Difference | +3.76 km/h |
| Russell Faster | 78.40% |
| Leclerc Faster | 21.20% |
| Within ±1 km/h | 7.90% |

### Largest Speed Differences

**Russell's largest speed advantage:**

- Distance: approximately **3981 m**
- Russell: **292.15 km/h**
- Leclerc: **264.60 km/h**
- Difference: **+27.55 km/h**

**Leclerc's largest speed advantage:**

- Distance: approximately **4563 m**
- Russell: **131.11 km/h**
- Leclerc: **167.58 km/h**
- Difference: approximately **36.47 km/h**

---

# 🟢 Throttle Analysis

Throttle telemetry was analyzed to determine how frequently each driver operated at high and low throttle levels.

### Results

| Metric | George Russell | Charles Leclerc |
|---|---:|---:|
| ≥95% Throttle | 63.14% | 64.36% |
| ≤5% Throttle | 16.40% | 13.84% |

This provides an indication of how the drivers differed in throttle application during their fastest laps.

---

# 🛑 Braking Analysis

Braking zones were detected from the telemetry data.

The analysis identifies:

- Braking start distance
- Braking end distance
- Braking distance
- Maximum braking state

### George Russell

Russell's detected braking zones include approximately:

- 273–335 m
- 953–1084 m
- 1775–1831 m
- 4004–4098 m
- 4515–4597 m

### Charles Leclerc

Leclerc's detected braking zones include approximately:

- 266–338 m
- 964–1066 m
- 1171–1188 m
- 1807 m
- 3225–3248 m
- 4027–4084 m
- 4539–4602 m

These zones are visualized in the Streamlit dashboard.

---

# 🛞 Tire Strategy Analysis

Race-session data is used to analyze tire strategy.

The analysis includes:

- Tire compounds
- Tire stints
- Stint duration
- Tire life
- Compound pace
- Tire degradation

## Longest Tire Stints

| Driver | Compound | Start Lap | End Lap | Laps |
|---|---|---:|---:|---:|
| George Russell | HARD | 13 | 58 | 46 |
| Charles Leclerc | HARD | 26 | 58 | 33 |

Russell completed the longest detected hard-tire stint with **46 laps**.

---

# 🏎️ Compound Pace

## George Russell

| Compound | Average Lap Time | Best Lap Time | Lap Count |
|---|---:|---:|---:|
| HARD | 83.060 s | 82.670 s | 40 |
| MEDIUM | 84.824 s | 83.967 s | 10 |

## Charles Leclerc

| Compound | Average Lap Time | Best Lap Time | Lap Count |
|---|---:|---:|---:|
| HARD | 83.068 s | 82.579 s | 31 |
| MEDIUM | 84.324 s | 83.322 s | 17 |

---

# 📉 Tire Degradation Analysis

Tire degradation is estimated using **linear regression** between tire life and lap time.

The regression produces:

- Degradation in seconds per lap
- Correlation
- Number of data points

### Results

| Driver | Compound | Degradation (sec/lap) | Correlation |
|---|---|---:|---:|
| George Russell | HARD | 0.0007 | 0.0283 |
| George Russell | MEDIUM | -0.1016 | -0.3597 |
| Charles Leclerc | HARD | -0.0028 | -0.0841 |
| Charles Leclerc | MEDIUM | -0.0883 | -0.7301 |

> **Note:** A negative regression slope in this analysis means lap times tended to decrease as tire life increased in the available data. This can be influenced by factors such as fuel load, traffic, track evolution, and the relatively small number of laps in some compound groups. Therefore, the regression should be interpreted as an observed relationship rather than pure physical tire degradation.

---

# 📈 Visualizations

The project generates several visualizations, including:

- Fastest lap comparison
- Lap time distribution
- Speed vs distance
- Speed difference
- Throttle vs distance
- Brake vs distance
- Russell tire degradation
- Leclerc tire degradation
- Tire strategy timeline

These visualizations are stored in:

```text
outputs/figures/