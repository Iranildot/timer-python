import customtkinter as ctk
from timer import Timer

# ============================================================
# UI Configuration
# ============================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class TechTimerApp(ctk.CTk):
    """
    Modern and tech-styled timer application using CustomTkinter.
    """

    def __init__(self):
        """
        Creates the main application window and initializes UI state.
        """
        super().__init__()
        self.title("⚡ Tech Timer")
        self.geometry("520x440")
        self.resizable(False, False)

        self.timer = Timer()
        self.running = False

        self._build_ui()

    def _build_ui(self):
        """
        Builds and lays out all UI components.
        """
        # Main card container (dashboard style)
        self.card = ctk.CTkFrame(
            self,
            corner_radius=24,
            fg_color=("#0b0f19", "#0b0f19"),
            border_width=2,
            border_color="#00f0ff"
        )
        self.card.pack(expand=True, fill="both", padx=20, pady=20)

        # Header label
        self.title_label = ctk.CTkLabel(
            self.card,
            text="SYSTEM TIMER",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#00f0ff"
        )
        self.title_label.pack(pady=(20, 5))

        # Time display
        self.time_var = ctk.StringVar(value="0.000 s")
        self.time_label = ctk.CTkLabel(
            self.card,
            textvariable=self.time_var,
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color="#ffffff"
        )
        self.time_label.pack(pady=(10, 5))

        # Time unit selector
        self.unit_combo = ctk.CTkOptionMenu(
            self.card,
            values=["ns", "us", "ms", "s", "min", "h"],
            fg_color="#0f1629",
            button_color="#00f0ff",
            button_hover_color="#00c2cc",
        )
        self.unit_combo.set("s")
        self.unit_combo.pack(pady=10)

        # Status indicator
        self.status_var = ctk.StringVar(value="STATUS: OFFLINE")
        self.status_label = ctk.CTkLabel(
            self.card,
            textvariable=self.status_var,
            text_color="#888888"
        )
        self.status_label.pack(pady=(5, 15))

        # Control buttons
        self.buttons = ctk.CTkFrame(self.card, fg_color="transparent")
        self.buttons.pack(pady=10)

        self.start_btn = ctk.CTkButton(
            self.buttons,
            text="▶ START",
            fg_color="#00f0ff",
            text_color="#000000",
            hover_color="#00c2cc",
            command=self.start
        )
        self.start_btn.grid(row=0, column=0, padx=8)

        self.pause_btn = ctk.CTkButton(
            self.buttons,
            text="⏸ PAUSE",
            fg_color="#1f2a44",
            hover_color="#2b3b5f",
            command=self.pause
        )
        self.pause_btn.grid(row=0, column=1, padx=8)

        self.reset_btn = ctk.CTkButton(
            self.buttons,
            text="⟳ RESET",
            fg_color="#3a0f14",
            hover_color="#5a141c",
            command=self.reset
        )
        self.reset_btn.grid(row=0, column=2, padx=8)

        # Footer label
        self.footer = ctk.CTkLabel(
            self.card,
            text="SYSTEM READY • v1.0",
            text_color="#444444"
        )
        self.footer.pack(side="bottom", pady=12)

    def start(self):
        """
        Starts the timer loop if it is not already running.
        """
        if not self.running:
            self.running = True
            self.status_var.set("STATUS: ONLINE")
            self.status_label.configure(text_color="#00ff88")
            self._loop()

    def pause(self):
        """
        Pauses the timer updates.
        """
        self.running = False
        self.status_var.set("STATUS: PAUSED")
        self.status_label.configure(text_color="#ffaa00")

    def reset(self):
        """
        Stops and resets the timer.
        """
        self.running = False
        self.timer.reset()
        self.time_var.set("0.000 s")
        self.status_var.set("STATUS: OFFLINE")
        self.status_label.configure(text_color="#888888")

    def _loop(self):
        """
        Main UI update loop. Updates the timer value and refreshes the display.
        """
        if not self.running:
            return

        unit = self.unit_combo.get()
        self.timer._tick()
        elapsed = self.timer.elapsed(unit)

        self.time_var.set(f"{elapsed:,.3f} {unit}")
        self.after(16, self._loop)  # ~60 FPS UI refresh


if __name__ == "__main__":
    app = TechTimerApp()
    app.mainloop()
