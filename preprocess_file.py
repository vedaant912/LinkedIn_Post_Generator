import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)
            
    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode='w') as outfile:
        json.dump(enriched_posts, outfile, indent=4)
def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    # Create a comma separate list of unique tags: "Job Search, "Job Hunt, "Job hungin"
    # I am giving you a list of tags, unify them; for example.
    unique_tags_list = ', '.join(unique_tags)
    template = ''' I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unifiet and merged to create a shorter list.
        Example 1: "Jobseekers", "Job Hunting" can all be merge into a single tag "Job Search".
        Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation".
        Example 3: "Personal Growth", "Personal Development", "Self Improvement", can be mapped to "Self Improvement".
        Example 4: "Scam Alert", "Job Scam", etc. can be mapped to "Scam".
    2. Each tag should follow title case convention. Example: "Motivation", "Job Search", "Motivation", etc.
    3. Output should be a Json object, No preamble
    4. Ouput should have mapping of original tag and the unified tag.
       For example: {{"Jobseekers": "Job Search", "Job Hunting": "Job Search", "Motivation":"Motivation"}}

    Here is the list of tags:
    {tags}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags": str(unique_tags_list)})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")

    return res

def extract_metadata(post):
    ''''
    Returns line count, language and tags using LLM
    '''

    template = '''
    You are given a LinkeIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language, tags.
    3. tags is an array of tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish means hindi + english)

    Here is the actual post on which you need to perform this task:
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post': post})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")

    return res 


if __name__ == "__main__":

    process_posts("data/raw_posts.json", "data/processed_posts.json")