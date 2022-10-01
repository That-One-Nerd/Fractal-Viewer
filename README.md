# Fractal Viewer

This is a small program I made in Python with Pygame to visualize the Mandlebrot set, or any other recursive function.
It's a tiny program I made in just a couple days (at school because I was bored, obviously).
It's mostly single-threaded, but has a multithreading option that adds an extra thread to monitor the screen. It's on by default.

Any settings you feel like customizing can be found in the [objects.py](objects.py) file in the `settings` class. There are comments to help guide you through the settings.

You can modify the actual recursive function in the [main.py](main.py) file in the `fractalContains()` ~~method~~ function. Again, some comments to at least *try* and help.

## Prerequisites

Not many, just a fairly recent Python, as well as pygame, cmath, and the threading and random libraries. Most of these (except pygame) come installed with Python from the beginning, I think.

---

Anyway, that's all. Just a small program I made. I'm only using Python for this thing because it's got a really easy-to-use drawing library. Nothing else I've found is anywhere as quick-and-easy. Sure, there are *definitely* overall better ones, but I made this in school as a bored-project. I don't want to spend an hour doing setup.

Yeah, that's all I've got.
