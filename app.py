import os

from datetime import datetime

import pandas as pd

import streamlit as st



st.set_page_config(page_title="Order Nhà Hàng", layout="wide")


# Đường dẫn file dữ liệu dùng chung trên máy chủ

CSV_FILE = "history.csv"


# Thực đơn cố định của nhà hàng Mr. Bình

menu = {

"Đồ ăn": {

"Pizza Hải Sản": 150000,"Pizza cá": 500000,

"Mì Ý Bò Bằm": 95000,"GÀ CHIÊN MẮM TỎI":29000,

"Burger Gà": 35000,

"Bít tết Bò Mỹ": 250000,

"Sườn nướng BBQ": 150000,

"Cánh gà chiên mắm": 75000,

"Lẩu cá diêu hồng": 200000,

"Lẩu Thái hải sản": 300000,
