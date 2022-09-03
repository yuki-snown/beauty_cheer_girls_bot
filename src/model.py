from transformers import T5Tokenizer, AutoModelForCausalLM


class Model():
    def __init__(self) -> None:
        self.tokenizer = T5Tokenizer.from_pretrained(
            "ushikado/yuyuyui-chatbot")
        self.model = AutoModelForCausalLM.from_pretrained(
            "ushikado/yuyuyui-chatbot")

    def dialog(self, chat: str, name: str) -> str:
        query_text = f"<某>{chat}</s><{name}>"
        input_tensor = self.tokenizer.encode(
            query_text, add_special_tokens=False, return_tensors="pt")
        output_list = self.model.generate(
            input_tensor, max_length=100,
            do_sample=True, pad_token_id=self.tokenizer.eos_token_id)
        output_text = self.tokenizer.decode(output_list[0])
        return output_text
