from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load model and tokenizer once at module level for efficiency
MODEL_NAME = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def ask_gpt(prompt: str, model_name: str = MODEL_NAME) -> str:
    # For T5 models, prepend a task prefix
    task_prompt = "Write a story: " + prompt
    inputs = tokenizer(task_prompt, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
