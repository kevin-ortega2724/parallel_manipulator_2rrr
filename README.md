# Manipulador Paralelo Plano en SolidWorks Integrado con ROS

Este proyecto representa un manipulador paralelo plano diseñado en SolidWorks y su integración con el sistema operativo de robots (ROS). El objetivo principal de este proyecto es permitir el control y la comunicación con el manipulador paralelo plano a través de ROS.

## Contenido del Proyecto

El repositorio incluye los siguientes elementos clave:


- **Launch:** El directorio 'launch' contiene archivos de lanzamiento (launch files) para configurar y ejecutar el manipulador en ROS.

<a name="launch1"></a>
![Archivo Launch](imagenes/launch.svg)

La [imagen](#launch1) resume la importancia fundamental de este archivo launch en un entorno de trabajo, ya que este permite efectuar su lanzamiento.


- **URDF (Unified Robot Description Format):** El directorio 'urdf' contiene la descripción del robot en el formato URDF, que se utiliza para definir la estructura y las características del manipulador.

<a name="urdf"></a>
![Archivo urdf](imagenes/urdf2.svg)

La [imagen](#urdf) proporciona una representación visual que esencialmente ilustra la descripción del robot a través del archivo URDF (Universal Robot Description Format). En este archivo, se encuentra codificada información crítica relacionada con la cinemática, las inercias y otros aspectos fundamentales que desempeñan un papel crucial en el funcionamiento y control del robot.


- **Archivo YAML:** El archivo YAML contiene configuraciones y parámetros importantes para la comunicación y el control del manipulador.


- **Nodos de Comunicación:** El proyecto también incluye nodos de ROS que facilitan la comunicación y el control del manipulador paralelo plano. Estos nodos están en desarrollo continuo para mejorar la funcionalidad de la comunicación con el manipulador.

## Estado del Proyecto

El proceso de comunicación y control del manipulador está en desarrollo activo. Actualmente, estamos trabajando en la implementación de las capacidades de control y en la mejora de la interacción con el manipulador a través de ROS. A medida que el proyecto avanza, esperamos agregar más funcionalidades y características.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar o tienes ideas para mejorar este proyecto, no dudes en enviar pull requests o reportar problemas (issues). Estamos ansiosos por trabajar junto a la comunidad de ROS para hacer de este proyecto una herramienta valiosa para la investigación y desarrollo de manipuladores paralelos planos.

¡Gracias por tu interés en nuestro proyecto!
