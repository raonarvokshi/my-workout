import pandas as pd
from tabulate import tabulate

day = input("Select the day you want: ")

def program(which_day):
    capitalize = which_day.capitalize()

    if capitalize == "Day 1":
      day_1 = pd.read_csv("data/days/day_1.csv")
      day_1 = day_1.drop(columns=["Unnamed: 0"], errors="ignore")
      print(tabulate(day_1, headers="keys", tablefmt="pretty", showindex=False))

    elif capitalize == "Day 2":
      day_2 = pd.read_csv("data/days/day_2.csv")
      day_2 = day_2.drop(columns=["Unnamed: 0"], errors="ignore")
      print(tabulate(day_2, headers="keys", tablefmt="pretty", showindex=False))

    elif capitalize == "Day 3":
      day_3 = pd.read_csv("data/days/day_3.csv")
      day_3 = day_3.drop(columns=["Unnamed: 0"], errors="ignore")
      print(tabulate(day_3, headers="keys", tablefmt="pretty", showindex=False))

    elif capitalize == "Day 4":
      day_4 = pd.read_csv("data/days/day_4.csv")
      day_4 = day_4.drop(columns=["Unnamed: 0"], errors="ignore")
      print(tabulate(day_4, headers="keys", tablefmt="pretty", showindex=False))

    elif capitalize == "Day 5":
      day_5 = pd.read_csv("data/days/day_5.csv")
      day_5 = day_5.drop(columns=["Unnamed: 0"], errors="ignore")
      print(tabulate(day_5, headers="keys", tablefmt="pretty", showindex=False))

    elif capitalize == "Day 6":
      day_6 = pd.read_csv("data/days/day_6.csv")
      day_6 = day_6.drop(columns=["Unnamed: 0"], errors="raise")
      print(tabulate(day_6, headers="keys", tablefmt="pretty", showindex=False))

    elif capitalize == "Day 7":
      day_7 = pd.read_csv("data/days/day_7.csv")
      day_7 = day_7.drop(columns=["Unnamed: 0"], errors="ignore")
      print(tabulate(day_7, headers="keys", tablefmt="pretty", showindex=False))

program(which_day=day)
