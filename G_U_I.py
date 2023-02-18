from funcs import *
from tkinter import * 
from tkinter.ttk import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


specimen = pd.read_csv("specimenDate_ageDemographic-unstacked.xls - specimenDate_ageDemographic-unstacked.csv")
new_data = specimen[['areaType', 'areaCode', 'areaName', 'date', 'newCasesBySpecimenDate-0_4', 'newCasesBySpecimenDate-0_59',
       'newCasesBySpecimenDate-10_14', 'newCasesBySpecimenDate-15_19',
       'newCasesBySpecimenDate-20_24', 'newCasesBySpecimenDate-25_29',
       'newCasesBySpecimenDate-30_34', 'newCasesBySpecimenDate-35_39',
       'newCasesBySpecimenDate-40_44', 'newCasesBySpecimenDate-45_49',
       'newCasesBySpecimenDate-50_54', 'newCasesBySpecimenDate-55_59',
       'newCasesBySpecimenDate-5_9', 'newCasesBySpecimenDate-60+',
       'newCasesBySpecimenDate-60_64', 'newCasesBySpecimenDate-65_69',
       'newCasesBySpecimenDate-70_74', 'newCasesBySpecimenDate-75_79',
       'newCasesBySpecimenDate-80_84', 'newCasesBySpecimenDate-85_89',
       'newCasesBySpecimenDate-90+', 'newCasesBySpecimenDate-unassigned',]]

url = "https://data.police.uk/api/stops-force"
forces = requests.get("https://data.police.uk/api/forces").json()






root = Tk()
root.title("GUI")
root.geometry("800x600")

Label1 = Label(root, text= "-------------FIRST QUESTION(COVID SEARCH)---------------")
Label1.pack()


#------------------------------- SUB WINDOWS FUNCTIONS -----------------------------
def sub_cases_per_day_window():
    sub = Toplevel(root)

    sub.title("Cases Per Day")

    Label(sub, text="Enter start date and End Date in the format YYYY-MM-DD").pack()

    sub.geometry("400x400")

    St = StringVar(sub)
    Et = StringVar(sub)

    start = Entry(sub, text="Start", textvariable=St)
    end = Entry(sub, text="End", textvariable=Et)

    confirm = Button(sub, text = "Confirm", command=lambda: plot_of_cases_per_day(St, Et))

    start.pack()
    end.pack()
    confirm.pack()
    
def sub_cases_per_week_window():
    sub = Toplevel(root)

    sub.title("Cases Per Week")

    Label(sub, text="Enter start date and End Date in the format YYYY-MM-DD").pack()

    sub.geometry("400x400")

    St = StringVar(sub)
    Et = StringVar(sub)

    start = Entry(sub, text="Start", textvariable=St)
    end = Entry(sub, text="End", textvariable=Et)

    confirm = Button(sub, text = "Confirm", command=lambda: plot_of_cases_per_week(St, Et))

    start.pack()
    end.pack()
    confirm.pack()

def sub_cases_per_area_per_day_window():
    sub = Toplevel(root)

    sub.title("Cases Per area per day")

    Label(sub, text="Enter start date and End Date in the format YYYY-MM-DD").pack()

    sub.geometry("400x400")

    St = StringVar(sub)

    start = Entry(sub, text="Start", textvariable=St)

    confirm = Button(sub, text = "Confirm", command=lambda: plot_of_cases_per_area_day(St))

    start.pack()
    confirm.pack()    

def sub_cases_per_area_per_week_window():
    sub = Toplevel(root)

    sub.title("Cases Per area per week")

    Label(sub, text="Enter start date and End Date in the format YYYY-MM-DD").pack()

    sub.geometry("400x400")

    St = StringVar(sub)
    Et = StringVar(sub)

    start = Entry(sub, text="Start", textvariable=St)
    end = Entry(sub, text="End", textvariable=Et)

    confirm = Button(sub, text = "Confirm", command=lambda: plot_of_cases_per_area_week(St, Et))

    start.pack()
    end.pack()
    confirm.pack()

def sub_cases_compare_daily_window():
    sub = Toplevel(root)

    sub.title("Cases compare daily")

    Label(sub, text="Enter start date and End Date in the format YYYY-MM-DD").pack()

    sub.geometry("600x600")

    St = StringVar(sub)
    Et = StringVar(sub)
    Af = StringVar(sub)
    As = StringVar(sub)

    Label(sub, text="Enter Dates Below").pack()
    start = Entry(sub, text="Start", textvariable=St)
    end = Entry(sub, text="End", textvariable=Et)
    Label(sub, text="Enter Areas Below").pack()
    area1 = Entry(sub, text="Start", textvariable=Af)
    area2 = Entry(sub, text="End", textvariable=As)

    confirm = Button(sub, text = "Confirm", command=lambda: plot_of_areas_comapare_day(St, Et, Af, As))

    start.pack()
    end.pack()
    area1.pack()
    area2.pack()
    confirm.pack()

