import tkinter as tk
import openai

openai.api_key = "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"

#generating a response using OpenAi GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

#for GUI interface

def display_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

    
#creating the main window

    
root = tk.Tk()
root.title("OpenAI Chatbox")
''
root.geometry("600x700")
''
#creating an input field
input_field = tk.Entry(root, font=("Arial", 14))
input_field.pack(pady=10)

#creating submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=display_response)
submit_button.pack(pady=10)

#creating an output field
output_field = tk.Text(root, font=("Arial", 14), state='disabled')
output_field.pack(pady=10)

#starting the GUI event loop
root.mainloop()

