# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import FmriRealign4d


def test_FmriRealign4d_inputs():
    input_map = dict(
        between_loops=dict(usedefault=True, ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(mandatory=True, ),
        loops=dict(usedefault=True, ),
        slice_order=dict(requires=['time_interp'], ),
        speedup=dict(usedefault=True, ),
        start=dict(usedefault=True, ),
        time_interp=dict(requires=['slice_order'], ),
        tr=dict(mandatory=True, ),
        tr_slices=dict(requires=['time_interp'], ),
    )
    inputs = FmriRealign4d.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FmriRealign4d_outputs():
    output_map = dict(
        out_file=dict(),
        par_file=dict(),
    )
    outputs = FmriRealign4d.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
