Mutable Instruments UGens
=========

Source
--------

Source and binaries available here: https://github.com/v7b1/mi-UGens

Installation
--------

Instructions adapted from https://tidalcycles.org/docs/reference/mi-ugens-installation/

- Put the mi-UGens directory extracted from the download binaries in your in Extensions dir (`Platform.userExtensionDir`)
Example: ~/.local/share/SuperCollider/Extensions

- Create a new synthdef file mi-ugens.scd, with these synthdefs
  
Linux: ~/.local/share/SuperCollider/synthdefs/mi-ugens.scd

Configure SuperCollider - edit your startup.scd:
Linux: ~/.conf/SuperCollider/startup.scd

Load the mi-ugens.scd synthdef in startup.scd.
load("~/.local/share/SuperCollider/synthdefs/mi-ugens.scd");

