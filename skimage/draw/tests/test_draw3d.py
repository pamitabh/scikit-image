import numpy as np

from skimage._shared import testing
from skimage._shared.testing import assert_allclose, assert_array_equal
from skimage.draw import ellipsoid, ellipsoid_stats, rectangle


def test_ellipsoid_sign_parameters1():
    with testing.raises(ValueError):
        ellipsoid(-1, 2, 2)


def test_ellipsoid_sign_parameters2():
    with testing.raises(ValueError):
        ellipsoid(0, 2, 2)


def test_ellipsoid_sign_parameters3():
    with testing.raises(ValueError):
        ellipsoid(-3, -2, 2)


def test_ellipsoid_bool():
    test = ellipsoid(2, 2, 2)[1:-1, 1:-1, 1:-1]
    test_rotation = ellipsoid(2, 2, 2, rotation=(np.pi / 2, np.pi / 2, np.pi / 2))
    test_rotation = test_rotation[1:-1, 1:-1, 1:-1]
    test_anisotropic = ellipsoid(2, 2, 4, spacing=(1.0, 1.0, 2.0))
    test_anisotropic = test_anisotropic[1:-1, 1:-1, 1:-1]

    expected = np.array(
        [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        ]
    )

    assert_array_equal(test, expected.astype(bool))
    assert_array_equal(test_rotation, expected.astype(bool))
    assert_array_equal(test_anisotropic, expected.astype(bool))


def test_ellipsoid_levelset():
    test = ellipsoid(2, 2, 2, levelset=True)[1:-1, 1:-1, 1:-1]
    test_rotation = ellipsoid(
        2, 2, 2, rotation=(np.pi / 2, np.pi / 2, np.pi / 2), levelset=True
    )
    test_rotation = test_rotation[1:-1, 1:-1, 1:-1]
    test_anisotropic = ellipsoid(2, 2, 4, spacing=(1.0, 1.0, 2.0), levelset=True)
    test_anisotropic = test_anisotropic[1:-1, 1:-1, 1:-1]

    expected = np.array(
        [
            [
                [2.0, 1.25, 1.0, 1.25, 2.0],
                [1.25, 0.5, 0.25, 0.5, 1.25],
                [1.0, 0.25, 0.0, 0.25, 1.0],
                [1.25, 0.5, 0.25, 0.5, 1.25],
                [2.0, 1.25, 1.0, 1.25, 2.0],
            ],
            [
                [1.25, 0.5, 0.25, 0.5, 1.25],
                [0.5, -0.25, -0.5, -0.25, 0.5],
                [0.25, -0.5, -0.75, -0.5, 0.25],
                [0.5, -0.25, -0.5, -0.25, 0.5],
                [1.25, 0.5, 0.25, 0.5, 1.25],
            ],
            [
                [1.0, 0.25, 0.0, 0.25, 1.0],
                [0.25, -0.5, -0.75, -0.5, 0.25],
                [0.0, -0.75, -1.0, -0.75, 0.0],
                [0.25, -0.5, -0.75, -0.5, 0.25],
                [1.0, 0.25, 0.0, 0.25, 1.0],
            ],
            [
                [1.25, 0.5, 0.25, 0.5, 1.25],
                [0.5, -0.25, -0.5, -0.25, 0.5],
                [0.25, -0.5, -0.75, -0.5, 0.25],
                [0.5, -0.25, -0.5, -0.25, 0.5],
                [1.25, 0.5, 0.25, 0.5, 1.25],
            ],
            [
                [2.0, 1.25, 1.0, 1.25, 2.0],
                [1.25, 0.5, 0.25, 0.5, 1.25],
                [1.0, 0.25, 0.0, 0.25, 1.0],
                [1.25, 0.5, 0.25, 0.5, 1.25],
                [2.0, 1.25, 1.0, 1.25, 2.0],
            ],
        ]
    )

    assert_allclose(test, expected)
    assert_allclose(test_rotation, expected)
    assert_allclose(test_anisotropic, expected)


