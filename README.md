# Viva La Colifata

Repositorio local inicial para el sitio estático de https://vivalacolifata.org.

## Origen y propósito

- Este repositorio comenzó como un snapshot estático de la web en vivo.
- La página original está construida con WordPress 7.0.3 y Elementor 3.25.11.
- El objetivo es mantener la identidad visual del sitio mientras se limpia y optimiza el contenido para un despliegue estático simple.
- No se agregó ningún framework ni proceso de build adicional hasta que haya una justificación clara.

## Estado actual

- Branch de trabajo: `preview/static-import`
- Export estático alojado en `export/vivalacolifata.org`
- Captura móvil guardada en `docs/screenshots/mobile-preview.png`
- No hay commits previos; este repositorio se inició en este workspace recién.

## Estructura principal

- `export/vivalacolifata.org/index.html` — página principal en español
- `export/vivalacolifata.org/en/index.html` — versión en inglés
- `export/vivalacolifata.org/fr/index.html` — versión en francés
- `export/vivalacolifata.org/robots.txt`
- `export/vivalacolifata.org/wp-content/...` — recursos CSS/JS heredados de WordPress/Elementor
- `docs/screenshots/` — capturas de referencia visual

## Cómo previsualizar localmente

```bash
cd vivalacolifata
python3 -m http.server 8000 --directory export/vivalacolifata.org
```

Luego abrir `http://localhost:8000/`.

## Observaciones iniciales

- La exportación mantiene los enlaces de idioma locales (`index.html`, `en/index.html`, `fr/index.html`).
- El sitio usa recursos externos para Google Fonts, SoundCloud, PayPal, Drive, redes sociales y streaming de audio.
- Las tres versiones de idioma ya están presentes, pero el HTML exportado requiere revisión de SEO (descripciones, Open Graph, canonical y hreflang) y de semántica (`main`, encabezados y `alt`).
- Hay recursos de WordPress/Elementor que deben evaluarse para limpieza, incluyendo scripts y estilos no necesarios en un sitio estático simple.

## Próximos pasos

1. Auditar el HTML exportado y corregir SEO multilingüe.
2. Revisar enlaces internos y rutas relativas.
3. Limpiar CSS/JS innecesarios de WordPress/Elementor.
4. Verificar que el selector de idioma y la navegación responsive funcionen sin romper el diseño.
