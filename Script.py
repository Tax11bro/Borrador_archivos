import os

def borrar_archivos(ruta=None, extensiones=None):
    if ruta is None:
        ruta = os.path.expanduser("~")
    if extensiones is None:
        extensiones = [".txt"]

    # Convertir a set para búsqueda más rápida
    extensiones_set = set(ext.lower() for ext in extensiones)

    archivos = []
    for carpeta, subcarpetas, ficheros in os.walk(ruta):
        for fichero in ficheros:
            if os.path.splitext(fichero)[1].lower() in extensiones_set:
                archivos.append(os.path.join(carpeta, fichero))

    if not archivos:
        print("No se encontraron archivos con esas extensiones en:", ruta)
        return

    print(f"Se encontraron {len(archivos)} archivos:\n")
    for f in archivos:
        print(" ", f)

    confirmar = input("\n¿Seguro que quieres borrarlos todos? (escribe SI para confirmar): ")

    if confirmar.strip().upper() == "SI":
        borrados, errores = 0, 0
        for f in archivos:
            try:
                os.remove(f)
                print(f"  [OK] Borrado: {f}")
                borrados += 1
            except PermissionError:
                print(f"  [SIN PERMISOS] {f}")
                errores += 1
            except Exception as e:
                print(f"  [ERROR] {f}: {e}")
                errores += 1
        print(f"\nListo. {borrados} borrados, {errores} sin permisos o con error.")
    else:
        print("Operación cancelada.")

# --- USO ---
borrar_archivos(
    ruta=r"C:\\",
    extensiones=[
        # Texto y documentos
        ".txt", ".doc", ".docx", ".pdf", ".odt", ".rtf", ".md", ".tex",
        ".wpd", ".pages", ".html", ".htm", ".xml", ".xhtml", ".mhtml",
        ".mht", ".wps", ".abw", ".zabw", ".lwp", ".602", ".sdw",

        # Hojas de cálculo
        ".xlsx", ".xls", ".csv", ".ods", ".numbers", ".xlsm", ".xlsb",
        ".xltx", ".xlt", ".sxc", ".dif", ".sylk", ".slk",

        # Presentaciones
        ".pptx", ".ppt", ".odp", ".key", ".pps", ".ppsx", ".pptm",
        ".potx", ".pot", ".sxi",

        # Imágenes
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg",
        ".ico", ".tiff", ".tif", ".raw", ".psd", ".ai", ".eps",
        ".heic", ".heif", ".avif", ".cr2", ".nef", ".orf", ".arw",
        ".dng", ".rw2", ".pct", ".pict", ".xcf", ".cdr", ".wmf",
        ".emf", ".jfif", ".jp2", ".j2k", ".exr", ".hdr", ".tga",
        ".pcx", ".pbm", ".pgm", ".ppm",

        # Video
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",
        ".m4v", ".3gp", ".3g2", ".vob", ".ts", ".mts", ".m2ts",
        ".ogv", ".rm", ".rmvb", ".asf", ".divx", ".xvid", ".f4v",
        ".mpg", ".mpeg", ".m2v", ".m1v", ".qt",

        # Audio
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a",
        ".opus", ".mid", ".midi", ".aiff", ".aif", ".ape", ".mka",
        ".ra", ".rm", ".ac3", ".dts", ".amr", ".au", ".caf",
        ".pcm", ".wv", ".tta", ".spx",

        # Comprimidos
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",
        ".cab", ".iso", ".img", ".dmg", ".tgz", ".tbz2", ".lzma",
        ".lz", ".zst", ".br", ".lz4", ".ar", ".cpio",

        # Temporales y logs
        ".tmp", ".log", ".bak", ".old", ".cache", ".dmp", ".chk",
        ".gid", ".temp", ".swp", ".swo", ".part", ".crdownload", ".download",

        # Código
        ".py", ".js", ".ts", ".c", ".cpp", ".h", ".hpp", ".java",
        ".cs", ".php", ".rb", ".go", ".rs", ".swift", ".kt", ".json",
        ".yaml", ".yml", ".toml", ".css", ".scss", ".sass", ".less",
        ".bat", ".sh", ".ps1", ".lua", ".pl", ".r", ".m", ".f",
        ".f90", ".asm", ".s", ".vb", ".vbs", ".coffee", ".jsx",
        ".tsx", ".vue", ".svelte", ".dart", ".ex", ".exs", ".erl",
        ".hs", ".ml", ".clj", ".lisp", ".scm", ".nim", ".cr",
        ".zig", ".sql", ".graphql", ".proto",

        # Bases de datos
        ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".dbf",
        ".fdb", ".gdb", ".sdb",

        # Fuentes
        ".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon", ".fnt",

        # 3D y diseño
        ".obj", ".fbx", ".blend", ".stl", ".dae", ".3ds", ".max",
        ".maya", ".mb", ".ma", ".c4d", ".lwo", ".lws", ".ply",
        ".gltf", ".glb", ".usdz",

        # Ebooks
        ".epub", ".mobi", ".azw", ".azw3", ".fb2", ".lit", ".lrf", ".djvu",

        # Email y contactos
        ".eml", ".msg", ".pst", ".ost", ".mbox", ".vcf", ".ics",

        # Configs
        ".ini", ".cfg", ".conf", ".config", ".reg", ".inf", ".properties", ".env",

        # Subtítulos
        ".srt", ".sub", ".ass", ".ssa", ".vtt", ".sbv",

        # Torrents
        ".torrent",

        # Mapas y geo
        ".gpx", ".kml", ".kmz", ".geojson", ".shp",

        # Sistema (intentará borrar, fallará sin admin)
        ".dll", ".sys", ".exe", ".msi", ".drv", ".ocx", ".cpl",
        ".scr", ".mui", ".cat", ".manifest", ".policy",

        # Otros
        ".iso", ".bin", ".cue", ".nrg", ".mdf", ".mds",
        ".jar", ".war", ".apk", ".ipa",
        ".pem", ".crt", ".cer", ".key", ".csr",
        ".blend1", ".blend2", ".lnk", ".url",
    ]
)
