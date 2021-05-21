import folium

from __Parameters import *
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator


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
    plt.savefig('./figure/map_KMeans.png')
    

# if __name__ == '__main__':
#     new_color = '#FF0000'
#     for i in range(870):
#         new_color = color_select(new_color)
#         print(new_color)