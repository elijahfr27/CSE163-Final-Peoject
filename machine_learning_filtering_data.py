"""
CSE163 Final Project

This function takes in the original datasets, filters them to the appropriate
data and creates a condensed csv for each filtered dataset.
"""
# import statements
import pandas as pd
import state_data_visualizations
import ml
import district_data_visualizatons


def state_graduation_rates(data, visualizations=True):
    """ Takes in graduation data as dataframe. Filters the data to only
    state graduation rates for all students. """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "StudentGroup",
               "Cohort", "GraduationRate"]
    cut_data = data[columns]
    # masks for data
    if visualizations:
        area = cut_data["DistrictName"] == "State Total"
    else:
        area = cut_data["DistrictName"] != "State Total"
    student_group = cut_data["StudentGroup"] == "All Students"
    cohort = cut_data["Cohort"] == "Four Year"
    return cut_data[area & student_group & cohort]


def state_enrollment(data, visualization=True):
    """ Takes in enrollment data as dataframe. Filters to only
    state data for all high school grades """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "Gradelevel", "All Students",
               "American Indian/ Alaskan Native", "Asian",
               "Black/ African American", "Hispanic/ Latino of any race(s)",
               "Native Hawaiian/ Other Pacific Islander",
               "Two or More Races", "White"]
    cut_data = data[columns]
    # masks for data
    if visualization:
        area = cut_data["DistrictName"] == "State Total"
        grade = (cut_data["Gradelevel"] == "9th Grade") | \
            (cut_data["Gradelevel"] == "10th Grade") | \
            (cut_data["Gradelevel"] == "11th Grade") | \
            (cut_data["Gradelevel"] == "12th Grade")
    else:
        area = cut_data["DistrictName"] != "State Total"
        grade = cut_data["Gradelevel"] == "12th Grade"
    return cut_data[area & grade]


def state_assessment(data, visualization=True):
    """ Takes in testing data as dataframe and filters to the
    appropriate columns. """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "StudentGroup",
               "GradeLevel", "Test Administration (group)",
               "TestSubject", "PercentMetTestedOnly"]
    cut_data = data[columns]
    # masks for data
    if visualization:
        area = cut_data["DistrictName"] == "State Total"
        grade = (cut_data["GradeLevel"] == "9th Grade") | \
                (cut_data["GradeLevel"] == "10th Grade") | \
                (cut_data["GradeLevel"] == "11th Grade") | \
                (cut_data["GradeLevel"] == "12th Grade")
    else:
        area = cut_data["DistrictName"] != "State Total"
        grade = cut_data['GradeLevel'] == '12th Grade'
    student_group = cut_data["StudentGroup"] == "All Students"
    test = cut_data["Test Administration (group)"] == "General"
    return cut_data[area & student_group & grade & test]


def state_classes(data, visualization=True):
    """ Takes in data about class enrollment and filters down
    to the appropriate columns. """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "StudentGroup", "GradeLevel",
               "Measures", "PercentTakingAP", "PercentTakingIB",
               "PercentTakingCollegeInTheHighSchool", "PercentTakingCambridge",
               "PercentTakingRunningStart", "PercentTakingCTETechPrep"]
    cut_data = data[columns]
    # masks for data
    if visualization:
        area = cut_data["DistrictName"] == "State Total"
        grade = (cut_data["GradeLevel"] == "9") | \
                (cut_data["GradeLevel"] == "10") | \
                (cut_data["GradeLevel"] == "11") | \
                (cut_data["GradeLevel"] == "12")
    else:
        area = cut_data["DistrictName"] != "State Total"
        grade = cut_data['GradeLevel'] == '12'
    measures = cut_data["Measures"] == "Dual Credit"
    student_group = cut_data["StudentGroup"] == "All Students"
    return cut_data[area & student_group & grade & measures]


def district_graduation_rates(data):
    """ Takes in graduation dataset, filters to only
    graduation rates for all students for each district. """
    # reducing to relevant columns
    columns = ["DistrictName", "StudentGroup", "Cohort", "GraduationRate"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] != "State Total"
    student_group = cut_data["StudentGroup"] == "All Students"
    cohort = cut_data["Cohort"] == "Four Year"
    return cut_data[area & student_group & cohort]


def district_enrollment(data):
    # reducing to relevant columns
    columns = ["DistrictName", "CurrentSchoolType", "Gradelevel",
               "All Students", "American Indian/ Alaskan Native", "Asian",
               "Black/ African American", "Hispanic/ Latino of any race(s)",
               "Native Hawaiian/ Other Pacific Islander",
               "Two or More Races", "White"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] != "State Total"
    school_type = cut_data["CurrentSchoolType"] == "P"
    grade = (cut_data["Gradelevel"] == "9th Grade") | \
            (cut_data["Gradelevel"] == "10th Grade") | \
            (cut_data["Gradelevel"] == "11th Grade") | \
            (cut_data["Gradelevel"] == "12th Grade")
    return cut_data[area & school_type & grade]


