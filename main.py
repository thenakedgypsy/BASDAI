import tkinter as tk  # Importing the Tkinter module with an alias

# Create the main window
root = tk.Tk()
root.title("BASDAI")
# make a pad
pad = tk.Label(root, text="--------------------------------------------------------------------------------------------------------------------------------------------------------")
pad.pack(pady=10)

#make the main label
label = tk.Label(root, text="This program will assess your Bath Ankylosing Spondylitis Disease Activity Index")
label.pack(pady=10)

#make a list to store buttons for later
buttons = []

#question counter 
question = 1



def cleanupButtons():
    for button in buttons:
        button.pack_forget()

def calculateScore(q1,q2,q3,q4,q5,q6):
    return ((q1 + q2 + q3 + q4) + ((q5 + q6) / 2)) / 5   

#add score selected and move to next question
def enterScore(number): 
    global question, score1, score2, score3, score4, score5, score6    
    if question == 1:
        score1 = number      
        setLabel("2. How would you describe the overall level of AS neck, back, or hip pain you have had?")
    elif question == 2:
        score2 = number        
        setLabel("3. How would you describe the overall level of pain/swelling in joints other than neck, back, or hips you have had?")
    elif question == 3:
        score3 = number       
        setLabel("4. How would you describe the overall level of discomfort you have had from any areas tender to touch or pressure?")
    elif question == 4:
        score4 = number        
        setLabel("5. How would you describe the overall level of discomfort you have had from the time you wake up?")
    elif question == 5:
        score5 = number        
        setLabel("6. How long does your morning stiffness last from the time you wake up? (0 = 0 hours, 5 = 1 hour, 10 = 2 hours+)")
    elif question == 6:
        score6 = number
        cleanupButtons()
        finalScore = calculateScore(score1, score2, score3, score4, score5, score6) 
        setLabel(f"Your BASDAI Score: {finalScore}")
    question += 1


def setLabel(labelText):
    label.config(text=labelText)

#  start button click
def start_button_click():
    # Update label first time:
    label.config(text="1. How would you describe the overall level of fatigue/tiredness you have experienced?")
    
    # cleanup start button
    start_button.pack_forget()
    
    
    # Add the new buttons
    for i in range(11):
        btn = tk.Button(root, text=str(i), command=lambda i=i: enterScore(i))
        btn.pack(padx=5)
        buttons.append(btn) #store these in a list so can be cleared up later. 
    lowpad = tk.Label(root, text="--------------------------------------------------------------------------------------------------------------------------------------------------------")
    lowpad.pack(pady=10)


# Create the start button
start_button = tk.Button(root, text="Start the questionnaire", command=start_button_click)
start_button.pack(pady=10)

lowpadStart = tk.Label(root, text="--------------------------------------------------------------------------------------------------------------------------------------------------------")
lowpadStart.pack(pady=10)


# Run the main event loop
root.mainloop()