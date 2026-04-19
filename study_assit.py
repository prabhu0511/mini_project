import tkinter as tk
from tkinter import filedialog

def load_file():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, content)

def summarize():
    text = input_text.get("1.0", tk.END)
    sentences = text.split(".")
    summary = ".".join(sentences[:3])  # simple summary
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)

def generate_questions():
    text = input_text.get("1.0", tk.END)
    words = text.split()
    
    questions = []
    for i in range(min(5, len(words))):
        questions.append(f"What is {words[i]}?")
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(questions))

def extract_keywords():
    text = input_text.get("1.0", tk.END)
    words = text.split()
    keywords = list(set(words[:20]))
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ", ".join(keywords))

# UI
root = tk.Tk()
root.title("Smart Study Assistant")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

tk.Label(root, text="📚 Smart Study Assistant", font=("Arial", 16),
         bg="#1e1e1e", fg="white").pack(pady=10)

input_text = tk.Text(root, height=10, width=70)
input_text.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

tk.Button(frame, text="Load Notes", command=load_file).pack(side="left", padx=5)
tk.Button(frame, text="Summarize", command=summarize).pack(side="left", padx=5)
tk.Button(frame, text="Generate Questions", command=generate_questions).pack(side="left", padx=5)
tk.Button(frame, text="Extract Keywords", command=extract_keywords).pack(side="left", padx=5)

output_text = tk.Text(root, height=10, width=70)
output_text.pack(pady=10)

root.mainloop()