def district_assessment(data):
    # reducing to relevant columns
    columns = ["DistrictName", "CurrentSchoolType",
               "StudentGroup", "GradeLevel", "Test Administration (group)",
               "TestSubject", "PercentMetTestedOnly"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] != "State Total"
    school_type = cut_data["CurrentSchoolType"] == "P"
    student_group = cut_data["StudentGroup"] == "All Students"
    grade = (cut_data["GradeLevel"] == "9th Grade") | \
            (cut_data["GradeLevel"] == "10th Grade") | \
            (cut_data["GradeLevel"] == "11th Grade") | \
            (cut_data["GradeLevel"] == "12th Grade")
    test = cut_data["Test Administration (group)"] == "General"
    return cut_data[area & school_type & student_group & grade & test]


def district_classes(data):
    # reducing to relevant columns
    columns = ["DistrictName", "CurrentSchoolType",
               "StudentGroup", "GradeLevel", "Measures", "PercentTakingAP",
               "PercentTakingIB", "PercentTakingCollegeInTheHighSchool",
               "PercentTakingCambridge", "PercentTakingRunningStart",
               "PercentTakingCTETechPrep"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] != "State Total"
    school_type = cut_data["CurrentSchoolType"] == "P"
    student_group = cut_data["StudentGroup"] == "All Students"
    grade = (cut_data["GradeLevel"] == "9") | \
            (cut_data["GradeLevel"] == "10") | \
            (cut_data["GradeLevel"] == "11") | \
            (cut_data["GradeLevel"] == "12")
    measures = cut_data["Measures"] == "Dual Credit"
    return cut_data[area & school_type & student_group & grade & measures]


def behavior(data):
    """ Take in the behavior data and filters to the appropriate columns."""
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "CurrentSchoolType",
               "Student Group", "GradeLevel", "DisciplineRate"]
    cut_data = data[columns]
    # masks for data
    school_type = cut_data["CurrentSchoolType"] == "P"
    student_group = cut_data["Student Group"] == "All Students"
    grade = (cut_data["GradeLevel"] == "9th Grade") | \
            (cut_data["GradeLevel"] == "10th Grade") | \
            (cut_data["GradeLevel"] == "11th Grade") | \
            (cut_data["GradeLevel"] == "12th Grade")
    return cut_data[school_type & student_group & grade]


def main():
    # graduation data
    grad_data = pd.read_csv(
        "data/Report_Card_Graduation_2014-15_to_Most_Recent_Year.csv",
        low_memory=False)
    state_grad = state_graduation_rates(grad_data)
    state_grad.to_csv("altered data/state_graduation_rate.csv",
                      index=False)
    district_grad = district_graduation_rates(grad_data)
    district_grad.to_csv("altered data/district_graduation_rate.csv",
                         index=False)

    # enrollment data
    enroll_data = pd.read_csv(
        "data/Report_Card_Enrollment_from_2014-15_to_Current_Year.csv",
        low_memory=False)
    state_enroll = state_enrollment(enroll_data)
    state_enroll.to_csv("altered data/state_enrollment.csv", index=False)
    district_enroll = district_enrollment(enroll_data)
    district_enroll.to_csv("altered data/district_enrollment.csv", index=False)

    # assessment data
    assess_data = pd.read_csv(
        "data/Report_Card_Assessment_Data_from_2014-15_to_Current_Year.csv",
        low_memory=False)
    state_assess = state_assessment(assess_data)
    state_assess.to_csv("altered data/state_assessment.csv", index=False)
    district_assess = district_assessment(assess_data)
    district_assess.to_csv("altered data/district_assessment.csv", index=False)

    # behavior data
    behavior_data = pd.read_csv(
        "data/Report_Card_Discipline_for_2014-15_to_Current_Year.csv",
        low_memory=False)
    state_discipline = behavior(behavior_data)
    state_discipline.to_csv("altered data/behavior.csv", index=False)

    # classes data
    class_data = pd.read_csv(
        "data/Report_Card_SQSS_from_2014-15_to_Current_Year.csv",
        low_memory=False)
    state_class = state_classes(class_data)
    state_class.to_csv("altered data/state_classes.csv", index=False)
    district_class = district_classes(class_data)
    district_class.to_csv("altered data/district_classes.csv", index=False)

    #district_data.main()
    #state_data.main()
    ml.main(class_data, assess_data, enroll_data, grad_data)

    #Dataframes for ML


if __name__ == '__main__':
    main()
