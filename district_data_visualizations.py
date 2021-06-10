"""
CSE 163 Final Project

This file containes the functions for mergining the condensed csv
data files into a single dataframe and creates the appropriate
visualizations for the district based data.
"""

# import statements
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

sns.set()


def district_graduation_dataframe(grad, enroll, assess, behavior, classes):
    """ This function takes graduation rates, school enrollment,
    assessment results, discipline rates, and class enrollment dataframes
    corresponding to state data and returns a single dataframe containing
    all the data averaged and merged according to school district. The
    returned dataframe only includes the top 15 districts according to
    the graduation rate.
    """
    # graduation data
    district_grad = grad.dropna()
    district_grad = grad[["DistrictName", "GraduationRate"]]
    district_grad = (district_grad.groupby("DistrictName").mean()) * 100

    # enrollment data
    district_enroll = enroll[["DistrictName", "All Students", "White"]]
    district_enroll = district_enroll.groupby("DistrictName").sum()
    district_enroll["Diversity"] = (
        1 - district_enroll["White"] / district_enroll["All Students"]) * 100
    district_enroll = district_enroll["Diversity"]

    # assessment data
    district_assess = assess.dropna()
    district_assess = district_assess[["DistrictName", "PercentMetTestedOnly"]]
    district_assess = (district_assess.groupby("DistrictName").mean()) * 100

    # behavior data
    district_discipline = behavior[["DistrictName", "DisciplineRate"]]
    district_discipline["DisciplineRate"] = district_discipline[
        "DisciplineRate"].str.strip("< %")
    district_discipline["DisciplineRate"] = district_discipline[
        "DisciplineRate"].apply(pd.to_numeric, errors="coerce")
    district_discipline = district_discipline.dropna()
    district_discipline = district_discipline.groupby("DistrictName").mean()

    # classes data
    district_classes = classes.dropna()
    district_classes = district_classes[
        ["DistrictName", "PercentTakingAP",
         "PercentTakingCollegeInTheHighSchool",
         "PercentTakingRunningStart"]]
    district_classes = (district_classes.groupby("DistrictName").mean()) * 100

    # merging data
    district_data = district_grad.merge(district_enroll, how="left",
                                        on="DistrictName")
    district_data = district_data.merge(district_assess, how="left",
                                        on="DistrictName")
    district_data = district_data.merge(district_discipline, how="left",
                                        on="DistrictName")
    district_data = district_data.merge(district_classes, how="left",
                                        on="DistrictName")
    district_data = district_data.nlargest(15, "GraduationRate")
    return district_data


def plotting_district_graduation_rates(data):
    """ This function takes the merged district dataframe and plots
    the top 15 4 year graduation rates by school district.
    """
    sns.barplot(x="GraduationRate", y=data.index, data=data, palette="Blues_d")
    plt.title("Average Graduation Rate by District")
    plt.xlabel("Graduation Rate (%)")
    plt.ylabel("")
    plt.savefig("visualizations/district_grad_rates.png", bbox_inches="tight")
    plt.clf()


def subplot_setup(axis):
    """ This function takes in an axes or graph positions
    and sets up the axes labels.
    """
    axis.set_xlabel("")
    axis.set_ylabel("")
    axis.set_xlim(0, 100)


def plotting_district_other_rates(data):
    """ This function takes in the merged state data dataframe
    and plots different factors for the school districts with
    4 year graduation rate in the top 15.
    """
    fig, [[ax1, ax2, ax3], [ax4, ax5, ax6]] = plt.subplots(
        2, 3, figsize=(20, 10))

    sns.barplot(x="Diversity", y=data.index, data=data,
                palette="Blues_d", ax=ax1)
    ax1.set_title("Average Diversity by District")
    ax1.set_yticklabels(data.index, fontsize=10)
    subplot_setup(ax1)

    sns.barplot(x="PercentMetTestedOnly", y=data.index, data=data,
                palette="Blues_d", ax=ax2)
    ax2.set_title("Average % Meeting Standard for Testing by District")
    ax2.set_yticklabels("")
    subplot_setup(ax2)

    sns.barplot(x="DisciplineRate", y=data.index, data=data,
                palette="Blues_d", ax=ax3)
    ax3.set_title("Average Discipline Rate by District")
    ax3.set_yticklabels("")
    subplot_setup(ax3)

    sns.barplot(x="PercentTakingAP", y=data.index, data=data,
                palette="Blues_d", ax=ax4)
    ax4.set_title("Average % of Students Taking AP by District")
    subplot_setup(ax4)
    ax4.set_yticklabels(data.index, fontsize=10)

    sns.barplot(x="PercentTakingCollegeInTheHighSchool", y=data.index,
                data=data, palette="Blues_d", ax=ax5)
    ax5.set_title("Average % of Students Taking College In The High"
                  + " School by District", fontsize=10)
    subplot_setup(ax5)
    ax5.set_yticklabels("")

    sns.barplot(x="PercentTakingRunningStart", y=data.index, data=data,
                palette="Blues_d", ax=ax6)
    ax6.set_title("Average % of Students in Running Start by District")
    subplot_setup(ax6)
    ax6.set_yticklabels("")

    fig.tight_layout(pad=1.0)
    plt.savefig("visualizations/district_other_factors.png",
                bbox_inches="tight")


def main():
    district_grad = pd.read_csv("altered data/district_graduation_rate.csv",
                                na_values=["---"])
    district_enroll = pd.read_csv("altered data/district_enrollment.csv")
    district_assess = pd.read_csv("altered data/district_assessment.csv",
                                  na_values=["---"])
    district_behavior = pd.read_csv("altered data/behavior.csv")
    district_classes = pd.read_csv("altered data/district_classes.csv",
                                   na_values=["---"])
    district_data = district_graduation_dataframe(
        district_grad, district_enroll, district_assess,
        district_behavior, district_classes)
    plotting_district_graduation_rates(district_data)
    plotting_district_other_rates(district_data)


if __name__ == "__main__":
    main()
