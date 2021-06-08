"""
CSE163 Final Project

This function merges the condensed csv data into a single
dataframe and creates the appropriate visualizations for
each set of data.
"""

# import statements
import pandas as pd


def adding_school_year(data):
    """ Takes in dataframe and adds the columns needed """
    years = data["SchoolYear"].str.slice(0, 4)
    years = years.astype(int) + 1
    data.loc[:, "SchoolYear"] = years
    return data


def state_graduation_dataframe(grad, enroll, assess, behavior, classes):
    """ Read in the corresponding dataframe and merge them. Return the merged
    dataframe to use for plotting.
    """
    # enrollment data
    state_enroll = enroll[["SchoolYear", "All Students", "White"]]
    state_enroll = adding_school_year(state_enroll)
    state_enroll = state_enroll.groupby("SchoolYear").sum()
    state_enroll["Ethnicity"] = 1 - \
        (state_enroll["White"] / state_enroll["All Students"])
    state_enroll = state_enroll["Ethnicity"]

    # assessment data
    state_assess = assess[["SchoolYear", "PercentMetTestedOnly"]]
    state_assess = adding_school_year(state_assess)
    state_assess = state_assess.groupby("SchoolYear").mean()

    # behavior data
    state_behavior = behavior[["SchoolYear", "DisciplineRate"]]
    state_behavior = adding_school_year(state_behavior)
    # converting the rates into numeric rates
    state_behavior["DisciplineRate"] = state_behavior[
        "DisciplineRate"].str.strip("< %")
    state_behavior["DisciplineRate"] = state_behavior[
        "DisciplineRate"].apply(pd.to_numeric, errors="coerce")
    state_behavior = state_behavior.dropna()
    state_behavior = state_behavior.groupby("SchoolYear").mean()

    # classes data
    state_classes = classes[
        ["SchoolYear", "PercentTakingAP", "PercentTakingIB",
         "PercentTakingCollegeInTheHighSchool", "PercentTakingCambridge",
         "PercentTakingRunningStart", "PercentTakingCTETechPrep"]]
    state_classes = state_classes.groupby("SchoolYear").sum()

    # mergining dataframes
    state_graduation = grad[["SchoolYear", "GraduationRate"]]
    state_data = state_graduation.merge(state_enroll, how="outer",
                                        on="SchoolYear")
    state_data = state_data.merge(state_assess, how="outer", on="SchoolYear")
    state_data = state_data.merge(state_behavior, how="outer", on="SchoolYear")
    state_data = state_data.merge(state_classes, how="outer", on="SchoolYear")
    return state_data


def main():
    state_grad = pd.read_csv("altered data/state_graduation_rate.csv")
    state_enroll = pd.read_csv("altered data/state_enrollment.csv")
    state_assess = pd.read_csv("altered data/state_assessment.csv")
    state_behavior = pd.read_csv("altered data/behavior.csv")
    state_classes = pd.read_csv("altered data/state_classes.csv")
    state_data = state_graduation_dataframe(
        state_grad, state_enroll, state_assess, state_behavior, state_classes)
    print(state_data)


if __name__ == '__main__':
    main()
