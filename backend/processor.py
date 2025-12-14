import json
import cv2
import os

from utils.segmentation import segment_clouds
from utils.clustering import extract_clusters
from utils.tracking import match_clusters

def run_pipeline():
    images = []
    for i in range(3):
        img = cv2.imread(f"cache/t{i}.png", cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)

    clusters_over_time = []

    for img in images:
        mask = segment_clouds(img)
        clusters = extract_clusters(mask)
        clusters_over_time.append(clusters)

    nodes = []
    edges = []

    for t, clusters in enumerate(clusters_over_time):
        for c in clusters:
            nodes.append({
                "id": f"T{t}_C{c['id']}",
                "time": t
            })

    for t in range(len(clusters_over_time) - 1):
        matches = match_clusters(
            clusters_over_time[t],
            clusters_over_time[t + 1]
        )
        for p_id, c_id, _ in matches:
            edges.append({
                "from": f"T{t}_C{p_id}",
                "to": f"T{t+1}_C{c_id}",
                "type": "continue"
            })

    graph = {"nodes": nodes, "edges": edges}

    os.makedirs("cache", exist_ok=True)
    with open("cache/graph.json", "w") as f:
        json.dump(graph, f, indent=2)

if __name__ == "__main__":
    run_pipeline()
