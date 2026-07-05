<p align="center">
  <img src="assets/Gemini_Generated_Image_m8c1b6m8c1b6m8c1.png" alt="cev banner" width="100%">
</p>

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
```

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask, OpenCV (`opencv-python-headless`), SciPy, NumPy
* **Frontend:** Vanilla HTML5, CSS3, JavaScript (ES6)

---

## ⚡ Getting Started

### Prerequisites

Python 3.8 or higher installed on your host system.

### Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Install the necessary processing libraries:

```bash
pip install -r requirements.txt
```

Execute the pipeline processor to generate tracking metrics (ensure target images exist in `backend/cache/t0.png`, `t1.png`, `t2.png` beforehand):

```bash
python processor.py
```

Start the Flask application server:

```bash
python app.py
```

### Frontend Setup

Because the client interface is completely decoupled, you can run it by opening `frontend/index.html` directly in your browser, or serving it with a basic web server:

```bash
cd frontend
python -m http.server 8000
```

Navigate your browser to `http://127.0.0.1:8000`.

## ⚙️ How It Works

**Preprocessing:** Individual greyscale frame assets are processed through a Gaussian filter to reduce high-frequency noise and parsed via adaptive thresholding.

**Feature Extraction:** Spatial clusters are located via connected components, logging structural features (`area`, `centroid`, `bbox`) for each entity.

**Graph Generation:** Entities in frame `T` are mapped to entities in frame `T+1`. A match is confirmed if the physical movement distance falls within acceptable boundaries, their area sizes don't drastically diverge, and their bounding boxes maintain spatial overlap.

**Serialization:** The resulting state relationship maps to a Directed Acyclic Graph (DAG) indicating structural persistence over time.

## 📄 License

MIT — see [LICENSE](LICENSE).
