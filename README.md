# TEXT-EMOTION-CLASSIFIER

Text Emotion Classifier using Logistic Regression and Streamlit with Docker and GitHub Actions deployed to Azure App Service.

# Requirements

* **Python**: If you don't have Python installed on your computer, you can download it from the official Python website: [python.org/downloads](https://www.python.org/downloads/). Make sure to select the appropriate version for your operating system.

# Running the Application

To run the application, follow these steps:

1. Clone the repository from GitHub by opening your command line or terminal and running the following command:

```bash
git clone https://github.com/itz-Mathankumar/TEXT-EMOTION-CLASSIFIER.git
```

2. Change the current directory to the cloned repository:

```bash
cd TEXT-EMOTION-CLASSIFIER
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Run FastAPI:
   
```bash
uvicorn FastAPI:app --reload
```

5. Run Streamlit:
```bash
streamlit run ./App/app.py
```

6. Run the Text-Emotion-Classifier.ipynb from the Notebooks in a Jupyter Notebook.
   
Please note that these instructions assume you have Git installed on your system. If you don't have Git, you can also manually download the repository from GitHub by visiting the repository URL https://github.com/itz-Mathankumar/TEXT-EMOTION-CLASSIFIER and clicking on the "Code" button, then selecting "Download ZIP". After extracting the ZIP file, navigate to the extracted directory using the command line or terminal and proceed with step 3 to run the application.
