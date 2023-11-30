import re

def add_gazebo_tags(urdf_file, modified_urdf_file):
    with open(urdf_file, 'r') as file:
        urdf_content = file.read()

    # Patrones para encontrar enlaces y articulaciones
    link_pattern = re.compile(r'(<link name="[^"]+">.*?</link>)', re.DOTALL)
    joint_pattern = re.compile(r'(<joint name="[^"]+" type="[^"]+">.*?</joint>)', re.DOTALL)

    # Función para añadir etiqueta <gazebo> después de cada enlace o articulación
    def add_gazebo_tag(match):
        tag = match.group(1)
        if '<link' in tag:
            # Añadir configuración de gazebo para enlace
            return tag + '\n<gazebo reference="{}">\n    <material>Gazebo/Grey</material>\n</gazebo>'.format(tag.split('"')[1])
        elif '<joint' in tag:
            # Añadir configuración de gazebo para articulación
            return tag + '\n<gazebo reference="{}">\n    <limit>\n        <effort>30</effort>\n        <velocity>1.0</velocity>\n    </limit>\n    <PID>\n        <p>1000.0</p>\n        <i>0</i>\n        <d>100.0</d>\n    </PID>\n</gazebo>'.format(tag.split('"')[1])
        return tag

    # Aplicar la función a todos los enlaces y articulaciones
    modified_content = re.sub(link_pattern, add_gazebo_tag, urdf_content)
    modified_content = re.sub(joint_pattern, add_gazebo_tag, modified_content)

    # Escribir el contenido modificado en un nuevo archivo
    with open(modified_urdf_file, 'w') as file:
        file.write(modified_content)

# Usar el script
urdf_file = '/home/ko/ws1_mp1/src/manipulador/urdf/manipulador.urdf'  # Ruta a tu archivo URDF original
modified_urdf_file = 'manipulator_modifie.urdf'  # Ruta al archivo URDF modificado
add_gazebo_tags(urdf_file, modified_urdf_file)

