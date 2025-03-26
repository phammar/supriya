from .core import UGen, param, ugen

@ugen(ar=True)
class MiPlaits(UGen):
    """
    Mutable Instruments Plaits UGen.
    https://github.com/v7b1/mi-UGens
    
    Instructions adapted from https://tidalcycles.org/docs/reference/mi-ugens-installation/

    Built here: ~/SuperCollider/mi-UGens/build/mi-UGens
    Extensions dir: Platform.userExtensionDir
    Copied mi-UGens to ~/.local/share/SuperCollider/Extensions

    Create a new synthdef file mi-ugens.scd, with these synthdefs
    Linux: ~/.local/share/SuperCollider/synthdefs/mi-ugens.scd

    Create a new parameter definitions file, mi-ugens-params.hs, with these parameters
    Linux: ~/.local/share/SuperCollider/synthdefs/mi-ugens-params.hs
    Configure SuperCollider - edit your startup.scd:
    Linux: ~/.conf/SuperCollider/startup.scd

    Load the mi-ugens.scd synthdef in startup.scd. Use the full path from 3.
    load("~/.local/share/SuperCollider/synthdefs/mi-ugens.scd");

    see: mi-UGens/build/mi-UGens/Classes/MiPlaits.sc
    MiPlaits : MultiOutUGen {

	*ar {
		arg pitch=60.0, engine=0, harm=0.1, timbre=0.5, morph=0.5, trigger=0.0, level=0, fm_mod=0.0, timb_mod=0.0,
		morph_mod=0.0, decay=0.5, lpg_colour=0.5, mul=1.0;
		^this.multiNew('audio', pitch, engine, harm, timbre, morph, trigger, level, fm_mod, timb_mod, morph_mod,
			decay, lpg_colour).madd(mul);
	}
	//checkInputs { ^this.checkSameRateAsFirstInput }

	init { arg ... theInputs;
		inputs = theInputs;
		^this.initOutputs(2, rate);
	}
}

    ::

        >>> supriya.ugens.MiPlaits.ar()
        <MiPlaits.ar()[0]>
    """
    # out=0
    freq = param(440)
    sustain = param(1)
    pan = param(0)
    begin = param(0)
    end = param(1)
    speed = param(1)
    accelerate = param(0)
    timbre = param(0.5)
    engine = param(0)
    harm = param(0.5)
    morph = param(0.5)
    level = param(1)
    lpgdecay = param(0)
    lpgcolour = param(0)
    mode = param(0)

    # fm_mod = param(0.0)
    # trigger = param(0.0)
    # decay = param(0.5)
    # timbre = param(0.5)
    # mul = param(1.0)
    # harm = param(0.1)
    # morph_mod = param(0.0)
    # pitch = param(60.0)
    # morph = param(0.5)
    # lpg_colour = param(0.5)
    # level = param(0)
    # engine = param(0)
    # timb_mod = param(0.0)

# Output of
# ugen.postln;
# ugen.superclass.postln;
# ugen.class.methods.do({
#     arg method;
#     method.postln;
#     method.keyValuePairsFromArgs.asDict.postln;
# });
# MiPlaits
# MultiOutUGen
# Meta_MiPlaits:ar
# IdentityDictionary[ (fm_mod -> 0.0), (trigger -> 0.0), (decay -> 0.5), (timbre -> 0.5), (mul -> 1.0), 
#   (harm -> 0.1), (morph_mod -> 0.0), (pitch -> 60.0), (morph -> 0.5), (lpg_colour -> 0.5), 
#   (level -> 0), (engine -> 0), (timb_mod -> 0.0) ]

# class MiPlaits(MultiOutUGen):
#     """

#     ::

#         >>> mi_plaits = supriya.ugens.MiPlaits.ar(
#         ...     fm_mod=0.0,
#         ...     trigger=0.0,
#         ...     decay=0.5,
#         ...     timbre=0.5,
#         ...     mul=1.0 ,
#         ...     harm=0.1,
#         ...     morph_mod=0.0,
#         ...     pitch=60.0,
#         ...     morph=0.5,
#         ...     lpg_colour=0.5 ,
#         ...     level=0,
#         ...     engine=0,
#         ...     timb_mod=0.0
#         ...     )
#         >>> mi_plaits
#         MiPlaits.ar()

#     """

#     ### CLASS VARIABLES ###

#     _ordered_input_names = collections.OrderedDict(
#         'fm_mod',
#         'trigger',
#         'decay',
#         'timbre',
#         'mul',
#         'harm',
#         'morph_mod',
#         'pitch',
#         'morph',
#         'lpg_colour',
#         'level',
#         'engine',
#         'timb_mod',
#         )

