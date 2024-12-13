# Figure generation folder

This folder contains the necessary scripts to generate the figures, visualizing the data in the *measurements/* folder.

## Usage

Use the provided *makefile* to generate figure PDFs. The following make targets are available:
- `fig`: Generate all PDFs.
- `fig_svg`: Generate all SVGs.
- `figures/pdf/[figure name].pdf`: Only generate *[figure name].pdf*.
- `clean_fig`: Remove PDFs (included in `clean`).
- `realclean_fig`: `clean_fig` and remove all generates SVG and data files (included in `realclean`).
- `mrproper_fig`: Same as `realclean_fig`.
- `clean_fig_pdf`: Same as `clean_fig`.
- `clean_fig_svg`: Remove all generated SVGs and *svg/* folder if empty (included in `realclean_fig`).
- `clean_fig_data`: Remove all data files and *data/* folder (included in `realclean_fig`).

## Note

Many figure generation scripts store processed data in the *data/* folder.
Using this processed data allows for faster figure regeneration.