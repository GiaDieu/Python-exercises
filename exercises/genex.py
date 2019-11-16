#!/usr/bin/env python

import argparse


def main():
    with open('ex.tpl') as f:
        tpl = f.read()

    argp = argparse.ArgumentParser()
    argp.add_argument('exercise',
                      help='exercise number to generate, in format X_N',
                      )

    args = argp.parse_args()
    output_fn = 'ex{0}.py'.format(args.exercise)
    print('Writing {0}'.format(output_fn))
    with open(output_fn, 'w') as f:
        f.write(tpl.format(ex=args.exercise))

    print('Done')


if __name__ == "__main__":
    main()
