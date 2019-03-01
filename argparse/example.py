#!/usr/bin/python3

import argparse

UNIGE_YAML_PATH="/etc/test.yaml"

def main():
    parser = argparse.ArgumentParser(description='tools to manage salt')
    subparsers = parser.add_subparsers(dest="sub", help="sub-command help")
    # utils
    utils_parser = subparsers.add_parser("utils", help="utils")
    utils_subparsers = utils_parser.add_subparsers(dest="subsub", help="utils-command")
    ## clean
    utilsclean_parser = utils_subparsers.add_parser("clean", help="clean it")
    utilsclean_parser.add_argument("filename", default="", type=str, help="filename")
    ## day
    utilsday_parser = utils_subparsers.add_parser("day", help="print a working-day-X using apt-spread defined in {}".format(UNIGE_YAML_PATH))
    # minion
    minion_parser = subparsers.add_parser("minion", help="minion")
    minion_subparsers = minion_parser.add_subparsers(dest="subsub", help="minion-command")
    ## list
    minionlist_parser = minion_subparsers.add_parser("list", help="show list (none:restarting, all:normal)")
    minionlist_parser.set_defaults(name="minion-list")
    minionlist_parser.add_argument("pattern", default="", type=str, help="re matching the indices", nargs='?', )
    ## create
    minioncreate_parser = minion_subparsers.add_parser("create", help="show create (none:restarting, all:normal)")
    minioncreate_parser.set_defaults(name="minion-create")
    minioncreate_parser.add_argument("name", type=str, help="re matching the indices")
    minioncreate_parser.add_argument("--auto", type=bool, help="do not ask question", default=False)

    args = parser.parse_args()

    did_something = False
    if "minion" == args.sub:
        if "create" == args.subsub:
            main_minion_create(args.name, auto=args.auto)
            did_something = True
        elif "list" == args.subsub:
            main_minion_list(pattern=args.pattern)
            did_something = True
    if "utils" == args.sub:
        if "clean" == args.subsub:
            clean(args.minion_id)
            did_something = True
        elif "day" == args.subsub:
            print(get_day())
            did_something = True

    if not did_something:
        parser.print_usage()


if __name__ == '__main__':
    main()
