import os
import ctypes
import pyautogui as ag
import pygetwindow as gw
import pyperclip
import tkinter as tk
from tkinter import messagebox
from time import sleep


# ===========================
# Keyboard Utilities
# ===========================
def Check_Keyboard_Is_En():
    """تأكد أن لوحة المفاتيح على الإنجليزية"""
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lid_hex = hex(klid & 0xFFFF)

    if lid_hex != '0x409':  # English
        with ag.hold("shift"):
            ag.press("alt")
        return Check_Keyboard_Is_En()


# ===========================
# Window Utilities
# ===========================
def Check_Maximum_Window():
    active_window = gw.getActiveWindow()
    if not active_window.isMaximized:
        active_window.maximize()


def Minimize_Windows():
    with ag.hold("win"):
        ag.press("d")
    ag.moveTo(x=1026, y=586)


def Minimize_The_Window():
    active_window = gw.getActiveWindow()
    if not active_window.isMinimized:
        active_window.minimize()


def Close_Window():
    active_window = gw.getActiveWindow()
    active_window.close()


# ===========================
# Timing Utilities
# ===========================
def Wait00():
    sleep(1)
    sleep(2)
    sleep(2)


def Wait01():
    sleep(10)  # Consolidated multiple sleeps


# ===========================
# Scrolling
# ===========================
def Scroll_Down():
    ag.keyDown("ctrl")
    ag.keyDown("down")
    ag.keyUp("down")
    ag.keyUp("ctrl")


# ===========================
# Bluetooth & Improvements
# ===========================
def Bleutooth_And_Improvements():
    def Repair_Bluetooth():
        ag.press("win")
        sleep(0.3)
        ag.click(1341, 461)
        sleep(0.6)
        Check_Maximum_Window()
        sleep(0.9)
        ag.click(1820, 323)
        sleep(0.5)
        ag.click(1079, 695)
        sleep(1.2)
        ag.click(x=416, y=168)
        Wait00()
        ag.click(x=416, y=168)
        sleep(0.7)

    def Add_Earphone():
        ag.click(1766, 285)
        sleep(0.5)
        user_choice = ag.confirm(" :السماعة", buttons=["متصل", "غير متصل"])
        if user_choice != "متصل":
            sleep(0.5)
            ag.click(x=1371, y=365)
            sleep(0.5)
            ag.press("space")
            sleep(1)
            ag.press("space")
            ag.moveTo(x=962, y=335)
            ag.moveTo(x=1022, y=336)
            sleep(0.5)
            ag.alert("أختار السماعة، وأضغط علي موافق")
            sleep(0.5)
            ag.click(x=779, y=767)

    def Add_Advantages():
        ag.click(1811, 247)
        sleep(1)
        ag.click(1167, 322)
        sleep(1)
        ag.press("pagedown")
        sleep(1)
        ag.click(x=732, y=879)
        sleep(1)
        ag.press("pagedown")
        sleep(0.4)
        ag.press("space")
        sleep(0.6)
        ag.keyDown("ctrl")
        ag.keyDown("tab")
        ag.keyDown("tab")
        ag.keyUp("tab")
        ag.keyUp("ctrl")
        ag.alert("ضيف التحسينات، وأضغط علي موافق")
        sleep(0.6)
        ag.keyDown("ctrl")
        ag.keyDown("tab")
        ag.keyDown("tab")
        ag.keyUp("tab")
        ag.keyUp("ctrl")
        ag.alert("شغل التحسينات، وأضغط علي موافق")
        ag.press("enter")
        ag.press("enter")
        Close_Window()

    Repair_Bluetooth()
    Add_Earphone()
    Add_Advantages()
    Close_Window()


# ===========================
# Open Applications
# ===========================
def Edge():
    ag.click(1395, 1053)
    sleep(0.6)
    ag.click(1395, 1053)
    sleep(0.1)


def VS_Code():
    ag.press("win")
    sleep(0.25)
    ag.click(1541, 631)
    sleep(1)


