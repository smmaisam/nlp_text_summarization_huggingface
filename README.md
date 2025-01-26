# nlp_text_summarization_huggingface


## **Overview**

In this project, we build a **summarization system** using the **PEGASUS** model, fine-tuned to summarize conversations from the **Samsum dataset**. The fine-tuned model can generate concise, human-like summaries of dialogue exchanges, making it suitable for a variety of applications in automated conversation summarization.

**Key Steps**

1. **Data Preparation:**
   - We started by loading and pre-processing the **Samsum dataset**, which contains dialogues and their corresponding summaries.
   - The dataset was tokenized using the **PEGASUS tokenizer**, converting dialogues and summaries into a suitable format for training.

2. **Model Selection and Fine-Tuning:**
   - We used the pre-trained **PEGASUS model**, a transformer-based model optimized for text generation tasks like summarization.
   - The model was fine-tuned on the **Samsum dataset** to adapt it to the specific task of conversation summarization.

3. **Model Training:**
   - The training process was carried out using the **Hugging Face Trainer API**, with custom configurations for batch size, learning rate, and number of epochs.
   - We prepared the dataset and defined the **data collator** to process the dialogues and summaries correctly during training.

4. **Model Evaluation:**
   - The fine-tuned model was evaluated on a test set, with performance measured using **ROUGE** scores (ROUGE-1, ROUGE-2, ROUGE-L, and ROUGE-Lsum).
   - The evaluation function generates summaries for test dialogues and compares them to reference summaries to compute the ROUGE metrics.

5. **Inference and Prediction:**
   - For inference, the model was used to generate summaries for unseen dialogues. A sample dialogue from the test set was processed, and the generated summary was compared to the reference summary.

## **Workflows**

Follow the steps below to update and manage the system:

1. Update config.yaml: Modify the configuration parameters as needed.
2. Update params.yaml: Adjust the parameters for model training or other tasks.
3. Update Entity: Modify entities in the system as required.
4. Update Configuration Manager: Edit the configuration manager in src/config to handle new configurations.
4. Update the Components: Modify or add new components as necessary in the codebase.
5. Update the Pipeline: Update the data processing and training pipeline to reflect changes.
5. Update main.py: Adjust the entry-point script for any necessary changes.
6. Update app.py: Modify the web app script (if applicable) to incorporate new updates.
