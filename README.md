# Viva La Colifata

Repositorio de la versión estática inicial de https://vivalacolifata.org.

## Origen y propósito

- El sitio original fue construido con WordPress 7.0.3 y Elementor 3.25.11.
- Este repositorio comenzó como un snapshot estático de la web en vivo.
- El objetivo es preservar la identidad visual y convertir la página en un sitio estático ligero, sin agregar frameworks o procesos de build innecesarios.

## Estado actual

- Branch principal: `main`
- Snapshot estático importado y movido al raíz del repositorio.
- Captura de referencia móvil en `docs/screenshots/mobile-preview.png`.

## Estructura principal

- `index.html` — página principal en español
- `en/index.html` — versión en inglés
- `fr/index.html` — versión en francés
- `robots.txt`
- `wp-content/...` — estilos de Elementor, recursos de los temas e imágenes necesarios para el render actual
- `docs/screenshots/` — capturas de referencia visual

## Cómo previsualizar localmente

```bash
cd vivalacolifata
python3 -m http.server 8000
```

Luego abrir `http://localhost:8000/`.

## Validación del stream

```bash
python3 scripts/check_stream.py
```

La comprobación valida la URL configurada en las tres páginas y confirma que
la señal pública responde como audio de Radio La Colifata.

## Observaciones clave

- La navegación de idioma ya funciona con `index.html`, `en/index.html` y `fr/index.html`.
- El sitio conserva los estilos estáticos de Elementor y los recursos de los temas Lalita/Madhura, pero ya no carga jQuery ni el runtime JavaScript de Elementor.
- La interacción se resuelve con los pequeños scripts del tema para el menú, accesibilidad y regreso al inicio.

## Próximos pasos

1. Evaluar una reducción adicional del CSS heredado sin alterar el diseño.
2. Optimizar imágenes y carga de fuentes.
3. Verificar cada cambio en las tres versiones antes de publicarlo desde `main`.
