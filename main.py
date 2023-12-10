import tkinter as tk
from tkinter import ttk
import re
from ttkbootstrap import Style


def disable_resize(event=None):
    return False

class User:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

class LoginPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)
        self.email_entry.insert(0,'admin@gmail.com')

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''            


class MainMenu(ttk.Frame):
    def __init__(self, parent, width=10, borderwidth=10):
        super().__init__(parent, width=width, borderwidth=borderwidth)
        self.pack(side=tk.LEFT, fill=tk.Y)
        ttk.Button(self, text="QL Giả Lập", width=10, command=self.show_content("quanly")).pack(pady=5)
        ttk.Button(self, text="Cài Đặt", width=10).pack( pady=5)
        ttk.Button(self, text="Thoát", width=10).pack(pady=5)

    def show_content(self,page):
        match page:
            case "quanly":
                print("QL Giả Lập")
            case "thoat":
                print("Thoát")

                
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:
            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)    

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        style = Style(theme="litera")
        window = style.master

        self.resizable(False, False)
        self.title("Social Marketing Tool")
        self.geometry("800x600")
        # create a model
        # model = User('admin@gmail.com')

        # create a view and place it on the root window
        # view = MainMenu(self)
        # view.grid(row=0, column=0, padx=10, pady=10)
        # controller = Controller(model, view)
        # view.set_controller(controller)

        view = MainMenu(self)   

if __name__ == '__main__':
    app = App()
    app.mainloop()