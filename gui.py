import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

from analyzer import analyze_password_strength
from wordlist import generate_wordlist, save_wordlist

def toggle_password():
    password_entry.config(show="" if show_password.get() else "*")

def analyze_action():
    password = password_entry.get()
    result = analyze_password_strength(password)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)

def save_analysis():
    result = result_box.get("1.0", tk.END)
    if result.strip():
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w") as f:
                f.write(result)
            messagebox.showinfo("Saved", "Analysis result saved successfully.")
    else:
        messagebox.showwarning("No Data", "Please analyze a password first.")

def generate_and_save():
    name = name_entry.get()
    dob = dob_entry.get()
    pet = pet_entry.get()
    fav = fav_entry.get()

    if not any([name, dob, pet, fav]):
        messagebox.showwarning("Input Required", "Please enter at least one detail.")
        return

    wordlist = generate_wordlist(name, dob, pet, fav)
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if path:
        save_wordlist(wordlist, path)
        messagebox.showinfo("Success", f"Wordlist saved with {len(wordlist)} entries.")


root = tk.Tk()
root.title("Password Analyzer + Wordlist Generator")
root.geometry("720x700")
root.configure(bg="#1e1e2e")


tk.Label(root, text="Password Strength Analyzer with Wordlist Generator", font=("Helvetica", 16, "bold"), bg="#1e1e2e", fg="#ffffff").pack(pady=20)


frame1 = tk.LabelFrame(root, text="Analyze Password", bg="#2c2c3c", fg="white", font=("Arial", 11, "bold"), padx=15, pady=10, bd=2)
frame1.pack(padx=20, pady=10, fill="x")

tk.Label(frame1, text="Enter Password:", bg="#2c2c3c", fg="white").pack(anchor="w")
show_password = tk.BooleanVar()
password_entry = tk.Entry(frame1, width=50, show="*")
password_entry.pack(pady=5)

tk.Checkbutton(frame1, text="Show Password", variable=show_password, command=toggle_password, bg="#2c2c3c", fg="white", selectcolor="#1e1e2e").pack()

tk.Button(frame1, text="Analyze", command=analyze_action, bg="#4caf50", fg="white", width=20).pack(pady=5)
tk.Button(frame1, text="Save Result", command=save_analysis, bg="#2196f3", fg="white", width=20).pack()

tk.Label(frame1, text="Analysis Output:", bg="#2c2c3c", fg="white").pack(anchor="w", pady=(10, 0))
result_box = tk.Text(frame1, height=7, width=80, wrap="word", bg="#1e1e2e", fg="white")
result_box.pack(pady=5)


frame2 = tk.LabelFrame(root, text="Custom Wordlist Generator", bg="#2c2c3c", fg="white", font=("Arial", 11, "bold"), padx=15, pady=10, bd=2)
frame2.pack(padx=20, pady=10, fill="x")

form_frame = tk.Frame(frame2, bg="#2c2c3c")
form_frame.pack()

tk.Label(form_frame, text="Name", bg="#2c2c3c", fg="white").grid(row=0, column=0, padx=5, pady=4, sticky="e")
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Year of Birth", bg="#2c2c3c", fg="white").grid(row=1, column=0, padx=5, pady=4, sticky="e")
dob_entry = tk.Entry(form_frame, width=30)
dob_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Pet's Name", bg="#2c2c3c", fg="white").grid(row=2, column=0, padx=5, pady=4, sticky="e")
pet_entry = tk.Entry(form_frame, width=30)
pet_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Favorite Word/Team", bg="#2c2c3c", fg="white").grid(row=3, column=0, padx=5, pady=4, sticky="e")
fav_entry = tk.Entry(form_frame, width=30)
fav_entry.grid(row=3, column=1)

tk.Button(frame2, text="Generate & Save Wordlist", command=generate_and_save, bg="#ff9800", fg="white", width=30).pack(pady=10)


tk.Label(root, text="Use this tool ethically. Do not use it for unauthorized access.", font=("Arial", 9, "italic"), fg="red", bg="#1e1e2e").pack(pady=(10, 10))

root.mainloop()
