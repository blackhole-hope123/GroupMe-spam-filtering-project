# GroupMe Spam Filtering — Machine Learning and Web Application

## 1. Project Overview

This project develops and deploys a machine learning-based spam filtering application for GroupMe messages.

The repository contains components for data preparation, labeling, model training and evaluation, and web application deployment. The trained classification model is integrated into a Flask application and deployed using Docker and Microsoft Azure.

The project also includes a separate Streamlit application for reviewing and refining message labels.

## 2. Project Components

### Flask Web Application (`app/`)

The `app/` directory contains the Flask application and supporting Python modules.

The main entry point is `app.py`, which defines the web application, handles HTTP GET and POST requests, and integrates the trained classification model to process user input.

Supporting modules provide data loading, cleaning, and labeling functionality.

### Machine Learning Pipeline (`app/ML model/`)

This directory contains the resources used for developing and evaluating the spam classification model, including:

- Raw and processed datasets
- Labeled and refined training data
- Model training and evaluation scripts
- Model outputs and experiment logs
- A serialized classification pipeline (`groupme_spam_pipeline.pkl`)

For further information about the machine learning workflow, see the [ML Model README](app/ML%20model/README.md).

### Streamlit Label Refinement Application (`streamlit/`)

This directory contains a separate Streamlit application for reviewing and refining message labels.

The application is implemented in `label_refining_streamlit_app.py` and includes its own Dockerfile and Python dependencies.

## 3. Project Directory Structure

```text
GroupMe-spam-filtering-project/
├── .vscode/                         # VS Code workspace configuration
├── __pycache__/                     # Python-generated cache files
│
├── app/                             # Flask application and ML resources
│   ├── ML model/                    # Model development and evaluation
│   │   ├── bert_output/             # BERT-related outputs
│   │   ├── clean_data/              # Cleaned datasets
│   │   ├── data/                    # Input datasets
│   │   ├── labelled_data/           # Labeled datasets
│   │   ├── logs/                    # Experiment and execution logs
│   │   ├── refined_labels/          # Refined message labels
│   │   ├── README.md                # ML pipeline documentation
│   │   ├── groupme_spam_pipeline.pkl
│   │   └── model_training_and_evaluation...  # Exact filename to be confirmed
│   │
│   ├── .deployment                  # Azure deployment configuration
│   ├── .gitattributes               # Git file handling configuration
│   ├── Dockerfile                   # Flask application container definition
│   ├── app.py                       # Flask application entry point
│   ├── data_labelling.py            # Data labeling utilities
│   ├── data_loading.py              # Data loading and cleaning
│   ├── requirements.txt             # Flask application dependencies
│   ├── runtime.txt                  # Python runtime specification
│   └── test.py                      # Application testing script
│
├── streamlit/                        # Label refinement application
│   ├── Dockerfile                   # Streamlit container definition
│   ├── label_refining_streamlit_app.py
│   └── requirements.txt             # Streamlit application dependencies
│
├── azure-pipelines.yml              # Azure CI/CD pipeline configuration
├── docker-compose.yml               # Multi-container configuration
└── README.md                        # Main project documentation
```

*Note: The model training script name is abbreviated above. Update the directory structure with its exact filename.*

## 4. Application Workflow

The project follows a modular workflow:

**Step 1 — Data Preparation**

Raw GroupMe message data is loaded and cleaned using the data-processing modules.

**Step 2 — Data Labeling and Refinement**

Messages are labeled for classification. A separate Streamlit application supports reviewing and refining labels.

**Step 3 — Model Training and Evaluation**

Machine learning models are trained and evaluated using the prepared datasets. The resulting classification pipeline is saved for use by the application.

**Step 4 — Flask Application Integration**

The trained classification pipeline is integrated into a Flask web application, which handles user requests and returns classification results.

**Step 5 — Containerization and Deployment**

Docker configuration files define the application environments. Azure deployment and pipeline configuration files support cloud deployment and application delivery.

## 5. Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Machine Learning | Scikit-learn, BERT |
| Web Application | Flask |
| Label Refinement Interface | Streamlit |
| Containerization | Docker, Docker Compose |
| Cloud Deployment | Microsoft Azure |
| CI/CD | Azure Pipelines |
| Version Control | Git |

## 6. Testing and Validation

The repository includes `app/test.py` for application testing.

Model training and evaluation resources are maintained separately in `app/ML model/`, allowing model development and application-level testing to be organized independently.

Further details about the testing procedures, expected outputs, and validation criteria should be documented after reviewing the implementation of `test.py`.

## 7. Deployment

The repository contains the following deployment-related configuration files:

- `app/Dockerfile` — container definition for the Flask application
- `streamlit/Dockerfile` — container definition for the Streamlit application
- `docker-compose.yml` — configuration for coordinating containerized services
- `azure-pipelines.yml` — Azure pipeline configuration
- `app/.deployment` — Azure deployment configuration

These files separate application code from deployment configuration and support reproducible deployment workflows.

Specific build commands, environment variables, service ports, and deployment procedures should be documented after verifying the configuration files.

## 8. Additional Documentation

For details about dataset preparation, model training, evaluation, and saved model artifacts, refer to:

[Machine Learning Pipeline Documentation](app/ML%20model/README.md)
