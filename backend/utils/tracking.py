from scipy.spatial.distance import euclidean
from utils.iou import iou

def match_clusters(prev, curr, max_dist=80):
    matches = []

    for p in prev:
        for c in curr:
            d = euclidean(p["centroid"], c["centroid"])
            area_ratio = p["area"] / (c["area"] + 1e-6)
            overlap = iou(p["bbox"], c["bbox"])

            if d < max_dist and 0.25 < area_ratio < 4.0 and overlap > 0.01:
                matches.append((p["id"], c["id"], d))

    return matches
