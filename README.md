# xmltools

A Collection of XML Tools

---Value Parser---

Valueparser.py finds {key, value} pairs at defined path in XML file. Usage: "python xmlparse.py --path /path/to/root input_file key1 key2 ..."

Input format: XML, output format: JSON

More information: python valueparser.py -h

---Element Parser---

Elementparser.py finds elements from XML in a specific path and removes any other paths and elements.

More information: python elementparser.py -h

---File name parser---

Filenameparser.py finds filenames from a text file. If the filename isn't at the beginning of each line, optional search key can be defined.

More information: python filenameparser.py -h
