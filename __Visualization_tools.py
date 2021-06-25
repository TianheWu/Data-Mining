import folium
import joblib

from __Parameters import *
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
# from pyecharts.charts import Bar
# from pyecharts.charts import Line
# from pyecharts import options as opts
# from pyecharts.charts import Pie


def get_type_icon_color(type):
    color_bar = ['purple', 'darkblue', 'darkgreen', 'orange', 'black']
    return color_bar[type]


def add_point(in_location, label, in_color, companent):
    folium.Marker(
        location=in_location,
        popup=label,
        icon=folium.Icon(color=in_color)
    ).add_to(companent)


def add_circle(in_location, label, in_color, in_radius, companent):
    folium.CircleMarker(
        location=in_location,
        radius=in_radius,
        popup=label,
        color=in_color,
        fill=True,
        fill_color=in_color
    ).add_to(companent)


def add_line(in_locations, in_color, companent):
    folium.PolyLine(
        locations=in_locations,
        color=in_color
    ).add_to(companent)


def color_select(in_color):
    out_color = BASIC_COLOR
    top_hexadecimal_num = ''
    middle_hexadecimal_num = ''
    bottom_decimal_num = int('0x' + in_color[-1], 16)
    bottom_decimal_num += 1
    bottom_hexadecimal_num = hex(bottom_decimal_num)
    middle_flag = False
    top_flag = False
    if bottom_hexadecimal_num[2:] == '10':
        middle_decimal_num = int('0x' + in_color[-2], 16)
        middle_decimal_num += 1
        middle_hexadecimal_num = hex(middle_decimal_num)
        middle_flag = True
        bottom_hexadecimal_num = '0x0'
        if middle_hexadecimal_num[2:] == '10':
            top_decimal_num = int('0x' + in_color[-3], 16)
            top_decimal_num += 1
            top_hexadecimal_num = hex(top_decimal_num)
            top_flag = True
            middle_hexadecimal_num = '0x0'
    if top_flag:
        out_color = in_color[:len(in_color) - 3] + top_hexadecimal_num[2:] + middle_hexadecimal_num[2:] + bottom_hexadecimal_num[2:]
    elif middle_flag:
        out_color = in_color[:len(in_color) - 2] + middle_hexadecimal_num[2:] + bottom_hexadecimal_num[2:]
    else:
        out_color = in_color[:len(in_color) - 1] + bottom_hexadecimal_num[2:]
    return out_color


def visualization_kmeans(x, y, k_means):
    x_major_locator = MultipleLocator(0.1)
    y_major_locator = MultipleLocator(0.1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap='viridis')
    centers = k_means.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=20, alpha=0.5)
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    # plt.savefig('./figure/map_KMeans.png')
    plt.show()


def visualization_acc(pred_test, train_data):
    plt.plot(pred_test, 'r', label='prediction')
    plt.plot(train_data, 'b', label='real')
    plt.legend(loc='best')
    plt.savefig('./figure/acc.png')


def visualization_fit(x, y, pred_y):
    plt.plot(x, y, '*', label='original values')
    plt.plot(x, pred_y, 'r', label='polyfit values')
    plt.legend()
    plt.show()
    # plt.savefig('./figure/fit.png')


# def plot_line_picture(x_info, y_info):
#     line_plot = (
#         Line()
#         .add_xaxis(x_info)
#         .add_yaxis('People num', y_info, is_smooth=True,
#                     linestyle_opts=opts.LineStyleOpts(color='red', width=4),
#                     markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='average')]))
#         .set_global_opts(title_opts=opts.TitleOpts(title='Line of the number in the epidemic', subtitle="2020 year",
#     )))
#     line_plot.render(path='./figure/num_line.html')
#
#
# def plot_pie_charts(data):
#     pie = Pie()
#     pie.add(
#         series_name="Number",
#         data_pair=data,
#         radius=["30%", "70%"],
#     )
#     pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
#     pie.set_global_opts(title_opts=opts.TitleOpts(title="Distribution of people"))
#     pie.render_notebook()
#     pie.render(path='./figure/pie.html')


if __name__ == '__main__':
    patient_type_idx = joblib.load('./patient/patient_type_idx.pkl')
    type_num = {0:0, 1:0, 2:0, 3:0, 4:0}
    x = []
    y = []
    for key, val in patient_type_idx.items():
        x.append(key)
        y.append(len(val))
    in_data = list(zip(x, y))
    plot_pie_charts(in_data)
