import argparse
import os
import subprocess
import datetime


pbrt_exe = "~/Dropbox/developer/graphics/pbrt-minus/cmake-build-release/pbrt-minus"

scenes = [
    "cornell-box/cornell-box-environment-map.pbrt",
    # "cornell-box/cornell-box-instance.pbrt",
    # "cornell-box/cornell-box-specular.pbrt",

    "veach-mis/veach-mis-colorized.pbrt",
    # "killeroos/killeroo-gold.pbrt",
    # "killeroos/killeroo-simple.pbrt",
    # "crown/crown.pbrt",
    # "sssdragon/dragon_10.pbrt",
    "ganesha/ganesha.pbrt",
    "ganesha/ganesha-coated-gold.pbrt",
    "lte-orb/lte-orb-rough-glass.pbrt",
    "lte-orb/lte-orb-silver.pbrt",

    # "zero-day/frame25.pbrt",
    # "zero-day/frame35.pbrt",
    # "zero-day/frame52.pbrt",
    # "zero-day/frame85.pbrt",
    # "zero-day/frame120.pbrt",
    # "zero-day/frame180.pbrt",
    # "zero-day/frame210.pbrt",
    # "zero-day/frame300.pbrt",
]


regular_scenes = scenes


def bash(command):
    return subprocess.call([command], shell=True)


def get_current_time():
    # print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
    return datetime.datetime.now().strftime("%B-%d-%H-%M")


def regular_render(_folder: str):
    spp = 4

    os.chdir(folder)
    for scene_file in regular_scenes:
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-{}-independent.png".format(spp))

        command = "{} ../{} --spp {} --output {}".format(
            pbrt_exe, scene_file, spp, output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))

        print("\n")


def debug_run(_folder: str):
    # scene_file = "ganesha/ganesha.pbrt"
    scene_file = "ganesha/ganesha-coated-gold.pbrt"
    # scene_file = "bmw-m6/bmw-m6.pbrt"
    # scene_file = "cornell-box/cornell-box-environment-map.pbrt"
    # scene_file = "crown/crown.pbrt"
    # scene_file = "killeroos/killeroo-wall.pbrt"

    os.chdir(folder)

    # for spp in [1, 4, 16, 64, 128]:
    for spp in [128, 256, 512, 1024]:
        # spp = spp * spp
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-path-stratified-{}.png".format(spp))
        command = "{} ../{} --spp {} --output {}".format(
            pbrt_exe, scene_file, spp, output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))
        print("\n")


def quality_render(_folder: str):
    spp = 256

    os.chdir(folder)
    for scene_file in scenes:
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-path-stratified-{}.png".format(spp))
        command = "{} ../{} --spp {} --output {}".format(
            pbrt_exe, scene_file, spp, output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))
        print("\n")


def surfacenormal_render(_folder: str):
    spp = 100

    os.chdir(folder)
    for scene_file in regular_scenes:
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-{}.pbrt".format(spp))

        command = "{} ../{} --spp {} --integrator surfacenormal --output {}".format(
            pbrt_exe, scene_file, spp, output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))

        print("\n")


def memory_test(_folder: str):
    os.chdir(folder)

    for scene_file in regular_scenes:
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

    args = parser.parse_args()

    folder = "out-{}".format(get_current_time())
    bash("mkdir {}".format(folder))

    if args.debug:
        debug_run(folder)
    elif args.memory:
        memory_test(folder)
    elif args.quality:
        quality_render(folder)
    elif args.surfacenormal:
        surfacenormal_render(folder)
    else:
        regular_render(folder)

    print("\n\nout folder: {}".format(folder))
