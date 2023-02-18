import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple, Dict, Union
from datetime import datetime
import requests
from requests.exceptions import RequestException
import numpy as np
from collections import Counter

def plot_cases_per_day(data, col: str, start: str, end: str) -> Tuple[List[int], List[str]]:
    """plots total number of reported cases daily"""
    res = []
    temp = data[data[col].between(start, end)]
    uniques = temp[col].unique()
    for i in uniques:
        t = temp[temp[col] == i]
        s = t.drop(["areaType", "areaCode", "areaName", "date"], axis=1).sum().sum()
        res.append(s)
    return res, uniques


def plot_cases_per_week(data, col: str, start: str, end: str) -> Tuple[List[int], List[str]]:
    """plots total number of reported cases daily"""
    res = []
    weeks = []
    temp = data[data[col].between(start, end)]
    uniques = temp[col].unique()
    st = 0
    en = 7
    c = 1
    while en <= len(uniques):
        ran = uniques[st:en]
        st = en
        en += 7
        nxt = temp["date"].unique()[st:en]
        for i in ran:
            t = temp[temp[col] == i]
            s = t.drop(["areaType", "areaCode", "areaName", "date"], axis=1).sum().sum()
        res.append(s)
        weeks.append(f"week {c}")
        if len(nxt) < 7:
            for i in nxt:
                t = temp[temp[col] == i]
                s = t.drop(["areaType", "areaCode", "areaName", "date"], axis=1).sum().sum()
            res.append(s)
            weeks.append(f"week {c + 1}")
            break
        else:
            pass
        c += 1
    return res, weeks


def plot_monthly_cases(data: pd.DataFrame, col: str) -> Tuple[List[int], List[str]]:
    """plots the total number of reported cases per month"""
    ms = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    new_date = pd.to_datetime(data[col])
    months = []
    res = []
    month_names = []
    for d in new_date:
        months.append(d.month)
    u_m = sorted(list(set(months)))
    for i in u_m:
        su = 0
        for k, d in data.iterrows():
            if str(i) in d.values[3].split("-")[1]:
                su += d.drop(["areaType", "areaCode", "areaName", "date"]).sum()
            else:
                pass
        res.append(su)
        month_names.append(ms.get(i))
    return res, month_names

def plot_cases_per_area_day(data: pd.DataFrame, col: str, dat: str) -> Tuple[List[str], List[int]]:
    target = data[data[col] == dat].drop(["areaType", "areaCode", "date"], axis=1)
    unique_areas = target["areaName"].unique()
    areas = []
    vals = []
    res = []
    res_n = []
    for a in unique_areas:
        t = target[target["areaName"] == a].drop(["areaName"], axis=1).sum().sum()
        vals.append(t)
        areas.append(a)
    new_vals = sorted(vals, reverse=True)
    for i, k in enumerate(new_vals[:6]):
        res.append(k)
        res_n.append(areas[vals.index(k)])
    return res_n, res
    
def plot_cases_per_area_week(data: pd.DataFrame, col: str, start: str, end: str) -> Tuple[List[str], List[int]]:
    """plots the areas with the highest positive change in cases over a seven day period"""
    if diff := (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days < 7:
        raise ValueError("Difference in dates not up to seven days")

    first = data[data[col] == start].drop(["areaType", "areaCode", "date"], axis=1)
    second = data[data[col] == end].drop(["areaType", "areaCode", "date"], axis=1)
    res = []
    diff = []
    are = []
    new_areas = []
    areas = data["areaName"].unique()
    for area in areas:
        ft = first[first["areaName"] == area].drop(["areaName"], axis=1).sum().sum()
        sd = second[second["areaName"] == area].drop(["areaName"], axis=1).sum().sum()
        are.append(area)
        diff.append(sd - ft)
    
    new_diff = sorted(diff, reverse=True)
    for i, k in enumerate(new_diff[:6]):
        res.append(k)
        new_areas.append(are[diff.index(k)])
    return new_areas, res

def plot_areas_compare_day(data: pd.DataFrame, col1: str, col2: str, area1: str, area2: str, start: str, end: str) -> Tuple[List[str], List[int], List[int]]:
    """plots the daily change in cases for the two areas"""
    if area1 not in data["areaName"].unique() and area2 not in data["areaName"].unique():
        raise ValueError("The areas are not present in the dataset")

    first = data[data[col1].between(start, end)].drop(["areaType", "areaCode"], axis=1)
    second = data[data[col1].between(start, end)].drop(["areaType", "areaCode"], axis=1)

    ff = first[first[col2] == area1]
    ss = second[second[col2] == area2]

    s1 = []
    s2 = []
    day = []

    days = ff[col1].unique()
    for d in days:
        ft = ff[ff[col1] == d].drop(["areaName", "date"] , axis = 1).sum().sum()
        sc = ss[ss[col1] == d].drop(["areaName", "date"], axis = 1).sum().sum()
        s1.append(ft)
        s2.append(sc)
        day.append(d)
    return day, s1, s2

def plot_areas_compare_cumm_day(data: pd.DataFrame, col1: str, col2: str, area1: str, area2: str, start: str, end: str) -> Tuple[List[str], List[int], List[int]]:
    """plots the daily change in cases for the two areas"""
    if area1 not in data["areaName"].unique() and area2 not in data["areaName"].unique():
        raise ValueError("The areas are not present in the dataset")

    first = data[data[col1].between(start, end)].drop(["areaType", "areaCode"], axis=1)
    second = data[data[col1].between(start, end)].drop(["areaType", "areaCode"], axis=1)

    ff = first[first[col2] == area1]
    ss = second[second[col2] == area2]

    s1 = []
    s2 = []
    day = []

    days = ff[col1].unique()
    for d in days:
        ft = ff[ff[col1] == d].drop(["areaName", "date"] , axis = 1).sum().sum()
        sc = ss[ss[col1] == d].drop(["areaName", "date"], axis = 1).sum().sum()
        s1.append(ft)
        s2.append(sc)
        day.append(d)
    
    l = len(s1)
    cu1 = [sum(s1[0:x:1]) for x in range(0, l + 1)][1:]
    cu2 = [sum(s2[0:x:1]) for x in range(0, l + 1)][1:]
    return day, cu1, cu2

#------------------------------------- ASSIGNMENT 2----------------------------------------------------
def get_data(url: str, params: Dict[str, str]) -> Union[List[dict], None]:
    """returns the data for the url and parameters provided"""
    try:
        req = requests.get(url=url, params=params)
        if req.status_code == 200:
            return req.json()
        else:
            return None
    except RequestException:
        print("Invalid request")

def young_adults(url: str, params: Dict[str, str], age_range: str) -> int:
    """gets the number of stop and searches for the age range and force"""
    respone = get_data(url=url, params=params)
    if respone is not None:
        res = 0
        for r in respone:
            if r['age_range'] == age_range:
                res += 1
        return res
    else:
        return 0

def age_breakdown(url: str, params: Dict[str, str]) -> dict:
    response = get_data(url, params)
    res = {}
    if response is not None:
        ages = [r["age_range"] for r in response]
        return Counter(ages)

def gender_stop(url: str, params: Dict[str, str]):
    response = get_data(url, params)
    if response is not None:
        res = [ "Unspecified" if x is None else x for x in [r["gender"] for r in response]]
        return Counter(res)
    else:
        return {}