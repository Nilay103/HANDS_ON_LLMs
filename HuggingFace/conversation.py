from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "Qwen/Qwen2.5-0.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map='auto')
tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer)
chat_history = [
    {"role": "system", "content": "You are a smart chatbot"},
    {"role": "user", "content": "What is the capital of France?"}
]

outputs = pipe(
    chat_history,
    max_new_tokens=512
)

print(outputs[0]["generated_text"][-1]['content'])

outputs