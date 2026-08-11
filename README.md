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
- `wp-content/...` — recursos CSS/JS heredados de WordPress/Elementor necesarios para el render actual
- `wp-includes/...` — dependencias JS locales (jQuery) incluidas en el snapshot
- `docs/screenshots/` — capturas de referencia visual

## Cómo previsualizar localmente

```bash
cd vivalacolifata
python3 -m http.server 8000
```

Luego abrir `http://localhost:8000/`.

## Observaciones clave

- La navegación de idioma ya funciona con `index.html`, `en/index.html` y `fr/index.html`.
- El sitio depende de recursos estáticos locales de Elementor, el tema Lalita/Madhura y Google Fonts.
- Actualmente hay scripts inline de Elementor y WordPress que deben revisarse y posiblemente limpiarse para optimizar el sitio.
- También se observó una inyección de Cloudflare en el HTML exportado; esa parte no es necesaria para el despliegue estático.

## Próximos pasos

1. Auditar y limpiar HTML/SEO multilingüe.
2. Depurar rutas relativas e internalización de enlaces.
3. Evaluar y reducir CSS/JS de WordPress/Elementor si no es necesario.
4. Verificar previews posteriores en Vercel usando la rama `main`.
