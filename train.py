from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding
)
import numpy as np
import evaluate

from data import get_data

# ----------------------
# 1. DATASET
# ----------------------
data = get_data()

texts = [t for t, l in data]
labels = [l for t, l in data]

dataset = Dataset.from_dict({
    "text": texts,
    "label": labels
})

# Splitting dataset into train (80%) and validation (20%)
split_dataset = dataset.train_test_split(test_size=0.2, seed=42)
train_raw = split_dataset["train"]
eval_raw = split_dataset["test"]

# ----------------------
# 2. TOKENIZER
# ----------------------
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True)

train_dataset = train_raw.map(tokenize)
eval_dataset = eval_raw.map(tokenize)

# Format for PyTorch
train_dataset.set_format("torch")
eval_dataset.set_format("torch")

# ----------------------
# 3. DATA COLLATOR
# ----------------------
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# ----------------------
# 4. MODEL
# ----------------------
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=6
)

# ----------------------
# 5. METRICS (Accuracy & F1-score)
# ----------------------
accuracy_metric = evaluate.load("accuracy")
f1_metric = evaluate.load("f1")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    
    acc = accuracy_metric.compute(predictions=preds, references=labels)["accuracy"]
    # We use weighted average F1 score because of class distribution
    f1 = f1_metric.compute(predictions=preds, references=labels, average="weighted")["f1"]
    
    return {
        "accuracy": acc,
        "f1": f1
    }

# ----------------------
# 6. TRAINING ARGS
# ----------------------
args = TrainingArguments(
    output_dir="./model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=30,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    logging_dir="./logs",
    logging_steps=1,
    load_best_model_at_end=True,
    metric_for_best_model="f1"
)

# ----------------------
# 7. TRAINER
# ----------------------
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    compute_metrics=compute_metrics,
    data_collator=data_collator
)

# ----------------------
# 8. TRAIN
# ----------------------
trainer.train()

# ----------------------
# 9. EVALUATE
# ----------------------
eval_results = trainer.evaluate()
print("\nEvaluation Results:")
for key, value in eval_results.items():
    print(f"  {key}: {value}")

# ----------------------
# 10. SAVE MODEL
# ----------------------
trainer.save_model("./model")
tokenizer.save_pretrained("./model")

print("\nTraining completed successfully and model saved!")