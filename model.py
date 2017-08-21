from country import Country
from worldwide import WorldWide
import pandas as pd
import numpy as np
def process_data(tt_filename, ut_filename, ES_only=True):
    # create tt and ut dataframe
    tt = pd.read_csv(tt_filename,parse_dates=['date']).set_index('user_id').sort_index()

    if ES_only:
        tt = tt[tt.browser_language == 'ES']
    ut = pd.read_csv(ut_filename).set_index('user_id').sort_index()

    # get the list of user_ids in tt that do not exist in ut
    no_profile = np.setdiff1d(tt.index.unique(), ut.index.unique())

    # exclude user_ids with no profile
    df = pd.concat([tt[~tt.index.isin(no_profile)],ut],axis=1)
    df['count'] = 1
    return df

df = process_data('test_table.csv', 'user_table.csv')
ww = WorldWide(df)
# print ww.summary()
print "Country \t t-stat \t p-value"
for country_name in sorted(ww.countries):
    country = ww.country(country_name)
    stat, p = country.test()
    print "{}\t{}\t{}".format(country_name, stat, p)
    # ww.country(country_name).histogram()
