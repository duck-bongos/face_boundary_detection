import os
from pathlib import Path

from facial_boundary_detection.src.utils import parse_cli
from facial_boundary_detection.src.keypoints import run_keypoints
from facial_boundary_detection.src.pipeline import run_pipeline

def run():
    os.chdir(os.path.dirname(__file__))
    args = parse_cli()
    fpath_img = Path(args.image_path)
    fpath_obj = Path(args.obj_path)
    fpath_bound = Path(args.boundary_path)
    if args.get("chunk_path"):
        fpath_chunk = Path(args.chunk_path)
    else:
        fpath_chunk = None

    if args.skip_boundary:
        run_keypoints(fpath_img=fpath_img, fpath_obj=fpath_obj)

    else:
        cname = "" if fpath_chunk is None else fpath_chunk.as_posix()
        print(f"Running boundary detection for {fpath_bound.as_posix()} | {cname}")
        run_pipeline(
            fpath_img=fpath_img,
            fpath_obj=fpath_obj,
            fpath_boundary=fpath_bound,
            fpath_chunk=fpath_chunk,
            debug=args.debug,
        )

if __name__ in "__main__":
    run()