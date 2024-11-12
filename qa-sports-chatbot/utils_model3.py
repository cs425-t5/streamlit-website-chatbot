"""This module contains utility functions for the project"""
import streamlit as st
import torch
import torch.nn as nn
from model_custom import Seq2SeqTransformer

from tokenizers import Tokenizer
from tokenizers import decoders
from pathlib import Path

# Set the path to the tokenizer
base = Path('tokenizer')
tokenizer_path = str(base / 'sportsQA_context.json')

# Load the tokenizer
bert_tokenizer = Tokenizer.from_file('tokenizer/sportsQA_context.json')

# Specify CPU device
device = torch.device('cpu')

# Load the saved model configuration
config = {
    'dim': 768,
    'n_heads': 12,
    'attn_dropout': 0.1,
    'mlp_dropout': 0.1,
    'depth': 6,
    'vocab_size': bert_tokenizer.get_vocab_size(),  # Set to tokenizer vocabulary size
    'max_len': 128,
    'pad_token_id': bert_tokenizer.token_to_id('<pad>')
}

# Initialize model
model = Seq2SeqTransformer(config)

# Load the state dictionary
state_dict = torch.load('best_model_custom_768-12-6.pt', map_location=device)

new_state_dict = {}

model.load_state_dict(state_dict)
model.eval()

def generate_ans(text_input):

    if text_input is not None:
        try:
            # Debug prints
            print(bert_tokenizer.encode(f"<bos>{text_input}<eos>"))
            input_ids = bert_tokenizer.encode(f"<bos>{text_input}<eos>").ids
            input_ids = torch.tensor(input_ids,dtype=torch.long).unsqueeze(0)

            bos = bert_tokenizer.token_to_id('<bos>')
            
            tgt_out = model.generate(input_ids,bos=bos,deterministic=True)

            print(f"Output token IDs: {tgt_out.tolist()}")
            tgt_out = bert_tokenizer.decode(tgt_out.numpy())
    
            print(f"Decoded output: {tgt_out}")
            
            st.write(f"{tgt_out}")
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(f"Error type: {type(e)}")
            import traceback
            print(traceback.format_exc())
            st.write("An error occurred while processing your question.")