import customtkinter as ctk
from datetime import datetime

# ==================================================
# Application Configuration
# ==================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# ==================================================
# Theme Colors
# ==================================================

BG_COLOR = "#09090B"
CARD_COLOR = "#111827"
INNER_CARD = "#1F2937"
BORDER_COLOR = "#374151"

TEXT_COLOR = "#F9FAFB"
MUTED_TEXT = "#9CA3AF"

PRIMARY = "#10B981"
PRIMARY_HOVER = "#34D399"

SUCCESS = "#22C55E"
ERROR = "#EF4444"

# ==================================================
# Application State
# ==================================================

conversion_history = []


# ==================================================
# Logic
# ==================================================

def convert_values(event=None):
    try:
        miles = float(miles_entry.get())

        kilometers = miles * 1.60934

        result_value.configure(
            text=f"{kilometers:.2f}"
        )

        result_unit.configure(
            text="Kilometers"
        )

        status_label.configure(
            text="✓ Conversion completed successfully",
            text_color=SUCCESS
        )

        add_history(
            miles,
            kilometers
        )

    except ValueError:

        status_label.configure(
            text="⚠ Please enter a valid number",
            text_color=ERROR
        )


def reset():
    miles_entry.delete(
        0,
        "end"
    )

    result_value.configure(
        text="0.00"
    )

    result_unit.configure(
        text="Kilometers"
    )

    status_label.configure(
        text="Ready",
        text_color=MUTED_TEXT
    )


def add_history(miles, kilometers):
    item = (
        f"{miles:g} miles  →  {kilometers:.2f} km"
    )

    conversion_history.insert(
        0,
        item
    )

    update_history()


def update_history():
    for widget in history_frame.winfo_children():
        widget.destroy()

    for item in conversion_history[:5]:
        label = ctk.CTkLabel(
            history_frame,
            text=item,
            anchor="w",
            font=(
                "Arial",
                13
            ),
            text_color=TEXT_COLOR
        )

        label.pack(
            fill="x",
            padx=15,
            pady=5
        )


# ==================================================
# Main Window
# ==================================================

app = ctk.CTk()

app.title(
    "KM Converter Enterprise"
)

app.geometry(
    "700x650"
)

app.resizable(
    False,
    False
)

app.configure(
    fg_color=BG_COLOR
)

# ENTER shortcut

app.bind(
    "<Return>",
    convert_values
)

# ==================================================
# Header
# ==================================================

header = ctk.CTkFrame(
    app,
    fg_color=BG_COLOR
)

header.pack(
    fill="x",
    padx=40,
    pady=(30, 10)
)

title = ctk.CTkLabel(
    header,
    text="🚀 KM Converter",
    font=(
        "Arial",
        32,
        "bold"
    ),
    text_color=TEXT_COLOR
)

title.pack(
    anchor="w"
)

subtitle = ctk.CTkLabel(
    header,
    text="Enterprise Distance Conversion Toolkit",
    font=(
        "Arial",
        14
    ),
    text_color=MUTED_TEXT
)

subtitle.pack(
    anchor="w"
)

version = ctk.CTkLabel(
    header,
    text="v1.0",
    fg_color=PRIMARY,
    corner_radius=8,
    width=50,
    height=25,
    text_color="#000000",
    font=(
        "Arial",
        12,
        "bold"
    )
)

version.place(
    relx=0.9,
    rely=0.15
)

# ==================================================
# Main Card
# ==================================================

main_card = ctk.CTkFrame(
    app,
    fg_color=CARD_COLOR,
    corner_radius=20,
    border_width=1,
    border_color=BORDER_COLOR
)

main_card.pack(
    padx=40,
    pady=20,
    fill="both",
    expand=True
)

# ==================================================
# Converter Section
# ==================================================

section_title = ctk.CTkLabel(
    main_card,
    text="Distance Converter",
    font=(
        "Arial",
        22,
        "bold"
    ),
    text_color=TEXT_COLOR
)

section_title.pack(
    pady=(25, 15)
)

# Input card

input_card = ctk.CTkFrame(
    main_card,
    fg_color=INNER_CARD,
    corner_radius=15
)

input_card.pack(
    padx=35,
    pady=10,
    fill="x"
)

input_label = ctk.CTkLabel(
    input_card,
    text="Miles",
    font=(
        "Arial",
        14,
        "bold"
    ),
    text_color=MUTED_TEXT
)

input_label.pack(
    pady=(15, 5)
)

miles_entry = ctk.CTkEntry(
    input_card,
    height=45,
    width=300,
    placeholder_text="Enter miles",
    font=(
        "Arial",
        16
    ),
    fg_color=BG_COLOR,
    border_color=BORDER_COLOR
)

miles_entry.pack(
    pady=(0, 20)
)

# ==================================================
# Result Card
# ==================================================

result_card = ctk.CTkFrame(
    main_card,
    fg_color=INNER_CARD,
    corner_radius=15
)

result_card.pack(
    padx=35,
    pady=15,
    fill="x"
)

result_value = ctk.CTkLabel(
    result_card,
    text="0.00",
    font=(
        "Arial",
        42,
        "bold"
    ),
    text_color=PRIMARY
)

result_value.pack(
    pady=(20, 5)
)

result_unit = ctk.CTkLabel(
    result_card,
    text="Kilometers",
    font=(
        "Arial",
        15
    ),
    text_color=MUTED_TEXT
)

result_unit.pack(
    pady=(0, 20)
)

# ==================================================
# Buttons
# ==================================================

button_frame = ctk.CTkFrame(
    main_card,
    fg_color="transparent"
)

button_frame.pack(
    pady=15
)

convert_button = ctk.CTkButton(
    button_frame,
    text="Convert",
    width=150,
    height=45,
    corner_radius=10,
    font=(
        "Arial",
        15,
        "bold"
    ),
    fg_color=PRIMARY,
    hover_color=PRIMARY_HOVER,
    command=convert_values
)

convert_button.grid(
    row=0,
    column=0,
    padx=10
)

reset_button = ctk.CTkButton(
    button_frame,
    text="Reset",
    width=150,
    height=45,
    corner_radius=10,
    fg_color="#374151",
    hover_color="#4B5563",
    command=reset
)

reset_button.grid(
    row=0,
    column=1,
    padx=10
)

# ==================================================
# Status
# ==================================================

status_label = ctk.CTkLabel(
    main_card,
    text="Ready",
    font=(
        "Arial",
        13
    ),
    text_color=MUTED_TEXT
)

status_label.pack(
    pady=5
)

# ==================================================
# History
# ==================================================

history_title = ctk.CTkLabel(
    main_card,
    text="Recent Conversions",
    font=(
        "Arial",
        16,
        "bold"
    ),
    text_color=TEXT_COLOR
)

history_title.pack(
    pady=(20, 5)
)

history_frame = ctk.CTkFrame(
    main_card,
    fg_color=INNER_CARD,
    corner_radius=12
)

history_frame.pack(
    padx=35,
    pady=(0, 20),
    fill="x"
)

# ==================================================
# Footer
# ==================================================

footer = ctk.CTkLabel(
    app,
    text="KM Converter • Desktop Utility",
    font=(
        "Arial",
        12
    ),
    text_color=MUTED_TEXT
)

footer.pack(
    pady=10
)

# Start

app.mainloop()
