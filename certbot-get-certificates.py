#!/usr/bin/env python3

import sys
import subprocess
import os
import re

EMAIL = ***INSERT EMAIL HERE***

def get_certificates(domains):
    for d in domains:

        # build args
        cmd_args = [
            "docker",
            "run",
            "--rm",
            "-p",
            "80:80",
            "-v",
            f"{os.getcwd()}/certbot/conf:/etc/letsencrypt",
            "certbot/certbot",
            "certonly",
            "--standalone",
            "--email",
            EMAIL,
            "--agree-tos",
            "--force-renewal",
            "--non-interactive",
        ]
        for d2 in d:
            cmd_args.append("-d")
            cmd_args.append(d2)

        # run command
        subprocess.run(cmd_args)


def process_arguments(args):
    final_args = []
    for arg in args:
        current_args = []
        if re.search(r"^[a-zA-Z0-9-]+.[a-zA-Z]+$", arg):
            current_args.append(arg)
            current_args.append(f"www.{arg}")
        else:
            current_args.append(arg)
        final_args.append(current_args)
    return final_args


def main(domains):
    get_certificates(domains)


if(__name__ == "__main__"):
    main(process_arguments(sys.argv[1:]))