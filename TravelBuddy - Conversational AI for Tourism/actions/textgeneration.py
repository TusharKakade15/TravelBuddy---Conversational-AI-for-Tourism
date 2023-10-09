# import tensorflow as tf
import transformers
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def textGenerator(input):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

    sentence = input
        #HERE WE ARE ENCODING THE STRING INTO NUMBERS USING THE TOKENIZER
    # input_ids = tokenizer.encode('what color is your buggate', return_tensors='pt')
    input_ids = tokenizer.encode(sentence, return_tensors='pt')
    train = model.generate(input_ids, 
                        max_length=70,
                        min_length=30, 
                        num_beams=5, 
                        no_repeat_ngram_size=2,
                        top_p=0.92,
                        top_k=50,
                        num_return_sequences=3,
                        early_stopping=True)
        
        # randomRes = random.randint(0, 2)

    # output = tokenizer.decode(train[0], skip_special_tokens=True)
    # print(output)
    # return output
    res = tokenizer.decode(train[0], skip_special_tokens=True)
    l=len(sentence)
    return res[l+1:]
    # return (tokenizer.decode(train[0], skip_special_tokens=True))



# import tensorflow as tf
# from transformers import TFGPT2LMHeadModel, GPT2Tokenizer


# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# # add the EOS token as PAD token to avoid warnings
# model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)


# # encode context the generation is conditioned on
# input_ids = tokenizer.encode('I enjoy walking with my cute dog', return_tensors='tf')

# # generate text until the output length (which includes the context length) reaches 50
# greedy_output = model.generate(input_ids, max_length=50)

# print("Output:\n" + 100 * '-')
# print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))
