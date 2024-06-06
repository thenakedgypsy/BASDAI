import tkinter as tk  

print("BASDAI is launching...")
# make the tkinter window
root = tk.Tk()
root.title("BASDAI")

# make a padding string so things look a bit less jank
pad = tk.Label(root, text="♤----------------------------------------------------------------------------------------------------------------------------------------------------♡")
pad.pack(pady=10)

#make the main label
label = tk.Label(root, text="This program will assess your Bath Ankylosing Spondylitis Disease Activity Index")
label.pack(pady=10)

#make a list to store buttons for later
buttons = []

#question counter 
question = 1

# clean up the 10 buttons once they are done with
def cleanupButtons():
    for button in buttons:
        button.pack_forget()

# get the basdai score
def calculateScore(q1,q2,q3,q4,q5,q6):
    return ((q1 + q2 + q3 + q4) + ((q5 + q6) / 2)) / 5   

# add score for each question and move to next question
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
        setLabel(f"Your BASDAI Score: {calculateScore(score1, score2, score3, score4, score5, score6)}")
    question += 1

# update the main label
def setLabel(labelText):
    label.config(text=labelText)

#  remove start button and create the 10 score buttons, update label to first question
def startButtonClick():
    # update the tabel for the first question
    label.config(text="1. How would you describe the overall level of fatigue/tiredness you have experienced?")
    
    # cleanup start button
    startButton.pack_forget()
    
    
    # make and pack 10 buttons
    for i in range(11):
        btn = tk.Button(root, text=str(i), command=lambda i=i: enterScore(i)) # this lambda function captures i at the moment the button is...
        btn.pack(padx=5)                                                      #...created, rather than at the end. 
        buttons.append(btn) #store these in a list so can be cleared up later. 
    adjustBottomPad()

# repacks the bottom pad - needed to ensure it remains at the bottom   
def adjustBottomPad():
    lowPad.pack_forget()
    lowPad.pack(pady=10)

# create start button
startButton = tk.Button(root, text="Start the questionnaire", command=startButtonClick)
startButton.pack(pady=10)

# create the bottom pad
lowPad = tk.Label(root, text="♢------------------------------------------------------------------------------------------------------------------------------------------------------♧")
lowPad.pack()

# run tkinters loop
root.mainloop()