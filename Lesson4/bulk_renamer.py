#==========================================================================================
# Bulk File Renamer
# Syntax at CLI: python3 bulk_renamer.py <new_name> <target_dir>
# Programmed by: Ma. Beatriz Salazar - 07/16/2022
# Enhancements:
# 1. Add an optional string parameter to your script to set the 
#   logging level (“--log-level”). This will allow your script to
#   show the log hierarchy for the given level. Set the default value to “info”.
# 
# 2. The code for traversing directory and filtering for matching 
#   files, and renaming the target files is separated into its
#   own functions: search_files() and rename_files().
#
# 3. When the target file will be renamed to an already existing file name,
#   the count will skip to another index to avoid error 
#   (# Ex. if pic_1.png already exists, use pic_2.png for renaming).
#==========================================================================================


import logging, shutil
import glob, os, pathlib, sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, 
    format=(
        '[%(asctime)s] %(levelname)s %(module)s '
        '%(funcName)s:%(lineno)d - %(message)s'
            )
)
log = logging.getLogger(__name__)


def rename_files(new_name, found_files):
    try:
        for file in found_files: # For isolating the extension of the file to be renamed.
            fname, ext = os.path.splitext(file)

        rename = []
        j = 0
        i = 1 # For new_name iteration numbering
        for file in os.getcwd(): # For files in /images
            if os.path.isfile(os.getcwd()+f'/{new_name}{i}{ext}'):   
                i += 1
            else:
                shutil.move(found_files[j],f'{new_name}{i}{ext}')
                log.info(f'Renamed {found_files[j]} --> {new_name}{i}{ext}')
                i += 1
                j += 1
        
    except UnboundLocalError:
        log.warning('An UnboundLocalError prompt has appeared, but the files are successfully renamed.')
    except IndexError:
        log.warning('An IndexError prompt has appeared, but the files are successfully renamed.')

    return rename


def search_files(file_pattern, target_dir):
    found = [] 
    filepath = os.getcwd() + '/' + target_dir

    os.chdir(filepath)
    found = glob.glob(file_pattern)

    log.info(f'Searching for files in {target_dir}')
    log.debug(f'pat - {file_pattern}')
    log.debug(f'target_dir - {target_dir}')
    log.debug(f'found - {found}')
    log.info(f'Found {len(found)} files!')
    return found


def main(xargs):
    log.info('Start processing...')

    log.debug(f'xargs.new_name - {xargs.new_name}')
    log.debug(f'xargs.filter_pat - {xargs.file_pattern}')
    log.debug(f'xargs.target_dir - {xargs.target_dir}')

    # Search and Rename files:
    found_files = search_files(xargs.file_pattern, xargs.target_dir)
    success = rename_files(xargs.new_name, found_files)
    
    if success:
        log.info('Done.')
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'new_name', 
        help='the file name patter used to rename target files.'
    )
    parser.add_argument(
        'file_pattern',
        help='the file name pattern to match for renaming.'
    )
    parser.add_argument(
        'target_dir',
        help='The directory where the files to be renamed are located.'
    )

    parser.add_argument(
        '-L', '--log-level',
        help='Set log level.',
        default='info'
    )

    xargs = parser.parse_args()

    logging.basicConfig(                                 
        #level = logging.INFO,
        level = getattr(logging, xargs.log_level.upper()),     
        format=(
            '[%(asctime)s] %(levelname)s %(module)s '
            '%(funcName)s:%(lineno)d - %(message)s'
        ),
    )
    log = logging.getLogger('bulk_renamer')

    main(xargs)