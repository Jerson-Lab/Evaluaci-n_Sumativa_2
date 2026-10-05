from django.http import Http404
from django.shortcuts import render

TEMAS = [
    {
        "slug": "realidad-virtual",
        "nombre": "Realidad Virtual",
        "descripcion": "La realidad virtual crea entornos 3D inmersivos que se pueden "
                       "explorar con visores como Google Cardboard.",
        "detalle": "Se usa en videojuegos, educación, simuladores y capacitación. "
                   "Combina gráficos 3D, sensores de movimiento y audio espacial.",
        "imagenes": ["images/rv1.png", "images/rv2.png"],
        "destacado": True,
    },
    {
        "slug": "internet-de-las-cosas",
        "nombre": "Internet de las Cosas",
        "descripcion": "IoT conecta sensores y dispositivos a internet para medir y "
                       "controlar el mundo físico, por ejemplo con Arduino.",
        "detalle": "Se aplica en domótica, agricultura, monitoreo de agua y energía. "
                   "Los sensores envían datos que luego se procesan y visualizan.",
        "imagenes": ["images/iot1.png", "images/iot2.png"],
        "destacado": False,
    },
]


def inicio(request):
    contexto = {"titulo": "Bienvenido", "temas": TEMAS}
    return render(request, "inicio/inicio.html", contexto)


def tema_detalle(request, slug):
    tema = next((t for t in TEMAS if t["slug"] == slug), None)
    if tema is None:
        raise Http404("Tema no encontrado")
    return render(request, "inicio/tema.html", {"tema": tema})