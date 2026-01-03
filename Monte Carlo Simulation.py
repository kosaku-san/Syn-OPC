import random
import csv

#Open list of all genes
with open('List of Genes Expressed in Brain.csv', newline='') as f:
    reader = csv.reader(f)
    genes = [row[0] for row in reader if row[0]]
    
#Load Cluster 2 genes 
with open('C2genes.csv', newline='') as f:
    reader = csv.reader(f)
    cluster2_genes = {row[0].strip() for row in reader if row and row[0].strip()}

# Generate 100 random sets of 800 genes
num_sets = 10000
set_size = 800
random_sets = []

for _ in range(num_sets):
    random_sets.append(random.sample(genes, set_size))
    
#Count overlap between each random set and Cluster 2
overlap_counts = []
for rset in random_sets:
    overlap = len(set(rset) & cluster2_genes)
    overlap_counts.append(overlap)
    
#Save the overlaps (counts + percent overlap) 
with open('null_distribution.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Random_Set', 'Overlap_Count', 'Overlap_Percent'])
    for i, overlap in enumerate(overlap_counts, start=1):
        percent = overlap / set_size * 100
        writer.writerow([i, overlap, percent])
        
print("Done! Null distribution saved to 'null_distribution.csv'")
print(f"Mean overlap: {sum(overlap_counts)/len(overlap_counts):.2f}")
