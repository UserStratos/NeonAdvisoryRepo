import warnings;
warnings.simplefilter("ignore")
from TimeSeriesModel.load_data_AMD.constants import file_name
from TimeSeriesModel.load_data_AMD.functions import opencsv, data_info, data_shape, data_description, data_columns, data_dtypes, \
    data_missing_values, duplicated_data, data_head, data_size, data_empty, data_duplicated, sort_data_by_column,\
    replace_dollar_sign, change_data_type, plot_allgraphs_in_one, plot_Close_Last, plot_Volume,\
    plot_histogramgraph, plot_scatter_plot, plot_multi_graphs, ACF_PACF, Dickey_Fuller

opencsv(file_name)
replace_dollar_sign()
change_data_type()
#data_info()
#data_shape()
#data_description()
#data_columns()
#data_dtypes()
#sort_data_by_column()
#duplicated_data()
#data_head()
#data_size()
#data_empty()
#data_duplicated()
#plot_allgraphs_in_one()
#plot_Volume()
#plot_Close_Last()
#plot_histogramgraph()
#plot_scatter_plot()
#plot_multi_graphs()
#ACF_PACF()
Dickey_Fuller()




