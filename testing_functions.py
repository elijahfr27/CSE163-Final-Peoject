"""
CSE 163 Final Project

This file contains functions for testing the functions
within the filtering_data and the data_visualizations files.
"""
import pandas as pd
import filtering_data
import state_data_visualizations as sdv
import district_data_visualizations as ddv
pd.options.mode.chained_assignment = None


def state_data():
    """ This function tests the different filtering_data functions
    regarding the state based data. Tests are done with small datasets
    and an error is raised if an assertion is false.
    """
    test_graduation = pd.read_csv("testing data/state_graduation_test.csv")
    assert (3, 5) == (filtering_data.state_graduation_rates(
        test_graduation)).shape
    test_enrollment = pd.read_csv("testing data/state_enrollment_test.csv")
    assert (5, 5) == (filtering_data.state_enrollment(test_enrollment)).shape
    test_assessment = pd.read_csv("testing data/state_assessment_test.csv")
    assert (1, 7) == (filtering_data.state_assessment(test_assessment)).shape
    test_behavior = pd.read_csv("testing data/behavior_test.csv")
    assert (7, 6) == (filtering_data.behavior(test_behavior)).shape
    test_classes = pd.read_csv("testing data/state_classes_test.csv")
    assert (4, 8) == (filtering_data.state_classes(test_classes)).shape


def district_classes(data):
    """ Copied from the original district_classes function with the
    filtering_data.py. Revision for grade level to take integers
    rather than strings. When the test file was created the dtype for
    GradeLevel changed to integers from string, so the original function
    doesn't work for the test but does for the original data file.
    """
    # reducing to relevant columns
    columns = ["DistrictName", "CurrentSchoolType",
               "StudentGroup", "GradeLevel", "Measures", "PercentTakingAP",
               "PercentTakingCollegeInTheHighSchool",
               "PercentTakingRunningStart"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] != "State Total"
    school_type = cut_data["CurrentSchoolType"] == "P"
    student_group = cut_data["StudentGroup"] == "All Students"
    grade = (cut_data["GradeLevel"] == 9) | \
            (cut_data["GradeLevel"] == 10) | \
            (cut_data["GradeLevel"] == 11) | \
            (cut_data["GradeLevel"] == 12)
    measures = cut_data["Measures"] == "Dual Credit"
    return cut_data[area & school_type & student_group & grade & measures]


def district_data():
    """ This function tests the different filtering_data functions
    regarding the district based data. Tests are done with small
    datasets and an error is raised if an assertion fails.
    """
    test_graduation = pd.read_csv("testing data/district_graduation_test.csv")
    assert (2, 4) == (filtering_data.district_graduation_rates(
        test_graduation)).shape
    test_enrollment = pd.read_csv("testing data/district_enrollment_test.csv")
    assert (6, 5) == (filtering_data.district_enrollment(
        test_enrollment)).shape
    test_assessment = pd.read_csv("testing data/district_assessment_test.csv")
    assert (3, 7) == (filtering_data.district_assessment(
        test_assessment)).shape
    test_behavior = pd.read_csv("testing data/behavior_test.csv")
    assert (7, 6) == (filtering_data.behavior(test_behavior)).shape
    test_classes = pd.read_csv("testing data/district_classes_test.csv")
    assert (4, 8) == (district_classes(test_classes)).shape


def adding_school_year(data):
    """ This function takes in education data dataframes
    and changes the form of the school year column to only
    include the ending year as an integer.
    """
    years = data["SchoolYear"].str.slice(0, 4)
    data.loc[:, "SchoolYear"] = years.astype(int) + 1
    return data


def state_data_merge():
    test_grad = pd.read_csv("testing data/state_graduation_test.csv")
    grad = filtering_data.state_graduation_rates(test_grad)
    test_enroll = pd.read_csv("testing data/state_enrollment_test.csv")
    enroll = filtering_data.state_enrollment(test_enroll)
    test_assess = pd.read_csv("testing data/state_assessment_test.csv")
    assess = filtering_data.state_assessment(test_assess)
    test_behavior = pd.read_csv("testing data/behavior_test.csv")
    behavior = filtering_data.behavior(test_behavior)
    test_classes = pd.read_csv("testing data/state_classes_test.csv")
    classes = filtering_data.state_classes(test_classes)
    test_merge = sdv.state_graduation_dataframe(
        grad, enroll, assess, behavior, classes)
    assert (5, 8) == test_merge.shape


def district_data_merge():
    test_grad = pd.read_csv("testing data/district_graduation_test.csv")
    grad = filtering_data.district_graduation_rates(test_grad)
    test_enroll = pd.read_csv("testing data/district_enrollment_test.csv")
    enroll = filtering_data.district_enrollment(test_enroll)
    test_assess = pd.read_csv("testing data/district_assessment_test.csv")
    assess = filtering_data.district_assessment(test_assess)
    test_behavior = pd.read_csv("testing data/behavior_test.csv")
    behavior = filtering_data.behavior(test_behavior)
    test_classes = pd.read_csv("testing data/district_classes_test.csv")
    classes = district_classes(test_classes)
    test_merge = ddv.district_graduation_dataframe(
        grad, enroll, assess, behavior, classes)
    assert (1, 7) == test_merge.shape


def regression_tester():
    test


def main():
    state_data()
    district_data()
    state_data_merge()
    district_data_merge()


if __name__ == "__main__":
    main()
