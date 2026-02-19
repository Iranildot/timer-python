# ⚡ Tech Timer --- CustomTkinter UI

A modern and tech-styled desktop timer application built with
**CustomTkinter** and Python.\
It provides a high-resolution timer with multiple time units and a
futuristic dashboard-like interface.

------------------------------------------------------------------------

## ✨ Features

-   🕒 High-precision timer based on `perf_counter_ns`
-   🎛 Multiple time units: ns, us, ms, s, min, h
-   🖥 Modern & futuristic UI (dashboard style)
-   ▶ Start / ⏸ Pause / ⟳ Reset controls
-   🌙 Dark mode interface
-   ⚡ Smooth \~60 FPS updates

------------------------------------------------------------------------

## 📸 Preview

*Add a screenshot or GIF of the app here*

------------------------------------------------------------------------

## 🧩 Project Structure

``` text
.
├── app.py        # Main UI application (CustomTkinter)
├── timer.py      # Timer utility class
└── README.md     # Project documentation
```

------------------------------------------------------------------------

## 🚀 Installation

Make sure you have **Python 3.10+** installed.

``` bash
pip install customtkinter
```

Clone the repository:

``` bash
git clone https://github.com/your-username/tech-timer.git
cd tech-timer
```

Run the application:

``` bash
python app.py
```

------------------------------------------------------------------------

## 🛠 Usage

1.  Click **START** to begin counting time\
2.  Click **PAUSE** to stop temporarily\
3.  Click **RESET** to clear the timer\
4.  Select the desired time unit from the dropdown menu

------------------------------------------------------------------------

## 📦 Packaging as an Executable (Optional)

``` bash
pip install pyinstaller
pyinstaller --onefile --windowed app.py
```

------------------------------------------------------------------------

## 🧠 Timer API

``` python
from timer import Timer
import time

timer = Timer()
time.sleep(1.5)
timer._tick()
print(timer.elapsed("s"))
```

------------------------------------------------------------------------

## 🛣 Roadmap

-   ⏳ Countdown mode\
-   📊 Performance benchmark mode\
-   🎨 Theme switcher\
-   📈 Real-time charts\
-   📁 Export results to CSV

------------------------------------------------------------------------

## 🤝 Contributing

Pull requests are welcome!

------------------------------------------------------------------------
