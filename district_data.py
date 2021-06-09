"""
CSE 163 Final Project

This function merges the condensed csv data into a single
dataframe and creates the appropriate visualizations for
the district data.
"""

# import statements
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def district_graduation_dataframe(grad, enroll, assess, behavior, classes):
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
        ["DistrictName", "PercentTakingAP", "PercentTakingIB",
         "PercentTakingCollegeInTheHighSchool", "PercentTakingCambridge",
         "PercentTakingRunningStart", "PercentTakingCTETechPrep"]]
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
    sns.barplot(x="GraduationRate", y=data.index, data=data, palette="Blues_d")
    plt.title("Average Graduation Rate by District")
    plt.xlabel("Graduation Rate (%)")
    plt.ylabel("")
    plt.savefig("visualizations/district_grad_rates.png", bbox_inches="tight")
    plt.clf()


def subplot_setup(axis):
    axis.set_xlabel("")
    axis.set_ylabel("")


def plotting_district_other_rates(data):
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(30, 10))
    sns.barplot(x="Diversity", y=data.index, data=data,
                palette="Blues_d", ax=ax1)
    ax1.set_title("Average Diversity by District")
    ax1.set_yticklabels(data.index, fontsize=7)
    subplot_setup(ax1)

    sns.barplot(x="PercentMetTestedOnly", y=data.index, data=data,
                palette="Blues_d", ax=ax2)
    ax2.set_title("Average % Meeting Standard for Testing by District")
    ax2.set_yticklabels(data.index, fontsize=7)
    subplot_setup(ax2)

    sns.barplot(x="DisciplineRate", y=data.index, data=data,
                palette="Blues_d", ax=ax3)
    ax3.set_title("Average Discipline Rate by District")
    ax3.set_yticklabels(data.index, fontsize=7)
    subplot_setup(ax3)

    sns.barplot(x="PercentTakingAP", y=data.index, data=data,
                palette="Blues_d", ax=ax4)
    ax4.set_title("Average % of Students Taking AP by District")
    subplot_setup(ax4)
    ax4.set_yticklabels(data.index, fontsize=7)

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