def sub_cases_compare_cumm_daily_window():
    sub = Toplevel(root)

    sub.title("Compare Cases cummulative daily")

    Label(sub, text="Enter start date and End Date in the format YYYY-MM-DD").pack()

    sub.geometry("600x600")

    St = StringVar(sub)
    Et = StringVar(sub)
    Af = StringVar(sub)
    As = StringVar(sub)

    Label(sub, text="Enter Dates Below").pack()
    start = Entry(sub, text="Start", textvariable=St)
    end = Entry(sub, text="End", textvariable=Et)
    Label(sub, text="Enter Areas Below").pack()
    area1 = Entry(sub, text="Start", textvariable=Af)
    area2 = Entry(sub, text="End", textvariable=As)

    confirm = Button(sub, text = "Confirm", command=lambda: plot_of_areas_comapare_cumm_day(St, Et, Af, As))

    start.pack()
    end.pack()
    area1.pack()
    area2.pack()
    confirm.pack()

#-------------------------- PLOT FUNCTIONS --------------------------------------------------------------
def plot_of_cases_per_day(st: StringVar, et: StringVar):

    res,name = plot_cases_per_day(specimen, "date", st.get(), et.get())

    plt.plot(name, res)
    plt.xlabel("Dates")
    plt.ylabel("Number of cases")
    plt.title("Reported cases daily")
    plt.tight_layout()
    plt.show()

my_button = Button(root, text="1. Plot of Cases Per Day", command=sub_cases_per_day_window)
my_button.pack()

def plot_of_cases_per_week(st: StringVar, et: StringVar):

    val, wks = plot_cases_per_week(new_data, "date", st.get(), et.get())

    plt.bar(wks, val)
    plt.xlabel("Weeks")
    plt.ylabel("Number of Reported cases")
    plt.title("Number of reported cases per week")
    plt.tight_layout()
    plt.show()

my_button2 = Button(root, text="2. Plot of Cases Per Week", command=sub_cases_per_week_window)
my_button2.pack()

def plot_of_cases_per_month():

    m_val, m_names = plot_monthly_cases(new_data, "date")

    plt.bar(m_names, m_val)
    plt.xlabel("Months")
    plt.ylabel("Number of Reported cases")
    plt.title("Number of Reported cases each month")
    plt.tight_layout()
    plt.show()

my_button3 = Button(root, text="3. Plot of Cases Per Month", command=plot_of_cases_per_month)
my_button3.pack()

def plot_of_cases_per_area_day(st: StringVar):

    areas, cs = plot_cases_per_area_day(new_data, "date", st.get())
    plt.pie(x = cs, labels = areas)
    plt.title("Areas with the highest number of reported cases for 2020-03-20")
    plt.xlabel("Area")
    plt.ylabel("Number of reported cases")
    plt.tight_layout()
    plt.show()

my_button4 = Button(root, text="4. Plot of Cases Per Area Day", command=sub_cases_per_area_per_day_window)
my_button4.pack()

def plot_of_cases_per_area_week(st: StringVar, et: StringVar):

    na, diff = plot_cases_per_area_week(new_data, "date", st.get(), et.get())
    plt.pie(x = diff, labels = na)
    plt.title("Areas with the highest number of reported cases from 2020-03-20 to 2020-03-27")
    plt.xlabel("Area")
    plt.ylabel("Number of reported cases")
    plt.tight_layout()
    plt.show()

my_button5 = Button(root, text="5. Plot of Cases Per Area Week", command=sub_cases_per_area_per_week_window)
my_button5.pack()

def plot_of_areas_comapare_day(st: StringVar, et: StringVar, af: StringVar, a2: StringVar):

    area1 = af.get()
    area2 = a2.get()
    day1 = st.get()
    day2 = et.get()
    dt, a1, a2 = plot_areas_compare_day(new_data, "date", "areaName", area1, area2, day1, day2)
    plt.plot(dt, a1, "--", label = area1)
    plt.plot(dt, a2, label =area2)
    plt.legend()
    plt.title(f"Daily change in reported cases for {area1} and {area2}")
    plt.xlabel("Dates")
    plt.ylabel("Number of Reported cases")
    plt.tight_layout()
    plt.show()

my_button6 = Button(root, text="6. Plot of Areas compared to day", command=sub_cases_compare_daily_window)
my_button6.pack()

