ADD_DEFINITIONS(
    -DPYIMATH_EXPORTS
    )

ADD_LIBRARY ( PyImath ${LIB_TYPE}
    PyImath.cpp
    PyImathAutovectorize.cpp
    PyImathBox2Array.cpp
    PyImathBox3Array.cpp
    PyImathBox.cpp
    PyImathColor3.cpp
    PyImathColor4.cpp
    PyImathEuler.cpp
    PyImathFixedArray.cpp
    PyImathFrustum.cpp
    PyImathLine.cpp
    PyImathMatrix33.cpp
    PyImathMatrix44.cpp
    PyImathPlane.cpp
    PyImathQuat.cpp
    PyImathRandom.cpp
    PyImathShear.cpp
    PyImathStringArray.cpp
    PyImathStringTable.cpp
    PyImathTask.cpp
    PyImathUtil.cpp
    PyImathFixedVArray.cpp
    PyImathVec2fd.cpp
    PyImathVec2si.cpp
    PyImathVec3fd.cpp
    PyImathVec3siArray.cpp
    PyImathVec3si.cpp
    PyImathVec4fd.cpp
    PyImathVec4siArray.cpp
    PyImathVec4si.cpp

    PyImath.h
    PyImathAutovectorize.h
    PyImathBasicTypes.h
    PyImathBox.h
    PyImathBoxArrayImpl.h
    PyImathColor.h
    PyImathColor3ArrayImpl.h
    PyImathColor4Array2DImpl.h
    PyImathColor4ArrayImpl.h
    PyImathDecorators.h
    PyImathEuler.h
    PyImathExport.h
    PyImathFixedArray.h
    PyImathFixedArray2D.h
    PyImathFixedMatrix.h
    PyImathFixedVArray.h
    PyImathFrustum.h
    PyImathFun.h
    PyImathLine.h
    PyImathM44Array.h
    PyImathMathExc.h
    PyImathMatrix.h
    PyImathOperators.h
    PyImathPlane.h
    PyImathQuat.h
    PyImathRandom.h
    PyImathShear.h
    PyImathStringArray.h
    PyImathStringArrayRegister.h
    PyImathStringTable.h
    PyImathTask.h
    PyImathUtil.h
    PyImathVec.h
    PyImathVec2Impl.h
    PyImathVec3ArrayImpl.h
    PyImathVec3Impl.h
    PyImathVec4ArrayImpl.h
    PyImathVec4Impl.h
    PyImathVecOperators.h
)

TARGET_LINK_LIBRARIES ( PyImath
	Iex${ILMBASE_LIBSUFFIX}
	IexMath${ILMBASE_LIBSUFFIX}
	Imath${ILMBASE_LIBSUFFIX}
	${Boost_LIBRARIES}
	${PYTHON_LIBRARIES}
)

INSTALL ( TARGETS PyImath
	DESTINATION
	lib
)

ADD_LIBRARY ( imath ${LIB_TYPE}
    imathmodule.cpp
    PyImathFun.cpp
    PyImathBasicTypes.cpp 
)

SET_TARGET_PROPERTIES ( imath
	PROPERTIES PREFIX "" SUFFIX ".pyd" BUILD_WITH_INSTALL_RPATH ON
)

TARGET_LINK_LIBRARIES ( imath
	PyImath
	PyIex
	Imath${ILMBASE_LIBSUFFIX}
	Iex${ILMBASE_LIBSUFFIX}
	${Boost_LIBRARIES}
)

INSTALL ( TARGETS imath PyImath
    DESTINATION ${INSTALL_DIR}
    )

