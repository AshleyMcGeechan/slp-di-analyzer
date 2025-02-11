# SLP-DI-Analyzer

A tool for generating Directional Influence heatmaps from Slippi files.

## Installation
Download the newest executable version from [*Releases*](http://github.com/AshleyMcGeechan/slp-di-analyzer/releases).

Or download as a package from PyPI with:
```
pip install slp-di-analyzer
```

If you are using Python 3.13 or higher you will also need to run:
```
pip install peppi-py --no-deps
```

## Usage
Simply run the executable found at [*Releases*](http://github.com/AshleyMcGeechan/slp-di-analyzer/releases).

Or if you installed the package using PyPI you can run it using this command:
```
python -m slp_di_analyzer
```

![gui](https://raw.githubusercontent.com/AshleyMcGeechan/slp-di-analyzer/assets/gui_example.png)

Click the Select Slippi File Directory button and navigate to a folder containing your SLP files. This will also search any subfolders.

The Load Slippi Files button will then load and filter the files. Progress will be displayed in the box at the bottom.

Enter your connect code in the box, this is required to display any data. The code is not case sensitive and doesn't require the \# symbol.

You can then use the dropdown menus to filter by character and move.

If no heatmap is displayed that means no DI events were found for that character and move. If no label is displayed that means the selected character does not have that move or that move is not able to be DI'ed.

If you want to see your DI only at certain percents, to differentiate between combo DI or survival DI for example, enter the percent range and click the Update Percentage Range button.

The program separates DI events by the direction you were attacked from. Click the Change Knockback Direction button to switch between left and right.

The Toggle Knockback Angle Display button will display lines showing the exact knockback direction of the selected move. Moves with multiple knockback directions will display multiple lines labeled based on their source. For example Fox Up Air has a first and second hit while a Marth Forward Air has different knockbacks based on its connecting hitbox.

If you want to see the exact number of times you DI'ed a certain direction the Display Magnitudes will display a grid of numbers overlaying the heatmap. These numbers aggregate from nearby stick coordinates and are not a \1:1 representation.

Finally you can save an image of the heatmap using the Save Heatmap button.

## Acknowledgments

Thank you to Fizzi and everyone who has contributed to [Project Slippi](https://slippi.gg/). 10 more years <3

Thank you to Schmoo and GentleFox for the [Melee Calculator](https://ikneedata.com/calculator.html), where I sourced the knockback angle data.

Thank you to [hohav](https://github.com/hohav) for their python SLP parser, I'm really glad I didn't have to make one from scratch.