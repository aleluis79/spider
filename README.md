# Spider Shooter

Un juego de disparos desarrollado con Python y Pygame donde debes defender la parte inferior de la pantalla de arañas que descienden desde arriba.

## Descripción del Juego

Las arañas aparecen en la parte superior de la pantalla y descienden por su telaraña. El jugador controla una nave en la parte inferior que puede moverse horizontalmente y disparar láseres para eliminar a las arañas. El juego termina cuando una araña llega a la parte inferior de la pantalla.

## Características

- 🕷️ Arañas que descienden con velocidad progresiva
- 🚀 Nave espacial con movimiento horizontal
- ⚡ Sistema de disparo con láseres
- 🎯 Sistema de puntuación
- 📈 Niveles progresivos con aumento de dificultad
- ⏸️ Función de pausa
- 🔄 Reinicio del juego
- 🎮 Controles intuituosos

## Controles

| Tecla | Acción |
|-------|--------|
| ← → | Mover la nave izquierda/derecha |
| Espacio | Disparar láser |
| P | Pausar/Reanudar juego |
| R | Reiniciar (cuando el juego termina) |

## Instalación

1. Asegúrate de tener Python instalado (versión 3.7+)
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   O instala directamente Pygame:
   ```bash
   pip install pygame
   ```

## Ejecución

```bash
python spider_shooter.py
```

## Sistema de Juego

- **Puntuación**: Cada araña eliminada otorga 10 puntos
- **Niveles**: Cada 50 puntos aumenta el nivel
- **Dificultad**: La velocidad de las arañas aumenta con cada nivel
- **Game Over**: El juego termina cuando una araña llega a la parte inferior

## Estructura del Proyecto

```
spider/
├── spider_shooter.py    # Archivo principal del juego
├── requirements.txt      # Dependencias del proyecto
└── README.md           # Documentación del proyecto
```

## Clases Principales

- **Spider**: Representa las arañas enemigas
- **Player**: Controla la nave del jugador
- **Laser**: Proyectiles disparados por el jugador
- **Game**: Gestiona el estado y la lógica del juego

## Requisitos del Sistema

- Python 3.7 o superior
- Pygame 2.5.2
- Sistema operativo: Windows, macOS o Linux

## Licencia

Este proyecto es de código abierto y puede ser modificado y distribuido libremente.

## Créditos

Desarrollado como un proyecto de aprendizaje de programación de videojuegos con Python y Pygame.