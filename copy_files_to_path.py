# this file has not tested yet
import shutil
fileList = [
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKernel.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKMath.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKXSBase.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKBRep.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKG2d.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKG3d.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKTopAlgo.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKGeomBase.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKShHealing.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKGeomAlgo.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKPrim.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKLCAF.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKXCAF.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKDESTEP.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKBinXCAF.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKBO.dll",
"C:/3rdparty/occt-7.8.0/win64/vc14/bind/TKMesh.dll",
]
destDir = "C:/WorkSpace"
for file in fileList:
    shutil.copy(file, destDir)
