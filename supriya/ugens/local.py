from .core import UGen, param, ugen

@ugen(ar=True, is_multichannel=True, channel_count=2)
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
    # mul=param(1.0)

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

