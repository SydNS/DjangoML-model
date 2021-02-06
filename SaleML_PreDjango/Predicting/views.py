from django.shortcuts import render

from ml_code.ml_process import server_predictor
from predict.forms import ProductForm


def operate_function(product_detail):
    back_camera = product_detail.back_camera
    front_camera = product_detail.front_camera
    resolution_1 = product_detail.resolution_1
    resolution_2 = product_detail.resolution_2
    screen_size = product_detail.screen_size
    battery = product_detail.battery
    price = product_detail.price
    pre_release_demand = product_detail.pre_release_demand
    # sales = product_detail.sales
    # quarter = product_detail.quarter
    cluster_assigned, predicted_sales = server_predictor.get_prediction(back_camera, front_camera, resolution_1,
                                                                        resolution_2, screen_size,
                                                                        battery, price, pre_release_demand
                                                                        )
    return cluster_assigned[0], int(predicted_sales[0])