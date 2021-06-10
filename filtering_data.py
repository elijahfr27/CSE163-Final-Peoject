"""
CSE163 Final Project

This file contains the functions for filtering the original datasets in terms
of the state and district data. The filtered dataset is then saved to a new
csv file to be used for visualizations and machine learning.
"""
import pandas as pd


def state_graduation_rates(data):
    """ This function takes in the Washington State graduation dataset
    as a datframe and returns a dataframe containing the graduation
    rates for students graduating in 4 years for each included year.
    """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "StudentGroup",
               "Cohort", "GraduationRate"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] == "State Total"
    student_group = cut_data["StudentGroup"] == "All Students"
    cohort = cut_data["Cohort"] == "Four Year"
    return cut_data[area & student_group & cohort]


def district_graduation_rates(data):
    """ This functions takes in a Washington state graudation dataset
    as a dataframe and returns a dataframe containing the graduation rates
    per district for students graduating in 4 years for each year included.
    """
    # reducing to relevant columns
    columns = ["DistrictName", "StudentGroup", "Cohort", "GraduationRate"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] != "State Total"
    student_group = cut_data["StudentGroup"] == "All Students"
    cohort = cut_data["Cohort"] == "Four Year"
    return cut_data[area & student_group & cohort]


def state_enrollment(data):
    """ This function takes in a Washington State school enrollment
    dataset as a dataframe and returns a dataframe containing certain
    groups of high school students per year included.
    """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "Gradelevel", "All Students",
               "White"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] == "State Total"
    grade = (cut_data["Gradelevel"] == "9th Grade") | \
            (cut_data["Gradelevel"] == "10th Grade") | \
            (cut_data["Gradelevel"] == "11th Grade") | \
            (cut_data["Gradelevel"] == "12th Grade")
    return cut_data[area & grade]


def district_enrollment(data):
    """ This function takes in a Washington state school enrollment
    dataset as a dataframe and returns a dataframe containing certain
    groups of public high school students per district for each
    year included.
    """
    # reducing to relevant columns
    columns = ["DistrictName", "CurrentSchoolType", "Gradelevel",
               "All Students", "White"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] != "State Total"
    school_type = cut_data["CurrentSchoolType"] == "P"
    grade = (cut_data["Gradelevel"] == "9th Grade") | \
            (cut_data["Gradelevel"] == "10th Grade") | \
            (cut_data["Gradelevel"] == "11th Grade") | \
            (cut_data["Gradelevel"] == "12th Grade")
    return cut_data[area & school_type & grade]


def state_assessment(data):
    """ This function takes in a Washington state standardized testing
    dataset as a dataframe and returns a dataframe containing the specific
    tests and percentage of high school students who passed per year
    included in the data.
    """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "StudentGroup",
               "GradeLevel", "Test Administration (group)",
               "TestSubject", "PercentMetTestedOnly"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] == "State Total"
    student_group = cut_data["StudentGroup"] == "All Students"
    grade = (cut_data["GradeLevel"] == "9th Grade") | \
            (cut_data["GradeLevel"] == "10th Grade") | \
            (cut_data["GradeLevel"] == "11th Grade") | \
            (cut_data["GradeLevel"] == "12th Grade")
    test = cut_data["Test Administration (group)"] == "General"
    return cut_data[area & student_group & grade & test]


def district_assessment(data):
    """ This function takes in a Washington state standardized testing
    dataset as a dataframe and returns a dataframe containing specific tests
    and percentage of public high school students who passed per district per
    year included in the data.
    """
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


def behavior(data):
    """ This function takes in a Washington state disciple dataset
    as a dataframe and returns a dataframe containing the discipline
    rates for all public high school students per district per year
    included in the data.
    """
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


def state_classes(data):
    """ This function takes a Washington state classes dataset
    as a dataframe and returns a dataframe containing the percentage
    of high school students taking AP classes, taking College In The
    High School and enrolled in Running Start for each year.
    """
    # reducing to relevant columns
    columns = ["SchoolYear", "DistrictName", "StudentGroup", "GradeLevel",
               "Measures", "PercentTakingAP",
               "PercentTakingCollegeInTheHighSchool",
               "PercentTakingRunningStart"]
    cut_data = data[columns]
    # masks for data
    area = cut_data["DistrictName"] == "State Total"
    student_group = cut_data["StudentGroup"] == "All Students"
    grade = (cut_data["GradeLevel"] == "9") | \
            (cut_data["GradeLevel"] == "10") | \
            (cut_data["GradeLevel"] == "11") | \
            (cut_data["GradeLevel"] == "12")
    measures = cut_data["Measures"] == "Dual Credit"
    return cut_data[area & student_group & grade & measures]


def district_classes(data):
    """ This function takes in a Washington state class enrollment
    dataset as a dataframe and returns a dataframe containing the
    percentage of public high school students taking AP, College
    in the High School classes or Running Start classes per district
    per year included.
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
    grade = (cut_data["GradeLevel"] == "9") | \
            (cut_data["GradeLevel"] == "10") | \
            (cut_data["GradeLevel"] == "11") | \
            (cut_data["GradeLevel"] == "12")
    measures = cut_data["Measures"] == "Dual Credit"
    return cut_data[area & school_type & student_group & grade & measures]


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
    discipline = behavior(behavior_data)
    discipline.to_csv("altered data/behavior.csv", index=False)

    # classes data
    class_data = pd.read_csv(
        "data/Report_Card_SQSS_from_2014-15_to_Current_Year.csv",
        low_memory=False)
    state_class = state_classes(class_data)
    state_class.to_csv("altered data/state_classes.csv", index=False)
    district_class = district_classes(class_data)
    district_class.to_csv("altered data/district_classes.csv", index=False)


if __name__ == '__main__':
    main()
