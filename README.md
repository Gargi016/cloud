# Cloud Evolution Visualizer

A full-stack computer vision application designed to segment, cluster, and track moving entities (such as cloud formations or aerial objects) across discrete time sequences. The project combines a modular Python backend pipeline with a minimal frontend interface for rapid visualization of tracking graphs.

## 🚀 Features

- **Classical Image Segmentation:** Employs Gaussian blurring and adaptive thresholding for robust object isolation under varying illumination conditions.
- **Connected Component Clustering:** Automatically extracts structural metadata including centroids, bounding boxes, and surface areas from isolated masks.
- **Spatio-Temporal Tracking:** Relates objects across consecutive frames using combined heuristic metrics (Euclidean distance proximity, area deformation scale, and Bounding Box Intersection over Union).
- **Data Visualization:** Provides a synchronized slider interface to step through cached image timesteps and examine the structural graph output.

---

## 📂 Project Structure

```text
cloud-main/
├── backend/                  # Python Services & Framework
│   ├── app.py                # Flask API application server
│   ├── processor.py          # Frame orchestration pipeline engine
│   ├── requirements.txt      # Python dependencies
│   ├── cache/                # Local cache storage for frame assets and data
│   └── utils/                # Computer Vision utility modules
│       ├── clustering.py     # Connected components extraction
│       ├── iou.py            # Intersection over Union (IoU) calculator
│       ├── segmentation.py   # Adaptive thresholding and preprocessing
│       └── tracking.py       # Heuristic frame-to-frame matching logic
└── frontend/                 # Client Web Interface
    ├── index.html            # Core dashboard layout
    ├── script.js             # Asset streaming and API interaction
    └── style.css             # Presentation and responsive layout rules
