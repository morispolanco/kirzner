import os
import openai

TOKEN = os.getenv("TOKEN")


def conect_entrevista_covey(data):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")

    text_example = read_text_example()
    prompt = "Usted es Israel Kirzner. Kizner es un economista estadounidense de origen británico estrechamente identificado con la Escuela Austriaca. Kirzner piensa que el descubrimiento de nuevas oportunidades y el consiguiente aumento de la actividad económica pueden conducir a una distribución más justa de los recursos. Observa que el proceso de competencia capitalista tiende a dar lugar a una distribución más equitativa de los recursos a lo largo del tiempo, ya que aquellos que son capaces de explotar nuevas oportunidades suelen ser recompensados con una mayor riqueza. Esta dinámica puede conducir a un aumento de la desigualdad a corto plazo, pero Kirzner sostiene que en última instancia conduce a una sociedad más justa."+text_example+data

    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=1,
            max_tokens=850,
            top_p=0,
            frequency_penalty=0.8,
            presence_penalty=0.8,
            stop=["###"])

        return dict(response["choices"][0])["text"].replace("\n\n", "") , 200
    except Exception as err:
        return {"Error": err}, 500


def read_text_example():
    f = open('texto.txt', 'r')
    content = f.read()
    print(content)
    return content
