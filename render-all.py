import argparse
import os
import subprocess
import datetime


pbrt_exe = "~/Dropbox/developer/graphics/pbrt-minus/cmake-build-release/pbrt-minus"

quality_scenes = [
    "cornell-box/cornell-box.pbrt",
    "cornell-box/cornell-box-specular.pbrt",
    "veach-mis/veach-mis-colorized.pbrt",
    "killeroos/killeroo-simple.pbrt",
    "crown/crown.pbrt",
    "sssdragon/dragon_10.pbrt",
    "ganesha/ganesha.pbrt",
    "lte-orb/lte-orb-rough-glass.pbrt",
    "lte-orb/lte-orb-silver.pbrt",
]

regular_scenes = quality_scenes + \
    ["killeroos/killeroo-simple-sn.pbrt", "ganesha/ganesha-ao.pbrt",]


def bash(command):
    return subprocess.call([command], shell=True)


def get_current_time():
    # print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
    return datetime.datetime.now().strftime("%B-%d-%H-%M")


def regular_render(_folder: str):
    spp = 1

    os.chdir(folder)
    for scene_file in regular_scenes:
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-{}.pbrt".format(spp))

        command = "{} ../{} --spp {} --output {}".format(
            pbrt_exe, scene_file, spp, output)

        print("{}: rendering {}".format(_folder, scene_file))

        if bash(command) != 0:
            raise Exception("\n\n fail rendering {}\n\n".format(scene_file))
        print("\n")


def quality_render(_folder: str):
    spp = 512

    os.chdir(folder)
    for scene_file in quality_scenes:
        output = os.path.basename(scene_file).replace(
            ".pbrt", "-simplepath-{}.pbrt".format(spp))
        command = "{} ../{} --spp {} --output {}".format(
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

    parser.add_argument('-m', '--memory',
                        default=False,
                        action='store_true')  # on/off flag

    parser.add_argument('-q', '--quality',
                        default=False,
                        action='store_true')  # on/off flag

    args = parser.parse_args()

    folder = "out-{}".format(get_current_time())
    bash("mkdir {}".format(folder))

    if args.memory:
        memory_test(folder)
    elif args.quality:
        quality_render(folder)
    else:
        regular_render(folder)

    print("\n\nout folder: {}".format(folder))