#     _valid_calculation_rates = None

#     ### INITIALIZER ###

#     def __init__(
#         self,
#         calculation_rate=None,
#         fm_mod=0.0,
#         trigger=0.0,
#         decay=0.5,
#         timbre=0.5,
#         mul=1.0 ,
#         harm=0.1,
#         morph_mod=0.0,
#         pitch=60.0,
#         morph=0.5,
#         lpg_colour=0.5,
#         level=0,
#         engine=0,
#         timb_mod=0.0
#         ):
#         MultiOutUGen.__init__(
#             self,
#             calculation_rate=calculation_rate,
#             fm_mod=fm_mod,
#             trigger=trigger,
#             decay=decay,
#             timbre=timbre,
#             mul=mul,
#             harm=harm,
#             morph_mod=morph_mod,
#             pitch=pitch,
#             morph=morph,
#             lpg_colour=lpg_colour,
#             level=level,
#             engine=engine,
#             timb_mod=timb_mod,
#             )

#     ### PUBLIC METHODS ###

#     @classmethod
#     def ar(
#         cls,
#         fm_mod=0.0,
#         trigger=0.0,
#         decay=0.5,
#         timbre=0.5,
#         mul=1.0 ,
#         harm=0.1,
#         morph_mod=0.0,
#         pitch=60.0,
#         morph=0.5,
#         lpg_colour=0.5,
#         level=0,
#         engine=0,
#         timb_mod=0.0,
#         ):
#         """
#         Constructs an audio-rate MiPlaits.

#         ::

#             >>> mi_plaits = supriya.ugens.MiPlaits.ar(
#             ...     fm_mod=0.0,
#             ...     trigger=0.0,
#             ...     decay=0.5,
#             ...     timbre=0.5,
#             ...     mul=1.0 ,
#             ...     harm=0.1,
#             ...     morph_mod=0.0,
#             ...     pitch=60.0,
#             ...     morph=0.5,
#             ...     lpg_colour=0.5,
#             ...     level=0,
#             ...     engine=0,
#             ...     timb_mod=0.0,
#             ...     )
#             >>> mi_plaits
#             MiPlaits.ar()

#         Returns ugen graph.
#         """
#         import supriya.synthdefs
#         calculation_rate = supriya.CalculationRate.AUDIO
#         ugen = cls._new_expanded(
#             calculation_rate=calculation_rate,
#             fm_mod=fm_mod,
#             trigger=trigger,
#             decay=decay,
#             timbre=timbre,
#             mul=mul,
#             harm=harm,
#             morph_mod=morph_mod,
#             pitch=pitch,
#             morph=morph,
#             lpg_colour=lpg_colour,
#             level=level,
#             engine=engine,
#             timb_mod=timb_mod,
#             )
#         return ugen

#     # def newFromDesc(): ...

#     ### PUBLIC PROPERTIES ###

#     @property
#     def fm_mod(self):
#         """
#         Gets `fm_mod` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('fm_mod')
#         return self._inputs[index]

#     @property
#     def trigger(self):
#         """
#         Gets `trigger` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('trigger')
#         return self._inputs[index]

#     @property
#     def decay(self):
#         """
#         Gets `decay` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('decay')
#         return self._inputs[index]

#     @property
#     def timbre(self):
#         """
#         Gets `timbre` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('timbre')
#         return self._inputs[index]

#     @property
#     def mul(self):
#         """
#         Gets `mul` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('mul')
#         return self._inputs[index]

#     @property
#     def harm(self):
#         """
#         Gets `harm` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('harm')
#         return self._inputs[index]

#     @property
#     def morph_mod(self):
#         """
#         Gets `morph_mod` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('morph_mod')
#         return self._inputs[index]

#     @property
#     def pitch(self):
#         """
#         Gets `pitch` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('pitch')
#         return self._inputs[index]

#     @property
#     def morph(self):
#         """
#         Gets `morph` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('morph')
#         return self._inputs[index]

#     @property
#     def lpg_colour(self):
#         """
#         Gets `lpg_colour` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('lpg_colour')
#         return self._inputs[index]

#     @property
#     def level(self):
#         """
#         Gets `level` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('level')
#         return self._inputs[index]

#     @property
#     def engine(self):
#         """
#         Gets `engine` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('engine')
#         return self._inputs[index]

#     @property
#     def timb_mod(self):
#         """
#         Gets `timb_mod` input of MiPlaits.

#         Returns ugen input.
#         """
#         index = self._ordered_input_names.index('timb_mod')
#         return self._inputs[index]

    
