import numpy as np

def read_embedding_file(file_path):
    embeddings = {}
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split()
            user_id = int(values[0])
            embedding = np.array([float(val) for val in values[1:]])
            embeddings[user_id] = embedding
    return embeddings

def calculate_distance(embedding1, embedding2):
    return np.linalg.norm(embedding1 - embedding2)

def main():
    # Read embeddings from poison.txt
    poison_embeddings = read_embedding_file('poison.txt')

    # Read embeddings from dataset/Kmeans_Beauty_max_8.txt
    dataset_embeddings = read_embedding_file('dataset/Kmeans_Beauty_max_8.txt')

    # Calculate distance sums
    distance_sums = {}
    for poison_user_id, poison_embedding in poison_embeddings.items():
        distance_sum = 0
        for dataset_user_id, dataset_embedding in dataset_embeddings.items():
            if poison_user_id != dataset_user_id:
                distance_sum += calculate_distance(poison_embedding, dataset_embedding)
        distance_sums[poison_user_id] = distance_sum

    # Find the row with the minimum distance sum
    min_distance_user_id = min(distance_sums, key=distance_sums.get)
    min_distance_sum = distance_sums[min_distance_user_id]

    print(f"The row with the minimum distance sum is user ID {min_distance_user_id} with distance sum {min_distance_sum}")

if __name__ == "__main__":
    main()
