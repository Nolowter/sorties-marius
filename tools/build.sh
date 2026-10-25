#!/bin/sh
# Reconstruit index.html à partir de la page de l'artifact (page.html)
cd "$(dirname "$0")/.."
{ printf '%s\n' '<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex"><style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'; cat page.html; printf '%s\n' '</body></html>'; } > index.html
