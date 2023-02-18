from collections import Counter
import pytest
from funcs import *
import pandas as pd

data = pd.read_csv("specimenDate_ageDemographic-unstacked.xls - specimenDate_ageDemographic-unstacked.csv")

data = data[['areaType', 'areaCode', 'areaName', 'date', 'newCasesBySpecimenDate-0_4', 'newCasesBySpecimenDate-0_59',
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


def test_plot_cases_per_day():
    expected = [5388, 6688, 8958, 9108, 10548, 10192, 11940, 19820, 19972, 22216, 25588, 25796,
               23456, 24104, 34586, 36996,40226
               ]
    res, _ = plot_cases_per_day(data, col="date", start='2020-03-16', end='2020-04-01')
    assert expected == res

def test_plot_monthly_cases():
    expected = [4924692, 554, 321048, 1147652, 672492, 252384, 190962, 295326, 1264930, 4792684, 131994]

    res, _ = plot_monthly_cases(data, col="date")
    assert expected == res

def test_plot_cases_per_week():
    expected = [11940, 24104, 40226]

    res, _ = plot_cases_per_week(data, "date", "2020-03-16", "2020-04-01")
    assert expected == res

def test_plot_areas_compare_day():
    expected = [2166, 2072, 2418, 4030, 4052, 4526, 5228, 5314]
    expected2 = [852, 702, 874, 1378, 1274, 1518, 1532, 1642]

    _, res1, res2 = plot_areas_compare_day(data, "date", "areaName", "England", "London", "2020-03-20", "2020-03-27")

    assert expected == res1 and expected2 == res2

def test_plot_area_per_day():
    expected = [2166, 2166, 852, 302, 252, 208]

    _, res = plot_cases_per_area_day(data, "date", "2020-03-20")

    assert expected == res

def test_plot_cases_per_area_week():
    expected = [3148, 3148, 790, 502, 412, 346]
    _, res = plot_cases_per_area_week(data, "date", "2020-03-20", "2020-03-27")

    assert expected == res

def test_plot_per_areas_compare_cumm_day():
    expected1 = [2166, 4238, 6656, 10686, 14738, 19264, 24492, 29806]
    expected2 = [852, 1554, 2428, 3806, 5080, 6598, 8130, 9772]

    _, res1, res2 = plot_areas_compare_cumm_day(data, "date", "areaName", "England", "London", "2020-03-20", "2020-03-27")

    assert expected1 == res1 and expected2 == res2



#-------------------------------------- SECOND ASSIGNMENT TESTS ------------------------------------------
def test_data_is_not_none():
    assert get_data(url="https://data.police.uk/api/stops-force", params={"force": "cleveland", "date": "2021-06"}) is not None

def test_young_adults():
    res = young_adults(url=url, params={"force": "cleveland", "date": "2021-06"}, age_range="18-24")

    assert res == 88

def test_gender_stop():
    res = gender_stop(url=url, params={"force": "cleveland", "date": "2021-06"})
    assert res == Counter({'Male': 358, 'Female': 65, 'Unspecified': 49})

def test_age_breakdown():
    res = age_breakdown(url=url, params={"force": "cleveland", "date": "2021-06"})
    res = {"Unspecified" if k == None else k:v for k,v in res.items()}
    assert res == {'18-24': 88, '10-17': 40, 'Unspecified': 52, 'over 34': 176, '25-34': 116}



if __name__ == '__main__':
    pytest.main()