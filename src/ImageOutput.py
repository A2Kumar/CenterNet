from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import _init_paths

from opts import opts
from detectors.detector_factory import detector_factory

if __name__ == '__main__':
  opt = opts().init()
  image_name = opt.image_name_path
  Detector = detector_factory[opt.task]
  detector = Detector(opt)
  ret = detector.run(image_name)
  print(ret)
