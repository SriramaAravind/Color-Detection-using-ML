import cv2
import numpy as np
import pandas as pd
import argparse
from sklearn.neighbors import KNeighborsClassifier

# -------------------------
# ARGUMENT PARSER
# -------------------------
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

# -------------------------
# READ IMAGE
# -------------------------
img = cv2.imread(img_path)

# -------------------------
# LOAD DATASET
# -------------------------
columns = ["color", "color_name", "hex", "R", "G", "B"]
data = pd.read_csv("colors.csv", names=columns, header=None)

# -------------------------
# PREPARE ML DATA
# -------------------------
X = data[["R", "G", "B"]]
y = data["color_name"]

# -------------------------
# TRAIN MODEL (KNN)
# -------------------------
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# -------------------------
# GLOBAL VARIABLES
# -------------------------
clicked = False
r = g = b = xpos = ypos = 0

# -------------------------
# MOUSE FUNCTION
# -------------------------
def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked

    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# -------------------------
# WINDOW
# -------------------------
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

# -------------------------
# MAIN LOOP
# -------------------------
while True:

    cv2.imshow("image", img)

    if clicked:

        # ML Prediction
        predicted_color = model.predict([[r, g, b]])[0]

        # Draw rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        text = f"{predicted_color} R={r} G={g} B={b}"

        # Text color adjustment
        if r + g + b >= 600:
            text_color = (0, 0, 0)
        else:
            text_color = (255, 255, 255)

        cv2.putText(img, text, (50, 50), 2, 0.8, text_color, 2, cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()