import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    (r'<p class="producto-description">\s*Mantente alerta.*?efectos secundarios\.\s*</p>', 
     '''<p class="producto-description">
                            <strong>Componentes:</strong> GINSENG + ACAI BERRY + ANTOCIANINAS DE MAÍZ MORADO + TÉ VERDE
                        </p>
                        <div class="producto-caracteristicas">
                            <strong>Características:</strong>
                            <ul>
                                <li>Te mantiene con energía durante todo el día</li>
                                <li>Potente multivitamínico (+13 vitaminas)</li>
                                <li>Mejora el crecimiento de cabello y uñas</li>
                                <li>Mejora la calidad de la piel</li>
                                <li>Elimina la fatiga crónica</li>
                                <li>Calma la ansiedad y mejora la depresión</li>
                                <li>Disminuye fuertemente la inflamación abdominal</li>
                                <li>Reduce la retención de líquidos</li>
                                <li>Ideal para personas con HIPOTIROIDISMO</li>
                            </ul>
                        </div>'''),
    (r'<p class="producto-description">\s*Siéntete más liviana liberando desechos.*?forma efectiva\.\s*</p>',
     '''<p class="producto-description">
                            <strong>Componentes:</strong> INULINA DE ACHICORIA + PSYLLIUM + KELP + ANIS ESTRELLA + MUCILAGO DE LINAZA
                        </p>
                        <div class="producto-caracteristicas">
                            <strong>Características:</strong>
                            <ul>
                                <li>Regula el tránsito intestinal</li>
                                <li>Libérate del estreñimiento</li>
                                <li>Elimina el malestar y pesadez intestinal</li>
                                <li>Limpia el colon e intestino en profundidad</li>
                                <li>Mejora la digestión</li>
                                <li>Mejora la gastritis</li>
                                <li>Disminuye fuertemente la inflamación abdominal</li>
                                <li>Elimina toxinas acumuladas</li>
                            </ul>
                        </div>'''),
    (r'<p class="producto-description">\s*Transforma la grasa en energía.*?entrenamientos\.\s*</p>',
     '''<p class="producto-description">
                            <strong>Componentes:</strong> Mix de tés (té rojo, té verde y té negro) + L-carnitina + Tamarindo malabar + Ácido alfa lipoico + Aminoácidos + Vitamina B6 + Cromo
                        </p>
                        <div class="producto-caracteristicas">
                            <strong>Características:</strong>
                            <ul>
                                <li>Acelera el metabolismo por ende bajas de peso</li>
                                <li>Mejora la digestión</li>
                                <li>Reduce la retención de líquidos</li>
                                <li>Reduce las celulitis</li>
                                <li>Reduce el colesterol y triglicéridos</li>
                                <li>Ideal como pre entreno ya que transforma la grasa en energía</li>
                            </ul>
                        </div>'''),
    (r'<p class="producto-description">\s*Nutre tu piel, cabello y uñas.*?primera toma\.\s*</p>',
     '''<p class="producto-description">
                            <strong>Componentes:</strong> PÉPTIDOS DE COLÁGENO BIOACTIVO OPTIMIZADO + COENZIMA Q10 + SESBANIA (BIOTINA NATURAL) + CONCENTRADO DE SÚPER FRUTAS EXÓTICAS (VITAMINAS C Y E) + ZINC
                        </p>
                        <div class="producto-caracteristicas">
                            <strong>Características:</strong>
                            <ul>
                                <li>Mejora la estructura de la dermis; para tener una piel con mayor elasticidad, más firme y uniforme (sin arrugas).</li>
                                <li>Nutre, protege y repara la piel dañada.</li>
                                <li>Previene la aparición de los signos del envejecimiento prematuro causado por los radicales libres.</li>
                                <li>Fortalece también cabello y uñas.</li>
                            </ul>
                        </div>'''),
    (r'<p class="producto-description">\s*Favorece el equilibrio hormonal.*?armonía con tu cuerpo\.\s*</p>',
     '''<p class="producto-description">
                            <strong>Componentes:</strong> Aminoácidos (L-Arginina) + Jalea Real + Zinc
                        </p>
                        <div class="producto-caracteristicas">
                            <strong>Características:</strong>
                            <ul>
                                <li>Mejora la circulación sanguínea y promueve la vasodilatación</li>
                                <li>Mejora las varices, arañitas y celulitis</li>
                                <li>Eleva la potencia sexual y la fertilidad</li>
                                <li>Eleva el estado de ánimo</li>
                                <li>Potente pre entrenamiento</li>
                                <li>Ideal para la menopausia</li>
                            </ul>
                        </div>'''),
    (r'<p class="producto-description">\s*Disfruta tus comidas controlando.*?forma natural\.\s*</p>',
     '''<p class="producto-description">
                            <strong>Componentes:</strong> FIBRA DE ACACIA + FIBRA DE ACHICORIA + EXTRACTO DE CANELA + PECTINA DE MANZANA + EXTRACTO DE YACÓN + TÉ VERDE + CROMO
                        </p>
                        <div class="producto-caracteristicas">
                            <strong>Características:</strong>
                            <ul>
                                <li>Potente regulador de carbohidratos.</li>
                                <li>Regula el azúcar en sangre</li>
                                <li>Ideal para diabéticos</li>
                                <li>Mejora la digestión</li>
                                <li>Reduce la retención de líquidos</li>
                                <li>Reduce el colesterol y triglicéridos</li>
                            </ul>
                        </div>''')
]

for pat, rep in replacements:
    text = re.sub(pat, rep, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Replacement script executed.")
