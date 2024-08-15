from tkinter import *
root = Tk()
pictureNum = 0
label = Label(padx=10, pady=10)

def nextPicture():
    global pictureNum
    if pictureNum == 7:
        pictureNum = 1
    else:
        pictureNum += 1
    img = PhotoImage(file=f"pups/pup{pictureNum}.png")
    label.config(image=img)
    label.photo = img
    root.update()


nextButton = Button(
    text="Next",
    command=nextPicture,
    padx=10,
    pady=10
)

label.grid(row=0, column=0, sticky=NSEW)
nextButton.grid(row=1, column=0, columnspan=3, sticky=NSEW)
nextPicture()

root.mainloop()
