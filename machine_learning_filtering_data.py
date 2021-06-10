"""
CSE163 Final Project

This file contains the functions for filtering the original datasets in terms
of the state data for the maching learning model.
"""


def state_graduation_rates(data, visualizations=True):
    """ This function takes in the Washington State graduation dataset
    as a datframe and returns a dataframe containing the graduation
    rates for students graduating in 4 years for each included year.
    """
    # reducing to relevant columns
    if visualizations:
        columns = [
            "SchoolYear",
            "DistrictName",
            "StudentGroup",
            "Cohort",
            "GraduationRate",
        ]
    else:
        columns = [
            "SchoolCode",
            "DistrictCode",
            "SchoolYear",
            "Cohort",
            "StudentGroup",
            "GraduationRate",
            "DistrictName",
        ]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] == "State Total"
    student_group = cut_data["StudentGroup"] == "All Students"
    cohort = cut_data["Cohort"] == "Four Year"
    return cut_data[area & student_group & cohort]


def state_enrollment(data, visualization=True):
    """Takes in enrollment data as dataframe. Filters to only
    state data for all high school grades"""
    # reducing to relevant columns
    if visualization:
        columns = [
            "SchoolYear",
            "DistrictName",
            "Gradelevel",
            "All Students",
            "American Indian/ Alaskan Native",
            "Asian",
            "Black/ African American",
            "Hispanic/ Latino of any race(s)",
            "Native Hawaiian/ Other Pacific Islander",
            "Two or More Races",
            "White",
        ]
    else:
        columns = [
            "SchoolYear",
            "DistrictName",
            "Gradelevel",
            "All Students",
            "American Indian/ Alaskan Native",
            "Asian",
            "Black/ African American",
            "Hispanic/ Latino of any race(s)",
            "Native Hawaiian/ Other Pacific Islander",
            "Two or More Races",
            "White",
            "SchoolCode",
        ]
    cut_data = data[columns]
    # masks for data
    if visualization:
        area = cut_data["DistrictName"] == "State Total"
        grade = (
            (cut_data["Gradelevel"] == "9th Grade")
            | (cut_data["Gradelevel"] == "10th Grade")
            | (cut_data["Gradelevel"] == "11th Grade")
            | (cut_data["Gradelevel"] == "12th Grade")
        )
    else:
        area = cut_data["DistrictName"] != "State Total"
        grade = cut_data["Gradelevel"] == "12th Grade"
    return cut_data[area & grade]


def state_assessment(data, visualization=True):
    """Takes in testing data as dataframe and filters to the
    appropriate columns."""
    # reducing to relevant columns
    if visualization:
        columns = [
            "SchoolYear",
            "DistrictName",
            "StudentGroup",
            "GradeLevel",
            "Test Administration (group)",
            "TestSubject",
            "PercentMetTestedOnly",
        ]
    else:
        columns = [
            "DistrictName",
            "DistrictCode",
            "SchoolCode",
            "GradeLevel",
            "StudentGroup",
            "TestSubject",
            "PercentMetStandard",
            "PercentMetTestedOnly",
        ]
    cut_data = data[columns]
    # masks for data
    if visualization:
        area = cut_data["DistrictName"] == "State Total"
        grade = (
            (cut_data["GradeLevel"] == "9th Grade")
            | (cut_data["GradeLevel"] == "10th Grade")
            | (cut_data["GradeLevel"] == "11th Grade")
            | (cut_data["GradeLevel"] == "12th Grade")
        )
        test = cut_data["Test Administration (group)"] == "General"
        area = cut_data["DistrictName"] != "State Total"
        grade = cut_data["GradeLevel"] == "12th Grade"
        student_group = cut_data["StudentGroup"] == "All Students"
        return cut_data[area & student_group & grade & test]
    else:
        area = cut_data["DistrictName"] != "State Total"
        grade = cut_data["GradeLevel"] == "12th Grade"
        return cut_data[area & grade]


def state_classes(data, visualization=True):
    """Takes in data about class enrollment and filters down
    to the appropriate columns."""
    # reducing to relevant columns
    if visualization:
        columns = [
            "SchoolYear",
            "DistrictName",
            "StudentGroup",
            "GradeLevel",
            "Measures",
            "PercentTakingAP",
            "PercentTakingIB",
            "PercentTakingCollegeInTheHighSchool",
            "PercentTakingCambridge",
            "PercentTakingRunningStart",
            "PercentTakingCTETechPrep",
        ]
    else:
        columns = [
            "SchoolYear",
            "SchoolCode",
            "DistrictName",
            "GradeLevel",
            "PercentTakingAP",
            "PercentTakingIB",
            "PercentTakingCollegeInTheHighSchool",
            "PercentTakingRunningStart",
            "StudentGroup",
        ]
    cut_data = data[columns]
    # masks for data
    student_group = cut_data["StudentGroup"] == "All Students"
    if visualization:
        area = cut_data["DistrictName"] == "State Total"
        grade = (
            (cut_data["GradeLevel"] == "9")
            | (cut_data["GradeLevel"] == "10")
            | (cut_data["GradeLevel"] == "11")
            | (cut_data["GradeLevel"] == "12")
        )
        measures = cut_data["Measures"] == "Dual Credit"
        return cut_data[area & student_group & grade & measures]
    else:
        area = cut_data["DistrictName"] != "State Total"
        grade = cut_data["GradeLevel"] == "12"
        student_group = cut_data["StudentGroup"] == "All Students"
        return cut_data[area & student_group & grade]
