class dataRet(object):
    """description of class"""
    X = pd.read_csv('owid-covid-data.csv')

XF = X[(X == 'GBR').any(axis = 1)]

xx = pd.to_datetime(XF["date"], format = '%d/%m/%Y')
#xx = xx.dt.strftime('%d/%m/%Y')

yy = ((XF.filter(regex = 'new_cases_smoothed$', axis = 1))/(67))

