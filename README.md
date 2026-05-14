# Color-Detection-using-ML-

ColorDetectML is a Machine Learning based color detection system developed using Python, OpenCV, and the K-Nearest Neighbors (KNN) algorithm. 

The project allows users to detect and predict colors from an image by double-clicking on any region of the image. The system extracts RGB values from the selected pixel and predicts the nearest matching color using a trained machine learning model.

The application provides an interactive image-based interface for real-time color prediction and RGB analysis.

---

# Key Features

- Detect colors from images
- Real-time color prediction
- Machine Learning based color classification
- KNN algorithm implementation
- RGB value extraction
- Interactive mouse click detection
- OpenCV graphical interface
- Displays predicted color name and RGB values
- Simple and lightweight ML project

---

# Technologies Used

- Python
- OpenCV
- NumPy
- Pandas
- Scikit-learn

---

# Machine Learning Algorithm Used

## K-Nearest Neighbors (KNN)

The project uses the KNN classification algorithm.

### Working of KNN

1. RGB values are extracted from the selected image pixel.
2. The KNN model compares RGB values with dataset colors.
3. Nearest neighboring colors are identified.
4. The nearest matching color is predicted and displayed.

# Project Structure

ML project/
│
├── color_ml.py                 # Main ML project file
├── colors.csv                  # Dataset containing RGB values
├── test.jpg                    # Sample input image
├── requirements.txt            # Required Python libraries
└── README.md                   # Project documentation

Installation
Clone the Repository
git clone https://github.com/your-username/ColorDetectML.git
cd ColorDetectML
Install Required Libraries
pip install -r requirements.txt

Or manually install:

pip install opencv-python numpy pandas scikit-learn
Execution Process
Step 1: Open Project Folder

Open terminal or PowerShell inside the project folder.

Example:

E:\ml_project\ML project
Step 2: Execute the Program

Run the following command:

python color_ml.py -i test.jpg

Where:

color_ml.py → Main ML project file
-i → Input image argument
test.jpg → Input image file
Step 3: Program Execution Flow

After execution:

Image is loaded using OpenCV
Dataset (colors.csv) is loaded using Pandas
KNN model is trained using RGB values
Image window opens
User double-clicks on image
RGB values are extracted
KNN predicts nearest color
Predicted color name is displayed
Output Process
Input

The system accepts:

Image file
Mouse double-click on image
Processing
Pixel RGB values are extracted
RGB values are passed to KNN model
KNN compares RGB values with dataset colors
Nearest matching color is predicted
Output

The application displays:

Predicted Color Name
RGB Values
Color Preview Rectangle

Example Output:

Blue R=25 G=80 B=210
Controls
Action	Function
Double Click	Detect Color
ESC Key	Exit Application
Internal Working of the Project
Step 1: Image Loading
img = cv2.imread(img_path)

The image is loaded using OpenCV.

Step 2: Dataset Loading
data = pd.read_csv("colors.csv")

The dataset containing RGB values and color names is loaded.

Step 3: Model Training
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

The KNN model is trained using RGB values.

Step 4: Mouse Event Detection

The system detects mouse double-click events and extracts RGB values from the selected pixel.

Step 5: Prediction
predicted_color = model.predict([[r, g, b]])[0]

The nearest matching color is predicted.

Expected Output

The system displays:

Predicted color name
RGB values
Real-time color preview
Common Errors and Solutions
Error: colors.csv not found
Solution

Ensure:

colors.csv

exists inside the project folder.

Error: Image not loading
Solution

Check:

Correct image name
Correct image extension
Image exists in folder
Error: Module Not Found
Solution

Install required libraries:

pip install opencv-python numpy pandas scikit-learn
Learning Outcomes

This project demonstrates:

Machine Learning classification
KNN algorithm implementation
OpenCV image processing
RGB feature extraction
Real-time prediction
Dataset handling using Pandas
Interactive computer vision applications
Future Improvements
Live webcam color detection
GUI dashboard
Voice-based color announcement
Deep learning based color recognition
Real-time object and color detection
Author

Prepared by: Sriram Aravind

Project: Color Detection using ML project 

Submission: Machine Learning Color Detection Project
