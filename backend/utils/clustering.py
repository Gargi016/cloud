import cv2

def extract_clusters(mask):
    num, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)
    clusters = []

    for i in range(1, num):
        clusters.append({
            "id": i,
            "area": stats[i, cv2.CC_STAT_AREA],
            "centroid": centroids[i],
            "bbox": (
                stats[i, cv2.CC_STAT_LEFT],
                stats[i, cv2.CC_STAT_TOP],
                stats[i, cv2.CC_STAT_WIDTH],
                stats[i, cv2.CC_STAT_HEIGHT]
            )
        })

    return clusters
