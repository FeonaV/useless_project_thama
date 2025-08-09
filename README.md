<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# [Project Name] 🎯


## Basic Details
### Team Name: [Deep think]


### Team Members
- Team Lead: [Feona] - [CUSAT]
- Member 2: [Thamanna] - [CUSAT]
  

### Project Description
[ A web app that counts how many petals a flower has from a photo- perfect for people who urgently need to know petal counts but can't count themseleves]

### The Problem (that doesn't exist)
[People are wasting precious minutes counting petals manually when they could just… not.]

### The Solution (that nobody asked for)
[An AI-powered (well, sort of) petal counter that takes your flower photo and instantly tells you how many petals it has.
]

## Technical Details
### Technologies/Components Used
For Software:
- [python]
- [Streamlit (for web interface)]
- [OpenCV, NumPy, Pillow]
- [VS Code / PyCharm, Browser]
For Hardware:
- [just your computer and a flower photo
- [Specifications:Works best with 800×800px images, plain background]
- [Tools: Any device with Python installed]

### Implementation
For Software:User uploads an image via Streamlit web app
OpenCV processes the image: grayscale → blur → threshold → distance transform → watershed segmentation.

Segmented petals are colored and counted.

Output image + petal count shown to user.

# Installation
[pip install streamlit opencv-python pillow numpy]

# Run
[streamlit run petal_counter_app.py]

### Project Documentation
For Software:Flow: Upload image → Preprocessing → Segmentation → Petal counting → Display results.

Limitations: Works best on clear, top-down flower images with non-overlapping petals. Background clutter may affect accuracy.

Future Improvements: Train deep learning segmentation model for more complex flowers.





### Project Demo
# Video
https://github.com/FeonaV/useless_project_thama/raw/refs/heads/main/Screen%20Recording%202025-08-09%20163311.mp4


## Team Contributions
- [FEONA ]: [Developed image processing logic, integrated OpenCV with Streamlit UI.]
- [THAMANNA]: [Worked on debugging, testing with different flower images, created project documentation.]
  

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



