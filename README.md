# Image Draw Bounding Boxes
This microservice draws boxes on an image. It is intended to work with the
text recognition OCR service. The bounding boxes are passed in a JSON file that corresponds to the output of
the text recognition service. Namely, it must have the following structure:
```
{"boxes":[
    "position":{
        "left": ...,
        "top": ...,
        "width": ...,
        "height": ...,
    },
    {"position": ...},
    ...
]}
```
Where the values in "left", "top", "width" and "height" are given in pixels. 
The bounding boxes are drawn as red unfilled rectangles at the coordinates specified by the 4 fields above.

The JSON file may contain additional fields; they will be ignored.