from tkinter import *
from tkinter import ttk
import Dictionary
import sys
import tkinter as tk


class travelReview:
    preference = None
    preference1 = None
    preference2 = None

    def __init__(self, argv):

        func = tk.Tk()
        func.title('Attractions recommendations')
        func.geometry('400x300')

        Label(func, text="Preference", font=100).grid(row=2)
        Label(func, text="Preference", font=100).grid(row=3)
        Label(func, text="Preference", font=100).grid(row=4)

        self.preference = StringVar()
        self.preference1 = StringVar()
        self.preference2 = StringVar()

        comboBox = ttk.Combobox(func, textvariable=self.preference, state="readonly",
                                values=(Dictionary.names)).grid(row=2, column=1)
        comboBox1 = ttk.Combobox(func, textvariable=self.preference1, state="readonly",
                                 values=(Dictionary.names)).grid(row=3, column=1)
        comboBox2 = ttk.Combobox(func, textvariable=self.preference2, state="readonly",
                                 values=(Dictionary.names)).grid(row=4, column=1)

        Button(func, text='Recommend', command=self.execute).grid(row=6, column=1, sticky=W, pady=4)

        mainloop()

    def execute(self):

        func = tk.Tk()
        func.title('Recommended')
        func.geometry('400x300')

        pref = self.preference.get()
        pref1 = self.preference1.get()
        pref2 = self.preference2.get()

        rec = []
        recommendation = []

        recommendation_list = [pref, pref1, pref2]
        for item in recommendation_list:
            if item and item != '':
                for i in Dictionary.data[item]:
                    rec.append(i)
            else:
                continue

        recommendation_set = set(rec)
        for a in recommendation_set:
            recommendation.append(a)

        t = tk.Text(func, height=4, width=40)
        t.insert(tk.END, recommendation)

        t.pack()
        tk.mainloop()


travelReview(sys.argv)