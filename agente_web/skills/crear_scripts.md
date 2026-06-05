# Skill: Crear scripts JavaScript

## Objetivo
Generar JavaScript limpio para controlar la interacción y el comportamiento de la página.

## Instrucciones
- Usar ES6+: const y let (nunca var), arrow functions, template literals, destructuring.
- Envolver todo el código dentro de DOMContentLoaded para garantizar que el DOM esté listo:
  document.addEventListener('DOMContentLoaded', () => { ... });
- Separar la lógica en funciones pequeñas con nombres descriptivos.
- Registrar todos los eventos con addEventListener (no usar atributos onclick en HTML).
- Validar los inputs del usuario antes de procesarlos.
- Manejar errores con try/catch en operaciones que puedan fallar.
- Comentar las secciones principales del código.
- Evitar manipulación excesiva del DOM; preferir clases CSS para cambios visuales.
- No usar document.write() ni eval().

## Casos de uso comunes a implementar
- Menú hamburguesa para navegación en móvil.
- Validación de formularios en tiempo real.
- Mostrar/ocultar elementos (toggle de visibilidad).
- Filtrado o búsqueda de elementos en listas.
- Carrusel o slider de contenido.
- Manejo de pestañas (tabs).

## Formato de respuesta
Entregar:
1. Archivo scripts/main.js completo.
2. Funciones separadas por responsabilidad.
3. Comentarios explicativos en las secciones clave.
