import numpy as np
import torch

from conf import GPT3_SMALL

np.random.seed(42)
torch.manual_seed(42)

from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_tokenizer_and_model(model_name_or_path):
    return GPT2Tokenizer.from_pretrained(model_name_or_path),GPT2LMHeadModel.from_pretrained(model_name_or_path)

def generate(
    model,tok,text,
    do_sample=True,max_length=250, repetition_penalty=5.0,
    top_k=5, top_p=0.95, temperature=1,
    num_beams=None,
    no_repeat_ngram_size=3
    ):
    input_ids = tok.encode(text, return_tensors="pt").cpu()
    out = model.generate(
        input_ids.cpu(),
        max_length=max_length,
        attention_mask = None,
        repetition_penalty=repetition_penalty,
        do_sample=do_sample,
        top_k=top_k, top_p=top_p, temperature=temperature,
        num_beams=num_beams,no_repeat_ngram_size=no_repeat_ngram_size
        )
    return list(map(tok.decode, out))

def genarate_text(text:str) -> list:
    tok, model = load_tokenizer_and_model(GPT3_SMALL)

    return generate(model,tok,text,num_beams=10)


