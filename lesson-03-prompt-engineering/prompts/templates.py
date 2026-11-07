def build_research_prompt(topic, level, format):
    return f"""
    Research the topic "{topic}" and provide a detailed explanation suitable for a {level} audience.
    Format the response in {format} format.
    Include:
    1. Introduction
    2. core concept
    3. Technical Architecture 
    4. code examples
    5. Real world applications
    6. limitations
    """
