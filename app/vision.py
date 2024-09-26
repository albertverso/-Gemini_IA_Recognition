import google.generativeai as genai
from config.config import Config
from PIL import Image
import re

# Configurando a chave da API
genai.configure(api_key=Config.API_KEY)

def generate_text_from_image(image_path: str):
    # Abrindo a imagem usando PIL
    image = Image.open(image_path)
    
    # Criando o modelo
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Gerando conteúdo a partir da imagem
    response = model.generate_content(["Conte-me qual a placa desse veiculo", image])

    placa = extrair_placa(response.text)
    
    return placa

def extrair_placa(texto):
    # Definindo um padrão de regex para capturar a placa
    # Exemplo: 'HYT-5553', 'POL 3866', 'POL-3866', etc.
    padrao = r'\b[A-Z]{3}[-\s]?\d{4}\b|\b[A-Z]{3}\s\d{4}\b'

    # Usando re.search para encontrar a primeira ocorrência da placa
    resultado = re.search(padrao, texto)

    if resultado:
        # Constrói a placa sem espaços ou caracteres desnecessários
        placa = resultado.group(0).replace(" ", "").replace("-", "")  # Remove espaços e hifens
        return placa  # Retorna a placa encontrada
    else:
        return None  # Retorna None se não encontrar