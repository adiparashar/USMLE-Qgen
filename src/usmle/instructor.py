from InstructorEmbedding import INSTRUCTOR

class InstructorEmbed():
    def _init_():

    def embed(instruction, data):
        model = INSTRUCTOR('hkunlp/instructor-large')
        sentence = "3D ActionSLAM: wearable person tracking in multi-floor environments"
        instruction = "Represent the Science title:"
        question = data['question']
        answer = data['answer']
        options = data['options']
        embeddings = model.encode([[instruction,sentence]])
        print(embeddings)
