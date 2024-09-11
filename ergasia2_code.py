import pandas as pd
import networkx as nx
from node2vec import Node2Vec
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive

# Attach Google Drive
drive.mount('/content/drive')

# Paths to files within Google Drive
brca_path = '/content/drive/MyDrive/Colab Notebooks/brca.tsv'
leuk_path = '/content/drive/MyDrive/Colab Notebooks/leuk.tsv'

# Question about file selection
file_choice = input("Επιλέξτε το αρχείο που θέλετε να τρέξετε ('brca' ή 'leuk'): ").strip().lower()

if file_choice == 'brca':
    file_path = brca_path
elif file_choice == 'leuk':
    file_path = leuk_path
else:
    raise ValueError("Λάθος επιλογή αρχείου. Παρακαλώ επιλέξτε 'brca' ή 'leuk'.")

def load_graph_from_tsv(file_path):
    G_df = pd.read_csv(file_path, sep='\t')
    G = nx.from_pandas_edgelist(G_df, source=G_df.columns[0], target=G_df.columns[1])
    return G

# Παράδειγμα χρήσης
protein_graph = load_graph_from_tsv(file_path)

# Δημιουργία αντικειμένου Node2Vec
node2vec = Node2Vec(protein_graph, dimensions=64, walk_length=30, num_walks=200, workers=4)

# Εκπαίδευση του μοντέλου
model = node2vec.fit(window=10, min_count=1, batch_words=4)

# Αποθήκευση των ενσωματώσεων
embeddings = {str(node): model.wv[str(node)] for node in protein_graph.nodes()}

# Εκτύπωση μερικών από τα διανύσματα
print("Μερικά από τα διανύσματα που δημιουργούνται από τον node2vec:")
for i, (node, vector) in enumerate(embeddings.items()):
    print(f"Node {node}: {vector}")
    if i == 4:  # Εκτύπωση μόνο των πρώτων 5 διανυσμάτων
        break

# Μετατροπή των ενσωματώσεων σε πίνακα
embedding_values = np.array(list(embeddings.values()))

# Εφαρμογή του t-SNE
tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(embedding_values)

# Δημιουργία οπτικοποίησης
plt.figure(figsize=(10, 10))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], s=5)

# Προσθήκη ετικετών (προαιρετικά)
for i, node in enumerate(protein_graph.nodes()):
    plt.annotate(str(node), (embeddings_2d[i, 0], embeddings_2d[i, 1]), fontsize=8)
    
# Add title
plt.title(f"t-SNE Visualization of Node2Vec Embeddings ({file_choice.upper()} File)", fontsize=14)

plt.show()