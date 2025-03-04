Inspired and Written With Grok3!

To Run:
- install python and pygame
- python main.py

----------------------------------------------------------

memory-thief/
├── .git/                # Git repo (already initialized)
├── .gitignore           # Ignores venv/, __pycache__/, *.pyc
├── venv/                # Virtual environment with Pygame
├── README.md            # Basic project info
├── main.py              # Entry point: initializes and runs the game
├── config.py            # Global constants and tweakable settings
├── game/                # Core game logic
│   ├── __init__.py      # Makes game/ a package
│   ├── engine.py        # Game loop and state management
│   ├── dungeon.py       # Procedural dungeon generation
│   ├── player.py        # Player class and mechanics
│   ├── neuron.py        # Enemy (neuron) class and behavior
│   └── memory.py        # Memory system (abilities, corruption)
├── utils/               # Helper functions
│   ├── __init__.py      # Makes utils/ a package
│   └── render.py        # Rendering utilities (e.g., draw wrappers)
└── assets/              # Placeholder for sprites/fonts (optional later)
    ├── sprites/         # e.g., player.png, neuron.png
    └── fonts/           # e.g., pixel_font.ttf