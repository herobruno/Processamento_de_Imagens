import cv2
import numpy as np

# Carrega a imagem
imagem = cv2.imread("car1.jpg")
imagem = cv2.resize(imagem, (800, 600))
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)


vermelho_baixo = np.array([10, 100, 50])
vermelho_alto = np.array([8, 255, 255])
vermelho_baixo2 = np.array([172, 100, 50])
vermelho_alto2 = np.array([180, 255, 255])

mascara1 = cv2.inRange(hsv, vermelho_baixo, vermelho_alto)
mascara2 = cv2.inRange(hsv, vermelho_baixo2, vermelho_alto2)
mascara_vermelha = mascara1 + mascara2


kernel = np.ones((25, 25), np.uint8)
mascara_vermelha = cv2.morphologyEx(mascara_vermelha, cv2.MORPH_CLOSE, kernel)


contornos, _ = cv2.findContours(mascara_vermelha, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

area_minima = 500
area_maxima = 20000
caixas = []

for contorno in contornos:
    area = cv2.contourArea(contorno)
    if area_minima < area < area_maxima:
        x, y, largura, altura = cv2.boundingRect(contorno)
        caixas.append([x, y, x+largura, y+altura])

# Junta caixas próximas (se sobrepõem ou estão muito perto)
def juntar_caixas(caixas, dist=30):
    resultado = []
    while caixas:
        x1, y1, x2, y2 = caixas.pop(0)
        i = 0
        while i < len(caixas):
            a1, b1, a2, b2 = caixas[i]
            if not (x2 + dist < a1 or x1 - dist > a2 or y2 + dist < b1 or y1 - dist > b2):
                x1 = min(x1, a1)
                y1 = min(y1, b1)
                x2 = max(x2, a2)
                y2 = max(y2, b2)
                caixas.pop(i)
                i = 0  
            else:
                i += 1
        resultado.append([x1, y1, x2, y2])
    return resultado

caixas_unidas = juntar_caixas(caixas)

# Desenha as caixas finais
for i, (x1, y1, x2, y2) in enumerate(caixas_unidas, start=1):
    quantidade_carros += 1
    cv2.rectangle(imagem, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(imagem, f'{i}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

print(f"Quantidade de carros vermelhos detectados: {quantidade_carros}")
cv2.imshow("Resultado - Carros Vermelhos Detectados", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
