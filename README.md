# USMLE-Qgen
##United States Medical Licensing Examination (USMLE) Question generation 
This repository contains code for a USMLE Question generation framework based on self-refinement of LLM(GPT-3+) outputs.

The LLM takes in an actual clinical note as input and generates a context-based question at the level of USMLE, along with a correct answer and distractor options. It follows various intermediate steps, including a feedback loop used for later refinement. An overview of the pipeline is in the following flowchart. We experimented with both human annotated topics & keypoints and LLM generated topics & keypoints, for a given clinical note.


![USMLEQG](https://github.com/adiparashar/USMLE-Qgen/assets/13602896/e57bcec9-9cae-4ae8-8719-156da87f820f)
