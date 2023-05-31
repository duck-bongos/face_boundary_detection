# Boundary Detection
A package to find the boundary of a 3D face object, given an input image and input object. It can be used as a way to automate or partially automate facial trimming. Its initial use was for geometric processing.

## Installation
### Step 0: Create Environment
```
python3 -m venv venv_name
cd boundary_detection/
```

### Step 1: Install Dependencies
If you don't already have poetry installed, you can install it using 
```pip3 install poetry```

Then you can install the dependencies by running the following command at the same level as the `pyproject.toml` file:
```poetry install```

To see a list of the current dependencies, you can view the `pyproject.toml` file.

## Running boundary detection
### Step 2: Run Boundary Detection
#### 2.1 General useage:
Poetry installs a command-line argument, `fbd` (for brevity), that you can use like this:
```
fbd -i <path_to_img>.png -o <path_to_obj>.obj -b <path_to_boundary>.txt
```

with the basename for both the image and the object being the same.

If you use it using files from this repository, you can run it like this:
```
cd facial_boundary_detection
[[ -d boundaries ]]
fbd -i <../../source.png> -o <../../source.obj> -b boundaries/outer.txt
```

#### 2.2 Additional Useage
Below are all CLI arguments that may be useful
```
    -b, --boundary_path : The filepath to the boundary file. Ends in `.txt`.
    -c, --chunk_path    : The filepath to the boundary chunk file. Ends in `.txt`.
    -d, --debug         : A flag that determines whether to output intermediate images. Stores `True`.
    -i, --image_path    : The filepath to the image associated with the object. Ends in `.png`.
    -k, --skip_boundary : Skip boundary detection, only calculate the keypoints. Stores `True`.
    -o, --object_path   : The filepath to the object associated with the image. Ends in `.obj`.
```

## How to create your own boundary.
Warning: It's a completely manual process.

First, take a look at the [Canonical Face](https://raw.githubusercontent.com/tensorflow/tfjs-models/838611c02f51159afdd77469ce67f0e26b7bbb23/face-landmarks-detection/mesh_map.jpg) model provided by MediaPipe. Each point is labeled by index. To make a boundary or to take a chunk out of a face, you need to form a loop of connected points. You can find a few examples I put together in `boundaries/` and `inconsistent_boundaries/`. They are simple text files with an integer on each line. Additional examples from MediaPipe can be found here [MediaPipe Keypoints](https://github.com/tensorflow/tfjs-models/blob/838611c02f51159afdd77469ce67f0e26b7bbb23/face-landmarks-detection/src/mediapipe-facemesh/keypoints.ts).

## Special Thanks
I'd like to take a moment to say a special thank you to the MediaPipe team(s) over at Tensorflow. The work you did is incredible.