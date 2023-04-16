try:
    from tkinter import Label, Button, Tk, PhotoImage, filedialog, messagebox
    import pyautogui
    from sys import exit as jumpout
    from PIL import Image, ImageTk
    import pyperclip
    import io
    import base64
    from os import name, remove, system
except Exception as e:
    from os import system, name
    if name=='posix':
        system("pip3 install pillow pyautogui")
    else:
        from sys import exit as temp
        temp(2)
def exit(num):
    try:
        remove("/tmp/screenshot.png")
        jumpout(num)
    except Exception as e:
        if name == "posix":
            system("rm -r /tmp/screenshot.png")
        jumpout(num)

def taketempshot():
    try:
        pyautogui.screenshot("/tmp/screenshot.png")
        return 0
    except Exception as e:
        print(e)
        return 1


def copy():
    try:
        with open("/tmp/screenshot.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        pyperclip.copy(encoded_string)

        exit(0)
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Could not copy image to clipboard")
        exit(1)

def save():
    try:
        image = Image.open("/tmp/screenshot.png")
        savepath = filedialog.asksaveasfilename(defaultextension=".png", initialfile="screenshot.png")
        image.save(savepath)
        exit(0)
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Could not save image to location {savepath}")
        exit(1)


if name == "nt":
    messagebox.showinfo("Sorry, this program cannot run in Windows, we are working on it currently")
    jumpout(2)
else:
    # Posix
    pass

f = open("loc.txtx", "r")
fdata = f.read()
f.close()

fdata = fdata.strip()

root = Tk()
root.title("Xshot")
root.geometry("400x300+350+200")
favicon = PhotoImage(file=f"{fdata}/favicon.png")
root.iconphoto(False, favicon)
root.maxsize(height=300, width=400)
root.config(bg = "#121212")
root.resizable(0,0)

if taketempshot() == 0:
    pass
else:
    messagebox.showerror("Error", "Screenshot was not taken")
    exit(1)

image = Image.open("/tmp/screenshot.png")
width, height = image.size

max_width = 400
max_height = 400

scale = min(max_width/width, max_height/height)

new_width = int(width * scale)
new_height = int(height * scale)

image = image.resize((new_width, new_height), Image.LANCZOS)

scrshot = ImageTk.PhotoImage(image)

sshotw = Label(image=scrshot)
sshotw.pack()

bottomgrid = Label()
bottomgrid.pack(side="bottom", fill="both", expand=True)

leftb = Button(bottomgrid, text="Save", fg="white", bg="#121212", relief="flat", borderwidth=0, highlightthickness=0, command=save)
leftb.pack(side="left", fill="both", expand=True, anchor="w")

rightb = Button(bottomgrid, text="Copy", fg="white", bg="#121212", relief="flat", borderwidth=0, highlightthickness=0, command=copy)
rightb.pack(side="right", fill="both", expand=True, anchor="e")

root.mainloop()
exit(0)
