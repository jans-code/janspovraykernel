#!/usr/bin/env python
import os, shutil
from jupyter_client.kernelspec import KernelSpecManager
json ="""{"argv":["python","-m","janspovraykernel", "-f", "{connection_file}"],
 "display_name":"POV-Ray"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   version="1.1"
   width="300"
   height="300"
   id="svg4"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs8">
    <linearGradient
       id="linearGradient872">
      <stop
         style="stop-color:#ffbdbd;stop-opacity:1;"
         offset="0"
         id="stop870" />
      <stop
         style="stop-color:#ff0000;stop-opacity:1;"
         offset="0.82602119"
         id="stop868" />
    </linearGradient>
    <radialGradient
       xlink:href="#linearGradient872"
       id="radialGradient874"
       cx="108.15142"
       cy="106.10498"
       fx="108.15142"
       fy="106.10498"
       r="108.44332"
       gradientTransform="matrix(1.7691138,0.02284041,-0.01785666,1.3830957,-39.729397,-59.939644)"
       gradientUnits="userSpaceOnUse" />
  </defs>
  <path
     d="m 231.55789,152.61693 c -26.47544,26.2452 -72.94636,36.78463 -95.74622,32.08006 C 104.78806,229.45814 76.085789,269.72891 52.553026,300 54.808554,271.12073 66.035342,220.83319 80.5259,167.73972 52.842088,150.98514 44.840786,129.54264 44.840786,129.54264 c 12.260015,12.65938 25.002077,22.62367 38.685344,27.3285 3.700536,-13.25222 7.578027,-26.59924 11.545774,-39.75691 13.537126,19.05887 40.967666,31.3492 66.438876,30.28048 -3.23033,4.71279 -6.44281,9.39096 -9.63875,14.03726 30.20868,-7.45188 57.56794,-24.24178 66.26881,-52.71738 9.87039,-32.303167 -14.18356,-71.518861 -67.55761,-79.573794 -49.99238,-7.544582 -82.816607,11.217499 -109.026554,37.980148 0,0 24.116165,-68.8921322 110.628654,-67.08604003 31.97642,0.66759819 64.94063,16.53813803 85.28676,40.45858403 36.47089,42.877946 19.36813,87.060932 -5.9142,112.123442 z M 194.28788,86.417923 c 0,-24.117293 -19.92125,-43.668229 -44.49531,-43.668229 -24.57412,0 -44.49538,19.550936 -44.49538,43.668229 0,24.117297 19.92126,43.668177 44.49538,43.668177 24.57406,0 44.49531,-19.55089 44.49531,-43.668177 z"
     id="path2"
     style="fill:url(#radialGradient874);fill-opacity:1;stroke-width:0.585938" />
</svg>
"""

def install_kernelspec():
    kerneldir = "/tmp/janspovraykernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janspovraykernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janspovraykernel')