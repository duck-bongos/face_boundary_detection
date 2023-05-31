# Boundary Detection
A package to find the boundary of a 3D face object, given an input image and input object. It can be used as a way to automate or partially automate facial trimming. Its initial use was for geometric processing.


## Running boundary detection
### Step 0: Create Environment
```
python3 -m venv venv_name
cd boundary_detection/
```

### Step 1: Install Dependencies
```
cd boundary_detection/
pip install -r requirements.txt venv_name
```

### Step 2: Run Boundary Detection
General useage:
```
python3 main.py -i <path_to_img>.png -o <path_to_obj>.obj -b <path_to_boundary>.txt
```
with the basename for both the image and the object being the same.

If you use it using files from this repository, you can run it like this:
```
cd boundary_detection/
python3 main.py -i ../data/source.png -o ../data/source.obj -b boundaries/outer.txt
```


## How to create your own boundary.
Warning: It's a completely manual process.

First, take a look at the [Canonical Face](https://raw.githubusercontent.com/tensorflow/tfjs-models/838611c02f51159afdd77469ce67f0e26b7bbb23/face-landmarks-detection/mesh_map.jpg) model provided by MediaPipe. Each point is labeled by index. To make a boundary or to take a chunk out of a face, you need to form a loop of connected points. You can find a few examples I put together in `boundaries/` and `inconsistent_boundaries/`. They are simple text files with an integer on each line. Additional examples from MediaPipe can be found here [MediaPipe Keypoints](https://github.com/tensorflow/tfjs-models/blob/838611c02f51159afdd77469ce67f0e26b7bbb23/face-landmarks-detection/src/mediapipe-facemesh/keypoints.ts).


## Special Thanks
I'd like to take a moment to say a special thank you to the MediaPipe team(s) over at Tensorflow. 