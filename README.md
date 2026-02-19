# ⏱ Timer Utility --- High-Resolution Python Timer

A lightweight, high-resolution **Timer** utility for Python based on
`time.perf_counter_ns`.\
This project focuses on the **Timer class as the main component**, with
a modern CustomTkinter UI provided only as an **example of usage**.

------------------------------------------------------------------------

## ✨ Features

-   🕒 High-precision timer using `perf_counter_ns`
-   🎯 Multiple time units: ns, us, ms, s, min, h, d
-   🔁 Reset and delta tracking
-   🧩 Clean and reusable utility class
-   🖥 Optional modern UI example (CustomTkinter)

------------------------------------------------------------------------

## 🧩 Project Structure

``` text
.
├── timer.py      # Core Timer utility (main project focus)
├── exemple1.py   # Example UI showing how to use Timer (optional)
└── README.md     # Project documentation
```

> The UI application is **only an example**.\
> The main goal of this repository is to provide a reusable and precise
> **Timer utility**.

------------------------------------------------------------------------

## 🚀 Installation

Python 3.10+ recommended.

``` bash
pip install customtkinter
```

(CustomTkinter is only required if you want to run the example UI.)

------------------------------------------------------------------------

## 🧠 Using the Timer (Core API)

``` python
import time
from timer import Timer

timer = Timer()

# Simulate workload
time.sleep(1.2)

# Update internal state
timer._tick()

print(f"Elapsed (ms): {timer.elapsed('ms')}")
print(f"Elapsed (s): {timer.elapsed('s')}")
```

### Resetting the timer

``` python
timer.reset()
```

### Measuring expiration

``` python
limit_seconds = 2

while not timer.has_expired(limit_seconds, 's'):
    pass

print("Time limit reached!")
```

------------------------------------------------------------------------

## 🖥 Example UI (Optional)

This project includes a modern, tech-styled UI built with CustomTkinter
to demonstrate how the `Timer` can be used in a real application.

Run the UI example:

``` bash
python example1.py
```

The UI is meant for **demonstration purposes only** and is not required
to use the Timer utility.

https://github.com/user-attachments/assets/d973b874-3341-4949-a354-88979744cf6f

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome!\
Feel free to open issues or submit pull requests.

------------------------------------------------------------------------
