# This repository

is pyAlembic experiment on Windows and python3

* add [PyAlembic](https://github.com/alembic/alembic/tree/master/python/PyAlembic)
* add [AbcOpenGL](https://github.com/alembic/abcview/tree/master/lib/AbcOpenGL)

# OpenEXR

**OpenEXR** is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic (ILM) for use in computer imaging applications.
ILM subsequently released the source code and adjoining material as open source software.

The distribution has evolved to include support for stereoscopic and deep
images.  Weta Digital, Disney, Sony Pictures Imageworks, Pixar, DreamWorks
Animation and other studios have made contributions to the code base.
The file format has seen wide adoption in a number of industries.

The library, including all contributions, is released under the modified BSD license. 

OpenEXR's features include:

* Higher dynamic range and color precision than existing 8- and 10-bit
  image file formats.
* Support for 16-bit floating-point, 32-bit floating-point, and
  32-bit integer pixels. The 16-bit floating-point format, called "half",
  is compatible with the half data type in NVIDIA's Cg graphics language
  and is supported natively on their GPUs.
* Multiple image compression algorithms, both lossless and lossy. Some of
  the included codecs can achieve 2:1 lossless compression ratios on images
  with film grain.  The lossy codecs have been tuned for visual quality and
  decoding performance.
* Extensibility. New compression codecs and image types can easily be added
  by extending the C++ classes included in the OpenEXR software distribution.
  New image attributes (strings, vectors, integers, etc.) can be added to
  OpenEXR image headers without affecting backward compatibility with
  existing OpenEXR applications. 
* Support for sterescopic image workflows and a generalization
  to multi-views.

## Added Feature highlights for v2 release

* Flexible support for deep data: pixels can store a variable-length list
  of samples and, thus, it is possible to store multiple values at different
  depths for each pixel. Hard surfaces and volumetric data representations
  are accomodated.
* Multipart: ability to encode separate, but related, images in one file.
  This allows for access to individual parts without the need to read other
  parts in the file.
* Versioning: OpenEXR source allows for user configurable C++
  namespaces to provide protection when using multiple versions of the
  library in the same process space.
      
## Sub-modules
The distribution is divided into the following sub-modules:

* IlmBase
* OpenEXR
* OpenEXR_Viewers
* PyIlmBase
* Contrib
    
Please see the README files of each of the individual directories for more information.

A collection of OpenEXR images is available from the adjacent repository
[openexr-images](https://github.com/openexr/openexr-images).
