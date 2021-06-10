"""
CSE 163 Final Project

This file containes the functions for mergining the condensed csv
data files into a single dataframe and creates the appropriate
visualizations for the state based data.
"""

# import statements
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

sns.set()


def adding_school_year(data):
    """ This function takes in education data dataframes
    and changes the form of the school year column to only
    include the ending year as an integer.
    """
    years = data["SchoolYear"].str.slice(0, 4)
    data.loc[:, "SchoolYear"] = years.astype(int) + 1
    return data


def state_graduation_dataframe(grad, enroll, assess, behavior, classes):
    """ This function takes graduation rates, school enrollment,
    assessment results, discipline rates, and class enrollment dataframes
    corresponding to state data and returns a single dataframe containing
    all the data merged according to year.
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
        ["SchoolYear", "PercentTakingAP",
         "PercentTakingCollegeInTheHighSchool", "PercentTakingRunningStart"]]
    state_classes = state_classes.groupby("SchoolYear").sum()
    state_classes["PercentTakingAP"] *= 100
    state_classes["PercentTakingCollegeInTheHighSchool"] *= 100
    state_classes["PercentTakingRunningStart"] *= 100

    # mergining dataframes
    state_data = state_graduation.merge(state_enroll, how="outer",
                                        on="SchoolYear")
    state_data = state_data.merge(state_assess, how="outer", on="SchoolYear")
    state_data = state_data.merge(state_behavior, how="outer", on="SchoolYear")
    state_data = state_data.merge(state_classes, how="outer", on="SchoolYear")
    return state_data


def plotting_state_graduation_rates(data):
    """ This function takes in the merged state data dataframe
    and plots the 4 year high school graduation rate over time.
    """
    sns.relplot(x='SchoolYear', y='GraduationRate', data=data, kind="scatter")
    plt.title("Graduation Rates by Year")
    plt.xlabel("Year")
    plt.ylabel("Graduation Rate")
    plt.savefig("visualizations/state_grad_rates.png", bbox_inches="tight")
    plt.clf()


def subplot_setup(axis):
    """ This function takes in an axes or graph positions
    and sets up the axes labels and y axis scale.
    """
    axis.set_xlabel("")
    axis.set_ylabel("")
    axis.set_ylim(76, 84)


def plotting_state_graduation_vs_other(data):
    """ This function takes in the merged state data dataframe
    and plots the 4 year graduation rate against different factors
    calculated for the same year.
    """
    # graduation rate vs. different factors
    fig, [[ax1, ax2, ax3], [ax4, ax5, ax6]] = plt.subplots(
        2, 3, figsize=(20, 10))

    sns.scatterplot(x="Diversity", y="GraduationRate", data=data, ax=ax1)
    ax1.set_title("Graduation Rate vs. Diversity", fontsize=12)
    subplot_setup(ax1)

    sns.scatterplot(x="PercentMetTestedOnly", y="GraduationRate",
                    data=data, ax=ax2)
    ax2.set_title("Graduation Rate vs. Average % of Students Meeting"
                  + " Standard for Testing", fontsize=10)
    subplot_setup(ax2)

    sns.scatterplot(x="DisciplineRate", y="GraduationRate", data=data, ax=ax3)
    ax3.set_title("Graduation Rate vs. Discipline Rate", fontsize=12)
    subplot_setup(ax3)

    sns.scatterplot(x="PercentTakingAP", y="GraduationRate", data=data, ax=ax4)
    ax4.set_title("Graduation Rate vs. % Students Taking AP Classes",
                  fontsize=12)
    subplot_setup(ax4)

    sns.scatterplot(x="PercentTakingCollegeInTheHighSchool",
                    y="GraduationRate", data=data, ax=ax5)
    ax5.set_title("Graduation Rate vs. % Students Taking College"
                  + " in the High School", fontsize=10)
    subplot_setup(ax5)

    sns.scatterplot(x="PercentTakingRunningStart", y="GraduationRate",
                    data=data, ax=ax6)
    ax6.set_title("Graduation Rate vs. % Students in Running Start",
                  fontsize=12)
    subplot_setup(ax6)

    plt.savefig("visualizations/state_grad_vs_other.png", bbox_inches="tight")
    plt.clf()


def main():
    state_grad = pd.read_csv("altered data/state_graduation_rate.csv")
    state_enroll = pd.read_csv("altered data/state_enrollment.csv")
    state_assess = pd.read_csv("altered data/state_assessment.csv")
    state_behavior = pd.read_csv("altered data/behavior.csv")
    state_classes = pd.read_csv("altered data/state_classes.csv")
    state_data = state_graduation_dataframe(
        state_grad, state_enroll, state_assess, state_behavior, state_classes)
    # plotting_state_graduation_rates(state_data)
    plotting_state_graduation_vs_other(state_data)


if __name__ == '__main__':
    main()
