"""
MASA LexiMetrics: Advanced Text & Character Analytics
Developer: MASA
"""

import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MasaLexiMetrics(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MASA LexiMetrics - Text Analytics")
        self.geometry("540x620")
        self.resizable(False, False)
        self.configure(fg_color="#0A0D14")

        self._build_ui()

    def _build_ui(self):
        header = ctk.CTkFrame(self, fg_color="#121724", corner_radius=14)
        header.pack(fill="x", padx=20, pady=(20, 15))

        title = ctk.CTkLabel(
            header,
            text="MASA LEXIMETRICS",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#38BDF8",
        )
        title.pack(pady=(12, 2))

        subtitle = ctk.CTkLabel(
            header,
            text="Real-Time Computational Linguistics & Text Analysis",
            font=ctk.CTkFont(size=11),
            text_color="#94A3B8",
        )
        subtitle.pack(pady=(0, 12))

        self.textbox = ctk.CTkTextbox(
            self,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            fg_color="#121724",
            corner_radius=14,
            border_width=1,
            border_color="#1E293B",
            wrap="word",
        )
        self.textbox.pack(fill="both", expand=True, padx=20, pady=5)
        self.textbox.bind("<KeyRelease>", lambda _: self._analyze_text())

        stats_card = ctk.CTkFrame(self, fg_color="#121724", corner_radius=16)
        stats_card.pack(fill="x", padx=20, pady=12)

        for col in range(4):
            stats_card.grid_columnconfigure(col, weight=1, uniform="stat")

        self.box_chars = self._make_stat_box(stats_card, 0, "CHARS (TOTAL)")
        self.box_no_space = self._make_stat_box(stats_card, 1, "NO SPACES")
        self.box_words = self._make_stat_box(stats_card, 2, "WORDS")
        self.box_lines = self._make_stat_box(stats_card, 3, "LINES")

        actions_row = ctk.CTkFrame(self, fg_color="transparent")
        actions_row.pack(fill="x", padx=20, pady=(0, 20))
        actions_row.grid_columnconfigure((0, 1, 2), weight=1, uniform="act")

        ctk.CTkButton(
            actions_row,
            text="Clear Text",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#EF4444",
            hover_color="#DC2626",
            corner_radius=8,
            height=36,
            command=self._clear_all,
        ).grid(row=0, column=0, padx=4, sticky="ew")

        ctk.CTkButton(
            actions_row,
            text="UPPERCASE",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#1E293B",
            hover_color="#334155",
            corner_radius=8,
            height=36,
            command=self._to_uppercase,
        ).grid(row=0, column=1, padx=4, sticky="ew")

        ctk.CTkButton(
            actions_row,
            text="lowercase",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#1E293B",
            hover_color="#334155",
            corner_radius=8,
            height=36,
            command=self._to_lowercase,
        ).grid(row=0, column=2, padx=4, sticky="ew")

    def _make_stat_box(self, parent, col, title):
        box = ctk.CTkFrame(parent, fg_color="#0A0D14", corner_radius=10)
        box.grid(row=0, column=col, padx=4, pady=10, sticky="nsew")

        val_lbl = ctk.CTkLabel(
            box,
            text="0",
            font=ctk.CTkFont(family="Consolas", size=22, weight="bold"),
            text_color="#38BDF8",
        )
        val_lbl.pack(pady=(8, 0))

        sub_lbl = ctk.CTkLabel(
            box,
            text=title,
            font=ctk.CTkFont(size=9, weight="bold"),
            text_color="#64748B",
        )
        sub_lbl.pack(pady=(0, 8))
        return val_lbl

    def _analyze_text(self):
        text = self.textbox.get("0.0", "end")
        if text.endswith("\n"):
            text = text[:-1]

        total_chars = len(text)
        no_space_chars = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
        words = len(text.split()) if text.strip() else 0
        lines = len(text.splitlines()) if text else 0

        self.box_chars.configure(text=str(total_chars))
        self.box_no_space.configure(text=str(no_space_chars))
        self.box_words.configure(text=str(words))
        self.box_lines.configure(text=str(lines))

    def _clear_all(self):
        self.textbox.delete("0.0", "end")
        self._analyze_text()

    def _to_uppercase(self):
        content = self.textbox.get("0.0", "end")
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", content.upper())
        self._analyze_text()

    def _to_lowercase(self):
        content = self.textbox.get("0.0", "end")
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", content.lower())
        self._analyze_text()


if __name__ == "__main__":
    app = MasaLexiMetrics()
    app.mainloop()
