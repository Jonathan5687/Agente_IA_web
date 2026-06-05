# Skill: Revisar código web (HTML/CSS/JS)

## Objetivo
Analizar código web y detectar errores, malas prácticas o posibles mejoras.

## Criterios de revisión HTML
- ¿Tiene DOCTYPE y atributo lang?
- ¿Están presentes los meta tags (charset, viewport, description)?
- ¿Se usan etiquetas semánticas correctamente?
- ¿Existen imágenes sin atributo alt?
- ¿Los vínculos al CSS y al JS son correctos?
- ¿Hay estilos o scripts inline que deberían estar externalizados?

## Criterios de revisión CSS
- ¿Se definen variables en :root?
- ¿Existe un reset básico?
- ¿Hay media queries para responsive?
- ¿Se usan unidades consistentes (rem/em/px)?
- ¿Hay conflictos de especificidad o uso de !important innecesario?
- ¿Los nombres de clases son descriptivos?

## Criterios de revisión JavaScript
- ¿Se usa const/let en vez de var?
- ¿El código espera al DOMContentLoaded?
- ¿Se usan addEventListener en vez de atributos onclick?
- ¿Se validan los inputs del usuario?
- ¿Hay manejo de errores con try/catch donde corresponde?
- ¿Se usa eval() o document.write() (prácticas inseguras)?

## Formato de respuesta
Responder con:
1. Diagnóstico general del proyecto.
2. Errores encontrados por archivo (HTML / CSS / JS).
3. Mejoras recomendadas con justificación.
4. Versión corregida de los archivos problemáticos si aplica.
