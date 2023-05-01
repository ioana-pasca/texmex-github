#!/usr/bin/env python

fichero = "recetas.md"

with open(fichero, "r") as f:
    contenido = f.read()
    print(contenido)
