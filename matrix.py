import numpy as np
from numpy import array

# 相機影像座標 = 相機內部參數矩陣 * 相機座標

# 相機內部參數矩陣
intrinsic_matrix = array([[536.46723116,       0, 641.16747751],
              [      0, 538.70333239, 356.89628465],
              [      0,      0,       1]])

# 相機座標
camera_coordinate = array([[5, 6, 1]]).T

# 相機影像座標
#image_coordinate = array([[3.32350363e+03, 3.58911628e+03, 1]]).T

#image_coordinate = array([[682, 484, 1]]).T
#image_coordinate = array([[522, 415, 1]]).T
image_coordinate = array([[0, 415, 1]]).T

# 求相機影像座標
#intrinsic_matrix.dot(camera_coordinate)

# 求相機座標
np.linalg.inv(intrinsic_matrix.T.dot(intrinsic_matrix)).dot(intrinsic_matrix.T).dot(image_coordinate)*100
