# llm-anonymizer
Anti-stylometry tool for anonymous communication. Loosely inspired by [Staab et al. 2024](https://arxiv.org/abs/2402.13846), aiming to use an LLM interface to obfuscate region, age and gender-specific stylistic choices in online communication.  
The approach is to randomize a persona, that is, a combination of age, nationality and gender, and prompt the LLM to rewrite the text in that persona.  
I aim to make the app work either with APIs such as OpenAI, or with local models, such that the tool can be used under different threat models. 

## WORK IN PROGRESS
- [ ] Create first prototype using GPT
- [ ] Integrate local LLM support
- [ ] Evaluate the tool's performance under different stylometry techniques
