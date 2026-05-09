#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Adel Julian Meza Sandoval"
edad = 13
estatura = 1.67
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("adeljuliano", "adelmeza98")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "tu haces", "artista": "Cindy y Mei", "duracion": "3:30"},
{"titulo": "Like Him", "artista": "Tyler, the Creator", "duracion": "4:38"},
{"titulo": "Where This Flower Blooms", "artista": "tyler, the creator", "duracion": "3:14"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
for cancion in Playlist:
    print(f"{cancion['titulo']} - {cancion['artista']} ({cancion['duracion']}) min")
print ("----------------------------------")