import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from scipy.stats import ttest_ind

class Country(object):
    def __init__(self, df, country):
        self.df = df
        self.country = country
        self.control = df[(df.country == country)&(df.test == 0)]
        self.treatment = df[(df.country == country)&(df.test == 1)]

    def no_treatment(self):
        return self.treatment.shape[0] == 0

    def test(self):
        return ttest_ind(self.control.conversion.values, self.treatment.conversion.values)

    def histogram(self):
        if self.no_treatment(): return None
        fig, ax = plt.subplots()

        control_dates = self.control.groupby('date').sum()['count']
        treatment_dates = self.treatment.groupby('date').sum()['count']

        ind = np.arange(control_dates.shape[0])
        width = 0.35
        ax.bar(ind, control_dates.values, width)
        ax.bar(ind + width, treatment_dates.values, width)
        ax.legend(('Control', 'Treatment'))


        ax.set_ylabel('Users')
        ax.set_title('Traffic Distribution by Control / Treatment')
        ax.set_xticks(ind + width / 2)
        # import ipdb; ipdb.set_trace()
        ax.set_xticklabels(self.control.date.dt.date.unique(),rotation='vertical')
        plt.tight_layout()
        plt.savefig('test_date_' + self.country)