def File_explorer():
    ag.click(1442, 1054)
    sleep(1.5)
    Check_Maximum_Window()
    sleep(1)
    ag.alert("شغل القرأن، وأضغط علي موافق")
    sleep(1)
    ag.click(x=435, y=10)
    Close_Window()
    path = r"D:\محمد\Working Area"
    os.startfile(path)
    pyperclip.copy(path)
    ag.click(x=771, y=532)
    ag.alert("أختار الملف، وأضغط علي موافق")


# ===========================
# Other Orders
# ===========================
def Other_Orders():
    def RGB_Keyboard():
        ag.press("scrolllock")
        sleep(0.3)

    def Notification():
        ag.click(100, 1052)
        sleep(0.5)
        ag.click(x=100, y=1053)
        Minimize_Windows()

    def Task_Manager():
        ag.click(1353, 1046)
        ag.moveTo(x=345, y=288)
        sleep(0.2)

    RGB_Keyboard()
    Notification()
    Task_Manager()


# ===========================
# Color Utility
# ===========================
def Get_Colour():
    screenshot = ag.screenshot()
    r, g, b = screenshot.getpixel((896, 1062))
    return f"#{r:02X}{g:02X}{b:02X}"


# ===========================
# User Interface
# ===========================
def User_Orders():
    App = tk.Tk()
    App.title("Mahamed's Orders")
    App.geometry("185x230")
    background = "#272727"
    App.configure(bg=background)
    colour = Get_Colour()
    App.attributes("-alpha", 0.9)

    var1, var2, var3, var4, var5, var6 = [tk.IntVar() for _ in range(6)]
    check_vars = [var1, var2, var3, var4, var5, var6]

    text = tk.Label(App, text="      << أوامرك يا محمد بيه >>",
                    height=1, font=("Arial", 12), bg=background, fg=colour)
    text.grid(row=0, column=0, sticky="nsew")

    # Checkbuttons
    labels = ["Earphone", "Edge", "Vs Code", "Quran and File", "Mini All Windows", "Other Orders"]
    for i, (label, var) in enumerate(zip(labels, check_vars), start=1):
        chk = tk.Checkbutton(App, text=label, height=1, font=("Arial", 12),
                             bg=background, fg=colour, variable=var)
        chk.grid(row=i, sticky="w")

    # Buttons Frame
    frame = tk.Frame(App, bg=background)
    frame.grid(row=7, column=0, columnspan=2)

    def Execute_Selection(event=None):
        sleep(1)
        if var1.get():
            Bleutooth_And_Improvements()
        if var2.get():
            Edge()
        if var3.get():
            VS_Code()
        if var4.get():
            File_explorer()
        if var5.get():
            Minimize_Windows()
        if var6.get():
            Other_Orders()
        for var in check_vars:
            var.set(0)

    def Select_All(event=None):
        if all(var.get() == 1 for var in check_vars):
            for var in check_vars:
                var.set(0)
        else:
            for var in check_vars:
                var.set(1)

    def Close_App():
        if messagebox.askyesno("غلق التطبيق", "هل تريد حقاً غلق التطبيق؟"):
            App.destroy()

    btn1 = tk.Button(frame, text="Select All", height=0, font=("Arial", 12),
                     bg="#121212", fg=colour, borderwidth=0, command=Select_All)
    btn1.invoke()
    App.bind("<Control-A>", Select_All)
    App.bind("<Control-a>", Select_All)

    btn2 = tk.Button(frame, text="تنفيذ", height=0, font=("Arial", 12),
                     bg="#121212", fg=colour, borderwidth=0, command=Execute_Selection)
    App.bind("<Return>", Execute_Selection)

    btn3 = tk.Button(frame, text="غلق", height=0, font=("Arial", 12),
                     bg="#121212", fg=colour, borderwidth=0, command=Close_App)

    btn1.grid(row=0, column=1, padx=(2, 0))
    btn2.grid(row=0, column=0, padx=(15, 0))
    btn3.grid(row=0, column=2, padx=(2, 0))

    App.mainloop()


# ===========================
# Main Execution
# ===========================
def Open_App():
    sleep(1)
    Check_Keyboard_Is_En()
    Minimize_Windows()
    ag.alert("\t<< .مرحباً، محمد >>\n    نتمنى لك النجاح والتوفيق إن شاء الله")
    User_Orders()
    ag.moveTo(x=863, y=426)


Open_App()
