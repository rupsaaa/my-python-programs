import tkinter as tk
from tkinter import messagebox, filedialog, ttk

class ModernToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern To-Do List")
        self.root.geometry("520x600")
        self.root.config(bg="#F3F4F6")

        # --------------------- HEADER ---------------------
        tk.Label(root, text="📝 To-Do List", font=("Segoe UI", 28, "bold"),
                 bg="#F3F4F6", fg="#333").pack(pady=20)

        # --------------------- CARD FRAME ---------------------
        card = tk.Frame(root, bg="white", bd=0, relief="flat")
        card.pack(padx=20, pady=10, fill="both", expand=True)
        card.config(highlightbackground="#D1D5DB", highlightthickness=1)

        # Entry box
        self.task_entry = tk.Entry(card, font=("Segoe UI", 14), bd=0,
                                   highlightthickness=1, highlightcolor="#6366F1",
                                   relief="flat")
        self.task_entry.pack(pady=20, padx=20, fill="x")
        self.task_entry.config(highlightbackground="#A5B4FC")

        # --------------------- MODERN BUTTONS ---------------------
        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(pady=5)

        self.add_btn = self.create_button(btn_frame, "Add Task", "#4F46E5", self.add_task)
        self.add_btn.grid(row=0, column=0, padx=10)

        self.del_btn = self.create_button(btn_frame, "Delete", "#EF4444", self.delete_task)
        self.del_btn.grid(row=0, column=1, padx=10)

        self.complete_btn = self.create_button(btn_frame, "Complete", "#10B981", self.complete_task)
        self.complete_btn.grid(row=1, column=0, pady=15)

        self.save_btn = self.create_button(btn_frame, "Save", "#0EA5E9", self.save_tasks)
        self.save_btn.grid(row=1, column=1)

        # --------------------- TASK LIST WITH SCROLLBAR ---------------------
        list_frame = tk.Frame(card, bg="white")
        list_frame.pack(padx=15, pady=10, fill="both", expand=True)

        self.listbox = tk.Listbox(
            list_frame, font=("Segoe UI", 14),
            bg="#F9FAFB", fg="#333",
            activestyle="none", bd=0,
            highlightthickness=1, highlightbackground="#E5E7EB",
            selectbackground="#E0E7FF"
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

    # --------------------- BUTTON CREATOR ---------------------
    def create_button(self, parent, text, color, command):
        btn = tk.Button(
            parent, text=text, font=("Segoe UI", 12, "bold"),
            bg=color, fg="white",
            activebackground=color, activeforeground="white",
            cursor="hand2", bd=0, relief="flat",
            padx=20, pady=10, command=command
        )
        self.add_hover_effect(btn, color)
        return btn

    # --------------------- HOVER EFFECT ---------------------
    def add_hover_effect(self, widget, base_color):
        def on_enter(e):
            widget.config(bg=self.lighten(base_color))
        def on_leave(e):
            widget.config(bg=base_color)
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def lighten(self, color):
        # Slightly lighten a hex color
        c = int(color[1:], 16)
        r = (c >> 16) + 20
        g = ((c >> 8) & 0xff) + 20
        b = (c & 0xff) + 20
        r = min(255, r)
        g = min(255, g)
        b = min(255, b)
        return f'#{r:02x}{g:02x}{b:02x}'

    # --------------------- FUNCTIONALITY ---------------------
    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.listbox.insert(tk.END, "• " + task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def delete_task(self):
        idx = self.get_selected()
        if idx is not None:
            self.listbox.delete(idx)

    def complete_task(self):
        idx = self.get_selected()
        if idx is not None:
            task = self.listbox.get(idx)
            self.listbox.delete(idx)
            self.listbox.insert(idx, task + " ✔")

    def save_tasks(self):
        fp = filedialog.asksaveasfilename(defaultextension=".txt",
                                          filetypes=[("Text Files", "*.txt")])
        if fp:
            with open(fp, "w") as f:
                for t in self.listbox.get(0, tk.END):
                    f.write(t + "\n")
            messagebox.showinfo("Saved", "Tasks saved successfully")

    def load_tasks(self):
        fp = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if fp:
            self.listbox.delete(0, tk.END)
            with open(fp, "r") as f:
                for line in f:
                    self.listbox.insert(tk.END, line.strip())

    def get_selected(self):
        try:
            return self.listbox.curselection()[0]
        except:
            messagebox.showwarning("Warning", "Select a task first")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernToDoApp(root)
    root.mainloop()
