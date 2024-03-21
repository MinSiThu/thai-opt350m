# pip install transformers

from transformers import AutoModelForCausalLM,AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("jojo-ai-mst/thai-opt350m-instruct")
tokenizer = AutoTokenizer.from_pretrained("jojo-ai-mst/thai-opt350m-instruct")

def generate_text(prompt, max_length=200, temperature=0.8, top_k=50):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").cuda() # remove .cuda() if only cpu
    output = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True
    )
    for result in output:
      generated_text = tokenizer.decode(result, skip_special_tokens=True)
      print(generated_text)

generate_text("User: อะไรคือวิธีที่ดีที่สุดในการทําความสะอาดพรม Assistant:")