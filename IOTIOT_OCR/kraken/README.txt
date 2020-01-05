Execution steps. since kraken can be called directly by just activating the environment named venv present in parent folder.(i.e. in .. )

coammand
kraken -i kraken/image.png kraken/image.txt binarize segment ocr -m kraken/en_best.mlmodel



Binarization
kraken -i kraken/image.png kraken/test/bw.tif binarize

Segmenentation
kraken/test/binarized.tif kraken/test/segmen_lines.json segment

ocr

