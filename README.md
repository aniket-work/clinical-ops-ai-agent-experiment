# ClinicalOps AI Agent

![Title](https://raw.githubusercontent.com/aniket-work/clinical-ops-ai-agent-experiment/main/images/title-diagram.png)

## Overview
The **ClinicalOps AI Agent** is an experimental Proof of Concept (PoC) designed to assist Clinical Operations teams in monitoring ongoing clinical trials. By leveraging a simulated reasoning engine, it interprets natural language queries about patient safety, enrollment progress, and vital signs to generate professional, regulatory-grade visualizations.

> **Disclaimer:** This project is for experimental and educational purposes only. It is not intended for use in actual clinical trials or for medical decision-making.

## Key Features
- **Natural Language Interface**: Ask questions like "Show me the adverse event distribution" in plain English.
- **Automated Data Processing**: Ingests raw clinical CSV exports (simulated).
- **Professional Visualizations**: Generates high-quality Matplotlib/Seaborn charts.
- **Safety Signal Detection**: Highlights adverse events and vital sign trends.

## Architecture

![Architecture](https://raw.githubusercontent.com/aniket-work/clinical-ops-ai-agent-experiment/main/images/architecture.png)

The system consists of three main layers:
1.  **Data Layer**: Handles ingestion of clinical trial datasets (CSV).
2.  **Intelligence Layer**: Parses user queries and maps them to visualization intents.
3.  **Presentation Layer**: Renders charts and provides actionable insights.

## Project Structure
```
clinical_ops_agent/
├── agent.py               # Main agent logic and visualization engine
├── data_generator.py      # Generates synthetic clinical trial data
├── generate_diagrams.py   # Creates project documentation diagrams
├── requirements.txt       # Project dependencies
├── output/                # Directory for generated charts
└── images/                # Directory for documentation assets
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/aniket-work/clinical-ops-ai-agent-experiment.git
    cd clinical_ops_agent
    ```

2.  Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Generate Data**: First, create a dummy dataset.
    ```bash
    python data_generator.py
    ```

2.  **Run the Agent**: Execute the agent script to process queries and generate charts.
    ```bash
    python agent.py
    ```

3.  **Check Output**: View the generated charts in the `output/` directory.

## Sample Output

The agent generates charts such as:
- **Adverse Event Severity**: A count plot of adverse events by severity.
- **Enrollment Trend**: A cumulative line chart of patient enrollment.
- **Vitals Analysis**: A scatter plot of Blood Pressure vs. Age.

## License
MIT
