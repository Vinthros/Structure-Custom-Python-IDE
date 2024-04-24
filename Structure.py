import tkinter as tk
import subprocess as sb
import sys

application = tk.Tk()
application.geometry("1280x720")
application.title("Structure")

sidebar_left = tk.Frame(master=application, relief=tk.RIDGE, width=240, height=720, borderwidth=6)
sidebar_left.place(x=0, y=0)

scaffold_frame = tk.Frame(master=sidebar_left, relief=tk.SUNKEN, width=200, height=640, borderwidth=4)
scaffold_frame.place(x=15, y=40)

editor = tk.Text(master=application, relief=tk.GROOVE, width=124, height=42, borderwidth=4)
editor.place(x=260,y=20)
editor.insert("1.0", "# Structure IDE: Created by Liam Ng\n\nprint(\'Hello World\')")

def run():
    program = editor.get("1.0", "end")
    result = sb.run(['python', '-c', program], capture_output=True, text=True)
    
    output_window = tk.Tk()
    output_window.geometry("720x480")
    output_window.title("Structure: Output")

    output = tk.Text(master=output_window, relief=tk.GROOVE, width=84, height=20)
    output.place(x=20, y=20)
    output.insert("1.0", result.stdout)

    terminal = tk.Text(master=output_window, relief=tk.GROOVE, width=84, height=7)
    terminal.place(x=20, y=355)
    terminal.insert("1.0", result.stderr)

run_button = tk.Button(master=sidebar_left, text="RUN", command=run)
run_button.place(x=15, y=675)

def clear():
    confirmation_window = tk.Tk()
    confirmation_window.geometry("240x60")
    confirmation_window.title("Structure: Confirm Clear")

    def confirm():
        editor.delete("1.0", "end")
        confirmation_window.destroy()
    
    label_a = tk.Label(master=confirmation_window, text="Are you sure you want to clear the console?")
    label_a.place(x=0, y=0)

    confirm_button = tk.Button(master=confirmation_window, text="Confirm", command=confirm)
    confirm_button.place(x=90, y=25)

    confirmation_window.mainloop()

clear_button = tk.Button(master=application, text=" X ", command=clear)
clear_button.place(x=1230, y=25)

