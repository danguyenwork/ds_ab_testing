import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

tt = pd.read_csv('test_table.csv',parse_dates=['date']).set_index('user_id').sort_index()
ut = pd.read_csv('user_table.csv').set_index('user_id').sort_index()

# test table validation

tt.head()
tt.info()
tt.ads_channel.unique()
tt.source.unique()
tt.device.unique()
tt.browser_language.unique()
tt.browser.unique()
tt.conversion.unique()
tt.test.unique()
tt.date.min(), tt.date.max()

# user table validation

ut.country.unique()
ut.head()
ut.info()
ut.describe()
ut.sex.unique()
ut.age.unique()
ut.country.unique()

# users with no profile
tt_user_id = tt.index.unique()
ut_user_id = ut.index.unique()
no_profile = np.setdiff1d(tt_user_id, ut_user_id)
no_profile
# exclude user_ids with no profile
tt = tt[~tt.index.isin(no_profile)]
df = pd.concat([tt,ut],axis=1)
df.head()

df_by_country = {}
for country in df.country.unique():
    control = df[(df.country == country)&(df.test == 0)]
    treatment = df[(df.country == country)&(df.test == 1)]
    df_by_country[country] = (control, treatment)
for country, groups in df_by_country.iteritems():
    print "Country: " + country
    print "Treatment Size: {}. Treatment Conversion: {}".format(groups[1].shape[0], groups[1]['conversion'].mean())
    print "Control Size: {}. Control Conversion: {}".format(groups[0].shape[0], groups[0]['conversion'].mean())
    print "---"
