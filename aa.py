import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Multi-Frame App")

        # Create a container to hold all frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Define the frames and add them to the dictionary
        for F in (LoginForm, WelcomePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame(LoginForm)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create the widgets for the login form
        label = tk.Label(self, text="Login Form")
        label.pack()

        username_label = tk.Label(self, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(self)
        username_entry.pack()

        password_label = tk.Label(self, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        login_button = tk.Button(self, text="Login", command=lambda: self.login(controller))
        login_button.pack()

    def login(self, controller):
        # Perform login authentication logic here
        # For simplicity, let's assume the login is always successful
        controller.show_frame(WelcomePage)


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create the widgets for the welcome page
        label = tk.Label(self, text="Welcome!")
        label.pack()

        logout_button = tk.Button(self, text="Logout", command=lambda: controller.show_frame(LoginForm))
        logout_button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()