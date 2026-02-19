import time

# ============================================================
# Timer Utility Class
# ============================================================
class Timer:
    """
    High-resolution timer utility based on perf_counter_ns.

    This class can be used to measure elapsed time with different
    time units (ns, us, ms, s, min, h, d).
    """

    NANOSECONDS  = "ns"
    MICROSECONDS = "us"
    MILISECONDS  = "ms"
    SECONDS      = "s"
    MINUTES      = "min"
    HOURS        = "h"
    DAYS         = "d"

    _UNIT_FACTORS = {
        NANOSECONDS:  1,
        MICROSECONDS: 1_000,
        MILISECONDS:  1_000_000,
        SECONDS:      1_000_000_000,
        MINUTES:      60 * 1_000_000_000,
        HOURS:        60 * 60 * 1_000_000_000,
        DAYS:         24 * 60 * 60 * 1_000_000_000,
    }

    def __init__(self):
        """
        Initializes the timer internal state.
        """
        self.elapsed_ns = 0
        self.delta_ns = 0
        self.last_tick_ns = time.perf_counter_ns()

    def _unit_factor(self, unit: str) -> int:
        """
        Returns the conversion factor for the given time unit.

        :param unit: Unit identifier (e.g. 'ns', 'ms', 's').
        :raises KeyError: If the unit is invalid.
        """
        return self._UNIT_FACTORS[unit]

    def elapsed(self, unit: str = "ns") -> float:
        """
        Returns the total elapsed time in the given unit.

        :param unit: Desired time unit.
        :return: Elapsed time converted to the chosen unit.
        """
        return self.elapsed_ns / self._unit_factor(unit)

    def _tick(self):
        """
        Updates the internal timer state based on the current time.
        """
        now_ns = time.perf_counter_ns()
        delta = now_ns - self.last_tick_ns
        self.last_tick_ns = now_ns
        self.delta_ns = delta
        self.elapsed_ns += delta

    def reset(self):
        """
        Resets the timer counters and reference time.
        """
        self.elapsed_ns = 0
        self.delta_ns = 0
        self.last_tick_ns = time.perf_counter_ns()
