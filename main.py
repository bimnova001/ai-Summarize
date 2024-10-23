from transformers import pipeline
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox 
summarizer = pipeline("summarization",model="google-t5/t5-base")
def summarize_text():
    # Get the input text from the text area
    input_text = text_input.get("1.0", tk.END)
    
    # Check if input text is not empty
    if input_text.strip():
        # Summarize the text
        summary = summarize_long_text(input_text)
        # Display the summarized text in the output area
        summary_output.delete("1.0", tk.END)  # Clear previous output
        summary_output.insert(tk.END, summary)
    else:
        summary_output.delete("1.0", tk.END)  # Clear previous output
        summary_output.insert(tk.END, "Please enter some text to summarize.")

def summarize_long_text(text):
    max_lg = int(Max_Length.get())
    # Split the text into chunks if it's too long
    max_chunk_size = 1000  # Max tokens per chunk (adjust as needed)
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=max_lg, min_length=25, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return ' '.join(summaries)

# Create the main window
root = tk.Tk()
root.title("Text Summarization App by bim rmutl 1B")

text_max = tk.Label(root,text="max_Length")
text_max.pack()


Max_Length = tk.Entry(root)
Max_Length.pack(pady=2)

# Create a label
label = tk.Label(root, text="Enter Text to Summarize:")
label.pack(pady=10)

# Create a scrolled text area for input
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
text_input.pack(pady=10)

# Create a button to summarize the text
summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack(pady=10)

# Create a label for output
output_label = tk.Label(root, text="Summarized Text:")
output_label.pack(pady=10)

# Create a scrolled text area for output
summary_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
summary_output.pack(pady=10)


messagebox.showinfo("showinfo", "this ai is Eng only can't use thai : use google t5 base model ") 
messagebox.showwarning("showwarning", "you need wifi to load model first if any error don't ask me") 


# Start the GUI event loop
root.mainloop()