# Pythonové moduly pro PedF

Sada modulů pro práci s XML soubory z Almy a další projekty.

## Instalace

    $ git clone https://github.com/Knihovna-PedF-UK/pedfmodules
    $ cd  pedfmodules
    $ pip install .

## Moduly

### Almaxml

Nahraje  XML soubor z Analytik v Almě a převede ho na Pandas Data Frame.

```
import pedfmodules.almaxml as ax
data = ax.load("filename.xml", mapping = {'C1':'id', 'C2': 'author'})
```

`mapping` je volitelný, ale vzhledem k tomu, že každý výstup z analytik používá jiné
pole pro stejné údaje, je v praxi většinou třeba.
