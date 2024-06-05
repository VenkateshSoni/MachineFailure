# Machine Failure Prediction

This repository contains a Streamlit application for predicting machine failures based on various input parameters. The application uses a trained Random Forest model to make predictions and provides standard operating procedures (SOPs) for each failure type.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Machine Failure Prediction app allows users to input various parameters related to machine operation and predicts the likelihood of different types of machine failures. It also provides appropriate SOPs for handling each predicted failure type.

## Installation

To run this application, you'll need to have Python installed along with several libraries. Follow these steps to set up the environment:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/venkateshsoni/machine-failure-prediction.git
    cd machine-failure-prediction
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download and prepare the model, scaler, label encoder, and SOPs:**
    Make sure the following files are in the root directory of the project:
    - `model.pkl`
    - `scaler.pkl`
    - `label_encoder_y.pkl`
    - `sops.pkl`

## Usage

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```

This will launch the application in your default web browser. You can then input the machine parameters and get predictions along with SOPs.