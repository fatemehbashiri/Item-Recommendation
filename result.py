from sklearn.metrics import jaccard_score
import numpy as np

def save_results(pivot_table, clusters, kmeans_model, output_dir='./'):
    """
    Save the clustering results and additional analysis to CSV and Excel files.
    
    Parameters:
        pivot_table (DataFrame): Original pivot table with user behavior data.
        clusters (ndarray): Array containing cluster labels for each user.
        kmeans_model (KMeans): Fitted KMeans model with centroids.
        output_dir (str): Directory path to save the output files.
    """
    # Add cluster labels to the pivot table
    pivot_table['Cluster'] = clusters
    
    # Save user and category distribution in clusters
    pivot_table.to_csv(f'{output_dir}user_category_clusters.csv')
    
    # Save centroids for each cluster
    centroids = pd.DataFrame(kmeans_model.cluster_centers_, columns=pivot_table.columns[:-1])
    centroids.to_csv(f'{output_dir}cluster_centroids.csv')

    # Calculate the number of users in each cluster
    cluster_counts = pivot_table['Cluster'].value_counts()
    user_distribution = pd.DataFrame({'Cluster': cluster_counts.index, 'User_Count': cluster_counts.values})
    user_distribution.to_csv(f'{output_dir}user_cluster_distribution.csv')
    
    # Calculate and save Jaccard similarity between features
    feature_columns = pivot_table.columns[:-1]  # Exclude 'Cluster' column
    jaccard_matrix = np.zeros((len(feature_columns), len(feature_columns)))
    
    for i, feature1 in enumerate(feature_columns):
        for j, feature2 in enumerate(feature_columns):
            if i == j:
                jaccard_matrix[i, j] = 1.0  # Similarity with itself is 1
            else:
                jaccard_matrix[i, j] = jaccard_score(pivot_table[feature1] > 0, pivot_table[feature2] > 0)
    
    jaccard_df = pd.DataFrame(jaccard_matrix, index=feature_columns, columns=feature_columns)
    jaccard_df.to_csv(f'{output_dir}jaccard_similarity.csv')
    
    print("Results saved successfully!")
