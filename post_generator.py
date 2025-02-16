from  llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    elif length == "Long":
        return "11 to 16 lines"
    
def get_prompt(length, language, tag):
    
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preable.

    1. Topic: {tag}
    2. Length: {length_str}
    3. Language: {language}

    If langage is Hinglish then it means it is a mix of Hindi and English.
    The script for the generate post should always be English.
    '''

    examples = few_shot.get_filtered_posts(length, language, tag)
    if len(examples) > 0:
        prompt += "4. Use the writing style as per the following examples"
        for i, example in enumerate(examples):
            prompt += f"\n\nExample {i+1}:\n{example['text']}"

            if i == 1:
                break

    print(prompt)
    
    return prompt

def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":

    post = generate_post("Short", "English", "LinkedIn")
    print(post)