def plot_of_areas_comapare_cumm_day(st: StringVar, et: StringVar, af: StringVar, a2: StringVar):

    area1 = af.get()
    area2 = a2.get()
    day1 = st.get()
    day2 = et.get()
    ds, aa1, aa2 = plot_areas_compare_cumm_day(new_data, "date", "areaName", area1, area2, day1, day2)
    plt.plot(ds, aa1, "--", label = area1)
    plt.plot(ds, aa2, label = area2)
    plt.legend()
    plt.title(f"Cummulative number of cases for {area1} and {area2}")
    plt.xlabel("Dates")
    plt.ylabel("Number of Reported cases")
    plt.tight_layout()
    plt.show()

my_button7 = Button(root, text="7. Plot of Areas compared to cummulative day",
                     command=sub_cases_compare_cumm_daily_window)
my_button7.pack()

#----------------------------------- END OF PLOT FUNCTIONS -----------------------------------

Label2 = Label(root, text= "-------------2ND QUESTION(STOP AND SEARCH)---------------")
Label2.pack()

def Plot_of_young_adults():

    cle = []
    north = []

    for m in ["2021-06", "2021-07", "2021-08"]:
        cle.append(young_adults(url=url, params={"force": "cleveland", "date": m}, age_range="18-24"))
        north.append(young_adults(url=url, params={"force": "northumbria", "date": m}, age_range="18-24"))
    X = np.arange(len(cle))
    ticks = ["June", "July", "August"]
    plt.bar(X - 0.2, cle, 0.4, label="cleveland")
    plt.bar(X + 0.2, north, 0.4, label = "Northumberland")
    plt.xticks(X, ticks)
    plt.xlabel("Months")
    plt.ylabel("Number of young adults (18-24) stopped")
    plt.title("Number of young adults (18-24) stopped by Cleveland and Northumberland police forces in summer 2021")
    plt.legend()
    plt.show()

my_button8 = Button(root, text="1. Plot of Young Adults", command=Plot_of_young_adults)
my_button8.pack()

def plot_of_Age_breakdown():

    ag = age_breakdown(url=url, params={"force": "cleveland", "date": "2021-06"})
    ag = {"Unspecified" if k == None else k:v for k,v in ag.items()}

    plt.bar(list(ag.keys()), list(ag.values()))
    plt.title("Number of stop and searches by age group for Cleveland Police Force")
    plt.xlabel("Age Groups")
    plt.ylabel("Number of Stop and Search")
    plt.show()

my_button9 = Button(root, text="2. Plot of Age Breakdown", command=plot_of_Age_breakdown)
my_button9.pack()

def Number_of_Stop_Search_June2020_June2021():
    first = get_data(url=url, params={"force": "cleveland", "date": "2020-06"})
    second = get_data(url=url, params={"force": "cleveland", "date": "2021-06"})

    plt.bar(["June 2020", "June 2021"], [len(first), len(second)])
    plt.title("Number of stop and searches in June of 2020 and in June of 2021")
    plt.xlabel("Months")
    plt.ylabel("Number of Stop and Search")
    plt.show()

my_button10 = Button(root, text="3. Number of stop and searches in June of 2020 and in June of 2021 ",
                    command=Number_of_Stop_Search_June2020_June2021)
my_button10.pack()

def Arrest():
    fi = [r for r in get_data(url=url, params={"force": "cleveland", "date": "2020-06"}) if r["outcome"] == "Arrest"]
    se = [r for r in get_data(url=url, params={"force": "cleveland", "date": "2021-06"}) if r["outcome"] == "Arrest"]

    plt.bar(["June 2020", "June 2021"], [len(fi), len(se)])
    plt.title("Number of stop and searches in June of 2020 and in June of 2021 that resulted in an arrest")
    plt.xlabel("Months")
    plt.ylabel("Number of Stop and Search That Led to Arrest")
    plt.show()

my_button11 = Button(root, text="4.Number of Stop and Search That Led to Arrest ",
                    command=Arrest)
my_button11.pack()

def Plot_of_gender_stops():
    gen = gender_stop(url=url, params={"force": "cleveland", "date": "2021-06"})

    plt.bar(list(gen.keys()), list(gen.values()))
    plt.title("Number of stop and searches by Gender for Cleveland Police Force")
    plt.xlabel("Gender")
    plt.ylabel("Number of Stop and Search")
    plt.show()

my_button11 = Button(root, text="5.Number of stop and searches by Gender for Cleveland Police Force ",
                    command=Plot_of_gender_stops)
my_button11.pack()











root.mainloop()
