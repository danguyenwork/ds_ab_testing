import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from country import Country

class WorldWide(object):
    def __init__(self, df):
        self.df = df
        self.countries = {}
        for country in self.df.country.unique():
            self.countries[country] = Country(self.df, country)

    def country(self, country):
        return self.countries[country]

    def summary(self):
        pivot =  self.df.groupby(['country','test']).mean().reset_index().pivot(index='country',columns='test',values='conversion').reset_index()
        pivot.rename(columns={1.0: 'Treatment',0.0: 'Control'},inplace=True)
        pivot['delta'] = pivot['Treatment'] - pivot['Control']
        return pivot.set_index('country')
