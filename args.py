import argparse


def getArgs():
    parser = argparse.ArgumentParser()
    # add back to -b before 1.0 - required=True
    parser.add_argument('-b', dest='bd', action='store', type=str, nargs='+',
                        help='Blu-ray link from blu-ray.com')
    parser.add_argument('-i', dest='bdinfo', action='store', type=str,
                        help='BDInfoCLI-ng, add path to folder containing ISO or BDMV folder. Requires bdinfo.exe path in conf.txt')
    return parser.parse_args()


# def getArgs():
#     """ Get command-line arguments
#     """
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-a', dest='audio', action='store', type=str,
#                         help='Audio codec. Ex: DTS-HD, FLAC, Atmos')
#     parser.add_argument('-b', dest='bd', action='store', type=str, required=True,
#                         help='Blu-ray link from blu-ray.com')
#     parser.add_argument('-c', dest='container', action='store', type=str,
#                         help='Movie file container. Ex: AVC, HEVC, VC-1')
#     parser.add_argument('-d', dest='dgdemux', action='store_true',
#                         help='Use this for remuxes you used DGDemux for (removes eac logs)')
#     parser.add_argument('-e', dest='edition', action='store', type=str,
#                         help='Use for special editions such as "Director\'s Cut"')
#     parser.add_argument('-f', dest='file', action='store', type=str,
#                         help='Use for name of your movie file with .mkv')
#     parser.add_argument('-l', dest='layout', action='store', type=str,
#                         help='Audio channel spec. Ex: 2.0, 4.0, 5.1')
#     parser.add_argument('-m', dest='modifiers', action='store', type=str,
#                         help='Use for Hybrids or specific country editions such as GBR')
#     parser.add_argument('-n', dest='noup', action='store', type=str,
#                         help='Use to generate without uploading images.')
#     parser.add_argument('-r', dest='res', action='store', type=str,
#                         help='Resolution of your remux, the p/i should be included')
#     parser.add_argument('-s', dest='source', action='store', type=str,
#                         help='Use for file title of source. Feel free to include (thanks whoever) as it will print in template')
#     parser.add_argument('-t', dest='tags', action='store', type=str,
#                         help='Extra tags such as HDR. Input multiple as Tag.Tag.Tag in the proper order.')
#     parser.add_argument('-x', dest='encode', action='store', type=str,
#                         help='Use if this is an encode. Screenshots dont work right so upload is disabled.')
#     return parser.parse_args()
