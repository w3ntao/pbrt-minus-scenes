import argparse
import os
import subprocess
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

#pbrt_exe = "/home/wentao/Desktop/pbrt-v4/cmake-build-release/pbrt"
pbrt_exe = "/home/wentao/Dropbox/developer/graphics/pbrt-minus/cmake-build-release/pbrt-minus"
#pbrt_exe = "/home/wentao/Dropbox/developer/graphics/pbrt-minus/jerusalem-build/pbrt-minus"

simple_scenes = [
    "cornell-box/cornell-box-volume.pbrt",
    "cornell-box/cornell-box-specular.pbrt",
    "cornell-box/cornell-box-specular-volume.pbrt",
    "cornell-box/cornell-box-silver.pbrt",
    "cornell-box/cornell-box-environment-map.pbrt",
    "cornell-box/smallpt.pbrt",

    "killeroos/killeroo-gold.pbrt",
    "killeroos/killeroo-coated-gold.pbrt",
    "killeroos/killeroo-simple.pbrt",

    "lte-orb/lte-orb-rough-glass.pbrt",
    "lte-orb/lte-orb-silver.pbrt",
]

quality_scenes = [
    "material-testball/material-testball-sequence.pbrt",
    "material-testball/volumetric-sequance.pbrt",

    "veach-ajar/veach-ajar.pbrt",
    "veach-mis/veach-mis-colorized.pbrt",

    "caustic-glass/caustic-glass-v4.pbrt",

    "bathroom/bathroom.pbrt",
    "bathroom2/bathroom2.pbrt",

    "living-room/living-room.pbrt",

    "staircase/staircase.pbrt",
    "staircase2/staircase2.pbrt",

    "pbrt-book/book.pbrt",

    "crown/crown.pbrt",

    "ganesha/ganesha.pbrt",
    "ganesha/ganesha-coated-gold.pbrt",

    "bmw-m6/bmw-m6.pbrt",
    "chopper-titan/chopper-titan-v4.pbrt",

    "material-testball/material-testball.pbrt",
    "material-testball/material-testball-sequence.pbrt",

    "bathroom/bathroom.pbrt",
    "bathroom2/bathroom2.pbrt",

    "living-room/living-room.pbrt",

    "staircase/staircase.pbrt",
    "staircase2/staircase2.pbrt",

    "transparent-machines/frame542.pbrt",
    "transparent-machines/frame675.pbrt",
    "transparent-machines/frame812.pbrt",
    "transparent-machines/frame888.pbrt",
    "transparent-machines/frame1266.pbrt",

    "zero-day/frame25.pbrt",
    "zero-day/frame35.pbrt",
    "zero-day/frame52.pbrt",
    "zero-day/frame85.pbrt",
    "zero-day/frame120.pbrt",
    "zero-day/frame180.pbrt",
    "zero-day/frame210.pbrt",
    "zero-day/frame300.pbrt",
]

transparent_machines = [
    "transparent-machines/frame542.pbrt",
    "transparent-machines/frame675.pbrt",
    "transparent-machines/frame812.pbrt",
    "transparent-machines/frame888.pbrt",
    "transparent-machines/frame1266.pbrt",
]

def bash(command):
    return subprocess.call([command], shell=True)


def get_current_time():
    # print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
    # print(datetime.datetime.now().strftime("%Y-%B-%d-%H-%M"))
    # return datetime.datetime.now().strftime("%d-%H-%M")
    return datetime.datetime.now().strftime("%m-%d-%H-%M")


def regular_render(_folder: str, integrator: str):
    spp = 16

    os.chdir(_folder)
    for scene_file in (simple_scenes + quality_scenes):
        print("{}: rendering {}".format(_folder, scene_file))

        output = os.path.basename(scene_file).replace(
            ".pbrt", "-{}.png".format(spp))

        command = "{} ../{} --spp {} --outfile {}".format(
            pbrt_exe, scene_file, spp, output)

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))

        print("\n")

def debug_run(_folder: str):
    # scene_file = "ganesha/ganesha.pbrt"
    # scene_file = "ganesha/ganesha-coated-gold.pbrt"
    # scene_file = "bmw-m6/bmw-m6.pbrt"
    # scene_file = "cornell-box/cornell-box-specular.pbrt"
    # scene_file = "cornell-box/cornell-box-environment-map.pbrt"
    # scene_file = "crown/crown.pbrt"
    # scene_file = "killeroos/killeroo-simple.pbrt"
    scene_file = "veach-mis/veach-mis-colorized.pbrt"
    # scene_file = "veach-ajar/veach-ajar.pbrt"
    # scene_file = "caustic-glass/caustic-glass-v4.pbrt"

    #scene_file = "caustic-glass/debug-dielectric.pbrt"
    #scene_file = "caustic-glass/debug-dielectric-with-glass.pbrt"

    #scene_file = "killeroos/killeroo-dielectric.pbrt"
    #scene_file = "killeroos/killeroo-gold.pbrt"
    #scene_file = "killeroos/debug-dielectric.pbrt"

    # scene_file = "lte-orb/lte-orb-silver.pbrt"

    os.chdir(_folder)

    for spp in [9, 16, 64, 256, 1024]:
    #for spp in [16, 64, 128]:
        # spp = spp * spp
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-{}.png".format(spp))

        command = "{} ../{} --integrator path --spp {} --outfile {}".format(
            pbrt_exe, scene_file, spp, output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))
        print("\n")


def quality_render(_folder: str):
    spp = 16

    os.chdir(_folder)
    for scene_file in quality_scenes:
    #for scene_file in transparent_machines:
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-{}.png".format(spp))
        command = "{} ../{} --spp {} --outfile {}".format(
            pbrt_exe, scene_file, spp, output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))
        print("\n")

def surfacenormal_render(_folder: str):
    # spp = 100

    os.chdir(_folder)
    for scene_file in quality_scenes:
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-{}.pbrt".format(spp))

        command = "{} ../{} --integrator surfacenormal --outfile {}".format(
            pbrt_exe, scene_file,  output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))

        print("\n")


def memory_test(_folder: str):
    os.chdir(_folder)

    for scene_file in quality_scenes:
        command = "compute-sanitizer --tool memcheck --leak-check full {} ../{} --spp 1".format(
            pbrt_exe, scene_file)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))
        print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        description='a helper script for pbrt-minus')

    parser.add_argument('--debug',
                        default=False,
                        action='store_true')  # on/off flag

    parser.add_argument('--memory',
                        default=False,
                        action='store_true')  # on/off flag

    parser.add_argument('--quality',
                        default=False,
                        action='store_true')  # on/off flag

    parser.add_argument('--surfacenormal',
                        default=False,
                        action='store_true')  # on/off flag

    current_path = os.getcwd()

    args = parser.parse_args()

    folder = "out-{}".format(get_current_time())

    if "pbrt-v4" in pbrt_exe:
        folder += "-pbrt-v4"
    elif "pbrt-minus" in pbrt_exe:
        folder += "-pbrt-minus"
    else:
        raise Exception("error")

    bash("mkdir -p {}".format(folder))

    if args.debug:
        debug_run(folder)
    elif args.memory:
        memory_test(folder)
    elif args.quality:
        quality_render(folder)
    elif args.surfacenormal:
        surfacenormal_render(folder)
    else:
        regular_render(folder, "wavefrontpath")

    print("\n\nout folder: {}".format(folder))
