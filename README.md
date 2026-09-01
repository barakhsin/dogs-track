# dogs-track

Modified YOLOv8 tracking for counting stray dog populations from municipal camera
streams. Built for my BSc thesis at North-Eastern Federal University, Yakutsk
(2023): counting stray dog populations using computer vision and machine learning.

The problem is not detection, it is counting without double-counting. A dog that
leaves frame and returns must not be counted twice, so the pipeline pairs a YOLOv8
detector with OC-SORT tracking and maintains identity across a live stream, with
per-camera state so that counts can be attributed to a location.

## What is here

- `track.py` — detection and tracking over a video source or a live stream
- `trackers/` — OC-SORT and StrongSORT integration
- `estimator.py`, `worker.py`, `mypool.py` — multi-stream processing
- `train.py`, `val.py`, `evolve.py` — training and evaluation
- `Dockerfile`, `requirements.txt`

## Camera sources are not included

This code originally ran against municipal camera streams. **The camera endpoint
list and the example launch commands containing stream identifiers have been
removed from this repository and from its history**, because those endpoints are
third-party infrastructure and are not mine to publish. `track.py` still expects a
CSV mapping stream URLs to locations; supply your own, or pass any video file or
stream to `--source`.

## Installation

```
git clone https://github.com/barakhsin/dogs-track/
cd dogs-track
git clone --recurse-submodules https://github.com/ultralytics/ultralytics yolov8
pip install -r requirements.txt
```

## Running

```
python track.py --yolo-weights bestNano.pt --tracking-method ocsort \
  --source <video file or stream URL> --nosave --save-txt --conf-thres 0.2
```

## Licence

GPL-3.0, inherited from the YOLOv8 tracking code this is built on.
