import tkinter as tk
from tkinter import messagebox
import language_tool_python
from textblob import TextBlob


def spell_check(text):
    """Corrects spelling in the input text."""
    blob = TextBlob(text)
    return str(blob.correct())


def grammar_check(text):
    """Checks and corrects grammar in the input text."""
    tool = language_tool_python.LanguageTool('en-US')  # Use 'en-GB' for British English
    matches = tool.check(text)
    
    # Manually apply corrections based on matches
    corrected_text = text
    for match in matches:
        if match.replacements:  # Only apply if there are suggested replacements
            start = match.offset
            end = match.offset + match.errorLength
            corrected_text = (
                corrected_text[:start] +
                match.replacements[0] +
                corrected_text[end:]
            )
    return corrected_text


def process_text():
    """Processes the text for spell and grammar correction."""
    input_text = input_text_box.get("1.0", tk.END).strip()  # Get input text from the text box
    if not input_text:
        messagebox.showerror("Error", "Please enter some text to check!")
        return

    # Step 1: Perform spell correction
    spell_corrected_text = spell_check(input_text)

    # Step 2: Perform grammar correction
    grammar_corrected_text = grammar_check(spell_corrected_text)

    # Display the corrected text
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, grammar_corrected_text)


# Create the main GUI window
root = tk.Tk()
root.title("Grammar and Spell Checker")
root.geometry("600x400")
root.resizable(False, False)

# Input text box
tk.Label(root, text="Enter text:", font=("Arial", 14)).pack(pady=5)
input_text_box = tk.Text(root, wrap="word", font=("Arial", 12), height=10, width=70)
input_text_box.pack(pady=10)

# Process button
process_button = tk.Button(root, text="Check Spelling and Grammar", font=("Arial", 12), command=process_text)
process_button.pack(pady=10)

# Output text box
tk.Label(root, text="Corrected text:", font=("Arial", 14)).pack(pady=5)
output_text_box = tk.Text(root, wrap="word", font=("Arial", 12), height=10, width=70, state="normal")
output_text_box.pack(pady=10)

# Start the GUI event loop
root.mainloop()
