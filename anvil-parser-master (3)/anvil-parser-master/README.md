# Minecraft Anvil Parser
[![Documentation Status](https://readthedocs.org/projects/anvil-parser/badge/?version=latest)](https://anvil-parser.readthedocs.io/en/latest/?badge=latest)

Simple parser for the [Minecraft anvil file format](https://minecraft.wiki/w/Anvil_file_format) made in Python
# Installation
This project is available on GitHub
```
pip install git+https://github.com/DN2048/anvil-parser.git
```
# Usage
## Reading
```python
import anvil

region = anvil.Region.from_file('r.0.0.mca')

# You can also provide the region file name instead of the object
chunk = anvil.Chunk.from_region(region, 0, 0)

# If `section` is not provided, will get it from the y coords
# and assume it's global
block = chunk.get_block(0, 0, 0)

print(block) # <Block(minecraft:air)>
print(block.id) # air
print(block.properties) # {}
```
## Making own regions
```python
import anvil
from random import choice

# Create a new region with the `EmptyRegion` class at 0, 0 (in region coords)
region = anvil.EmptyRegion(0, 0)

# Create `Block` objects that are used to set blocks
stone = anvil.Block('minecraft', 'stone')
dirt = anvil.Block('minecraft', 'dirt')

# Make a 16x16x16 cube of either stone or dirt blocks
for y in range(16):
    for z in range(16):
        for x in range(16):
            region.set_block(choice((stone, dirt)), x, y, z)

# Save to a file
region.save('r.0.0.mca')
```
# Todo
*This is my personal list, different from 0xTiger and matcool (original creator)*
- [ ] More utility functions
- [ ] Assert compatibility with version 1.20.1
- [ ] Extra features depending on my needs for the other projects
# Notes
*These are matcool (original creator) notes. Haven't validated any of this*
- Testing done in 1.14.4 - 1.19, should work fine for other versions
- Writing chunks and regions is broken from 1.16 onwards
