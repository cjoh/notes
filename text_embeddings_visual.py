import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create figure with subplots
fig = plt.figure(figsize=(15, 5))

# Subplot 1: Text to Embedding Process
ax1 = fig.add_subplot(131)
ax1.text(0.5, 0.9, 'Text to Embedding Process', ha='center', fontsize=14, weight='bold')
ax1.text(0.1, 0.7, 'Input Text:', fontsize=11)
ax1.text(0.1, 0.6, '"I love programming"', fontsize=10, style='italic')
ax1.arrow(0.5, 0.55, 0, -0.15, head_width=0.05, head_length=0.02, fc='black')
ax1.text(0.5, 0.35, 'Embedding Model\n(BERT, GPT, etc.)', ha='center', fontsize=10, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
ax1.arrow(0.5, 0.25, 0, -0.1, head_width=0.05, head_length=0.02, fc='black')
ax1.text(0.1, 0.1, 'Output Vector:', fontsize=11)
ax1.text(0.1, 0.0, '[0.8, 0.2, 0.5, ..., 0.3]', fontsize=10, family='monospace')
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.1, 1)
ax1.axis('off')

# Subplot 2: 3D Embedding Space
ax2 = fig.add_subplot(132, projection='3d')
ax2.set_title('Embeddings in 3D Space', fontsize=14, weight='bold')

# Define embeddings
embeddings = {
    "I love programming": [0.8, 0.2, 0.5],
    "I enjoy coding": [0.7, 0.3, 0.6],
    "I like software": [0.75, 0.25, 0.55],
    "I hate bugs": [0.3, -0.5, 0.4],
    "Weather is nice": [-0.2, 0.8, -0.3]
}

# Plot points
colors = ['red', 'darkred', 'orange', 'blue', 'green']
for (text, coords), color in zip(embeddings.items(), colors):
    ax2.scatter(coords[0], coords[1], coords[2], c=color, s=100, alpha=0.8)
    ax2.text(coords[0]+0.05, coords[1]+0.05, coords[2]+0.05, 
             text.split()[0] + '...', fontsize=8)

# Draw lines between similar texts
similar_pairs = [
    ("I love programming", "I enjoy coding"),
    ("I enjoy coding", "I like software"),
    ("I love programming", "I like software")
]

for text1, text2 in similar_pairs:
    coords1 = embeddings[text1]
    coords2 = embeddings[text2]
    ax2.plot([coords1[0], coords2[0]], 
             [coords1[1], coords2[1]], 
             [coords1[2], coords2[2]], 'k--', alpha=0.3)

ax2.set_xlabel('Dimension 1')
ax2.set_ylabel('Dimension 2')
ax2.set_zlabel('Dimension 3')

# Subplot 3: Applications
ax3 = fig.add_subplot(133)
ax3.text(0.5, 0.9, 'Applications', ha='center', fontsize=14, weight='bold')

applications = [
    "• Semantic Search",
    "• Document Clustering", 
    "• Text Classification",
    "• Recommendation Systems",
    "• Question Answering",
    "• Language Translation",
    "• Sentiment Analysis",
    "• Duplicate Detection"
]

y_pos = 0.75
for app in applications:
    ax3.text(0.1, y_pos, app, fontsize=11)
    y_pos -= 0.08

ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.axis('off')

plt.tight_layout()
plt.savefig('/Users/cjoh/Library/Mobile Documents/com~apple~CloudDocs/notes/text_embeddings_diagram.png', 
            dpi=150, bbox_inches='tight')
plt.show()