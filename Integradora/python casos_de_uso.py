from graphviz import Digraph

# Crear el grafo
graph = Digraph(format='png', filename='modelo_entidad_relacion')
graph.attr(rankdir='TB', bgcolor='white')

# Entidades con atributos en formato de texto
entities = {
    "clientes": [
        ("ID_cliente", "INTEGER"),
        ("Nombre", "VARCHAR(100)"),
        ("Apellido", "VARCHAR(100)"),
        ("Direccion", "TEXT"),
        ("Telefono", "VARCHAR(20)"),
        ("Correo_electronico", "VARCHAR(100)")
    ],
    "detalle_venta": [
        ("ID_detalle_venta", "INTEGER"),
        ("ID_producto", "INTEGER"),
        ("cantidad", "INTEGER"),
        ("subtotal", "DECIMAL(10, 2)"),
        ("total", "DECIMAL(10, 2)")
    ],
    "empleado": [
        ("id_empleado", "INTEGER"),
        ("nombre", "VARCHAR(100)"),
        ("telefono", "VARCHAR(20)"),
        ("RFC", "VARCHAR(20)"),
        ("rol", "VARCHAR(50)"),
        ("contraseña", "VARCHAR(100)")
    ],
    "facturas": [
        ("ID_Factura", "INTEGER"),
        ("Fecha_venta", "DATE"),
        ("ID_detalle_venta", "INTEGER"),
        ("Metodo_Pago", "VARCHAR(50)"),
        ("ID_cliente", "INTEGER"),
        ("ID_empleado", "INTEGER"),
        ("ID_ruta", "INTEGER")
    ],
    "productos": [
        ("ID_Producto", "INTEGER"),
        ("Nombre", "VARCHAR(100)"),
        ("Descripcion", "TEXT"),
        ("Precio_unitario", "DECIMAL(10, 2)"),
        ("precio_mayoreo", "DECIMAL(10, 2)"),
        ("Stock", "INTEGER"),
        ("proveedor", "VARCHAR(100)")
    ],
    "proveedor": [
        ("id_proveedores", "INTEGER"),
        ("nombre", "VARCHAR(100)"),
        ("direccion", "TEXT"),
        ("telefono", "VARCHAR(20)"),
        ("email", "VARCHAR(100)")
    ],
    "ruta": [
        ("id_ruta", "INTEGER"),
        ("empleado_chofer", "VARCHAR(100)"),
        ("direcciones", "TEXT"),
        ("empleado_salida", "VARCHAR(100)")
    ]
}

# Crear nodos para cada entidad con formato de texto
for entity, attributes in entities.items():
    label = f"{entity}\n"
    for attribute, datatype in attributes:
        label += f"{attribute}: {datatype}\n"
    
    graph.node(entity, label=label, shape='box')

# Relaciones entre entidades
relations = [
    ("facturas", "clientes", "ID_cliente"),
    ("facturas", "detalle_venta", "ID_detalle_venta"),
    ("facturas", "empleado", "ID_empleado"),
    ("facturas", "ruta", "ID_ruta"),
    ("detalle_venta", "productos", "ID_producto"),
    ("productos", "proveedor", "proveedor")
]

# Dibujar las relaciones entre entidades
for start, end, label in relations:
    graph.edge(start, end, label=label)

# Renderizar el diagrama
graph.render(view=True)

print("El modelo entidad-relación se ha generado correctamente.")
