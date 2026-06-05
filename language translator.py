from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk

# Import Translator
try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Language Translator")
root.geometry("700x450")
root.config(bg="#F7DC6F")
root.resizable(False, False)

# ---------------- LANGUAGES ---------------- #

languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Russian": "ru",
    "Chinese": "zh-cn",
    "Romanian": "ro",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

# ---------------- FUNCTIONS ---------------- #

def translate():
    if GoogleTranslator is None:
        messagebox.showerror(
            "Module Error",
            "deep-translator is not installed.\n\nRun this command in terminal:\n\npip install deep-translator"
        )
        return

    text = input_text.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    target_lang = language_combo.get()

    try:
        translated = GoogleTranslator(
            source="auto",
            target=languages[target_lang]
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

# ---------------- HEADING ---------------- #

heading = Label(
    root,
    text="Language Translator",
    font=("Helvetica", 22, "bold"),
    bg="#F7DC6F",
    fg="black"
)

heading.pack(pady=15)

# ---------------- COMBOBOX ---------------- #

language_combo = ttk.Combobox(
    root,
    values=list(languages.keys()),
    font=("Verdana", 12),
    state="readonly",
    width=20
)

language_combo.current(0)
language_combo.pack(pady=10)

# ---------------- INPUT TEXT ---------------- #

Label(
    root,
    text="Enter Text",
    font=("Verdana", 12, "bold"),
    bg="#F7DC6F"
).place(x=60, y=100)

input_text = Text(
    root,
    width=30,
    height=10,
    font=("Verdana", 12),
    relief=RIDGE,
    bd=5
)

input_text.place(x=40, y=140)

# ---------------- OUTPUT TEXT ---------------- #

Label(
    root,
    text="Translated Text",
    font=("Verdana", 12, "bold"),
    bg="#F7DC6F"
).place(x=410, y=100)

output_text = Text(
    root,
    width=30,
    height=10,
    font=("Verdana", 12),
    relief=RIDGE,
    bd=5
)

output_text.place(x=380, y=140)

# ---------------- BUTTONS ---------------- #

translate_btn = Button(
    root,
    text="Translate",
    font=("Verdana", 12, "bold"),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
    command=translate
)

translate_btn.place(x=220, y=380)

clear_btn = Button(
    root,
    text="Clear",
    font=("Verdana", 12, "bold"),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
    command=clear_text
)

clear_btn.place(x=380, y=380)

# ---------------- RUN APP ---------------- #

root.mainloop()