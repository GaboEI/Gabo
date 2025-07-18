def read_event():
    events = []
    if os.path.exists(event_file):
        with open(event_file, encoding="utf-8") as f:
            lines = f.readlines()

            # Ignorar encabezado y línea de separación
            data_lines = lines[2:]

            for line in data_lines:
                line = line.strip()
                if not line:
                    continue

                # Extraer columnas por posición fija
                try:
                    name = line[7:27].strip()
                    desc = line[30:60].strip()
                    date = line[63:83].strip()
                    status = line[86:].strip()

                    events.append([status, name, desc, date])
                except IndexError:
                    continue  # en caso de línea mal formada
    return events