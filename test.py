from customtkinter import CTkFrame, CTkLabel
import customtkinter as ctk



app = ctk.CTk()
app.title("Tester")
app.configure(background="white", fg_color="white")
firstText = CTkLabel(app, text="Hello word", text_color="black")
firstText.pack()
div = CTkFrame(app, border_width=2,border_color="dodgerblue")
div.pack()
for widget in app.widgets():
    widget.destroy()
app.mainloop()
