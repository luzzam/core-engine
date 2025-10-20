"""
Core Engine Project

A high-performance, open-source engine for building complex systems.

Project Structure
----------------

* `core`: The main engine package.
* `utils`: Utility functions for tasks like logging and configuration.
* `data`: Data structures and algorithms for data manipulation and analysis.
* `plugins`: Extensible plugins for adding custom functionality to the engine.

Installation
------------

```bash
pip install -r requirements.txt
```

Usage
-----

```python
import core

# Create an instance of the engine
engine = core.Engine()

# Configure the engine
engine.configure(config_file="config.yaml")

# Run the engine
engine.run()
```

"""

# Import required modules
import logging
import importlib
import os
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load configuration
config = yaml.safe_load(open("config.yaml", "r"))

# Import plugins
plugins = []
for file in os.listdir("plugins"):
    if file.endswith(".py"):
        plugin = importlib.import_module(f"plugins.{file[:-3]}")
        plugins.append(plugin)

# Run the engine
def run():
    # Initialize the engine
    engine = CoreEngine(config, plugins)

    # Run the engine
    engine.run()

if __name__ == "__main__":
    run()