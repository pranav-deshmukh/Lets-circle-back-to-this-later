import os
from groq import Groq

def makeRequest(systemMsg, userMsg, models):
    client = Groq(
        api_key=os.environ.get("GROQ_KEY"),
    )
    chat_completion = None
    for model in models:
            try:
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "system", "content": systemMsg}, {"role": "user", "content": userMsg}],
                    model=model,
                    response_format = {"type": "json_object"}
                )
            except:
                 continue
            break
        
    final = None
    try: 
        final = chat_completion.choices[0].message.content
    except:
         pass
    return final


if __name__ == "__main__":
    systemMsg = "based on the given name and details of the electronic product classify it into one of the following categories: 'smartphone', 'laptop', 'tablet', 'smartwatche', 'television', 'gaming console', 'digital camera', 'bluetooth speaker', 'e-reader', 'smart home device', 'refrigerator', 'washing machine', 'dishwasher', 'microwave oven', 'air conditioner'\nreturn it form of a JSON like this: {'category': 'smartphones'}\nthe reply should be stricly json object and nothing else:\n"
    userMsg = str({"product-name": "Samsung Galaxy S21", "about": "The Samsung Galaxy S21 is a 5G smartphone that was released in January 2021. It features a 6.2-inch Dynamic AMOLED 2X display with a resolution of 1080 x 2400 pixels. The phone is powered by the Exynos 2100 chipset with 8GB of RAM and 128GB of internal storage. It has a triple camera setup on the back with a 12MP wide, 12MP ultrawide, and 64MP telephoto lens. The phone is powered by a 4000mAh battery and runs Android 11."})
    models = ["pinku-da-model", "gemma2-9b-it"]
    print(makeRequest(systemMsg, userMsg, models))


    """
    ChatCompletion(id='chatcmpl-3ee5ae11-e35a-4708-b890-2d7cecce3b2e', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='{\n  "category": "smartphones"\n}', role='assistant', function_call=None, tool_calls=None))], created=1727454182, model='gemma2-9b-it', object='chat.completion', system_fingerprint='fp_10c08bf97d', usage=CompletionUsage(completion_tokens=12, prompt_tokens=310, total_tokens=322, completion_time=0.021818182, prompt_time=0.017006441, queue_time=0.025395155, total_time=0.038824623), x_groq={'id': 'req_01j8t4nz0xfqs87jzzqb63g60k'})
    """