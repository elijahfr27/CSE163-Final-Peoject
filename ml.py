import pandas as pd
import sklearn.datasets as skdf
from IPython.display import display
import filtering_data as fd



def merge(grad, classes, enroll, assess):
        #df = grad.merge(classes, how = 'outer')
        #df = df.merge(enroll, how = 'outer')
        #df = df.merge(assess, how = 'outer')
        pd.concat([grad, classes, enroll, assess])
    #df = pd.concat(data, join = 'outer', ignore_index=True, )
    #df = df[df["GraduationRate"].notna()]
        return df


def create_training():
    data = pd.read_csv('altered data\ml_df.csv')
    scrub_mask = (data['GradeLevel'] == 12) & (data['SchoolYear'] < 2018)
    ata = data[scrub_mask]
    columns = ['SchoolYear', 'OrganizationLevel', 'County', 'DistrictName',
            'SchoolName', 'StudentGroup', 'GraduationRate']
    data = data[columns]
    data = data.dropna(subset = ['DistrictName', 'GraduationRate'])
    data.to_csv('altered data/test.csv')
    
    

    
def main(class_data,assess_data, enroll_data, grad_data):
    class_parsed = fd.state_classes(class_data, False)
    assess_parsed = fd.state_assessment(assess_data, False)
    enroll_parsed = fd.state_enrollment(enroll_data, False)
    grad_parsed = fd.state_graduation_rates(grad_data, False)
    df_merged = merge(grad_data, class_data, enroll_data, assess_data)
    df_merged.to_csv('altered data/ml_df.csv')
    create_training()

if __name__ == '__main__':
    #main()
    create_training()