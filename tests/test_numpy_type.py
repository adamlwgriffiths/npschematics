#!/usr/bin/env python

import unittest

from schematics.models import Model
from schematics.exceptions import ValidationError, ConversionError
from npschematics.types import NumpyArrayType

import numpy as np

class TestNumpyArrayType(unittest.TestCase):
    def test_numpy_type_with_model_with_numpy_array(self):
        class TestModel(Model):
            data = NumpyArrayType()

        m = TestModel()
        m.data = np.array([1,2,3,4])
        m.validate()

        self.assertTrue(isinstance(m.data, np.ndarray))
        self.assertTrue(np.array_equal(m.data, [1,2,3,4]))

    def test_numpy_type_with_model_with_list(self):
        class TestModel(Model):
            data = NumpyArrayType()

        m = TestModel()
        m.data = [1,2,3,4]
        m.validate()

        self.assertTrue(isinstance(m.data, np.ndarray))
        self.assertTrue(np.array_equal(m.data, [1,2,3,4]))

    def test_numpy_type_with_model_with_tuple(self):
        class TestModel(Model):
            data = NumpyArrayType()

        m = TestModel()
        m.data = (1,2,3,4)
        m.validate()

        self.assertTrue(isinstance(m.data, np.ndarray))
        self.assertTrue(np.array_equal(m.data, [1,2,3,4]))

    def test_numpy_conversion_with_string(self):
        with self.assertRaises(ConversionError):
            NumpyArrayType()('abc')

    def test_numpy_conversion_with_list(self):
        NumpyArrayType()([1,2,3])

    def test_numpy_conversion_with_tuple(self):
        NumpyArrayType()(((1,2,3,),(4,5,6,)))

    def test_numpy_conversion_with_list_of_tuples(self):
        NumpyArrayType()([(1,2,3,),(4,5,6,)])

    def test_numpy_type_with_numpy_array(self):
        NumpyArrayType().validate(np.array([1,2,3,4,5]))

    def test_numpy_type_with_dtype(self):
        with self.assertRaises(ValidationError):
            NumpyArrayType(dtype='float32').validate(np.array([1,2,3,4,5]))

    def test_numpy_type_with_different_dtype(self):
        with self.assertRaises(ValidationError):
            NumpyArrayType(dtype='int64').validate(np.array([1,2,3,4,5], dtype='float32'))

    def test_numpy_type_with_shape(self):
        NumpyArrayType(shape=(5,)).validate(np.array([1,2,3,4,5]))

    def test_numpy_type_with_invalid_shape(self):
        with self.assertRaises(ValidationError):
            NumpyArrayType(shape=(2,2,)).validate(np.array([1,2,3,4,5]))

    def test_numpy_type_with_size(self):
        NumpyArrayType(size=5).validate(np.array([1,2,3,4,5]))

    def test_numpy_type_with_invalid_size(self):
        with self.assertRaises(ValidationError):
            NumpyArrayType(size=6).validate(np.array([1,2,3,4,5]))

    def test_numpy_type_with_ndim(self):
        NumpyArrayType(ndim=2).validate(np.array([[1,2],[3,4],[5,6]]))

    def test_numpy_type_with_invalid_ndim(self):
        with self.assertRaises(ValidationError):
            NumpyArrayType(ndim=2).validate(np.array([1,2,3,4,5]))

    def test_numpy_type_with_string(self):
        with self.assertRaises(ValidationError):
            NumpyArrayType(ndim=2).validate('abc')

    def test_numpy_type_serialise(self):
        class TestModel(Model):
            i = NumpyArrayType(dtype='int32')
            f = NumpyArrayType(dtype='float32')

        m = TestModel({'i':[1,2,3,4,5], 'f':[1.,2.,3.,4.,5.]})
        d = m.serialize()
        m = TestModel(d)

        self.assertTrue(isinstance(m.i, np.ndarray))
        self.assertTrue(isinstance(m.f, np.ndarray))
        self.assertTrue(np.array_equal(m.i, [1,2,3,4,5]))
        self.assertTrue(np.array_equal(m.f, [1.,2.,3.,4.,5.]))

    def test_numpy_type_json(self):
        # commented out until 'Model.to_primitive' addition is pushed to pypi
        """
        class TestModel(Model):
            i = NumpyArrayType(dtype='int32')
            f = NumpyArrayType(dtype='float32')

        import json
        m = TestModel({'i':[1,2,3,4,5], 'f':[1.,2.,3.,4.,5.]})
        d = json.dumps(m.to_primitive())
        d = json.loads(d)
        m = TestModel(d)

        self.assertTrue(isinstance(m.i, np.ndarray))
        self.assertTrue(isinstance(m.f, np.ndarray))
        self.assertTrue(np.array_equal(m.i, [1,2,3,4,5]))
        self.assertTrue(np.array_equal(m.f, [1.,2.,3.,4.,5.]))
        """
        pass
