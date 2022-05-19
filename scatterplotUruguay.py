# Install required libraries by running the command below in the
# terminal (without the #).

# pip3 install seaborn

# Import required libraries.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set figure's overall theme
sns.set_theme(style="white")

# Load the dataset into a pandas DataFrame. The dataset used here is a
# modified output file from the program 'smartpca' of the EIGENSTRAT
# package. Specifically, this file contains the eigenvectors computed
# by 'smartpca' during Principal Component Analysis (PCA). Each row
# represents one sample in the dataset followed by their respective
# eigenvectors in the first 7 principal components computed by
# 'smartpca'.
df = pd.read_csv('Uruguay.pca.evec.csv')

# First, plot only Uruguayan samples.
sns.scatterplot(
    data=df[df['Region'] == 'Uruguay'],
    x="PC1", y="PC2", s=400, c=['yellow'],
    marker='*', edgecolor='k')

# Then plot all the other samples (non-Uruguayan) in the dataset.
sns.scatterplot(data=df[df['Region'] != 'Uruguay'], x="PC1", y="PC2",
                size='Type', sizes=(120, 80), hue='Region', style='Type',
                markers=['^', 'D'], edgecolor='k', palette='tab20')

# Plot legend.
lgd = plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left",
                 frameon=False).set_title('Legend',
                                          prop={'size': 14, 'weight': 'bold'})

# Save plot as a PDF file.
plt.savefig('PCAuruguay.pdf', dpi=600, bbox_inches='tight')

# The output/image was further modified using an image editor (mainly
# for proper overall labeling and better legend positioning).
