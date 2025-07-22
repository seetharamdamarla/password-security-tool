import tkinter as tk
from tkinter import messagebox, filedialog

from analyzer import analyze_password_strength
from wordlist import generate_wordlist, save_wordlist

root = tk.Tk()
root.title("🔐 Password Strength Analyzer with Custom Wordlist Generator")
root.geometry("600x600")
root.resizable(False, False)

# Password Entry
show_password = tk.BooleanVar()

def toggle_password():
    password_entry.config(show="" if show_password.get() else "*")

tk.Label(root, text="🔍 Enter Password to Analyze:").pack(pady=(10, 0))
password_entry = tk.Entry(root, width=50, show="*")
password_entry.pack(pady=5)
tk.Checkbutton(root, text="Show Password", variable=show_password, command=toggle_password).pack()

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

tk.Button(root, text="Analyze Password", command=analyze_action).pack(pady=5)
tk.Button(root, text="Save Analysis", command=save_analysis).pack(pady=(0, 10))

# Result Box
tk.Label(root, text="📊 Analysis Result:").pack()
result_box = tk.Text(root, height=8, width=70)
result_box.pack(pady=5)

# Wordlist Generator

# Form Fields
tk.Label(root, text="🛠️  Custom Wordlist Generator", font=("Arial", 12, "bold")).pack(pady=10)
form_frame = tk.Frame(root)
form_frame.pack()

tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=2)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Year of Birth").grid(row=1, column=0, padx=5, pady=2)
dob_entry = tk.Entry(form_frame)
dob_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Pet's Name").grid(row=2, column=0, padx=5, pady=2)
pet_entry = tk.Entry(form_frame)
pet_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Favorite Word/Team").grid(row=3, column=0, padx=5, pady=2)
fav_entry = tk.Entry(form_frame)
fav_entry.grid(row=3, column=1)

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

tk.Button(root, text="Generate & Save Wordlist", command=generate_and_save).pack(pady=10)

# Disclaimer
tk.Label(root, text="⚠️ For ethical use only. Don't use this for unauthorized access.", fg="red", font=("Arial", 8)).pack(pady=(10, 0))

root.mainloop()
