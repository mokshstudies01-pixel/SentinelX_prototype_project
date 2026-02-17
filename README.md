# SentinelX_prototype_project

This project uses AI to detect cyber threats from network traffic data
and display predictions in a live dashboard.
Pipeline: Dataset -> Preprocessing -> AI Model -> FastAPI Backend -> Dashboard
The current prototype acts as an AI-based Intrusion Detection System (IDS). 

# Model Performance
SentinelX currently uses a supervised machine learning model trained on the CICIDS2017 intrusion‑detection dataset.
The data is split into training, validation, and test sets to evaluate real‑world performance.
Dataset: CICIDS2017
  Training	   80%
  Validation	 0% (not separately used in prototype)
  Test	       20%

<img width="459" height="666" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/e29036a3-3403-483c-a787-3694cd0fc679" />

Python 3.11 recommended
Install dependencies:
pip install pandas numpy scikit-learn matplotlib fastapi uvicorn joblib

Main folder (AI_Cyber_Threat_Detection)
 -backend
 -docs
 -frontend
 -model
 -dataset (contains main data set - CICIDS2017)

* Dataset is a large file which could not be uploaded

## Train the Model Before Running
Run: (in terminal)
python model/train_model.py

This will generate:
- threat_model.pkl
- label_encoder.pkl

# Start backend API 
Run: (in terminal)
uvicorn backend.main:app
[API runs at: http://127.0.0.1:8000]

Test: http://127.0.0.1:8000/predict

# Launch dashboard
Open:
frontend/index.html 
in browser

The dashboard will automatically call the API and show live predictions.

# Overall Metrics (Test Set)

Overall Accuracy ≈ 100.0%
Precision (attack class avg): ~80.8%
Recall (attack class avg): ~75.2%
F1-score (attack class avg): ~77.2%
These metrics show how reliably SentinelX distinguishes between benign and malicious traffic on unseen data.

| Attack Class            | Precision | Recall | F1-Score |
| ----------------------- | --------- | ------ | -------- |
| Bot                     | 93.0%     | 70.0%  | 80.0%    |
| Dos Slowhttptest        | 99.0%     | 99.0%  | 99.0%    |
| Web Attack|Brute force  | 74.0%     | 82.0%  | 78.0%    |
| Web Attack|XSS          | 39.0%     | 25.0%  | 30.0%    |

## Inference & Performance
Even at prototype stage, SentinelX is designed with real‑time detection and high‑throughput environments in mind.
| Metric                                     | Measured Value                |
| ------------------------------------------ | ----------------------------- |
| Average inference latency (single request) |   68.54 ms                    |
| Throughput (batched requests on test log)  |   16,710.37 requests/second   |
| Typical dashboard update interval          |   2 seconds                   |


Folder arrangement -
<img width="800" height="336" alt="Screenshot 2026-02-15 205053" src="https://github.com/user-attachments/assets/b86a8e8e-1b2b-4736-baeb-190114252eaa" />

Model Training -
<img width="873" height="665" alt="Screenshot 2026-02-15 210431" src="https://github.com/user-attachments/assets/42d465ac-edff-4ab7-b259-e495eadfcf96" />
<img width="879" height="661" alt="Screenshot 2026-02-15 210454" src="https://github.com/user-attachments/assets/66b930d8-05ab-4fd6-9324-3d1244464f16" />

Starting API -
<img width="957" height="350" alt="Screenshot 2026-02-15 210714" src="https://github.com/user-attachments/assets/424321a7-94a1-4789-91fe-b79974061be9" />

Opening dashboard (./frontend/index.html)
<img width="1365" height="713" alt="Screenshot 2026-02-15 210833" src="https://github.com/user-attachments/assets/f490e513-bf2f-477c-a537-a538533f1813" />

Now to close API running, press Ctrl + C in the terminal.


The current prototype demonstrates real-time AI-based threat detection running on CPU, achieving low inference latency and high throughput suitable for live monitoring dashboards. The architecture is designed for future AMD GPU acceleration to further reduce latency and improve scalability for enterprise-level traffic volumes.
# Planned future updates To evolve this prototype into a production-level solution, the following enhancements are planned:

1.  Automated Response System
    -   Integrate firewall or network controls to automatically block
        malicious traffic.
    -   Move from detection (IDS) toward prevention (IPS).
2.  Advanced Dashboard
    -   Threat history timeline
    -   Live attack feed with filtering
    -   Visual charts and analytics
    -   GPU performance metrics
3.  Real-Time Streaming Integration
    -   Replace simulated data with real streaming network logs using
        tools such as Kafka or WebSocket pipelines.
4.  Scalability Enhancements
    -   Deployment using containers and cloud infrastructure.
    -   Distributed processing for enterprise-scale environments.
5.  Explainable AI Features
    -   Show why the AI marked traffic as suspicious.
    -   Improve transparency and analyst trust.
6.  Extended AMD Integration
    -   Benchmark CPU vs AMD GPU inference speed.
    -   Optimize model pipelines using ROCm for accelerated performance.

Vision Team SentinelX aims to build an intelligent, scalable
cybersecurity platform that combines AI and high-performance computing
to help organizations detect threats faster and improve digital security
resilience.

## Thank You for reviewing our project !



 
