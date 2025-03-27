from .core import UGen, param, ugen

@ugen(ar=True, is_multichannel=True, channel_count=2)
class MiPlaits(UGen):
    """Mutable Instruments Plaits UGen.

    Attributes
    ==========

    pitch
        pitch (midi note)

    engine
        chooses synthesis engine (0 -- 15): 0:virtual_analog_engine,
        1:waveshaping_engine, 2:fm_engine, 3:grain_engine, 4:additive_engine,
        5:wavetable_engine, 6:chord_engine, 7:speech_engine, 8:swarm_engine,
        9:noise_engine, 10:particle_engine, 11:string_engine, 12:modal_engine,
        13:bass_drum_engine, 14:snare_drum_engine, 15:hi_hat_engine

    harm
        harmonics parameter (0. -- 1.)

    timbre
        timbre parameter (0. -- 1.)

    morph
        morph parameter (0. -- 1.)

    trigger
        A non-zero value causes a trigger to
            a. fire the internal decaying envelope generator
            b. excites the physical and percussive models
            c. strikes the internal low-pass gate (LPG) (unless the 'level' input is
               modulated (patched))
            d. samples and holds the value of the 'model' input

    level
        Opens the internal low-pass gate, to simultaneously control the amplitude and
        brightness of the output signal. Also acts as an accent control when triggering
        the physical or percussive models.

    fm_mod
        fm modulation amount, if internal env is activated by trigger (-1. -- 1.)

    timb_mod
        timbre modulation amount, if internal env is activated by trigger (-1. -- 1.)

    morph_mod
        morph modulation amount, if internal env is activated by trigger (-1. -- 1.)

    decay
        decay rate of internal lowpass gate (0. -- 1.)

    lpg_colour
        "colour" of internal lowpass gate (0. -- 1.)

    mul
        set output gain

    ::

        >>> supriya.ugens.MiPlaits.ar()
        <MiPlaits.ar()[0]>
    """
    pitch=param(60.0)
    engine=param(0)
    harm=param(0.1)
    timbre=param(0.5)
    morph=param(0.5)
    trigger=param(0.0)
    level=param(0)
    fm_mod=param(0.0)
    timb_mod=param(0.0)
    morph_mod=param(0.0)
    decay=param(0.5)
    lpg_colour=param(0.5)
    mul=param(1.0)
