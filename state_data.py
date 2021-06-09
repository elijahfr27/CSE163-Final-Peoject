"""
CSE 163 Final Project

This function merges the condensed csv data into a single
dataframe and creates the appropriate visualizations for
the state data.
"""

# import statements
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def adding_school_year(data):
    """ Takes in dataframe and changes the form of the school
    year to only include the end year as an integer.
    """
    years = data["SchoolYear"].str.slice(0, 4)
    data.loc[:, "SchoolYear"] = years.astype(int) + 1
    return data


def state_graduation_dataframe(grad, enroll, assess, behavior, classes):
    """ Read in the corresponding dataframe and merge them. Return the merged
    dataframe to use for plotting.
    """
    # graduation data
    state_graduation = grad[["SchoolYear", "GraduationRate"]]
    state_graduation["GraduationRate"] *= 100

    # enrollment data
    state_enroll = enroll[["SchoolYear", "All Students", "White"]]
    state_enroll = adding_school_year(state_enroll)
    state_enroll = state_enroll.groupby("SchoolYear").sum()
    state_enroll["Diversity"] = (
        1 - (state_enroll["White"] / state_enroll["All Students"])) * 100
    state_enroll = state_enroll["Diversity"]

    # assessment data
    state_assess = assess[["SchoolYear", "PercentMetTestedOnly"]]
    state_assess = adding_school_year(state_assess)
    state_assess = state_assess.groupby("SchoolYear").mean()
    state_assess["PercentMetTestedOnly"] *= 100

    # behavior data
    state_behavior = behavior[["SchoolYear", "DisciplineRate"]]
    state_behavior = adding_school_year(state_behavior)
    # converting the rates into numeric values
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
    state_classes["PercentTakingAP"] *= 100

    # mergining dataframes
    state_data = state_graduation.merge(state_enroll, how="outer",
                                        on="SchoolYear")
    state_data = state_data.merge(state_assess, how="outer", on="SchoolYear")
    state_data = state_data.merge(state_behavior, how="outer", on="SchoolYear")
    state_data = state_data.merge(state_classes, how="outer", on="SchoolYear")
    return state_data


def plotting_state_graduation_rates(data):
    """ Takes in merged dataframe and produces the different plots
    """
    sns.relplot(x='SchoolYear', y='GraduationRate', data=data, kind="scatter")
    plt.title("Graduation Rates by Year")
    plt.xlabel("Year")
    plt.ylabel("Graduation Rate")
    plt.savefig("visualizations/grad_rates_year.png", bbox_inches="tight")
    plt.clf()


def subplot_setup(axis):
    axis.set_xlabel("")
    axis.set_ylabel("")
    axis.set_ylim(76, 84)


def plotting_state_graduation_vs_other(data):
    # graduation rate vs. different factors
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2)
    sns.scatterplot(x="Ethnicity", y="GraduationRate", data=data, ax=ax1)
    ax1.set_title("Graduation Rate vs. Student Diversity")
    subplot_setup(ax1)
    sns.scatterplot(x="PercentMetTestedOnly", y="GraduationRate",
                    data=data, ax=ax2)
    ax2.set_title("Graduation Rate vs. % Meeting Standard on Tests")
    subplot_setup(ax2)
    sns.scatterplot(x="DisciplineRate", y="GraduationRate", data=data, ax=ax3)
    ax3.set_title("Graduation Rate vs. Discipline Rate")
    subplot_setup(ax3)
    sns.scatterplot(x="PercentTakingAP", y="GraduationRate", data=data, ax=ax4)
    ax4.set_title("Graduation Rate vs. % Students Taking AP Classes")
    subplot_setup(ax4)
    plt.savefig("visualizations/grad_rate_factors.png", bbox_inches="tight")
    plt.clf()


def main():
    state_grad = pd.read_csv("altered data/state_graduation_rate.csv")
    state_enroll = pd.read_csv("altered data/state_enrollment.csv")
    state_assess = pd.read_csv("altered data/state_assessment.csv")
    state_behavior = pd.read_csv("altered data/behavior.csv")
    state_classes = pd.read_csv("altered data/state_classes.csv")
    state_data = state_graduation_dataframe(
        state_grad, state_enroll, state_assess, state_behavior, state_classes)
    print(state_data)
    plotting_state_graduation_rates(state_data)
    plotting_state_graduation_vs_other(state_data)


if __name__ == '__main__':
    main()
