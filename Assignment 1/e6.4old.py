import functools

from numpy.core import asarray, zeros, swapaxes, conjugate, take, sqrt
from . import _pocketfft_internal as pfi
from numpy.core.multiarray import normalize_axis_index
from numpy.core import overrides
def _raw_fft(a, n, axis, is_real, is_forward, inv_norm):
    axis = normalize_axis_index(axis, a.ndim)
    if n is None:
        n = a.shape[axis]

    fct = 1/inv_norm

    if a.shape[axis] != n:
        s = list(a.shape)
        index = [slice(None)]*len(s)
        if s[axis] > n:
            index[axis] = slice(0, n)
            a = a[tuple(index)]
        else:
            index[axis] = slice(0, s[axis])
            s[axis] = n
            z = zeros(s, a.dtype.char)
            z[tuple(index)] = a
            a = z

    if axis == a.ndim-1:
        r = pfi.execute(a, is_real, is_forward, fct)
    else:
        a = swapaxes(a, axis, -1)
        r = pfi.execute(a, is_real, is_forward, fct)
        r = swapaxes(r, axis, -1)
    return r


def _get_forward_norm(n, norm):
    if n < 1:
        raise ValueError(f"Invalid number of FFT data points ({n}) specified.")

    if norm is None or norm == "backward":
        return 1
    elif norm == "ortho":
        return sqrt(n)
    elif norm == "forward":
        return n
    raise ValueError(f'Invalid norm value {norm}; should be "backward",'
                     '"ortho" or "forward".')


def _get_backward_norm(n, norm):
    if n < 1:
        raise ValueError(f"Invalid number of FFT data points ({n}) specified.")

    if norm is None or norm == "backward":
        return n
    elif norm == "ortho":
        return sqrt(n)
    elif norm == "forward":
        return 1
    raise ValueError(f'Invalid norm value {norm}; should be "backward", '
                     '"ortho" or "forward".')


_SWAP_DIRECTION_MAP = {"backward": "forward", None: "forward",
                       "ortho": "ortho", "forward": "backward"}


def _swap_direction(norm):
    try:
        return _SWAP_DIRECTION_MAP[norm]
    except KeyError:
        raise ValueError(f'Invalid norm value {norm}; should be "backward", '
                         '"ortho" or "forward".') from None


def _fft_dispatcher(a, n=None, axis=None, norm=None):
    return (a,)


#@array_function_dispatch(_fft_dispatcher)
def fft(a, n=None, axis=-1, norm=None):
    """
    Compute the one-dimensional discrete Fourier Transform.
    This function computes the one-dimensional *n*-point discrete Fourier
    Transform (DFT) with the efficient Fast Fourier Transform (FFT)
    algorithm [CT].
    Parameters
    ----------
    a : array_like
        Input array, can be complex.
    n : int, optional
        Length of the transformed axis of the output.
        If `n` is smaller than the length of the input, the input is cropped.
        If it is larger, the input is padded with zeros.  If `n` is not given,
        the length of the input along the axis specified by `axis` is used.
    axis : int, optional
        Axis over which to compute the FFT.  If not given, the last axis is
        used.
    norm : {"backward", "ortho", "forward"}, optional
        .. versionadded:: 1.10.0
        Normalization mode (see `numpy.fft`). Default is "backward".
        Indicates which direction of the forward/backward pair of transforms
        is scaled and with what normalization factor.
        .. versionadded:: 1.20.0
            The "backward", "forward" values were added.
    Returns
    -------
    out : complex ndarray
        The truncated or zero-padded input, transformed along the axis
        indicated by `axis`, or the last one if `axis` is not specified.
    Raises
    ------
    IndexError
        If `axis` is not a valid axis of `a`.
    See Also
    --------
    numpy.fft : for definition of the DFT and conventions used.
    ifft : The inverse of `fft`.
    fft2 : The two-dimensional FFT.
    fftn : The *n*-dimensional FFT.
    rfftn : The *n*-dimensional FFT of real input.
    fftfreq : Frequency bins for given FFT parameters.
    Notes
    -----
    FFT (Fast Fourier Transform) refers to a way the discrete Fourier
    Transform (DFT) can be calculated efficiently, by using symmetries in the
    calculated terms.  The symmetry is highest when `n` is a power of 2, and
    the transform is therefore most efficient for these sizes.
    The DFT is defined, with the conventions used in this implementation, in
    the documentation for the `numpy.fft` module.
    References
    ----------
    .. [CT] Cooley, James W., and John W. Tukey, 1965, "An algorithm for the
            machine calculation of complex Fourier series," *Math. Comput.*
            19: 297-301.
    Examples
    --------
    >>> np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))
    array([-2.33486982e-16+1.14423775e-17j,  8.00000000e+00-1.25557246e-15j,
            2.33486982e-16+2.33486982e-16j,  0.00000000e+00+1.22464680e-16j,
           -1.14423775e-17+2.33486982e-16j,  0.00000000e+00+5.20784380e-16j,
            1.14423775e-17+1.14423775e-17j,  0.00000000e+00+1.22464680e-16j])
    In this example, real input has an FFT which is Hermitian, i.e., symmetric
    in the real part and anti-symmetric in the imaginary part, as described in
    the `numpy.fft` documentation:
    >>> import matplotlib.pyplot as plt
    >>> t = np.arange(256)
    >>> sp = np.fft.fft(np.sin(t))
    >>> freq = np.fft.fftfreq(t.shape[-1])
    >>> plt.plot(freq, sp.real, freq, sp.imag)
    [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
    >>> plt.show()
    """
    a = asarray(a)
    if n is None:
        n = a.shape[axis]
    inv_norm = _get_forward_norm(n, norm)
    output = _raw_fft(a, n, axis, False, True, inv_norm)
    return output


