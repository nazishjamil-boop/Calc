import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self):
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 28, "bold"),
            bg="#2a2a3d",
            fg="white",
            insertbackground="white",
            borderwidth=0,
            justify="right",
            state="readonly",
        )
        display.grid(row=0, column=0, columnspan=4, padx=15, pady=(15, 5), ipady=15, sticky="ew")

        buttons = [
            ("C",   1, 0, "#e55"),  ("√",  1, 1, "#7c6af7"), ("%",  1, 2, "#7c6af7"), ("÷",  1, 3, "#f7a23e"),
            ("7",   2, 0, "#2a2a3d"), ("8", 2, 1, "#2a2a3d"), ("9", 2, 2, "#2a2a3d"), ("×",  2, 3, "#f7a23e"),
            ("4",   3, 0, "#2a2a3d"), ("5", 3, 1, "#2a2a3d"), ("6", 3, 2, "#2a2a3d"), ("−",  3, 3, "#f7a23e"),
            ("1",   4, 0, "#2a2a3d"), ("2", 4, 1, "#2a2a3d"), ("3", 4, 2, "#2a2a3d"), ("+",  4, 3, "#f7a23e"),
            ("±",   5, 0, "#2a2a3d"), ("0", 5, 1, "#2a2a3d"), (".", 5, 2, "#2a2a3d"), ("=",  5, 3, "#7c6af7"),
        ]

        for (text, row, col, color) in buttons:
            btn = tk.Button(
                self.root,
                text=text,
                font=("Arial", 18, "bold"),
                bg=color,
                fg="white",
                activebackground=color,
                activeforeground="white",
                borderwidth=0,
                width=4,
                height=2,
                cursor="hand2",
                command=lambda t=text: self._on_click(t),
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

    def _on_click(self, text):
        if text == "C":
            self.expression = ""
            self.display_var.set("0")

        elif text == "=":
            try:
                result = eval(self.expression)
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 10)
                self.display_var.set(result)
                self.expression = str(result)
            except ZeroDivisionError:
                self.display_var.set("Error")
                self.expression = ""
            except Exception:
                self.display_var.set("Error")
                self.expression = ""

        elif text == "√":
            try:
                value = float(self.expression) if self.expression else 0
                if value < 0:
                    self.display_var.set("Error")
                    self.expression = ""
                else:
                    result = math.sqrt(value)
                    result = int(result) if result.is_integer() else round(result, 10)
                    self.display_var.set(result)
                    self.expression = str(result)
            except Exception:
                self.display_var.set("Error")
                self.expression = ""

        elif text == "±":
            try:
                value = float(self.expression) if self.expression else 0
                value = -value
                value = int(value) if float(value).is_integer() else value
                self.display_var.set(value)
                self.expression = str(value)
            except Exception:
                pass

        elif text == "÷":
            self.expression += "/"
            self.display_var.set(self.expression)

        elif text == "×":
            self.expression += "*"
            self.display_var.set(self.expression)

        elif text == "−":
            self.expression += "-"
            self.display_var.set(self.expression)

        else:
            self.expression += text
            self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