def test_ellipsoid_rotation_bool():
    test = ellipsoid(a=2, b=1, c=1, rotation=(np.pi / 2, np.pi / 2, np.pi / 2))
    test = test[1:-1, 1:-1, 1:-1]
    test_anisotropic = ellipsoid(
        a=2,
        b=1,
        c=2,
        rotation=(np.pi / 2, np.pi / 2, np.pi / 2),
        spacing=(1.0, 1.0, 2.0),
    )
    test_anisotropic = test_anisotropic[1:-1, 1:-1, 1:-1]

    expected = np.array(
        [
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
        ]
    )

    assert_array_equal(test, expected.astype(bool))
    assert_array_equal(test_anisotropic, expected.astype(bool))


def test_ellipsoid_rotation_levelset():
    test = ellipsoid(
        a=2, b=1, c=1, rotation=(np.pi / 2, np.pi / 2, np.pi / 2), levelset=True
    )
    test = test[1:-1, 1:-1, 1:-1]
    test_anisotropic = ellipsoid(
        a=2,
        b=1,
        c=2,
        rotation=(np.pi / 2, np.pi / 2, np.pi / 2),
        spacing=(1.0, 1.0, 2.0),
        levelset=True,
    )
    test_anisotropic = test_anisotropic[1:-1, 1:-1, 1:-1]

    expected = np.array(
        [
            [
                [2.0, 1.0, 2.0],
                [1.25, 0.25, 1.25],
                [1.0, 0.0, 1.0],
                [1.25, 0.25, 1.25],
                [2.0, 1.0, 2.0],
            ],
            [
                [1.0, 0.0, 1.0],
                [0.25, -0.75, 0.25],
                [0.0, -1.0, 0.0],
                [0.25, -0.75, 0.25],
                [1.0, 0.0, 1.0],
            ],
            [
                [2.0, 1.0, 2.0],
                [1.25, 0.25, 1.25],
                [1.0, 0.0, 1.0],
                [1.25, 0.25, 1.25],
                [2.0, 1.0, 2.0],
            ],
        ]
    )

    assert_allclose(test, expected)
    assert_allclose(test_anisotropic, expected)


def test_ellipsoid_stats():
    # Test comparison values generated by Wolfram Alpha
    vol, surf = ellipsoid_stats(6, 10, 16)
    assert_allclose(1280 * np.pi, vol, atol=1e-6)
    assert_allclose(1383.2828269179892359787, surf, atol=1e-6)

    # Test when a <= b <= c does not hold
    vol, surf = ellipsoid_stats(16, 6, 10)
    assert_allclose(1280 * np.pi, vol, atol=1e-6)
    assert_allclose(1383.2828269179892359787, surf, atol=1e-6)

    # Larger test to ensure reliability over broad range
    vol, surf = ellipsoid_stats(17, 27, 169)
    assert_allclose(103428 * np.pi, vol, atol=1e-4)
    assert_allclose(37426.253635465972897880, surf, atol=1e-6)

    # For equal a, b, c values
    vol, surf = ellipsoid_stats(10, 10, 10)
    assert_allclose(4000 * np.pi / 3, vol, atol=1e-6)
    assert_allclose(400 * np.pi, surf, atol=1e-6)


def test_rect_3d_extent():
    expected = np.array(
        [
            [
                [0, 0, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        ],
        dtype=np.uint8,
    )
    img = np.zeros((4, 5, 5), dtype=np.uint8)
    start = (0, 0, 2)
    extent = (5, 2, 3)
    pp, rr, cc = rectangle(start, extent=extent, shape=img.shape)
    img[pp, rr, cc] = 1
    assert_array_equal(img, expected)


def test_rect_3d_end():
    expected = np.array(
        [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        ],
        dtype=np.uint8,
    )
    img = np.zeros((4, 5, 5), dtype=np.uint8)
    start = (1, 0, 2)
    end = (3, 2, 3)
    pp, rr, cc = rectangle(start, end=end, shape=img.shape)
    img[pp, rr, cc] = 1
    assert_array_equal(img, expected)