#@array_function_dispatch(_fft_dispatcher)
def ifft(a, n=None, axis=-1, norm=None):
    """
    Compute the one-dimensional inverse discrete Fourier Transform.
    This function computes the inverse of the one-dimensional *n*-point
    discrete Fourier transform computed by `fft`.  In other words,
    ``ifft(fft(a)) == a`` to within numerical accuracy.
    For a general description of the algorithm and definitions,
    see `numpy.fft`.
    The input should be ordered in the same way as is returned by `fft`,
    i.e.,
    * ``a[0]`` should contain the zero frequency term,
    * ``a[1:n//2]`` should contain the positive-frequency terms,
    * ``a[n//2 + 1:]`` should contain the negative-frequency terms, in
      increasing order starting from the most negative frequency.
    For an even number of input points, ``A[n//2]`` represents the sum of
    the values at the positive and negative Nyquist frequencies, as the two
    are aliased together. See `numpy.fft` for details.
    Parameters
    ----------
    a : array_like
        Input array, can be complex.
    n : int, optional
        Length of the transformed axis of the output.
        If `n` is smaller than the length of the input, the input is cropped.
        If it is larger, the input is padded with zeros.  If `n` is not given,
        the length of the input along the axis specified by `axis` is used.
        See notes about padding issues.
    axis : int, optional
        Axis over which to compute the inverse DFT.  If not given, the last
        axis is used.
    norm : {"backward", "ortho", "forward"}, optional
        .. versionadded:: 1.10.0
        Normalization mode (see `numpy.fft`). Default is "backward".
        Indicates which direction of the forward/backward pair of transforms
        is scaled and with what normalization factor.
        .. versionadded:: 1.20.0
            The "backward", "forward" values were added.
    Returns
    -------
    out : complex ndarray
        The truncated or zero-padded input, transformed along the axis
        indicated by `axis`, or the last one if `axis` is not specified.
    Raises
    ------
    IndexError
        If `axis` is not a valid axis of `a`.
    See Also
    --------
    numpy.fft : An introduction, with definitions and general explanations.
    fft : The one-dimensional (forward) FFT, of which `ifft` is the inverse
    ifft2 : The two-dimensional inverse FFT.
    ifftn : The n-dimensional inverse FFT.
    Notes
    -----
    If the input parameter `n` is larger than the size of the input, the input
    is padded by appending zeros at the end.  Even though this is the common
    approach, it might lead to surprising results.  If a different padding is
    desired, it must be performed before calling `ifft`.
    Examples
    --------
    >>> np.fft.ifft([0, 4, 0, 0])
    array([ 1.+0.j,  0.+1.j, -1.+0.j,  0.-1.j]) # may vary
    Create and plot a band-limited signal with random phases:
    >>> import matplotlib.pyplot as plt
    >>> t = np.arange(400)
    >>> n = np.zeros((400,), dtype=complex)
    >>> n[40:60] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20,)))
    >>> s = np.fft.ifft(n)
    >>> plt.plot(t, s.real, label='real')
    [<matplotlib.lines.Line2D object at ...>]
    >>> plt.plot(t, s.imag, '--', label='imaginary')
    [<matplotlib.lines.Line2D object at ...>]
    >>> plt.legend()
    <matplotlib.legend.Legend object at ...>
    >>> plt.show()
    """
    a = asarray(a)
    if n is None:
        n = a.shape[axis]
    inv_norm = _get_backward_norm(n, norm)
    output = _raw_fft(a, n, axis, False, False, inv_norm)
    return output