class scripter:
    def __init__(self):
        self.methods = [{
            "name": "New Variable",
            "function": self.var
        }, {
            "name": "Modify Variable",
            "function": self.modify_var
        }, {
            "name": "Import Module",
            "function": self.module
        }, {
            "name": "Create Loop",
            "function": self.loop
        }, {
            "name": "Create Infinite Loop",
            "function": self.fvr_loop
        }, {
            "name": "Create Error Handler",
            "function": self.error_handle
        }]
    
    def var(self):
        global application, sidebar_left, scaffold_frame, editor

        definer_window = tk.Tk()
        definer_window.title("Scaffold: New Variable")
        definer_window.geometry("220x80")

        label_a = tk.Label(master=definer_window, text="Name:")
        label_a.place(x=0, y=0)
        
        label_b = tk.Label(master=definer_window, text="Value:")
        label_b.place(x=0, y=25)

        name_entry = tk.Entry(master=definer_window, width=25)
        name_entry.place(x=50, y=0)

        value_entry = tk.Entry(master=definer_window, width=25)
        value_entry.place(x=50, y=25)

        def confirm():
            global application, sidebar_left, scaffold_frame, editor
            editor.insert("insert", f"{name_entry.get()} = {value_entry.get()}\n")
            definer_window.destroy()
        
        confirm_button = tk.Button(master=definer_window, text="Confirm", command=confirm)
        confirm_button.place(x=80, y=50)

        definer_window.mainloop()

    def module(self):
        global application, sidebar_left, scaffold_frame, editor

        definer_window = tk.Tk()
        definer_window.title("Scaffold: Import Module")
        definer_window.geometry("220x100")

        label_a = tk.Label(master=definer_window, text="Name:")
        label_a.place(x=0, y=0)
        
        label_b = tk.Label(master=definer_window, text="Alias:")
        label_b.place(x=0, y=40)

        selected = tk.StringVar(definer_window)
        packages = sys.builtin_module_names
        package_list = list(packages)
        selected.set("Select...")

        name_entry = tk.OptionMenu(definer_window, selected, *package_list)
        name_entry.config(width=15, height=1)
        name_entry.place(x=50, y=0)

        def custom_module():
            selector_window = tk.Tk()
            selector_window.title("Scaffold: Import Module >> Custom Module")
            selector_window.geometry("220x60")

            label_c = tk.Label(master=selector_window, text="Module:")
            label_c.place(x=0, y=0)

            custom_name_entry = tk.Entry(master=selector_window, width=25)
            custom_name_entry.place(x=50, y=0)

            def custom_confirm():
                selected.set(custom_name_entry.get())
                selector_window.destroy()
            
            custom_confirm_button = tk.Button(master=selector_window, text="confirm", command=custom_confirm)
            custom_confirm_button.place(x=80, y=25)

            selector_window.mainloop()

        custom = tk.Button(master=definer_window, width=3, height=1, text="...", command=custom_module)
        custom.place(x=185, y=2)

        alias_entry = tk.Entry(master=definer_window, width=25)
        alias_entry.place(x=50, y=40)

        def confirm():
            global application, sidebar_left, scaffold_frame, editor
            if alias_entry.get() == "":
                editor.insert("1.0", f"import {selected.get()}\n")
            else:
                editor.insert("1.0", f"import {selected.get()} as {alias_entry.get()}\n")
            definer_window.destroy()
        
        confirm_button = tk.Button(master=definer_window, text="Confirm", command=confirm)
        confirm_button.place(x=80, y=65)
    
    def loop(self):
        global application, sidebar_left, scaffold_frame, editor

        definer_window = tk.Tk()
        definer_window.title("Scaffold: Create Loop")
        definer_window.geometry("220x60")

        label_a = tk.Label(master=definer_window, text="Repeats:")
        label_a.place(x=0, y=0)

        loop_entry = tk.Entry(master=definer_window, width=25)
        loop_entry.place(x=50, y=0)

        def confirm():
            global application, sidebar_left, scaffold_frame, editor
            editor.insert("insert", f"\nfor i in range({loop_entry.get()}):\n\tpass")
            definer_window.destroy()
        
        confirm_button = tk.Button(master=definer_window, text="Confirm", command=confirm)
        confirm_button.place(x=80, y=25)
    
    def error_handle(self):
        global application, sidebar_left, scaffold_frame, editor

        editor.insert("insert", "\ntry:\n\tpass\nexcept:\n\tpass")
    
    def modify_var(self):
        global application, sidebar_left, scaffold_frame, editor

        definer_window = tk.Tk()
        definer_window.title("Scaffold: Create Loop")
        definer_window.geometry("240x120")

        label_a = tk.Label(master=definer_window, text="Variable:")
        label_a.place(x=0, y=0)

        label_b = tk.Label(master=definer_window, text="Value:")
        label_b.place(x=0, y=25)

        label_c = tk.Label(master=definer_window, text="Operation:")
        label_c.place(x=0, y=50)

        var_entry = tk.Entry(master=definer_window, width=25)
        var_entry.place(x=70, y=0)

        val_entry = tk.Entry(master=definer_window, width=25)
        val_entry.place(x=70, y=25)

        opr = tk.StringVar(definer_window)
        opr.set("Select...")
        opr_list = ["None", "+", "-", "*", "/"]
        opr_entry = tk.OptionMenu(definer_window, opr, *opr_list)
        opr_entry.config(width=18, height=1)
        opr_entry.place(x=70, y=50)

        def confirm():
            global application, sidebar_left, scaffold_frame, editor
            if opr.get() == "None":
                editor.insert("insert", f"{var_entry.get()} = {val_entry.get()}")
            else:
                editor.insert("insert", f"{var_entry.get()} {opr.get()}= {val_entry.get()}")
            definer_window.destroy()
        
        confirm_button = tk.Button(master=definer_window, text="Confirm", command=confirm)
        confirm_button.place(x=90, y=90)
    def fvr_loop(self):
        global application, sidebar_left, scaffold_frame, editor

        editor.insert("insert", "\nwhile True:\n\tpass")

scaffold = scripter()

for methods in scaffold.methods:
    new_method = tk.Button(scaffold_frame, text=methods["name"], command=methods["function"], width=26, height=1)
    new_method.pack()

application.mainloop()