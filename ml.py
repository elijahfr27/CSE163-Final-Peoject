"""
CSE 163 Final Project

This file contains functions for formatting
state data, and creating a ML model.
"""
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import filtering_data as fd
from sklearn.metrics import mean_squared_error


def merge(grad, classes, enroll, assess):
    """
    This function is passed dataframes, and concatonates
    then returns them as a outer-joined larger dataframe.
    """
    df = pd.concat(
        [grad, classes, enroll, assess],
        axis=1,
        join="outer",
        keys=None,
        levels=None,
        names=None,
        copy=True,
    )
    return df


def create_training():
    """
    This function takes no paramaters, but reads in data
    from four CSV files. It calls the merge method to create
    a complete dataframe and filters it down to the appropriate
    columns. It then uses this data as a training set to build
    a linear regression model. 
    """
    class_parsed = pd.read_csv("sample_data/class.csv")
    assess_parsed = pd.read_csv("sample_data/assess.csv")
    enroll_parsed = pd.read_csv("sample_data/enroll.csv")
    grad_parsed = pd.read_csv("sample_data/grad.csv")
    data = merge(grad_parsed, class_parsed, enroll_parsed, assess_parsed)
    columns = [
        "SchoolCode",
        "SchoolYear",
        "GraduationRate",
        "PercentTakingAP",
        "PercentTakingIB",
        "PercentTakingCollegeInTheHighSchool",
        "PercentTakingRunningStart",
        "American Indian/ Alaskan Native",
        "Asian",
        "Black/ African American",
        "Hispanic/ Latino of any race(s)",
        "Native Hawaiian/ Other Pacific Islander",
        "Two or More Races",
        "White",
        "PercentMetStandard",
        "PercentMetTestedOnly",
    ]
    data = data[columns]
    data = data.drop(data.columns[[4]], 1)
    data = data.dropna()
    data["PercentMetStandard"] = data["PercentMetStandard"].str.replace("%", "")
    data.astype(float, copy=True)
    features = data.loc[
        :, (data.columns != "GraduationRate") & (data.columns != "Unnamed..0")
    ]
    labels = data["GraduationRate"]
    model = DecisionTreeRegressor()
    model.fit(features, labels)
    error = mean_squared_error(model.predict(features, labels))


def main():
    """
    Passed no paramaters. Reads in data from CSV, calls
    filtering_data to scrub the data, and stores the new
    datasets as separate csvs. 
    """
    class_data = pd.read_csv(
        "data/Report_Card_SQSS_from_2014-15_to_Current_Year.csv",
                             low_memory=False
    )
    assess_data = pd.read_csv(
        "data/Report_Card_Assessment_Data_from_2014-15_to_Current_Year.csv",
        low_memory=False,
    )
    enroll_data = pd.read_csv(
        "data/Report_Card_Enrollment_from_2014-15_to_Current_Year.csv",
                              low_memory=False
    )
    grad_data = pd.read_csv(
        "data/Report_Card_Graduation_2014-15_to_Most_Recent_Year.csv",
                            low_memory=False
    )
    class_parsed = fd.state_classes(class_data, False)
    assess_parsed = fd.state_assessment(assess_data, False)
    enroll_parsed = fd.state_enrollment(enroll_data, False)
    grad_parsed = fd.state_graduation_rates(grad_data, False)
    class_parsed.to_csv("sample_data/class.csv")
    assess_parsed.to_csv("sample_data/assess.csv")
    enroll_parsed.to_csv("sample_data/enroll.csv")
    grad_parsed.to_csv("sample_data/grad.csv")
    create_training()


if __name__ == "__main__":
    # main()
    create_training()
