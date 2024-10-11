from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def find_optimal_k(scaled_data, max_clusters=15):
    """
    Determine the optimal number of clusters using the Elbow Method.
    
    Parameters:
        scaled_data (ndarray): Scaled user-category data.
        max_clusters (int): Maximum number of clusters to evaluate. Default is 15.
        
    Returns:
        optimal_k (int): The optimal number of clusters based on the Elbow Method.
    """
    inertia = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(scaled_data)
        inertia.append(kmeans.inertia_)

    # Plot the Elbow Curve
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, max_clusters + 1), inertia, marker='o')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal k')
    plt.show()
    
    # Choose the elbow point visually; for this example, we assume k=5
    optimal_k = 5  # Replace with actual visual inspection value
    return optimal_k

def perform_clustering(scaled_data, k):
    """
    Apply K-Means clustering to the scaled data.
    
    Parameters:
        scaled_data (ndarray): Scaled user-category data.
        k (int): Optimal number of clusters.
        
    Returns:
        clusters (ndarray): Array containing cluster labels for each user.
        kmeans_model (KMeans): Fitted KMeans model.
    """
    kmeans_model = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans_model.fit_predict(scaled_data)
    
    return clusters, kmeans_model
