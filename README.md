# RNA 3D Geometry Prediction — Cross-Distribution Ensemble (Top 5% Kaggle)

Predicting the 3D geometry of RNA molecules using an ensemble of complementary foundation models.  
**Result:** Top 5% in a Stanford-organized global Kaggle competition (**Rank 88 / 1516**).

---

## Overview
RNA structure is tightly linked to biological function, but experimentally determining 3D geometry can be expensive and slow. This project focuses on **predicting RNA 3D geometry** using pretrained, foundation-style models and a competition-driven workflow (robust validation, careful iteration, and ensembling).

---

## Key Result
- **Placement:** **88 / 1516** (Top 5%)
- **What worked best:** a **two-model ensemble** that combined models trained on **meaningfully different pretraining datasets**, reducing correlated errors and improving stability.

---

## Unique Contribution: Cross-Distribution Ensembling
A core insight in this solution was that **models trained on different data distributions** can provide genuinely complementary signals:

- **RibonanzaNet** — pretrained using large-scale **user-generated gameplay inputs** (crowdsourced structural signals), capturing RNA-specific patterns and “human-informed” structure priors.
- **Open-source AF3-style model** — trained on a **broad mixture of structural biology data**, contributing more general geometric and physical priors.

Because these models learn from **distinct supervision sources**, blending them produced a more robust predictor than either model alone.

---

## Method Summary
### Models
- Transformer-based RNA foundation model (RibonanzaNet)
- Open-source AlphaFold3-style structural model (AF3-like)

### Ensembling
- Combined model predictions (e.g., weighted averaging) using validation performance to tune blend weights.
- Focused on reducing variance/outliers and improving generalization across RNA families.

### Validation Approach
- Used a competition-appropriate split strategy to avoid leakage and measure true generalization.
- Optimized directly for the competition metric.
